from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

correct = False
load = ''
answer = ''
server = ''

#if correct == False:
if not correct:
    load = input('What browser do you want to run? ')
    environment = input('What server to you want to access? ')
    region = input('Which account to login with? (com/jp) ')
    server = 'https://' + environment + '.abcmouse.com'
    print()
    print('Loading ' + server + ' with ' + load + ':' )
    answer = input('Is this correct? ')


if answer == 'yes':
    correct = True
if answer == 'no':
    correct = False


def login():
    #linkElem = browser.find_element_by_class_name('button_shadow').click() #find link/button by class
    browser.find_element_by_class_name('button_shadow').click() #find link/button by class
    browser.find_element_by_id('login_email').click()
    browser.find_element_by_id('login_email').send_keys(loginEmail)
    browser.find_element_by_id('login_password').click()
    browser.find_element_by_id('login_password').send_keys(loginPass)
    browser.find_element_by_css_selector('input.submit_button.aofl_century_bold').click()


def logout():
    WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.ID, "btn-changeuser")))
    browser.find_element_by_id('btn-changeuser').click()
    WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.ID, "change_user_leftside_logout")))
    browser.find_element_by_id('change_user_leftside_logout').click()


def shellButtons():
    browser.find_element_by_id("btn-home").click()


# load Firefox browser
if load == 'firefox':
    browser = webdriver.Firefox()
    browser.get(server)
if load == 'chrome':
    browser = webdriver.Chrome()
    browser.get(server)

# login with a US or JP account
if region == 'com':
    loginEmail = 'live@ftest.com'
    loginPass = 'test123'
    login()
elif region == 'jp':
    loginEmail = 'live@ftest.jp'
    loginPass = 'test123'
    login()
