from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.jd.com/?cu=true')
driver.find_element_by_class_name("link-login").click()
