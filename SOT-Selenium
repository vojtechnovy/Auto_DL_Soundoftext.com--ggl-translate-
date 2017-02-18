import time
from selenium import webdriver


wordList = ['put', 'your', 'words', 'here'] # input desired words

browser = webdriver.Chrome()  # download webdriver for Chrome and put it in the same directory as this py file

browser.get('http://soundoftext.com')

browser.find_element_by_xpath("//select[@name='lang']/option[text()='Korean']").click() # change to desired language

for i in wordList:
    time.sleep(0.2) # not necessary ot include this
    username = browser.find_element_by_id('input-text')
    username.send_keys(i)

    nextButton = browser.find_element_by_id('submit-text')
    nextButton.click()
