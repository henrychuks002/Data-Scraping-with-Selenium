#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 09:06:12 2021

@author: Henry Chuks
"""
"""
This script is an associate of the jumiadata.py script just to show how else the entire line 92 to 149 of the jumiadata.py script could have been written
In essence, the entire line 92 to 149 in the jumiadata.py can be comfortably replaced with lines 33 to 44 on here
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.jumia.com.ng/")
driver.implicitly_wait(10)
time.sleep(5)
driver.find_element(By.XPATH, "//input[contains(@id, 'fi-q')]").send_keys("samsung phones")
driver.find_element(By.XPATH, "//button[contains(@class, 'btn _prim _md -mls -fsh0')]").click()

#say you want to scrape about a 50 pages of the website

#click_main() for getting the first page
#print("Collected data on page 1")
for i in range(2,51):
    try:
        element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="jm"]/main/div[2]/div[3]/section/div[2]/a[6]'))
        )
        driver.execute_script("arguments[0].click();", element)
        print("Collected data on page ",i)
    except ElementClickInterceptedException:
        print("Driver couldn't reach page ",i)
        pass
    time.sleep(5)
    #click_main() 


#click_main method above is commented out because the method is not included in this in particular script, but the jumiadata.py file also in this repo
#however it is a method that collects the data for each device from each page.
