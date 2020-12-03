#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os
import pytest

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements

def test_page_loaded(web_browser):
    """ Make sure pictures are loaded. """
    web_browser.get('https://www.reddit.com/')
    while web_browser.find_element_by_tag_name('img'):
    web_browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    imgs=web_browser.find_element_by_tag_name('img').count()
    if 'imgs' == 20:
        print 'end'
        break
    else:
        continue
    pictures = web_browser.find_elements_by_css_selector('[@class='_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax marked-element-temp']/@src')
    pictures.count()
    assert imgs == pictures


# с остальным пока не разобралась