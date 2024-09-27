import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Med_supplies_page(Base):

    url = 'https://zdravcity.ru/'
    def __init__(self, driver):
        super().__init__(driver) # Указание, что даннный класс является потомком класса Base
        self.driver = driver


#Locators
    pansements_link = "//div[contains(text(), 'Перевязочные материалы')]" #Локатор ссылки на перевязочные материалы
    header_pansements = "//li[contains(text(), 'Перевязочные материалы')]" #Локатор заголовка из хлебных крошек на странице перевязочных материалов


#Getters
    def get_pansements_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pansements_link)))

    def get_header_pansements(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.header_pansements)))

#Actions

    def click_pansements_link(self):
        self.get_pansements_link().click()
        print('Клик по ссылке "Перевязочные материалы"')

#Methods
    def move_to_pansements_link(self):
        self.click_pansements_link()
        self.wait_for_page_to_stabilize()
        self.get_current_url()
        self.wait_for_page_to_stabilize()
        self.assert_url('https://zdravcity.ru/catalog/medicinskie-izdelija/perevjazochnye-materialy/')
        self.assert_word(self.get_header_pansements(),'Перевязочные материалы')







