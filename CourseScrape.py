from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import win32ui
import time

chromedriver = 'C:\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.get('https://arion.aut.ac.nz/')

time.sleep(0.1)

browser.find_element("id", "wucEntry_txtUsername").send_keys("REDACTED")
browser.find_element("id", "wucEntry_txtPassword").send_keys("REDACTED")
browser.find_element("id", "wucEntry_cmdLogin").click()

browser.get('https://arion.aut.ac.nz/ArionMain/Enrolments/Information/CurrentStudents/ClassEnrolments.aspx')

time.sleep(0.1)

select = Select(browser.find_element('id', 'wucEnrolmentListing_ddlSemester'))

courseConfirmation = False

for option in select.options:
    if '2024' in option.text:
        courseConfirmation = True

if courseConfirmation == True:
    win32ui.MessageBox('Course Selection now available!!! :]', 'Course Selection')