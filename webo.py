from selenium import webdriver
import time
from read import get_data
from selenium.webdriver.support.ui import Select

web = webdriver.Chrome()
web.get('https://weboworld.com/item/submit')
web.maximize_window()


data = get_data()


for i in data.index:

    entry = data.loc[i]

    link = web.find_element_by_css_selector('input[type="radio"][value="1"]')
    link.click()

    title = web.find_element_by_name('title')
    title.clear()
    title.send_keys(entry['Title'])

    url = web.find_element_by_name('url')
    url.clear()
    url.send_keys(entry['URL'])


    url1 = web.find_element_by_name('display_url')
    url1.clear()
    url1.send_keys(entry['URL'])

    description = web.find_element_by_name('description1')
    description.clear()
    description.send_keys(entry['Description'])


    s1= Select(web.find_element_by_name('category'))
    s1.select_by_value('59')

    name = web.find_element_by_name('name1')
    name.clear()
    name.send_keys(entry['Name'])

    email = web.find_element_by_name('email')
    email.clear()
    email.send_keys(entry['Email Id'])


    time.sleep(1)

    submit = web.find_element_by_xpath('//*[@id="item_submit"]/div/div[1]/div[1]/div/div[2]/div[3]/button')
    submit.click()

    time.sleep(5)

    web.get('https://weboworld.com/item/submit')
    time.sleep(1)

    
print('Finished process')

web.close()





