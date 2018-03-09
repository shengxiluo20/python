from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get('https://www.jd.com/?cu=true')
driver.find_element_by_class_name("link-login").click()
driver.find_element_by_link_text("账户登录").click()

driver.find_element_by_id("loginname").send_keys("111")

driver.find_element_by_id("nloginpwd").send_keys("111")

by_id = driver.find_element_by_id("JD_Verification1")
name = input("请手动输入验证码.....")
driver.find_element_by_id("authcode").send_keys(name)

driver.find_element_by_id("loginsubmit").click()

sleep(3)
driver.get("https://order.jd.com/center/list.action")
driver.find_element_by_link_text("收货地址").click()
sleep(3)
driver.find_element_by_link_text("新增收货地址").click()
