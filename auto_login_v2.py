from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

correct = False
load = ''
server = ''
region = ''

# find and fill out login info.
def login(email, password, login_button, email_field, password_field, submit_button):
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


#
def logout(change_user, logout_button):
    WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.ID, change_user)))
    browser.find_element_by_id(change_user).click()
    WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.ID, logout_button)))
    browser.find_element_by_id(logout_button).click()


while correct == False:
    load = input('What browser do you want to run? ')
    environment = input('What server to you want to access? ')
    if environment == 'live':
        environment = 'www'
    elif environment == 'www':
        environment = 'www'
    elif environment == 'jp':
        environment = 'jp'
    else:
        environment = environment + '.qtest'
    server = 'https://' + environment + '.abcmouse.com'
    print('\nLoading ' + server + ' with ' + load + ':' )
    answer = input('Is this correct? ')
    if answer == 'yes':
        correct = True
        print('Loading browser...')
    elif answer == 'no':
        correct = False
    else:
        correct = False
        print("Sorry, I didn't get that...try again.")


# load browser
if load == 'firefox':
    browser = webdriver.Firefox()
    browser.get(server)
if load == 'chrome':
    browser = webdriver.Chrome()
    browser.get(server)
if load == 'ie':
    browser = webdriver.Ie()
    browser.get(server)


# check to see what server to be used and load that account's region
if 'jp' in environment:
    region = 'jp'
else:
    region = 'com'


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