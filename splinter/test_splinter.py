from splinter import Browser
from time import sleep


browser = Browser("chrome")
browser.visit("https://a.libfintech.com/login")

text = browser.find_by_text('用户名')
