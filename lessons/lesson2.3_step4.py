from selenium import webdriver
import os
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn'))).click()

    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(2)


    x = browser.find_element_by_id('input_value')
    y = calc(x.text)
    browser.find_element_by_id('answer').send_keys(y)

    browser.find_element_by_css_selector(".btn").click()

    # WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//input[@name="lastname"]'))).send_keys('Lastname')
    # WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//input[@name="email"]'))).send_keys('email@email.com')
    #
    # current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, 'maibcr.txt')  # добавляем к этому пути имя файла
    # element = browser.find_element_by_id('file') #находим кнопку на странице
    # element.send_keys(file_path) #цепляем файл


finally:
    time.sleep(10)
    browser.quit()