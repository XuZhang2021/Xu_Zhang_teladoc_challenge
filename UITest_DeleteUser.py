#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import re

class UIDeleteTest():
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option('detach', True)
        
    def deleteRecord(self):
        webdriverlocation = 'E:/all py/chrome-selenium-python-master/chromedriver.exe' #Download the webdriver from Github and change the location to your location drive where you have the webdriver.exe saved at.
        self.driver = webdriver.Chrome(webdriverlocation, options=self.option)
        self.driver.get('https://www.way2automation.com/angularjs-protractor/webtables/')
        
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td[11]/button').click() 
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/button[2]').click()
        time.sleep(0.5)

        if 'Novak' in self.driver.page_source:
            print('Target not deleted')
        else:
            print('Target deleted')

        
if __name__ == "__main__":
    UIDeleteTest().deleteRecord()