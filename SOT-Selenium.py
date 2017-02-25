import time
from selenium import webdriver

# path to your txt file here with double "\\", here we want to work with utf8 encoding
word_file = open('C:\\Users\\antonin\\Desktop\\book2.txt', 'r',encoding='utf-8')

# Reading source file by lines and adding it to a list, no need to remove 
with word_file as f:
    lines = f.readlines()
  

# download webdriver for Chrome and put it in the same directory 
# as this py file or put path to the files into brackets below
browser = webdriver.Chrome('C:\\Users\\antonin\\PycharmProjects\\suresure\\chromedriver.exe') 


# Visit the website
browser.get('http://soundoftext.com')


# change 'Korean' to desired language; selects language from dropdown list
browser.find_element_by_xpath("//select[@name='lang']/option[text()='Korean']").click()

# adds lines from the file to the input line and hits submit
for i in lines:
    time.sleep(0.2) # not necessary ot include this
    username = browser.find_element_by_id('input-text')
    username.send_keys(i)

    nextButton = browser.find_element_by_id('submit-text')
    nextButton.click()
