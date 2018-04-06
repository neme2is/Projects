import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Search:
    def __init__(self):
        self.server = 'https://www.bing.com/'
        self.searches_to_make = 30
        self.count = 1

    def setup_browser(self, type):
        if 'chrome' == type:
            self.driver = webdriver.Chrome()
        elif 'edge' == type:
            self.driver = webdriver.Edge()
        elif 'mobile' == type:
            mobile_emulation = {"deviceName": "Nexus 6P"}
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        return self.driver

    def wait_until(self, selector):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_until_url_contains(self, url):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.url_contains(url))

    def click_element(self, selector):
        self.wait_until(selector)
        self.driver.find_element_by_css_selector(selector).click()

    def is_visible(self, selector):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def get_element(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def check_if_logged_in(self, type='main'):
        self.wait_until('#id_l')
        try:
            #self.get_element("#id_s")
            self.is_visible("#id_s")
            self.driver.get('https://login.live.com/')
            self.login(type)
        except:
            #self.get_element("#id_n")
            self.is_visible("#id_n")
            pass

    def login(self, type='main'):
        if 'main' == type:
            self.wait_until('#i0116')
            self.driver.find_element_by_css_selector('#i0116').send_keys('michael.gavidia@gmail.com')
            self.click_element('#idSIButton9')
            self.wait_until_url_contains('account')
            #self.wait_until(EC.url_contains('account'))
            self.driver.get("https://bing.com/")
        elif 'alt' == type:
            try:
                self.driver.find_element_by_css_selector('#mHamburger').click()
            except:
                self.driver.find_element_by_css_selector('#bnp_close_link > img').click()
                self.driver.find_element_by_css_selector('#mHamburger').click()
                time.sleep(1)
                self.driver.find_element_by_css_selector('#hb_s').click()
                time.sleep(1)
                self.driver.find_element_by_css_selector('#i0116').send_keys('michael.gavidia@gmail.com')
                self.driver.find_element_by_css_selector('#idSIButton9').click()

    def auto_search(self, search_word):
        e = self.get_element("#sb_form_q")
        print('(' + str(self.count) + ')' + ' Searching for ' + search_word)
        e.clear()
        e.click()
        e.send_keys(search_word)
        e.submit()

    def create_list(self):
        try:
            l = open('words.txt', 'r')
        except:
            print('File not found for search list: "words.txt"')
            quit()
        l = l.read()
        search_list = l.split('\n')
        return search_list


    def start_search(self):
        self.wait_until("#sb_form_q")
        search_list = self.create_list()
        while self.count <= self.searches_to_make:
            search = random.choice(search_list)
            self.auto_search(search)
            time.sleep(2)
            self.count += 1
        print('Your ' + str(self.searches_to_make) + ' random searches are done.\nClosing the browser automatically in 10 seconds.')
        time.sleep(10)
        self.driver.quit()
        self.count = 1
