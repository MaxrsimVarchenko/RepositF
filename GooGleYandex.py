from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


link = "https://www.google.com/"
y="https://yandex.ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    input1 = browser.find_element_by_class_name('gLFyf.gsfi')
    input1.send_keys(y)
    time.sleep(1)
    browser.find_elements_by_xpath("html.body.div[2].div[3].form.div[1].div[1].div[2].div[2].div[5].center.input[1]").click()
    time.sleep(1)
    assert browser.current_url =='https://yandex.ru/', 'Какая то хрень'



finally:
        time.sleep(10)
        browser.quit()

