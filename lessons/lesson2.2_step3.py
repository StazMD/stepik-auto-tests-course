from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num1 = num1.text
    n1 = int(num1)
    num2 = browser.find_element_by_id("num2")
    num2 = num2.text
    n2 = int(num2)
    sum = n1 + n2
    sumstr = str(sum)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(sumstr)

    browser.find_element_by_css_selector(".btn").click()

finally:
    time.sleep(5)
    browser.quit()



