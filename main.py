from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://food.semnan.ac.ir/')


username = driver.find_element(By.ID, 'username')
username.clear()
username.send_keys('40111360006')


password = driver.find_element(By.ID, 'password')
password.clear()
password.send_keys('Paypal5563#')


btn_login = driver.find_element(By.CLASS_NAME, 'btn') #weak - change it 
btn_login.send_keys(Keys.ENTER)

driver.get('https://food.semnan.ac.ir/#!/Reservation')

print(driver.find_element(By.XPATH, '//a[@href="' + '#tab_day3' + '"]'))

# week_day = driver.find_element(By.CSS_SELECTOR, "label[href='#tab_day3']")
# week_day = driver.find_element(By.CSS_SELECTOR, "label[value='#tab_day3']")
# week_day = driver.find_element(By.TAG_NAME, '#tab_day3')


# first = driver.find_element(By.TAG_NAME, '#tab_day3')


# articles = main.find_elements_by_tag_name("article")
# for article in articles:
# header = article.find_element_by_class_name("entry-summary")
# print(header.text)

time.sleep(100)


