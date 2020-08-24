from selenium import webdriver
import os
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//input[@name="firstname"]'))).send_keys('Name')
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//input[@name="lastname"]'))).send_keys('Lastname')
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//input[@name="email"]'))).send_keys('email@email.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'maibcr.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_id('file') #находим кнопку на странице
    element.send_keys(file_path) #цепляем файл

    browser.find_element_by_css_selector(".btn").click()

finally:
    time.sleep(10)
    browser.quit()