from pytesseract import image_to_string
from selenium import webdriver
import pytesseract
import time
from read import get_data
import cv2
from selenium.webdriver.support.ui import Select


web = webdriver.Chrome()
web.get('https://www.usawebsitesdirectory.com/submit.php')
web.maximize_window()



data = get_data()



def get_captcha_text(location, size):

    pytesseract.pytesseract.tesseract_cmd = 'tesseract.exe'
    im_gray = cv2.imread('screenshot.png',0)
    captcha_text = image_to_string(im_gray)
    return captcha_text




for i in data.index:

    entry = data.loc[i]

    link = web.find_element_by_css_selector('input[type="radio"][value="normal"]')
    link.click()

    title = web.find_element_by_name('TITLE')
    title.clear()
    title.send_keys(entry['Title'])

    check_box = web.find_element_by_name('AGREERULES')
    if check_box.is_selected() == False:
        check_box.click()

    url = web.find_element_by_name('URL')
    url.clear()
    url.send_keys(entry['URL'])

    description = web.find_element_by_name('DESCRIPTION')
    description.clear()
    description.send_keys(entry['Description'])

    meta_key = web.find_element_by_name('META_KEYWORDS')
    meta_key.clear()
    meta_key.send_keys(entry['Keyword'])

    meta_des = web.find_element_by_name('META_DESCRIPTION')
    meta_des.clear()
    meta_des.send_keys(entry['Meta Description'])

    name = web.find_element_by_name('OWNER_NAME')
    name.clear()
    name.send_keys(entry['Name'])

    email = web.find_element_by_name('OWNER_EMAIL')
    email.clear()
    email.send_keys(entry['Email Id'])

    s1= Select(web.find_element_by_name('CATEGORY_ID'))
    s1.select_by_value('420')


    time.sleep(2)

    #screenshot of image and captcha retreval 
    element = web.find_element_by_class_name('captcha')
    location = element.location
    #print(location)   
    size = element.size
    #print(size) 
    element.screenshot('screenshot.png')

    time.sleep(2)
    captcha = web.find_element_by_name('CAPTCHA')
    captcha.clear()    
    captcha_text = get_captcha_text(location, size)
    time.sleep(1)
    captcha.send_keys(captcha_text)
    #print(captcha_text)

    time.sleep(4)


    submit = web.find_element_by_css_selector('input[type="submit"][value="Continue"]')
    submit.click()

    time.sleep(2)


print('process completed')
web.close()

