from selenium import webdriver
import time
from read import get_data
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys

web = webdriver.Chrome()
web.get('http://www.findsites.net/business-directory/?wpbdp_view=submit_listing')
web.maximize_window()



data = get_data()

for i in data.index:

    entry = data.loc[i]

    choose = web.find_element_by_id('select2-wpbdp-field-13-container')
    choose.click()

    time.sleep(1)
    
    category = web.find_element_by_class_name('select2-search__field')
    category.send_keys('Business Services')
    category.send_keys(Keys.ENTER)
    

    title = web.find_element_by_name('listingfields[12]')
    title.clear()
    title.send_keys(entry['Title'])

    url = web.find_element_by_name('listingfields[15][0]')
    url.clear()
    url.send_keys(entry['URL'])

    description = web.find_element_by_name('listingfields[14]')
    description.clear()
    description.send_keys(entry['Description'])

    email = web.find_element_by_name('listingfields[16]')
    email.clear()
    email.send_keys(entry['Email Id'])

    
    sum = web.find_element_by_xpath('//*[@id="wpbdp-submit-listing"]/form/div[2]/div[2]/div[5]/div[1]/label')
    val = str(sum.text[8:])
    out = eval(val)

    output = web.find_element_by_name('listingfields[17]')
    output.send_keys(out)

    time.sleep(2)
    submit = web.find_element_by_css_selector('input[type="submit"][value="Complete Listing"]')
    submit.click()

    time.sleep(2)

    web.get('http://www.findsites.net/business-directory/?wpbdp_view=submit_listing')

    time.sleep(4)


print('Process Finished')
web.close()



