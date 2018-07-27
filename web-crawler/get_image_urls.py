#!/usr/bin/python3
from bs4 import BeautifulSoup
from urllib.request import urlopen as get


def get_urls(html_url):
    return [
        img.get('src')
        for img
        in BeautifulSoup(get(html_url))
    ]
