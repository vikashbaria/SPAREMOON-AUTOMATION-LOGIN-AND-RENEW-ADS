from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException        
import time


print("Thanks for choosing Vikash Harjeewan for your automation task\n-----------------------------------------------------------")



# This function will open chorme browser then check login status 

username =""
password =""


driver = webdriver.Chrome(executable_path='C:/Users/Vikash/Desktop/Selenium/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get("https://www.spareroom.co.uk/flatshare/london/wimbledon_common")


def isDisplayed():
    try:
        driver.find_element_by_xpath("//*[@id='show-user-auth-popup']")
    except NoSuchElementException:
        return False
    return True

    #use function

if (isDisplayed() == True):
	element = driver.find_element_by_xpath('//*[@id="show-user-auth-popup"]').click()
	element = driver.find_element_by_id("loginemail")
	element.send_keys(username)
	element = driver.find_element_by_id("loginpass")
	element.send_keys(password)
	element.send_keys(Keys.RETURN)
	print("\n------------------Login successfully------------------\n")
else:
    print('Please check manually something went wrong')



#After login we will start pagination
for x in range(5):
    listingpage = "https://www.spareroom.co.uk/flatshare/mylistings.pl?offset=" + str(x*10)
    pagination = driver.get(listingpage)
    time.sleep(4)
    all_reviews = driver.find_elements_by_link_text("Renew")
    for review in all_reviews:
        renewlink = review.get_attribute('href')
        if renewlink !=  'https://www.spareroom.co.uk/flatshare/mylistings.pl?offset=0#' and renewlink != 'https://www.spareroom.co.uk/flatshare/mylistings.pl?offset=10#' and renewlink != 'https://www.spareroom.co.uk/flatshare/mylistings.pl?offset=20#' and renewlink != 'https://www.spareroom.co.uk/flatshare/mylistings.pl?offset=30#' and renewlink != 'https://www.spareroom.co.uk/flatshare/mylistings.pl?offset=40#':
                main_window= driver.current_window_handle
                driver.execute_script('''window.open("","_blank");''')
                driver.switch_to.window(driver.window_handles[1])
                driver.get(renewlink)
                time.sleep(2)
                driver.close()
                driver.switch_to.window(main_window)
print("Your Renew Task has been finished!")

