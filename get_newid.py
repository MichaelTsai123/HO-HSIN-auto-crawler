from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime

def get_CID():


    driver = webdriver.Chrome(".\chromedriver.exe")

    CName = "名字"

    driver.maximize_window()
    driver.get("http://w3.loxa.com.tw/morisato/htdocs/SocialSecurityNumber/index.htm")
    driver.implicitly_wait(10)
    
    driver.find_element_by_id("Generate").click()
    
    CId = driver.find_element_by_id("sncode").get_attribute('value')
	
    return CId[0:10]
	
	