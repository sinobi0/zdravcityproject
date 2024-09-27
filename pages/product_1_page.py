from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.med_supplies_page import Med_supplies_page
from pages.pansements_page import Pansements_page


class Product_1_page(Base):
    header_catalog_product_1 = None
    price_catalog_product_1 = None
    vendor_catalog_product_1 = None
    vendor_country_catalog_product_1 = None

    url = 'https://zdravcity.ru/'
    def __init__(self, driver):
        super().__init__(driver) # Указание, что даннный класс является потомком класса Base
        self.driver = driver


    #Locators
    header_product_1_page_locator = "//h1[contains(text(),'Повязка стерильная пластырного типа с контактным слоем Cosmopor Silicone/Космопор Силикон 15х8см 10шт')]" #Заголовок товара
    price_product_1_page_locator = "(//div[contains(@class,'Price_price__Y1FnU')])[1]" #Цена товара на странице
    vendor_product_1_page_locator = "(//span[contains(@class,'ListInfo_list-value__6Cts2')])[2]"
    country_vendor_product_1_page_locator = "(//span[contains(@class,'ListInfo_list-value__6Cts2')])[3]"
    add_to_cart_button_locator = "//span[contains(text(),'Купить')]"
    cart_move_link_locator = "//a[@aria-label='Корзина']"
    cart_header_locator = "//span[contains(text(),'Ваш заказ')]"



#Getters
    def get_header_product_1_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.header_product_1_page_locator)))

    def get_price_product_1_page(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_product_1_page_locator)))

    def get_vendor_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.vendor_product_1_page_locator)))

    def get_vendor_country_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.country_vendor_product_1_page_locator)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_locator)))

    def get_cart_move_link(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_move_link_locator)))

    def get_cart_header(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_header_locator)))

    #Actions

    def click_add_to_cart(self):
        self.get_add_to_cart_button().click()
        print("Товар добавлен в корзину")

    def click_cart_move_link(self):
        self.get_cart_move_link().click()
        print("Совершен переход в корзину")



#Methods

    def save_catalog_product_price(self):
        pp = Pansements_page(self.driver)
        self.price_catalog_product_1 = pp.get_product_price().text

    def save_header_catalog_product_1(self):
        pp = Pansements_page(self.driver)
        self.header_catalog_product_1 = pp.get_header_product_1().text

    def save_vendor_catalog_product_1(self):
        pp = Pansements_page(self.driver)
        self.vendor_catalog_product_1 = pp.get_vendor_name().text

    def save_vendor_country_catalog_product_1(self):
        pp = Pansements_page(self.driver)
        self.vendor_country_catalog_product_1 = pp.get_vendor_country().text

    def check_assert_data(self):
        self.assert_word(self.get_header_product_1_page(), self.header_catalog_product_1)
        self.assert_word(self.get_vendor_product_1(), self.vendor_catalog_product_1)
        self.assert_word(self.get_vendor_country_product_1(), self.vendor_country_catalog_product_1)
        self.assert_word(self.get_price_product_1_page(), self.price_catalog_product_1 )


    def add_to_cart_product_1(self):
        self.click_add_to_cart()

    def move_to_cart(self):
        self.wait_for_page_to_stabilize()
        self.click_cart_move_link()
        self.wait_for_page_to_stabilize()
        self.assert_url('https://zdravcity.ru/cart/')
        self.assert_word(self.get_cart_header(),'Ваш заказ')



