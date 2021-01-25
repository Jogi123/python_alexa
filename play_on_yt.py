#!/bin/python

import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class PlayOnYt:
    def __init__(self, search_term):
        self.search_term = search_term
        self.init_webdriver()
        self.search_yt()

    def init_webdriver(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)
        addons = [f'{os.getcwd()}/uBlock0_1.32.5b9.firefox.signed.xpi']
        for addon in addons:
            self.driver.install_addon(addon)

    def search_yt(self):
        self.search_term = self.search_term.replace(' ', '+')
        url = f"https://www.youtube.com/results?search_query={self.search_term}"
        self.driver.get(url)
        time.sleep(6)
        # agree to consent management on youtube
        self.driver.switch_to.frame('iframe')
        self.driver.find_element_by_id('introAgreeButton').click()
        # click on title to play video
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_id('title-wrapper').click()
        # deny login prompt
        time.sleep(4)
        self.driver.find_element_by_css_selector('yt-button-renderer.style-text > a:nth-child(1) > '
                                                 'paper-button:nth-child(1)').click()
        # click again on video to finally play
        self.driver.find_element_by_id('movie_player').click()
