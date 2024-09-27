import time
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver import Keys  #импорт Keys, для имитации нажатия клавиши клавиатуры
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import Main_page
from pages.med_supplies_page import Med_supplies_page
from pages.pansements_page import Pansements_page
from pages.product_1_page import Product_1_page

url = 'https://zdravcity.ru/'
def test_smoke_road(set_up):

    mp = Main_page(set_up)
    mp.move_to_link_med_supplies()

    msp = Med_supplies_page(set_up)
    msp.move_to_pansements_link()

    pp = Pansements_page(set_up)
    pp.price_range_filter_slider()

    pp.pack_quantity_filter()
    # msp.filter_vendor() #Здесь баг, не работает фильтр по производителю
    # msp.sort_by_cheap_first() #Невозможно отсортировать из-за капчи

    p1p = Product_1_page(set_up)
    p1p.save_catalog_product_price()
    p1p.save_header_catalog_product_1()
    p1p.save_vendor_catalog_product_1()
    p1p.save_vendor_country_catalog_product_1()
    pp.move_product_1()

    p1p.check_assert_data()
    p1p.click_add_to_cart()
    p1p.move_to_cart()
