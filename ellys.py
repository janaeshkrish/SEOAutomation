from selenium import webdriver
import time
from read import get_data
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



web = webdriver.Chrome()
web.get('https://ellysdirectory.com/submit-link/')
web.maximize_window()


data = get_data()


for i in data.index:

    entry = data.loc[i]

    email = web.find_element_by_name('email')
    email.clear()
    email.send_keys(entry['Email Id'])

    page = web.find_element_by_name('pagename')
    page.clear()
    page.send_keys('Business-offshore', Keys.ENTER)


    title = web.find_element_by_name('linktitel')
    title.clear()
    title.send_keys(entry['Title'])

    url = web.find_element_by_name('linkurl')
    url.clear()
    url.send_keys(entry['URL'])


    time.sleep(1)
    description = web.find_element_by_xpath('//*[@id="linfo8"]/td[2]/textarea')
    description.clear()
    description.send_keys(entry['Description'])

    check_box = web.find_element_by_name('agreement')
    if check_box.is_selected() == False:
        check_box.click()

    time.sleep(1)


    submit = web.find_element_by_css_selector('input[type="button"][value="Request link"]')
    submit.click()
    #driver.find_element_by_class_name('ytd-searchbox').clear()

    time.sleep(5)

print('process completed')
web.close()

