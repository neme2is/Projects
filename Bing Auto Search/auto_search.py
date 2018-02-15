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


count = 0
searches_to_make = input('How many searches do you want to run? ')
custom_list = True
search_list = ['playstation', 'nintendo', 'xbox', 'switch', 'nintendo switch']
server = 'https://www.bing.com'
chrome = webdriver.Chrome()
chrome.get(server)
currenturl = (chrome.current_url)


def auto_search(search_word):
    print('Searching for ' + search)
    chrome.find_element_by_id('sb_form_q').clear()
    chrome.find_element_by_id('sb_form_q').click()
    chrome.find_element_by_id('sb_form_q').send_keys(search_word)
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
    while count < searches_to_make:
        search = random.choice(search_list)
        auto_search(search)
        time.sleep(2)
        count += 1
    print('Your ' + str(searches_to_make) + ' random searches are done.\nClosing the browser automatically in 10 seconds.')
    time.sleep(10)
    chrome.quit()