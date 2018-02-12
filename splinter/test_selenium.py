from time import sleep

from selenium import webdriver

ie = webdriver.Ie()
ie.get("http://www.baidu.com")

ie.find_element_by_id("kw").send_keys("selenium")
ie.find_element_by_id("su").click()