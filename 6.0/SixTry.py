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

class IpPool:
	def __init__(self,n):
		self.lenf=n
		self.proxy=[]
		for i in range(0,n):
			self.proxy.append(InitIp.get_proxy())
	def get_random_ip(self):
		while True:
			try:
				index= random.randint(0,self.lenf)			
				self.proxy[index]
				# print(self.proxy[index])
				con=self.test_ip(self.proxy[index])
				if con != True:
					print("con erro")
					continue
			except IndexError:
				print("out of index range")
				continue
			break
		return self.proxy[index]
	def up_ip(self,index):
		self.proxy[index]= self.get_random_ip()
	def test_ip(self,proxy_):
		res=requests.get("https://scholar.google.com",proxies={"http":"http://{}".format(proxy_['proxy'])})
		print({"http":"http://{}".format(proxy_['proxy'])})
		print(res.status_code)
		#print(res.text)
		if res.status_code != 200:
			return False
		else:
			return True


class InitIp:
	def get_proxy():
	    return requests.get("http://127.0.0.1:5010/get/").json()
	def delete_proxy(proxy):
	    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

#initial cvs
data={'Title':[],'Year':[],'Authors':[]}
df=DataFrame(data,columns=['Title','Year','Authors'])
df.to_csv('/Users/chengpengjiang/Documents/coding/python/project_estimation/google/test/6.0/6.csv',mode='a',index=False)
url='https://scholar.google.com/scholar?as_q=&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=&as_publication=&as_ylo=2015&as_yhi=2019&hl=en&as_sdt=0%2C5'
#initialize the proxy pool

#print(Pool.proxy)
# print(Pool.get_random_ip()['proxy'])





page=0
while page <6:
	Pool= IpPool(80)
	PROXY=Pool.get_random_ip()['proxy']
	#print(type(PROXY))
	chromeoptions=webdriver.ChromeOptions()
	chromeoptions.add_argument('--proxy-server=http://'+format(PROXY))
	driver=webdriver.Chrome(chrome_options=chromeoptions)
	driver.get(url)

	# time.sleep(4)
	# driver.quit()

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
	while page < 3:
		page=page+1
		title_=[]
		year_=[]
		author_=[]
		sleepT=random.randint(0,9)
		#get BibTex
		try:
			locator=(By.PARTIAL_LINK_TEXT,"Import into Bib")
			WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located(locator))
			BibElements=driver.find_elements_by_partial_link_text("Import into Bib")
		except NoSuchElementException:
			print("not find Bib")

		#based on requests and beautifulsoup to get all info
		for i in range(len(BibElements)):
			url=BibElements[i].get_attribute('href')
			if i == sleepT:
				time.sleep(random.randint(0,2))
			# proxy=get_proxy().get("proxy")
			while True:
				proxy=Pool.get_random_ip()['proxy']
				print(proxy)
				RESPONSE=requests.get(url,proxies={"http":"http://{}".format(proxy)})

				if RESPONSE.status_code != 200:
					print("as a robot")
					continue
					# os._exit(-1)
			SOUP=BeautifulSoup(RESPONSE.text,'html.parser')
			title_.append(re.findall('(?<=title={).*?(?=})',SOUP.get_text()))
			year_.append(re.findall('(?<=year={).*?(?=})',SOUP.get_text()))
			author_.append(re.findall('(?<=author={).*?(?=})',SOUP.get_text()))
			# delete_proxy(proxy)

	c= random.randint(0,1*page)
	time.sleep(c)
	dataGet={'Title':title_,'Year':year_,'Authors':author_}
	df=DataFrame(dataGet,columns=['Title','Year','Authors'])
	df.to_csv('/Users/chengpengjiang/Documents/coding/python/project_estimation/google/test/6.0/6.csv',mode='a',header=False,index=False)
	#turn to Next Page
	# if there is no next page 
	#break
	try:
		nextPage=driver.find_element_by_xpath("//b[contains(text(),'Next')]")
		# nextPage.click()
		urlNext=driver.find_element_by_xpath("//tr/td[12]/a").get_attribute('href')
		url=urlNext
	except NoSuchElementException:
		print("final Page")
		break
