#!/usr/bin/python3

from .search import *
from .urls import *


def get_image_urls(query, **kwargs):
    for website_url in websites(query, **kwargs):
        for image_url in get_urls(website_url):
            yield image_url
