from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    attrib = browser.find_element_by_id("treasure")
    x = attrib.get_attribute("valuex")
    # x = attrib.text
    # print(x)

    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    browser.find_element_by_css_selector(".btn").click()

finally:
    time.sleep(10)
    browser.quit()



