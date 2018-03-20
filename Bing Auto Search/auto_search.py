########################################################################
# This will automatically complete as many random searches
# that you specify in "searches_to_make" using a custom list
# which pulls words from the text file (words.txt or list.txt)
# if "custom_list = True". Otherwise it will run a search with
# whatever is in "search_list".
#
# Make sure to list how many searches you want ot make.
# the default is set to 55 which should be enough for Bing Rewards.
#
# When the page first loads you will need to click sign in and once you
# have entered your credentials you will be taken back to the search
# page and the script will being to auto search.
########################################################################

import random
import time
from selenium import webdriver


count = 1
#searches_to_make = input('How many searches do you want to run? ')
searches_to_make = 30
custom_list = True
search_list = ['playstation', 'nintendo', 'xbox', 'switch', 'nintendo switch']
server = 'https://www.bing.com'

currenturl = server

# chrome options for mobile device emulation
def browser(type):
    global server, chrome
    if 'desktop' == type:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('start-maximized')
        chrome = webdriver.Chrome()
        chrome.get(server)
    elif 'mobile' == type:
        mobile_emulation = { "deviceName": "Nexus 6P" }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome = webdriver.Chrome(chrome_options=chrome_options)
        chrome.get(server)
    return chrome

def edge():
    global server, chrome, count
    chrome = webdriver.Edge()
    chrome.get(server)
    #count = 1
    while count <= searches_to_make:
        search = random.choice(search_list)
        auto_search(search)
        time.sleep(2)
        count += 1
    print('Your ' + str(searches_to_make) + ' random searches are done.\nClosing the browser automatically in 10 seconds.')
    time.sleep(10)
    chrome.quit()
    #count = 0


def login(verison):
    if 'desktop' == verison:
        chrome.find_element_by_css_selector('#id_a').click()
        time.sleep(1)
        chrome.find_element_by_css_selector('#i0116').send_keys('michael.gavidia@gmail.com')
        chrome.find_element_by_css_selector('#idSIButton9').click()
    elif 'mobile' == verison:
        try:
            chrome.find_element_by_css_selector('#mHamburger').click()
        except:
            chrome.find_element_by_css_selector('#bnp_close_link > img').click()
            chrome.find_element_by_css_selector('#mHamburger').click()
        time.sleep(1)
        chrome.find_element_by_css_selector('#hb_s').click()
        time.sleep(1)
        chrome.find_element_by_css_selector('#i0116').send_keys('michael.gavidia@gmail.com')
        chrome.find_element_by_css_selector('#idSIButton9').click()

def auto_search(search_word):
    print('(' + str(count) + ')' + ' Searching for ' + search_word)
    chrome.find_element_by_id('sb_form_q').clear()
    chrome.find_element_by_id('sb_form_q').click()
    chrome.find_element_by_id('sb_form_q').send_keys(search_word)
    chrome.find_element_by_id('sb_form_q').submit()


def create_list():
    global search_list
    if custom_list == True:
        try:
            list = open('words.txt', 'r')
        except:
            print('File not found for search list: "words.txt"')
            quit()
        list = list.read()
        search_list = list.split('\n')


def check_url():
    global currenturl, count, search_list
    while currenturl != 'https://www.bing.com/?wlexpsignin=1':
        currenturl = chrome.current_url
    else:
        while count <= searches_to_make:
            search = random.choice(search_list)
            auto_search(search)
            time.sleep(2)
            count += 1
        print('Your ' + str(searches_to_make) + ' random searches are done.\nClosing the browser automatically in 10 seconds.')
        time.sleep(10)
        chrome.quit()
        count = 0
        currenturl = ''


create_list()
edge()

#browser('desktop')
#time.sleep(2)
#login('desktop')
#check_url()

browser('mobile')
time.sleep(3)
login('mobile')
check_url()

