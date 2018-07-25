#!/usr/bin/python3

from PIL import Image
from urllib.request import urlopen as get


def from_url(url):
    return Image.open(get(url))
