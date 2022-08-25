import time
import random
import requests
import json
import fake_useragent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def start():
    working_mode = input(
        "Hello, if you want to register new account - enter '1', if you want to sign in account and take token - enter '2': ")
    if working_mode == '1':
        registration()
    elif working_mode == '2':
        authorization()


def registration():
    user_email = input("Enter your email: ")
    user_nickname = input("Enter your nickname: ")
    user_password = ''
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for el in range(16):
        user_password += random.choice(chars)
    print("Your generated password is: " + user_password)

    user = fake_useragent.UserAgent().random
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user}')
    try:
        driver.get("https://discord.com/register")
        time.sleep(5)

        email_input = driver.find_element(by=By.NAME, value="email")
        email_input.send_keys(user_email)
        time.sleep(5)

        nickname_input = driver.find_element(by=By.NAME, value="username")
        nickname_input.send_keys(user_nickname)
        time.sleep(5)

        password_input = driver.find_element(by=By.NAME, value="password")
        password_input.send_keys(user_password)
        time.sleep(5)

        b_day_input = driver.find_element(by=By.XPATH,
                                          value='//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/form/div/div/fieldset/div[1]/div[1]/div/div/div/div/div[1]')
        b_day_input.click()
        day_click_elm = driver.find_element(by=By.CLASS_NAME, value='css-dwar6a-menu')
        day_click_elm.click()
        time.sleep(5)

        b_month_input = driver.find_element(by=By.XPATH,
                                            value='//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/form/div/div/fieldset/div[1]/div[2]/div/div/div/div/div[1]')
        b_month_input.click()
        month_click_elm = driver.find_element(by=By.CLASS_NAME, value='css-dwar6a-menu')
        month_click_elm.click()
        time.sleep(5)

        b_year_input = driver.find_element(by=By.XPATH,
                                           value='//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/form/div/div/fieldset/div[1]/div[3]/div/div/div/div/div[1]')
        b_year_input.click()
        year_click_elm = driver.find_element(by=By.XPATH, value='//*[@id="react-select-4-input"]')
        year_click_elm.send_keys("2000")
        time.sleep(5)

        register_button = driver.find_element(by=By.XPATH,
                                              value='//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/form/div/div/div[5]/button')
        register_button.click()
        time.sleep(10)

        kapcha_btn = driver.find_element(by=By.XPATH,
                                         value='//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/section/div/div[2]/div')
        kapcha_btn.click()

        time.sleep(100)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def authorization():
    user_email = input("Enter your email: ")
    user_password = input('Enter your password: ')

    user = fake_useragent.UserAgent().random
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user}')
    try:
        driver.get("https://discord.com/login")
        time.sleep(5)

        email_input = driver.find_element(by=By.NAME, value='email')
        email_input.send_keys(user_email)
        time.sleep(5)

        password_input = driver.find_element(by=By.NAME, value='password')
        password_input.send_keys(user_password)
        time.sleep(5)

        enter_button = driver.find_element(by=By.XPATH,
                                           value='//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]')
        enter_button.click()
        time.sleep(10)

        url = "https://discord.com/api/v9/auth/login"

        payload = json.dumps({
            "login": f"{user_email}",
            "password": f"{user_password}",
            "undelete": False,
            "captcha_key": None,
            "login_source": None,
            "gift_code_sku_id": None
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    start()
