#encoding:utf-8

import requests 
from bs4 import BeautifulSoup
from pandas import DataFrame
import re

#initial
URL=['https://scholar.google.com/scholar?as_q=&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=&as_publication=&as_ylo=2014&as_yhi=2020&hl=en&as_sdt=0%2C5']

#title_,authors_,years
title_=[]
authors_=[]
years=[]
count=0
head='https://scholar.google.com'
mid='/scholar?start='
tail='&hl=en&as_sdt=1,5&as_ylo=2014&as_yhi=2019&as_vis=1'

key=1
while key >= 0:
	RESPONSE=requests.get(URL[0])
	#RESPONSE.text
	if RESPONSE:
		print("continue")
	else:
		print("response error: be a robbot "+count)
		break


	SOUP=BeautifulSoup(RESPONSE.text, 'html.parser')


	library=SOUP.find_all('a', string="Library Search")
	links=[]

	for i in range(len(library)):
		links.append(library[i]['href'])


	#Year
	timeTag=SOUP.find_all("div",class_="gs_a")
	for i in range(len(timeTag)):
		time=re.findall('(?<=\s)\d{4}(?=\s)',timeTag[i].get_text())
		years.append(time)


	#search for title_authors
	for url in links:
		#count=links.index(url) 
		#Year=year[count]
		#years.append()
		response = requests.get(url)
		soup = BeautifulSoup(response.text,'html.parser')
		redirectLinks=re.findall('(?<=\')\S+(?=\')',soup.find('script').get_text())
		redirectRes=requests.get(redirectLinks[0])
		redirectSoup=BeautifulSoup(redirectRes.text,'html.parser')
		##title
		#authors=[]
		title=redirectSoup.find('h1').get_text()
		title_.append(title)
		authors=''
		
		au=redirectSoup.find_all(attrs={"title":"Search for more by this author"})
		for i in range(len(au)):
			#authors.append(au[i].string)
			authors=authors+','+au[i].string
		authors_.append(authors)

	count=count+10
	nextURL=head+mid+str(count)+tail
	URL[0]=nextURL


#enpack into dic
data={'Title':title_,'Year':years,'Authors':authors_}

df=DataFrame(data,columns=['Title','Year','Authors'])
df.to_csv('/Users/chengpengjiang/Documents/coding/python/project_estimation/google/test/1.csv',mode='a')

