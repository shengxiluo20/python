from splinter import Browser
from time import sleep


browser = Browser("chrome")
browser.visit("https://www.jd.com/?cu=true")


browser.find_by_text("你好，请登录").click()

browser.find_by_text("账户登录").click()

browser.find_by_id("loginname").fill("1221")
browser.find_by_id("nloginpwd").fill("1221")

by_id = browser.find_by_id("JD_Verification1")

if by_id:
    name = input("请手动输入验证码.....")
    browser.find_by_id("authcode").fill(name)

browser.find_by_id("loginsubmit").click()

sleep(3)
browser.visit("https://order.jd.com/center/list.action")
sleep(3)
browser.find_by_text("收货地址").last.click()
sleep(3)
browser.find_by_text("新增收货地址").click()


