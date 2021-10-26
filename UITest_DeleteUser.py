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
        
    def openpage(self):
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

        response = []

        for r in rawdata:
            response.append(r.text)

        response = list(filter(None, response))
        #print(response)
        response_lib = {'First Name':'',
                     'Last Name':'',
                     'User Name':'',
                     'Role':'',
                     'Email':'',
                     'Phone Number':''
                      }

        self.response_fromUI = dict(zip(response_lib.keys(), response)) #Creating a new dictionary with key value pair for further verification.
        global response_fromUI
        response_fromUI = self.response_fromUI
        return response_fromUI
    
    def verifyData(self):
        targetUserData = {'First Name':'1FirstName Test',
                     'Last Name':'1LastName Test1',
                     'User Name':'1UserName Test',
                     'Role':'1Admin',
                     'Email':'1E-mailTest@Test.com',
                     'Phone Number':'19040001234'
                         }
        #['FirstName Test', 'LastName Test', 'UserName Test', 'Admin', 'E-mailTest@Test.com', '9040001234'] # Set up a correct list of data to verify if UI returns the same.
        if response_fromUI is None:
            ('Please check UI, it is showing empty.')
        else:
            diff = response_fromUI.keys() & targetUserData.keys()
            diff_vals = [(k, response_fromUI[k], targetUserData[k]) for k in diff if response_fromUI[k] != targetUserData[k]]
            if diff_vals: 
                print('Please find the differnce between UI and the expected output {}.'.format(diff_vals))
            else:
                print('The UI shows the expected results.')

        
if __name__ == "__main__":
    UItest().openpage()
    UItest().verifyData()






# search_box = driver.find_element_by_id('menu2').click()
# time.sleep(3)

# driver.find_elements_by_name('seimei')[1].click()
# time.sleep(3)

# driver.find_element_by_name('submit_ranking').click()
# time.sleep(3)

# with open('names.txt', 'w') as w:
#     while True:
#         soup = BeautifulSoup(driver.page_source, 'html.parser')
#         table = soup.find_all('td', attrs={'class': None})
#         names = [str(c.contents[0]) for c in soup.find_all('td', attrs={'class': None})]
#         str_names = '\n'.join(names)
#         print(str_names)
#         w.write(str_names)
#         w.flush()
#         driver.find_elements_by_class_name('submit_button')[-1].click()
        
#         time.sleep(3)

# driver.quit()
