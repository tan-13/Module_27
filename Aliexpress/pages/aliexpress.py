#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://aliexpress.ru/'

        super().__init__(web_driver, url)

    # Banner appear
    banner = WebElement(xpath='//*[@id="6216442440"]/div/div')

    # Banner delete
    banner_delete = WebElement(css_selector='button[@data-spm-anchor-id="a2g0o.tm585518.9347857940.i1.7ddc1c90KRbzP9"]')
    
    # Products сategories

    products_categories = ManyWebElements(css_selector='div.categories-list-box dl.cl-item')

    # Subcategories

    products_categories_sub = ManyWebElements(css_selector='div.categories-list-box dl.cl-item dt.cate-name')

    # The first category in list with subcategories

    category_1 = WebElement(css_selector='div.categories-list-box dl.cl-item.cl-item-phones')

    # Products of the first category

    products_category_1 = WebElement(css_selector='div.categories-list-box dl.cl-item.cl-item-phones dd.sub-cate')

    
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/item") and @title!=""]')
