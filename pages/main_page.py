from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):


    url = 'https://zdravcity.ru/'
    def __init__(self, driver):
        super().__init__(driver) # Указание, что даннный класс является потомком класса Base
        self.driver = driver



#Locators
    link_med_supplies = "//span[contains(text(), 'Медтовары')]"
    header_med_supplies = "//li[contains(text(), 'Медицинские изделия')]"


#Getters
    def get_link_med_supplies(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_med_supplies)))

    def get_header_med_supplies(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.header_med_supplies)))


#Actions

    def click_link_med_supplies(self):
        self.get_link_med_supplies().click()
        print('Клик по ссылке "Медтовары"')



#Methods
    def move_to_link_med_supplies(self):
        self.click_link_med_supplies()
        self.get_current_url()
        self.assert_url('https://zdravcity.ru/catalog/medicinskie-izdelija/')
        self.assert_word(self.get_header_med_supplies(),'Медицинские изделия')
