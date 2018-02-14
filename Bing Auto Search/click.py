import random
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os

login = False
count = 0
searches_to_make = 55
custom_list = True
search_list = ['playstation', 'nintendo', 'xbox', 'switch', 'nintendo switch']
server = 'https://www.bing.com'
chrome = webdriver.Chrome()
chrome.get(server)
currenturl = (chrome.current_url)


def auto_search(search):
    print('Searching for ' + search)
    chrome.find_element_by_id('sb_form_q').clear()
    chrome.find_element_by_id('sb_form_q').click()
    chrome.find_element_by_id('sb_form_q').send_keys(search)
    chrome.find_element_by_id('sb_form_q').submit()


if custom_list == True:
    try:
        list = open('words.txt', 'r')
    except:
        list = open('list.txt', 'r')
    list = list.read()
    search_list = list.split('\n')


while currenturl != 'https://www.bing.com/?wlexpsignin=1':
    currenturl = str(chrome.current_url)
else:
#    for search in search_list:
    while count < searches_to_make:
        search = random.choice(search_list)
        auto_search(search)
        time.sleep(2)
        count += 1
    print('Your ' + str(searches_to_make) + ' random searches are done.')

