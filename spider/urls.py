#!/usr/bin/python3
from bs4 import BeautifulSoup
from urllib.request import urlopen as get


def get_urls(html_url):
    try:
        html_body = get(html_url)
        parsed = BeautifulSoup(html_body, 'html.parser')
    except Exception as e:
        print(e)
        return []

    return [
        _clean(img.get('src'), html_url)
        for img
        in parsed.find_all('img')
        if img.get('src')
    ]


def _clean(src, url):
    if src.startswith('/'):
        return '{url}{src}'.format(src=src, url=url)

    return src
