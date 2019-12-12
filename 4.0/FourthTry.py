from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests 
from bs4 import BeautifulSoup
from pandas import DataFrame
from selenium.common.exceptions import NoSuchElementException 
import re
import time
import random

#initial cvs
data={'Title':[],'Year':[],'Authors':[]}
df=DataFrame(data,columns=['Title','Year','Authors'])
df.to_csv('/Users/chengpengjiang/Documents/coding/python/project_estimation/google/test/5.csv',mode='a',index=False)


url='https://scholar.google.com/scholar?as_q=&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=&as_publication=&as_ylo=2015&as_yhi=2019&hl=en&as_sdt=0%2C5'
driver=webdriver.Chrome()
driver.implicitly_wait(20)
locator=(By.ID,'gs_hdr_mnu')
driver.get(url)
#setting bibtex
WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located(locator))
driver.find_element_by_id('gs_hdr_mnu').click()

locator=(By.LINK_TEXT,'Settings')
WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located(locator))
driver.find_element_by_link_text('Settings').click()

locator=(By.ID,'gs_settings_import_some')
WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located(locator))
driver.find_element_by_id('gs_settings_import_some').click()

locator=(By.NAME,'save')
WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located(locator))
driver.find_element_by_name('save').click()




title_=[]
year_=[]
author_=[]
sleepT=random.randint(0,9)
try:
	locator=(By.PARTIAL_LINK_TEXT,"Import into Bib")
	WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located(locator))
	BibElements=driver.find_elements_by_partial_link_text("Import into Bib")
except NoSuchElementException:
	print("not find Bib")

print(len(BibElements))


for i in range(len(BibElements)):
	url=BibElements[i].get_attribute('href')
	if i == sleepT:
			time.sleep(random.randint(0,5))
	RESPONSE=requests.get(url)
	SOUP=BeautifulSoup(RESPONSE.text,'html.parser')
	title_.append(re.findall('(?<=title={).*?(?=})',SOUP.get_text()))
	year_.append(re.findall('(?<=year={).*?(?=})',SOUP.get_text()))
	author_.append(re.findall('(?<=author={).*?(?=})',SOUP.get_text()))
c= random.randint(1,11)
time.sleep(c)

dataGet={'Title':title_,'Year':year_,'Authors':author_}
print(dataGet)