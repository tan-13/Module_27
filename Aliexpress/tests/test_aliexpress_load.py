#!/usr/bin/python3
# -*- encoding=utf8 -*-

import pytest
from pages.aliexpress import MainPage

def test_banner(web_browser):
    """ Make sure banner appear. """
    page = MainPage(web_browser)
    page.banner.is_visible()
    """Find element on banner to delete"""
    web_browser.find_element_by_class_name('rax-image')
    """Picture contains script """
    javaScript = "page.banner_delete('a2g0o.tm585518.9347857940.i1.7ddc1c90KRbzP9').click();"
    web_browser.execute_script(javaScript)
    assert page.banner.wait_until_not_visible()

def test_products_in_categories(web_browser):
    """ Make sure that there are products in categories. """

    page = MainPage(web_browser)

    # Go to main menu:
    page.category_1.click()

    # Go to sub menu:
    page.products_category_1.click()

    # Verify that there is a product:
    assert page.products_titles.count() >= 1

    # Check other categories
    ### пока не разобралась как сделать на все сразу, не по одной.

a = products_categories
b = products_categories_sub
c = products_titles





