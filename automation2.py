from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
username ="mohammedhaadizaman"
pwd1="Mhz@1997,"
mailid="mzaman@extremenetworks.com"
subj = "automation email"
content="This is the content"
gmail = webdriver.Chrome("C:/Users/mzaman/Downloads/chromedriver/chromedriver_win32/chromedriver.exe")
gmail.set_page_load_timeout(5)
gmail.get('https://www.google.com/gmail/')
time.sleep(1)
usr = gmail.find_element_by_id("identifierId")
usr.send_keys(username)
usr.send_keys(Keys.RETURN)
time.sleep(5)
try:
    pwd = gmail.find_element_by_name("password")
    pwd.send_keys(pwd1)
    time.sleep(5)
    b1=gmail.find_element_by_id("passwordNext")
    b1.click()
except:
    pass
time.sleep(10)
cmp=gmail.find_element_by_class_name("z0")
cmp.click()
time.sleep(10)
to=gmail.find_element_by_name("to")
to.send_keys(mailid)
time.sleep(5)
subject = gmail.find_element_by_name("subjectbox")
subject.send_keys(subj)
time.sleep(10)
'''msg=gmail.find_element_by_class_name("Am Al editable LW-avf")  #This is causing a problem
msg.send_keys(content)
time.sleep(5)'''
send=gmail.find_element_by_css_selector(".gU")
send.click()
time.sleep(5)
gmail.close()
