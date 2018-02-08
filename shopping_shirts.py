
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests

correct = False
load = ''
server = ''
region = ''
browser = ''
test_shopping = True


# find and fill out login info.
def login(email, password, login_button, email_field, password_field, submit_button):
    print('Logging in...')
    try:
        browser.find_element_by_class_name(login_button).click()
    except:
        browser.find_element_by_id(login_button).click()
    browser.find_element_by_id(email_field).click()
    browser.find_element_by_id(email_field).send_keys(email)
    browser.find_element_by_id(password_field).click()
    browser.find_element_by_id(password_field).send_keys(password)
    try:
        browser.find_element_by_css_selector(submit_button).click()
    except:
        browser.find_element_by_id(submit_button).click()
    print('Log In complete.')
    time.sleep(5)
    # what to test after log in.
    if test_shopping == True:
        check_shopping()



def logout(change_user, logout_button):
    print('Logging out...')
    WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.ID, change_user)))
    browser.find_element_by_id(change_user).click()
    WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.ID, logout_button)))
    browser.find_element_by_id(logout_button).click()


# load clothing store
def check_shopping():
    print('Beginning to test shopping...')
    clothing_store_url = server + '/html5#abc/sitemap/shopplaza?state=girl_item_store&zone=costumes&full_screen=true'
    browser.get(clothing_store_url)
    time.sleep(10)
    r = requests.post('https://www.abcmouse.com/apis/abc/0.1/json/Shopping/GetCategoryItems/init')
    print(r.status_code)
    print(r.json())


while correct == False:
    load_browser = input('What browser do you want to run? ')
    load = load_browser.lower()
    environment = input('What server to you want to access? ')
    if environment == 'live':
        environment = 'www'
        region = 'com'
    elif environment == 'www':
        region = 'com'
    elif environment == 'jp':
        region = 'jp'
    else:
        environment = environment + '.qtest'
        if 'jp' in environment:
            region = 'jp'
        else:
            region = 'com'
    server = 'https://' + environment + '.abcmouse.com'
    print('\nLoading ' + server + ' with ' + load_browser + ':')
    answer = input('Is this correct? ')
    if answer == 'yes':
        correct = True
    elif answer == 'no':
        correct = False
    else:
        correct = False
        print("Sorry, I didn't get that...try again.")


# load browser
if load == 'firefox':
    print('Loading browser...')
    browser = webdriver.Firefox()
    browser.get(server)
if load == 'chrome':
    print('Loading browser...')
    browser = webdriver.Chrome()
    browser.get(server)
if load == 'ie':
    print('Loading browser...')
    browser = webdriver.Ie()
    browser.get(server)


# enter account using: email, password, login_button, email_field, password_field, submit_button
if region == 'com':
    login('live@ftest.com', 'test123', 'button_shadow', 'login_email', 'login_password', 'input.submit_button.aofl_century_bold')
elif region == 'jp':
    login('live@ftest.jp', 'test123', 'page-login-button', 'login-email-field', 'login-password-field', 'login-submit')


# log out
#if region == 'com':
#    logout('btn-changeuser', 'change_user_leftside_logout')
#elif region == 'jp':
#    logout('option-btn-change', 'change_user_leftside_logout')
#print('You have now logged out.')