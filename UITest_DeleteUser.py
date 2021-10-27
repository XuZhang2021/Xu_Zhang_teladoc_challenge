#!/usr/bin/env python3
import time
from bs4 import element
from selenium import webdriver
from selenium.webdriver.support.select import Select
import re

class UItest():
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option('detach', True)
        
    def openPage(self):
        self.driver = webdriver.Chrome('E:/all py/chrome-selenium-python-master/chromedriver.exe', options=self.option)
        self.driver.get('https://www.way2automation.com/angularjs-protractor/webtables/')
        
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td[11]/button').click() 
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/button[2]').click()
        time.sleep(0.5)

        if 'Novak' in self.driver.page_source:
            print('Tagert not deleted')
        else:
            print('Tagert deleted')

        
if __name__ == "__main__":
    UItest().openPage()