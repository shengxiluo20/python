from selenium import webdriver

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get('https://www.jd.com/?cu=true')
driver.find_element_by_class_name("link-login").click()
driver.find_element_by_link_text("账户登录").click()

driver.find_element_by_id("loginname").send_keys("123")
driver.find_element_by_id("nloginpwd").send_keys("123")

by_id = driver.find_element_by_id("JD_Verification1")
print(len(by_id))
if len(by_id) == 1:
    print(by_id)
    name = input("请手动输入验证码.....")
    driver.find_element_by_id("authcode").send_keys(name)

driver.find_element_by_id("loginsubmit").click()
