from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import random
from data import login, password
import pickle


class GetlikeBot:

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
        self.driver = webdriver.Chrome(
            executable_path=r"chromedriver\chromedriver.exe",
            options=options
        )

    def load_instagram_account(self):
        driver = self.driver

        # Вход в инстаграм
        driver.get(url='https://www.instagram.com/')
        driver.implicitly_wait(10)
        time.sleep(1)

        # Подгрузка куки
        for cookie in pickle.load(open('instagram_cookies', 'rb')):
            driver.add_cookie(cookie)

        time.sleep(2)
        driver.refresh()
        time.sleep(1)

    def login_in_getlike(self):
        driver = self.driver

        # Вход на гетлайк
        driver.get(url='https://getlike.io/')
        driver.implicitly_wait(10)
        time.sleep(1)

        # Кнопка войти
        login_button = driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div[4]/a').click()
        driver.implicitly_wait(10)
        time.sleep(1)

        # Ввод логина
        email_input = driver.find_element_by_id('User_loginLogin')
        email_input.clear()
        email_input.send_keys(login)
        time.sleep(1)

        # Ввод пароля
        password_input = driver.find_element_by_id('User_passwordLogin')
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(random.randrange(20, 22))

        # Кнопка подтверждения
        submit_button = driver.find_element_by_name('submitLogin').click()
        driver.implicitly_wait(15)
        time.sleep(random.uniform(1.1, 1.8))

    def dump_cookies(self):
        driver = self.driver

        # Дамп куки
        pickle.dump(driver.get_cookies(), open('getlike_cookies', 'wb'))

    def login_with_cookies(self):
        driver = self.driver

        # Вход на гетлайк
        driver.get(url='https://getlike.io/')
        driver.implicitly_wait(10)
        time.sleep(1)

        # Подгрузка куки
        for cookie in pickle.load(open('getlike_cookies', 'rb')):
            driver.add_cookie(cookie)

        time.sleep(2)
        driver.refresh()
        time.sleep(1)

        # Кнопка войти
        login_button = driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div[4]/a').click()
        driver.implicitly_wait(10)
        time.sleep(1)

    def close_driver(self):
        driver = self.driver
        driver.close()
        driver.quit()

    def go_tasks(self):
        driver = self.driver

        # Биржа заданий
        driver.find_element_by_xpath('//*[@id="tasks-page"]/div[6]/nav/div/div[2]/ul[1]/li[2]').click()
        driver.implicitly_wait(15)
        time.sleep(random.randrange(2, 3))

    def go_instagram(self):
        driver = self.driver

        # Инстаграм
        driver.find_element_by_xpath('//*[@id="panelGroupMenu"]/div[2]').click()
        driver.implicitly_wait(15)
        time.sleep(random.randrange(1, 2))

    def go_instagram_subscribers(self):
        driver = self.driver

        # Инстаграм подписчики
        driver.find_element_by_xpath('//*[@id="list-3-3"]').click()
        driver.implicitly_wait(15)
        time.sleep(random.randrange(1, 2))

    def go_instagram_likes(self):
        driver = self.driver

        # Инстаграм лайки
        driver.find_element_by_xpath('//*[@id="list-3-1"]').click()
        driver.implicitly_wait(15)
        time.sleep(random.randrange(1, 2))

    def go_tiktok(self):
        driver = self.driver

        # Тикток
        driver.find_element_by_xpath('//*[@id="panelGroupMenu"]/div[3]').click()
        driver.implicitly_wait(15)
        time.sleep(random.randrange(1, 2))

    def go_tiktok_subscribers(self):
        driver = self.driver

        # Тикток подписчики
        driver.find_element_by_xpath('//*[@id="list-9-3"]').click()
        driver.implicitly_wait(15)
        time.sleep(random.randrange(1, 2))

    def go_tiktok_likes(self):
        driver = self.driver

        # Тикток лайки
        driver.find_element_by_xpath('//*[@id="list-9-1"]').click()
        driver.implicitly_wait(15)
        time.sleep(random.randrange(1, 2))

    def instasubscribe(self):
        driver = self.driver

        # Инстаподписка
        driver.find_element_by_tag_name('button').click()
        time.sleep(1)

    def instalike(self):
        driver = self.driver

        # Инсталайк
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
        time.sleep(1)

    def wait(self, time):
        driver = self.driver
        driver.implicitly_wait(time)

    def refresh(self):
        driver = self.driver
        driver.refresh()

    def find_by_xpath(self, xpath):
        driver = self.driver
        driver.find_element_by_xpath(xpath).click()
        time.sleep(1)

    def tab_amount(self):
        driver = self.driver
        return len(driver.window_handles)

    def switch_to_1(self):
        driver = self.driver
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)

    def switch_to_0(self):
        driver = self.driver
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def subscribing(self, xpath, i):
        driver = self.driver
        try:
            self.find_by_xpath(xpath)
            self.switch_to_1()
            driver.implicitly_wait(15)
            self.instasubscribe()
            time.sleep(1)
            self.switch_to_0()
            time.sleep(1)
            self.find_by_xpath(xpath)
            print('Подписка обработана №', i)
            time.sleep(5)
        except Exception as e:
            print('Подписка НЕ обработана №', i, e)
            if self.tab_amount() == 2:
                self.switch_to_0()
                self.find_by_xpath(xpath)
            time.sleep(2)

    def liking(self, xpath, i):
        driver = self.driver
        try:
            self.find_by_xpath(xpath)
            self.switch_to_1()
            driver.implicitly_wait(15)
            self.instalike()
            time.sleep(1)
            self.switch_to_0()
            time.sleep(1)
            self.find_by_xpath(xpath)
            print('Лайк обработан №', i)
            time.sleep(5)
        except Exception as e:
            print('Лайк НЕ обработан №', i, e)
            if self.tab_amount() == 2:
                self.switch_to_0()
                self.find_by_xpath(xpath)
            time.sleep(2)


def main():
    getlike = GetlikeBot(login, password)

    try:
        try:
            getlike.load_instagram_account()
        except Exception:
            print('Не удалось войти в инстаграм')
        try:
            getlike.login_with_cookies()
        except Exception:
            print('Не удалось войти в гетлайк')
        try:
            getlike.go_tasks()
            time.sleep(2)
        except Exception:
            print('Не удалось войти в биржу заданий')
        # try:
        #     getlike.go_instagram()
        #     time.sleep(3)
        # except Exception:
        #     print('Не удалось войти в раздел инстаграма')
        while True:
            # Подписки инстаграм
            getlike.go_instagram_subscribers()
            time.sleep(3)
            getlike.wait(5)
            for i in range(1, 21):
                getlike.subscribing(
                    f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i}]/div/div/div/div[4]', i)

            time.sleep(5)

            # Лайки инстаграм
            getlike.go_instagram_likes()
            time.sleep(3)
            getlike.wait(5)
            for i in range(1, 11):
                getlike.liking(
                    f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i}]/div/div/div/div[4]', i)

            time.sleep((random.randrange(3660, 3845)))
            getlike.refresh()
            getlike.wait(5)
    except Exception as e:
        print('Программа завершилась по причине:', e)
    finally:
        getlike.close_driver()


if __name__ == '__main__':
    main()
