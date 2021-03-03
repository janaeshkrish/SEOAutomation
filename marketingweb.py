from selenium import webdriver
import time
from read import get_data
from selenium.webdriver.support.ui import Select
from pytesseract import image_to_string 
from PIL import Image 
from selenium import webdriver
import pytesseract
import cv2
import numpy as np


web = webdriver.Chrome()
web.get('https://www.marketingwebdirectory.com/submit?c=27&LINK_TYPE=1')
web.maximize_window()


data = get_data()


def get_captcha_text(location, size):
    pytesseract.pytesseract.tesseract_cmd = 'tesseract.exe'
    im_gray = cv2.imread('screenshot.png',0)
    captcha_text = image_to_string(im_gray,config='digits')
    return captcha_text


for i in data.index:
    entry = data.loc[i]
    time.sleep(1)

    title = web.find_element_by_name('TITLE')
    title.clear()
    title.send_keys(entry['Title'])

    check_box = web.find_element_by_name('AGREERULES')
    #check_box.clear()
    print(check_box.is_selected())
    if check_box.is_selected() == False:
        check_box.click()

    url = web.find_element_by_name('URL')
    url.clear()
    url.send_keys(entry['URL'])

    description = web.find_element_by_name('DESCRIPTION')
    description.clear()
    description.send_keys(entry['Description'])

    name = web.find_element_by_name('OWNER_NAME')
    name.clear()
    name.send_keys(entry['Name'])

    email = web.find_element_by_name('OWNER_EMAIL')
    email.clear()
    email.send_keys(entry['Email Id'])


    #screenshot of image and captcha retreval 
    element = web.find_element_by_class_name('captcha')
    location = element.location
    print(location)   
    size = element.size
    print(size) 
    element.screenshot('screenshot.png')

    captcha = web.find_element_by_name('CAPTCHA')
    captcha.clear()    
    captcha_text = get_captcha_text(location, size)
    captcha.send_keys(captcha_text)
    time.sleep(1)
    print(captcha_text)

    time.sleep(2)

    
    submit = web.find_element_by_xpath('//*[@id="submitForm"]/div/div[11]/div/input')
    submit.click()

    time.sleep(5)

print('process finished')
web.close()


