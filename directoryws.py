from selenium import webdriver
import time
from read import get_data
from selenium.webdriver.support.ui import Select




web = webdriver.Chrome()
web.get('http://www.directoryws.com/submit.php')
web.maximize_window()

data = get_data()



for i in data.index:

    
    entry = data.loc[i]

    link = web.find_element_by_css_selector('input[type="radio"][value="free"]')
    link.click()

    title = web.find_element_by_name('TITLE')
    title.clear()
    title.send_keys(entry['Title'])

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

    s1= Select(web.find_element_by_name('CATEGORY_ID'))
    s1.select_by_value('24')

    submit = web.find_element_by_css_selector('input[type="submit"][value="Continue"]')
    submit.click()
    #driver.find_element_by_class_name('ytd-searchbox').clear()

    time.sleep(5)

print('process completed')
web.close()

