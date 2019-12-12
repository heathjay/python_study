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
url1='https://scholar.google.com/scholar?start=10&q=jifaj&hl=en&as_sdt=1,5'
driver.get(url1)