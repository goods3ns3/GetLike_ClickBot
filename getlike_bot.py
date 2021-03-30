from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import random
from data import loginst, passinst, login, password
import pickle

URL_Getlike = 'https://getlike.io/'
URL_Insta = 'https://www.instagram.com/'

options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36')
options.add_argument(
    'accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,\
    image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--headless')
driver = webdriver.Chrome(
    executable_path=r"chromedriver\chromedriver.exe",
    options=options
)


'''Instagram вход'''
# try:
#     # Вход в инстаграм
#     driver.get(url=URL_Insta)
#     driver.implicitly_wait(10)
#     time.sleep(random.uniform(0.8, 1.3))
#
#     # Логин
#     email_input = driver.find_element_by_name('username')
#     email_input.clear()
#     email_input.send_keys(loginst)
#     driver.implicitly_wait(10)
#     time.sleep(random.uniform(0.8, 1.3))
#
#     password_input = driver.find_element_by_name('password')
#     password_input.clear()
#     password_input.send_keys(passinst)
#     driver.implicitly_wait(10)
#     time.sleep(random.uniform(0.8, 1.3))
#
#     password_input.send_keys(Keys.ENTER)
#     driver.implicitly_wait(15)
#     time.sleep(random.uniform(2.1, 2.8))
#
#     # dump instagram cookies
#     pickle.dump(driver.get_cookies(), open('insta_cookies', 'wb'))
#
# except Exception as e:
#     print(e)
# finally:
#     driver.close()
#     driver.quit()
'''Instagram cookies'''
try:
    # Вход в инстаграм
    driver.get(url=URL_Insta)
    driver.implicitly_wait(10)
    time.sleep(random.uniform(0.8, 1.3))

    # load instagram cookies
    for cookie in pickle.load(open('insta_cookies', 'rb')):
        driver.add_cookie(cookie)

    time.sleep(2)
    driver.refresh()
    time.sleep(2)

except Exception as e:
    print(e)

'''GetLike вход'''
# try:
#     # Вход на гетлайк
#     driver.get(url=URL_Getlike)
#     driver.implicitly_wait(10)
#     time.sleep(random.uniform(0.8, 1.3))
#
#     # Логин
#     log_in = driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div[4]/a').click()
#     driver.implicitly_wait(10)
#     time.sleep(random.uniform(0.8, 1.3))
#
#     email_input = driver.find_element_by_id('User_loginLogin')
#     email_input.clear()
#     email_input.send_keys(login)
#     driver.implicitly_wait(10)
#     time.sleep(random.uniform(0.8, 1.3))
#
#     password_input = driver.find_element_by_id('User_passwordLogin')
#     password_input.clear()
#     password_input.send_keys(password)
#     driver.implicitly_wait(10)
#     time.sleep(random.uniform(20.2, 22.1))
#
#     login_button = driver.find_element_by_name('submitLogin').click()
#     driver.implicitly_wait(15)
#     time.sleep(random.uniform(1.1, 1.8))
#
#     # dump instagram cookies
#     pickle.dump(driver.get_cookies(), open('getlike_cookies', 'wb'))
#
# except Exception as e:
#     print(e)
# finally:
#     driver.close()
#     driver.quit()

'''GetLike cookies'''
try:
    # Вход на гетлайк
    driver.get(url=URL_Getlike)
    driver.implicitly_wait(10)
    time.sleep(random.uniform(0.8, 1.3))

    # load getlike cookies
    for cookie in pickle.load(open('getlike_cookies', 'rb')):
        driver.add_cookie(cookie)

    time.sleep(2)
    driver.refresh()
    time.sleep(2)

    # Логин
    log_in = driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div[4]/a').click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(0.8, 1.3))

    # Переход к серфингу
    driver.set_window_size(650, 350)
    driver.set_window_position(640, 0)
    # Биржа заданий
    driver.find_element_by_xpath('/html/body/div[6]/nav/div/div[1]/button').click()
    driver.implicitly_wait(15)
    time.sleep(random.uniform(2.1, 3.8))
    driver.find_element_by_xpath('/html/body/div[6]/aside[1]/div/div/div[4]').click()
    driver.implicitly_wait(15)
    time.sleep(random.uniform(2.1, 3.8))
    driver.find_element_by_xpath('/html/body/div[6]/aside[1]/div/div/div[4]/div[2]/div/a[1]').click()
    driver.implicitly_wait(15)
    time.sleep(random.uniform(2.1, 3.8))

    for x in range(10):

        # Инстаграм подписка
        driver.find_element_by_xpath('/html/body/div[6]/nav/div/div[1]/span/a').click()
        driver.implicitly_wait(15)
        time.sleep(random.uniform(2.1, 3.8))
        driver.find_element_by_xpath('/html/body/div[6]/nav/div/div[3]/ul/li[2]').click()
        driver.implicitly_wait(15)
        time.sleep(random.uniform(2.1, 3.8))
        for i in range(1, 21):
            try:
                # Клик по кнопке подписки
                driver.find_element_by_xpath(
                    f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i}]/div/div/div/div[4]/a').click()
                time.sleep(random.uniform(6.1, 6.8))
                driver.switch_to.window(driver.window_handles[1])
                driver.implicitly_wait(15)
                time.sleep(random.uniform(1.1, 1.8))
                driver.find_element_by_tag_name('button').click()
                time.sleep(random.uniform(1.1, 1.8))
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(random.uniform(0.3, 0.7))
                driver.find_element_by_xpath(
                    f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i}]/div/div/div/div[4]/a').click()
                print('Подписка обработана № ', i)
                time.sleep(random.uniform(5.1, 7.8))
            except Exception as e:
                print('Ошибка в подписках', e)

        time.sleep(5)

        # Инстаграм лайки
        driver.find_element_by_xpath('/html/body/div[6]/nav/div/div[1]/span/a').click()
        driver.implicitly_wait(15)
        time.sleep(random.uniform(2.1, 3.8))
        driver.find_element_by_xpath('/html/body/div[6]/nav/div/div[3]/ul/li[3]').click()
        driver.implicitly_wait(15)
        time.sleep(random.uniform(2.1, 3.8))
        for i in range(1, 21):
            try:
                # Клик по кнопке лайк
                driver.find_element_by_xpath(
                    f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i}]/div/div/div/div[4]/a').click()
                time.sleep(random.uniform(6.1, 6.8))
                driver.switch_to.window(driver.window_handles[1])
                driver.implicitly_wait(15)
                time.sleep(random.uniform(1.1, 1.8))
                driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
                time.sleep(random.uniform(1.1, 1.8))
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(random.uniform(0.3, 0.7))
                driver.find_element_by_xpath(
                    f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i}]/div/div/div/div[4]/a').click()
                print('Лайк обработан № ', i)
                time.sleep(random.uniform(5.1, 7.8))
            except Exception as e:
                print('Ошибка в лайках', e)
        time.sleep(random.uniform(3660.4, 3845.7))
        driver.refresh()

    time.sleep(5)

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
