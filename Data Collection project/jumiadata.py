"""
Created on Thu Apr  8 09:06:12 2021

@author: Henry Chuks
"""


#importing libraries
from openpyxl import Workbook
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib
from email.message import EmailMessage
from selenium.webdriver.chrome.options import Options


opt = Options()
opt.add_argument("--headless")

#initializing the driver and opening url
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)
driver.maximize_window()
driver.get("https://www.jumia.com.ng/")
driver.implicitly_wait(10)
time.sleep(5)
driver.find_element(By.XPATH, "//input[contains(@id, 'fi-q')]").send_keys("samsung phones")
driver.find_element(By.XPATH, "//button[contains(@class, 'btn _prim _md -mls -fsh0')]").click()

#creating empty list for phone names, prices and ratings
phonesList = []
ratingsList = []
priceList = []

#This function will be getting the actual data from each page for every device clicked
#and then appending the data gotten into the empty list as defined above
def get_data(phone_name, price, ratings): #function to get phone name, price and ratings for each samsung device
    try:
        phonenames = driver.find_element(By.XPATH, str(phone_name))
        phonesList.append(phonenames.text)
    except NoSuchElementException:
        phonenames = 'Nan'
        phonesList.append(phonenames)
    
    try:
        prices = driver.find_element(By.XPATH, str(price))
        priceList.append(prices.text)
    except NoSuchElementException:
        prices = 'Nan'
        priceList.append(prices)
        
    try:
        rating = driver.find_element(By.XPATH, str(ratings))
        ratingsList.append(rating.text)
    except NoSuchElementException:
        rating = 'Nan'
        ratingsList.append(rating)
    
    #priceList.pop()
        
"""
The function below is literally just to deal wth the stale element reference exception
"""
def get_page():
    try:
        get_data('//h1[@class="-fs20 -pts -pbxs"]', '//*[@id="jm"]/main/div[2]/section/div/div[2]/div[2]/div[3]/span',
                 '//*[@id="jm"]/main/div[2]/section/div/div[2]/div[2]/div[2]/div')
    except StaleElementReferenceException:
        get_data('//h1[@class="-fs20 -pts -pbxs"]', '//*[@id="jm"]/main/div[2]/section/div/div[2]/div[2]/div[3]/span',
                 '//*[@id="jm"]/main/div[2]/section/div/div[2]/div[2]/div[2]/div')

#This function will click on every device on the each page and get data with the get_data() function defined above       
def click_main():
    main = driver.find_elements(By.XPATH, '//div[@class="info"]')
    for c in range(1,len(main)+1):
        click_on = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article['+str(c)+']/a/div[2]'))
        )
        driver.execute_script("arguments[0].click();", click_on)
        #click_on.click()
        get_page()
        time.sleep(3)
        driver.execute_script("window.history.go(-1)")
        time.sleep(2)
 
#this will scrap the first page loaded
click_main()      
#get_data('//h3[contains(@class, "name")]', 'prc', 'stars _s') #ignore please

"""
the following try and except blocks will be responsible for clicking through the next pages after scraping each page
until it gets to the fifth page
"""
try:
    element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/section/div[2]/a[4]"))
    )
    driver.execute_script("arguments[0].click();", element)
    print("Collected data on First page")
except ElementClickInterceptedException:
    try:
        nextPage = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pg:nth-child(4)"))
        )
        driver.execute_script("arguments[0].click();", nextPage)
        print("Collected data on first page by Second try")
    except Exception as e:
        print("Driver couldn't reach the second page")
        print(e)
time.sleep(5)
click_main()

try:
    pageThree = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="jm"]/main/div[2]/div[3]/section/div[2]/a[5]'))
    )
    driver.execute_script("arguments[0].click();", pageThree)
    print("Collected data on Second page")
except ElementClickInterceptedException:
    print("Driver couldn't reach the third page")
    driver.quit()
time.sleep(5)
click_main()

try:
    pageFour = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="jm"]/main/div[2]/div[3]/section/div[2]/a[5]'))
    )
    driver.execute_script("arguments[0].click();", pageFour)
    print("Collected data on Third page")
except ElementClickInterceptedException:
    print("Driver couldn't reach the fourth page")
    driver.quit()
time.sleep(5)
click_main()

try:
    pageFive = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="jm"]/main/div[2]/div[3]/section/div[2]/a[5]'))
    )
    driver.execute_script("arguments[0].click();", pageFive)
    print("Collected data on Fourth page")
except ElementClickInterceptedException:
    print("Driver couldn't reach the fifth page")
    driver.quit()
time.sleep(5)
click_main()

print("Collected data on the fifth page")

print("Done!")


"""
The section above from line 92 to 149 would actually be a good part to implement the python loop, for loop to be precise, which I have also
written in a seperate file, it was only done this way given the few number of pages to be scraped, however if there were about a tens
of a bigger amount of pages to be scraped then the for loop which I ve written as is also part this github repo as "the for loop" should definitely
be implemented otherwise
"""

print(len(phonesList))
print(len(priceList))
print(len(ratingsList))

"""
The following 'if else' block will be responsible for creating and putting the scrapped data into as excel file and sending to the special
email address which is mine too, just to showcase it
But first it will compare the lengths of the price list, phone list and rating list to check if they are equal
because if not, then the finallist created to zip them will be inaccurate and hence will cause analytical error if the data should be used for
analysis
"""


if len(phonesList)==len(priceList) and len(phonesList)==len(ratingsList) and len(priceList)==len(ratingsList):
    finallist = zip(phonesList, priceList, ratingsList)
    
    wb = Workbook()
    wb['Sheet'].title = 'Jumia Samsung Data'
    sh1 = wb.active
    sh1.append(['Name', 'Price', 'Ratings'])
    
    for x in list(finallist):
        sh1.append(x)
        
    wb.save("JumiaSamsungData.xlsx")
    
    print("Sending Email...\n")
    password = input("Type password here and press enter: ")
    
    msg = EmailMessage()
    msg['Subject'] = 'Scraped Data on Samsung phones from jumia.com'
    msg['From'] = 'HENRY.ANG'
    msg['To'] = 'henrychukwu134@gmail.com'
    
    with open('EmailTemplate') as file:
        data = file.read()
        msg.set_content(data)
        
    with open('JumiaSamsungData.xlsx', 'rb') as f:
        file_data = f.read()
        file_name = f.name
        print("File name is ",file_name)
        msg.add_attachment(file_data,maintype="multipart",subtype="xlsx",filename=file_name)
        
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login("barrychukwu12@gmail.com", password)
        server.send_message(msg)

    print('Email Sent !!!')

else:
    print("Failed to create an Excel file and Email not sent")
    pass
