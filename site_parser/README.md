# Web-site parser
The parser is used to find all urls on a website with nested level 2.

## Prerequisites
Python3.8+

## Installing
```shell
python3.8 -m venv .venv
source .venv/bin/activate
pip install -r requirements --no-cache-dir
```

## Usage
### Help
```shell
./site_parser.py --help
Usage: site_parser.py [OPTIONS] WEB_SITE

  The parser is used to find all urls on a website with nested level 2.

Options:
  -o, --output [STDOUT|FILE]  Stdout by default.
  --help                      Show this message and exit.

```

### Example
```shell
./site_parser.py https://vk.com -o file
cat parsing_result.json
{
    "https://vk.com": [
        "https://vk.me/?act=dl",
        "https://static.vk.com/restore"
    ],
    "https://vk.me/?act=dl": [],
    "https://static.vk.com/restore": []
}
```

```shell
./site_parser.py https://ya.ru -o stdout
{
    "https://ya.ru": [
        "https://mail.yandex.ru"
    ],
    "https://mail.yandex.ru": [
        "https://yandex.ru/support/common/browsers-settings/browsers-java-js-settings.xml",
        "https://mail.yandex.ru?noretpath=1",
        "https://passport.yandex.ru/auth/register/lite?from=mail&origin=hostroot_homer_auth_oldbro_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&process_uuid=b86ad2ec-4726-42f3-86ef-116722313aca",
        "https://passport.yandex.ru/registration?from=mail&origin=hostroot_homer_auth_oldbro_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&process_uuid=b86ad2ec-4726-42f3-86ef-116722313aca",
        "https://id.yandex.ru/yafamily?origin=yandexid_auth_form",
        "https://yandex.ru/support/common/browsers-settings/incognito.html",
        "https://yandex.ru/support/passport/"
    ]
}
```

### Tests
```shell
cd site_parser
python -m unittest tests/test_site_parser.py 
```