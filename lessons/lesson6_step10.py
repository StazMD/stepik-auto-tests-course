from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # browser.find_elements_by_xpath('//input[@required]').send_keys("Ivan")
    browser.find_element_by_css_selector('.first_block .first').send_keys("Name")
    browser.find_element_by_css_selector('.first_block .second').send_keys("Last Name")
    browser.find_element_by_css_selector('.first_block .third').send_keys("Email")
    browser.find_element_by_css_selector('.second_block .first').send_keys("Phone")
    browser.find_element_by_css_selector('.second_block .second').send_keys("Address")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
#
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
