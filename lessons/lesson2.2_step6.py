from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "input_value")))
    y = calc(x.text)
    print(y)

    answer = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    browser.find_element_by_css_selector(".btn").click()

finally:
    time.sleep(10)
    browser.quit()