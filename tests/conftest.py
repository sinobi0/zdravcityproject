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



@pytest.fixture()
def set_up():

    print("\nЗапуск теста")    #перед тестом
    url = 'https://zdravcity.ru/'
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = 'eager'  # эта опция позволяет начинать работать со страницей, до того как она загрузится на 100%.
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    driver.get(url)
    driver.maximize_window()

    yield driver  # Возвращаем драйвер

    print("\nТест завершен!")    #после теста
    driver.quit()

