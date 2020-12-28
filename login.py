from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import requests
import time


def login():
    usernamestr = 'admin'
    passwordstr = '123456aA'

    req = requests.get('http://45.79.43.178/source_carts/wordpress/wp-login.php')

    #Xu ly dang nhap va dien thong tin username, password
    browser = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')

    browser.get('http://45.79.43.178/source_carts/wordpress/wp-admin')

    username = browser.find_element_by_id('user_login')
    password = browser.find_element_by_id('user_pass')
    nextbutton = browser.find_element_by_id('wp-submit')

    username.send_keys(usernamestr)
    password.send_keys(passwordstr)
    nextbutton.click()

    #HTML
    cookie = browser.get_cookie('wordpress_logged_in_9b3f1ac684a4401c524e27c6c40e95d5')['value']
    print('Ten User vua Login: ')
    print(cookie.split('%')[0])


    time.sleep(1000)




if __name__ == '__main__':
    login()






