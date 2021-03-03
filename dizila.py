from selenium import webdriver
import time
from read import get_data
from selenium.webdriver.support.ui import Select
import time


web = webdriver.Chrome()
web.get('https://www.dizila.com/submit?c=27&LINK_TYPE=1.')
web.maximize_window()
data = get_data()



for i in data.index:

    entry = data.loc[i]

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
    name.send_keys(entry['Keyword'])

    email = web.find_element_by_name('OWNER_EMAIL')
    email.clear()
    email.send_keys(entry['Email Id'])

    check = web.find_element_by_name('AGREERULES')
    value = check.is_selected()
    if value == False:

        check.click()

    #//*[@id="submitForm"]/div/div[9]/div/input
    submit = web.find_element_by_name('continue')
    submit.click()
    
    time.sleep(5)

print('Process Finished')
web.close()

