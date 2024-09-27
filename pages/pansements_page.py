import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Pansements_page(Base):

    url = 'https://zdravcity.ru/'
    def __init__(self, driver):
        super().__init__(driver) # Указание, что даннный класс является потомком класса Base
        self.driver = driver


#Locators

    slider_range_prices_to = "(//div[contains(@class,'range-handler')])[2]" # Локатор фильтрации слайдера по цене ДО
    slider_range_prices_from = "(//div[contains(@class,'range-handler')])[1]" # Локатор фильтрации слайдера по цене ОТ
    pack_quantity_10_filter_locator = "(//span[@class='Checkbox_checkbox-label-text__7xTS5'])[45]" # Фильтр по параметры "Количество в пачке" со значением: 10шт
    link_product_1_locator = "//span[@title='Повязка стерильная пластырного типа с контактным слоем Cosmopor Silicone/Космопор Силикон 15х8см 10шт']" #Ссылка на товар
    header_product_1_locator = "//span[@title='Повязка стерильная пластырного типа с контактным слоем Cosmopor Silicone/Космопор Силикон 15х8см 10шт']" #Заголовок товара
    price_product_1_locator = "(//div[contains(@class,'common-price')])[23]" #Цена товара
    vendor_name_locator = "(//span[@class='HorizontalInfoList_list-item-value__Dq5rF'])[1]" #Производитель товара
    vendor_country_locator = "(//span[@class='HorizontalInfoList_list-item-value__Dq5rF'])[3]" #Страна производителя
    """Неиспользуемые локаторы"""
    filter_vendor_view_all_btn = "(//div[contains(text(), 'Посмотреть все')])[1]"
    sort_by_locator = "//button[contains(text(), 'Популярные')]"
    sort_cheap_first_locator = "//li[contains(text(),'Сначала дешевые')]"

#Getters

    def get_filter_slider_range_prices_to(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_range_prices_to)))

    def get_filter_slider_range_prices_from(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_range_prices_from)))

    def get_pack_quantity_10_filter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.pack_quantity_10_filter_locator)))
    def get_vendor_view_all_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_vendor_view_all_btn)))

    def get_sort_by(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sort_by_locator)))

    def get_sort_cheap_first(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.sort_cheap_first_locator)))

    def get_link_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.link_product_1_locator)))

    def get_header_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.header_product_1_locator)))


    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.price_product_1_locator)))


    def get_vendor_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.vendor_name_locator)))

    def get_vendor_country(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.vendor_country_locator)))


#Actions

    def filter_slider_range_prices_to(self, range):  # Функция фильтрации диапазона цены на значение -100
        actions = ActionChains(self.driver)  # создание экземпляра класса для перемещения по окну браузера
        self.wait_for_page_to_stabilize()
        actions.click_and_hold(self.get_filter_slider_range_prices_to()).move_by_offset(range, 0).release().perform()
        print(f"Слайдер по диапазону цены перемещен на значение {range}")

    def filter_slider_range_prices_from(self, range):  # Функция фильтрации диапазона цены на значение 50
        actions = ActionChains(self.driver)  # создание экземпляра класса для перемещения по окну браузера
        self.wait_for_page_to_stabilize()
        actions.click_and_hold(self.get_filter_slider_range_prices_from()).move_by_offset(range, 0).release().perform()
        print(f"Слайдер по диапазону цены перемещен на значение {range}")

    def click_pack_quantity_10_filter(self):
        self.wait_for_page_to_stabilize()
        actions = ActionChains(self.driver)  # создание экземпляра класса для перемещения по окну браузера
        actions.move_to_element(self.get_pack_quantity_10_filter()).perform()
        self.get_pack_quantity_10_filter().click()
        print('Применен фильтр по количеству шт в упоковке со значением: 10')

    def click_vendor_view_all_btn(self):
        self.wait_for_page_to_stabilize()
        actions = ActionChains(self.driver)  # создание экземпляра класса для перемещения по окну браузера
        actions.move_to_element(self.get_vendor_view_all_btn()).perform()
        self.get_vendor_view_all_btn().click()
        print('Нажатие на кнопку "Просмотреть все" в фильтрации по производителю')

    def click_sort_by(self):
        self.wait_for_page_to_stabilize()
        self.get_sort_by().click()

    def click_sort_cheap_first(self):
        actions = ActionChains(self.driver)  # создание экземпляра класса для перемещения по окну браузера
        self.wait_for_page_to_stabilize()
        actions.move_to_element(self.get_sort_cheap_first()).perform()
        self.get_sort_cheap_first().click()
        print('Применена сортировка по: Сначала дешевые')

    def click_link_product_1(self):
        self.wait_for_page_to_stabilize()
        self.get_link_product_1().click()
        self.wait_for_page_to_stabilize()
        print("Переход на страницу товара успешен")

#Methods

    def price_range_filter_slider(self):
        self.filter_slider_range_prices_to(-50)
        self.wait_for_page_to_stabilize()
        self.get_current_url()
        self.assert_url('https://zdravcity.ru/catalog/medicinskie-izdelija/perevjazochnye-materialy/price-from:2_price-to:5395/')
        self.filter_slider_range_prices_from(40)
        self.get_current_url()
        self.wait_for_page_to_stabilize()
        self.assert_url('https://zdravcity.ru/catalog/medicinskie-izdelija/perevjazochnye-materialy/price-from:1363_price-to:5395/')

    def pack_quantity_filter(self):
        self.click_pack_quantity_10_filter()
        self.wait_for_page_to_stabilize()
        self.get_current_url()
        self.assert_url('https://zdravcity.ru/catalog/medicinskie-izdelija/perevjazochnye-materialy/price-from:1363_price-to:5395_kolichestvo-v-pachke:10-sht/')

    def filter_vendor(self):
        self.click_vendor_view_all_btn()

    def sort_by_cheap_first(self):
        self.wait_for_page_to_stabilize()
        self.click_sort_by()
        self.click_sort_cheap_first()

    def move_product_1(self):
        self.wait_for_page_to_stabilize()
        self.click_link_product_1()
        self.wait_for_page_to_stabilize()
        self.assert_url(
            'https://zdravcity.ru/p_povjazka-sterilnaja-plastyrnogo-tipa-s-kontaktnym-sloem-cosmopor-silicone-kosmopor-silikon-15h8sm-10sht-0195588.html')






