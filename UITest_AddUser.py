#!/usr/bin/env python3
import time
from bs4 import element
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class UItest():
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option('detach', True)
        
    def openPage(self):
        self.driver = webdriver.Chrome('E:/all py/chrome-selenium-python-master/chromedriver.exe', options=self.option)
        self.driver.get('https://www.way2automation.com/angularjs-protractor/webtables/')

        time.sleep(2)  # Let the user actually see something!
        self.driver.find_element_by_xpath('/html/body/table/thead/tr[2]/td/button').click()

        self.element = self.driver.find_element_by_name('FirstName')
        self.element.send_keys('FirstName Test') #Enter FirstName Test in FirstName box
        time.sleep(0.1)

        self.element = self.driver.find_element_by_name('LastName')
        self.element.send_keys('LastName Test')  #Enter LastName Test in LastName box
        time.sleep(0.1)

        self.element = self.driver.find_element_by_name('UserName')
        self.element.send_keys('UserName Test')  #Enter UserName Test in UserName box
        time.sleep(0.1)

        self.element = self.driver.find_element_by_name('Password')
        self.element.send_keys('Password Test')  #Enter Password Test in Password box
        time.sleep(0.1)

        self.element = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/table/tbody/tr[5]/td[2]/label[1]/input').click() #Click on Radio button Company AAA
        time.sleep(0.1)
        self.element = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/table/tbody/tr[5]/td[2]/label[2]').click()  #Click on Radio button Company BBB
        time.sleep(0.1)

        self.dropdown = self.driver.find_element_by_name('RoleId')
        select = Select(self.dropdown)
        
        select.select_by_value('0') #Select Sales Team as role from Role dropdown list.
        time.sleep(0.1)
        select.select_by_value('1') #Select Customer Team as role from Role dropdown list.
        time.sleep(0.1)
        select.select_by_value('2') #Select Admin Team as role from Role dropdown list.
        time.sleep(0.1)

        self.element = self.driver.find_element_by_name('Email')
        self.element.send_keys('E-mailTest@Test.com')  #Enter E-mailTest@Test.com in Email box
        time.sleep(0.1)

        self.element = self.driver.find_element_by_name('Mobilephone')
        self.element.send_keys('9040001234')  #Enter 9040001234 in Cell phone box
        time.sleep(0.1)

        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/button[2]').click() #Click on submit button to complete the transaction
        time.sleep(0.1)
        
        rawdata = self.driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/td") #Retrive data after keye into the webpage.

        response_ori = []

        for r in rawdata:
            response_ori.append(r.text)

        print(response_ori)

        #response = list(filter(None, response))
        response = []

        response.append(response_ori[0]) #append first name
        response.append(response_ori[1]) #append last name
        response.append(response_ori[2]) #append username
        response.append(response_ori[4]) #append Customer
        response.append(response_ori[5]) #append Role
        response.append(response_ori[6]) #append email address
        response.append(response_ori[7]) #append phone number

        print(response) 

        response_lib = {'First Name':'',
                     'Last Name':'',
                     'User Name':'',
                     'Company':'',
                     'Role':'',
                     'Email':'',
                     'Phone Number':''
                      }

        self.response_fromUI = dict(zip(response_lib.keys(), response)) #Creating a new dictionary with key value pair for further verification.
        global response_fromUI
        response_fromUI = self.response_fromUI
        return response_fromUI
    
    def verifyData(self):
        targetUserData = {'First Name':'FirstName Test',
                     'Last Name':'LastName Test',
                     'User Name':'UserName Test',
                     'Company':'Company BBB',
                     'Role':'Admin',
                     'Email':'E-mailTest@Test.com',
                     'Phone Number':'9040001234'
                         } #Set these as the actual test data in a library.
        if response_fromUI is None:
            ('Please check UI, it is showing empty.')
        else:
            diff = response_fromUI.keys() & targetUserData.keys()
            diff_vals = [(k, response_fromUI[k], targetUserData[k]) for k in diff if response_fromUI[k] != targetUserData[k]]
            if diff_vals:
                print('Please find the differnce between UI and the expected output.')
                print("{:<20}|{:<20}|{:<20}".format("Metadata Name", "Website value", "Expected value")) #Align all the column subject.
                for i in diff_vals:
                    print("{:<20} {:<20} {:<20}".format(*i)) #Align all the values.
            else:
                print('The UI shows the expected results.')

        
if __name__ == "__main__":
    UItest().openPage()
    UItest().verifyData()