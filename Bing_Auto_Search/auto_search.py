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
from Bing_Auto_Search.classes import Search


class StartSearch(Search):
    def desktop(self, type):
        self.setup_browser(type)
        self.driver.get('https://www.bing.com/')
        self.check_if_logged_in()
        self.start_search()

    def chrome_mobile(self):
        self.setup_browser('mobile')
        self.driver.get('https://login.live.com/')
        self.login()
        self.start_search()


search = StartSearch()
search.desktop('edge')
search.desktop('chrome')
search.chrome_mobile()
