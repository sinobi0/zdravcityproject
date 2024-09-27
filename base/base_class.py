import datetime
import time

from selenium.webdriver.support.wait import WebDriverWait


class Base():
    """ Базовый класс, содержащий универсальные методы """
    def __init__(self, driver):
        self.driver = driver

    """Получение текущей ссылки"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url: {get_url}")

    """Получения слова"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Слово успешно совпало")

    """Получения скриншота"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        self.driver.save_screenshot('D:\\JetBrains\\pythonProject\\screen\\' + 'screenshot' + now_date + '.png')
        print("Скриншот успешно сделан")

    """Сравнение URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URL успешно совпало")

    """Ожидание загрузки страницы"""
    def wait_for_page_to_stabilize(self, timeout=30):
        # Получаем текущий URL
        last_url = self.driver.current_url
        last_title = self.driver.title
        end_time = time.time() + timeout

        while time.time() < end_time:
            time.sleep(0.5)  # Пауза для уменьшения нагрузки на процессор
            # Проверяем, изменился ли URL или заголовок страницы
            if self.driver.current_url != last_url or self.driver.title != last_title:
                last_url = self.driver.current_url
                last_title = self.driver.title
            else:
                # Если URL и заголовок не изменились, значит страница стабилизировалась
                break
        else:
            print("Время ожидания истекло!")