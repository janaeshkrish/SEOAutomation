from selenium import webdriver
import time
from read import get_data
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


web = webdriver.Chrome()
web.get('https://www.advertiseera.com/post-an-ad.php')
web.maximize_window()

data = get_data()


for i in data.index:

    entry = data.loc[i]


    element = WebDriverWait(web, 10).until(
                EC.presence_of_element_located((By.ID, "catId"))
            )

    s1= Select(web.find_element_by_name('catId'))
    s1.select_by_value('54')

    #submit = web.find_element_by_css_selector('input[type="submit"][value="Continue"]')
    #submit = web.find_element_by_class_name('btnbtn-default')
    
    #submit =  web.find_element_by_xpath('//*[@id="item-post"]/div/div[2]/div/button')
    submit = web.find_element_by_css_selector('.btn btn-default')
    submit.click()

    element = WebDriverWait(web, 10).until(
                EC.presence_of_element_located((By.NAME, "title"))
            )


    title = web.find_element_by_id('titleen_US')
    title.clear()
    title.send_keys(entry['Title'])

    description = web.find_element_by_id('descriptionen_US')
    description.clear()
    description.send_keys(entry['Description'])


    #//*[@id="item-post"]/div/div[2]/div/button

    submit =  web.find_element_by_xpath('//*[@id="item-post"]/div/div[2]/div/button')
    submit.click()

    element = WebDriverWait(web, 10).until(
                EC.presence_of_element_located((By.NAME, "address"))
            )

    address = web.find_element_by_name('address')
    address.send_keys(entry['Address'])

    submit =  web.find_element_by_xpath('//*[@id="item-post"]/div/div[2]/div/button')
    submit.click()

    element = WebDriverWait(web, 10).until(
                EC.presence_of_element_located((By.NAME, "price"))
            )

    price = web.find_element_by_name('price')
    price.send_keys('0')

    time.sleep(2)

    submit =  web.find_element_by_xpath('//*[@id="item-post"]/div/div[2]/div/button')
    submit.click()


    element = WebDriverWait(web, 10).until(
                EC.presence_of_element_located((By.NAME, "contactName"))
            )

    name = web.find_element_by_name('contactName')
    name.clear()
    name.send_keys(entry['Name'])

    email = web.find_element_by_name('contactEmail')
    email.clear()
    email.send_keys(entry['Email Id'])

    #submit = web.find_element_by_css_selector('input[type="submit"][value="Continue"]')
    submit =  web.find_element_by_xpath('//*[@id="item-post"]/div/div/div[2]/div/button')
    submit.click()

    element = WebDriverWait(web, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "containernow"))
            )

    submit =  web.find_element_by_xpath('//*[@id="item-post"]/div[2]/div/div[2]/div/button')
    submit.click()

    element = WebDriverWait(web, 10).until(
                EC.presence_of_element_located((By.NAME, "countryId"))
            )

    s2= Select(web.find_element_by_name('countryId'))
    s2.select_by_value('IN')

    time.sleep(2)

    s3 = Select(web.find_element_by_xpath('//*[@id="regionId"]'))
    s3.select_by_visible_text('Tamil Nadu')

    time.sleep(2)
    s4 = Select(web.find_element_by_name('cityId'))
    s4.select_by_value('279723')

    time.sleep(2)
    submit = web.find_element_by_xpath('//*[@id="page-content"]/div/div/div/div/div[2]/div/div/form/div[5]/div/button')
    submit.click()

    element = WebDriverWait(web, 10).until(
                EC.presence_of_element_located((By.NAME, "qqfile"))
            )

    upload =  web.find_element_by_name('qqfile')

    upload.send_keys(os.getcwd()+'/mazelogo.jpg')


    time.sleep(2)
    submit =  web.find_element_by_xpath('//*[@id="item-post"]/div/div[2]/div/button')
    submit.click()

    time.sleep(4)

    web.get("https://www.advertiseera.com/post-an-ad.php")

    time.sleep(1)


print('process finished')
web.close()



















