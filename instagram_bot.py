from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import random
from data_instagram import login, password
import pickle

'''Program for logining in instagram and dump/load cookies'''


class InstagramBot:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        options = webdriver.ChromeOptions()
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36')
        options.add_argument(
            'accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,\
            image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
        options.add_argument('--disable-blink-features=AutomationControlled')
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(
            executable_path=r"chromedriver\chromedriver.exe",
            options=options
        )

    def close_driver(self):
        self.driver.close()
        self.driver.quit()

    def login_instagram(self):
        driver = self.driver

        # Вход в инстаграм
        driver.get(url='https://www.instagram.com/')
        driver.implicitly_wait(10)

        time.sleep(random.randrange(2, 4))

        # Логин
        email_input = driver.find_element_by_name('username')
        email_input.clear()
        email_input.send_keys(login)

        # Пароль
        password_input = driver.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)

        time.sleep(1)

        # Кнопка вход
        password_input.send_keys(Keys.ENTER)
        driver.implicitly_wait(15)

        time.sleep(2)

    def dump_cookies(self):
        driver = self.driver

        # Дамп куки
        pickle.dump(driver.get_cookies(), open('instagram_cookies', 'wb'))

    def login_with_cookies(self):
        driver = self.driver

        # Подгрузка куки
        for cookie in pickle.load(open('instagram_cookies', 'rb')):
            driver.add_cookie(cookie)

        time.sleep(2)
        driver.refresh()
        time.sleep(1)


instabot = InstagramBot(login, password)
instabot.login_with_cookies()
instabot.close_driver()
