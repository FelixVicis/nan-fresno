#!/usr/bin/python3

from PIL import Image
from urllib2 import urlopen as get


def from_url(url):
    return Image.open(get(url))
