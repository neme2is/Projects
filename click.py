import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os

login = False
count = 0
timer = 30
search_list = ['playstation', 'nintendo', 'xbox', 'switch', 'nintendo switch']
server = 'https://www.bing.com'
chrome = webdriver.Chrome()
chrome.get(server)


def auto_search(search):
    print('Searching for ' + search)
    chrome.find_element_by_id('sb_form_q').clear()
    chrome.find_element_by_id('sb_form_q').click()
    chrome.find_element_by_id('sb_form_q').send_keys(search)
    chrome.find_element_by_id('sb_form_q').submit()


while login == False:
    list = open('list.csv', 'r')
    list = list.read()
    search_list = list.split('\n')
    time.sleep(30)
    login = True


for search in search_list:
#    url = chrome.getLocation()
#    print(url)
    auto_search(search)
    time.sleep(2)

