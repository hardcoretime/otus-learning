#!/usr/bin/env python
import json
import sys
from enum import Enum
from typing import List
from urllib.parse import urlparse

import click
import requests
from bs4 import BeautifulSoup


class Output(Enum):
    STDOUT = 'stdout'
    FILE = 'file'


@click.command(help='The parser is used to find all urls on a website with nested level 2.')
@click.argument('web-site')
@click.option(
    '-o', '--output',
    type=click.Choice([option.name for option in Output], case_sensitive=False),
    default=Output.STDOUT.name,
    multiple=False,
    required=False,
    help='Stdout by default.'
)
def main(web_site: str, output: str) -> None:
    if not is_url(web_site):
        click.echo('Enter a valid url consist of scheme and netloc.')
        sys.exit(1)

    total_result = dict()
    checked_urls = list()

    web_site_urls = get_urls(web_site)
    total_result.update({web_site: web_site_urls})
    checked_urls.append(web_site)

    for url in web_site_urls:
        if url not in checked_urls:
            included_urls = get_urls(url)
            total_result.update({url: included_urls})
            checked_urls.append(url)

    formatted_result = json.dumps(total_result, indent=4)
    if output == Output.FILE.name:
        with open('parsing_result.json', 'w') as file:
            file.write(formatted_result)
    else:
        click.echo(formatted_result)


def is_url(url: str) -> bool:
    result = urlparse(url)

    return all([result.scheme, result.netloc])


def get_urls(web_site: str) -> List[str]:
    result = list()
    response = requests.get(web_site)
    soup = BeautifulSoup(response.text, 'html.parser')

    for a_tag in soup.find_all('a'):
        url = a_tag.get('href', None)
        if is_url(url):
            result.append(url)

    return result


if __name__ == '__main__':
    main()
