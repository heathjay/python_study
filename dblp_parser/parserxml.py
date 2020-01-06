from lxml import etree
from pandas import DataFrame

def write_cvs(_author,_title,_year,index_year):
	data={'Authors':_author,'Title':_title,'Year':_year}	
	df=DataFrame(data,columns=['Authors','Title','Year'])
	path='/home/jay/what/'+index_year+'.csv'
	df.to_csv(path,mode='a',header=0,index=0)

parser=etree.XMLParser(load_dtd=True)
tree=etree.parse("/home/jay/what/dblp.xml",parser)
root=tree.getroot()

for article in root:
	_author=''
	_year=[]
	_title=[]
	for field in article:
		if field.tag == "author":
			if len(_author) == 0:
				_author=field.text
			else:
				_author=_author+' and '+field.text
		if field.tag == "title":
			_title.append(field.text)
		if field.tag == "year":
			_year.append(field.text)
	if len(_author) == 0 or len(_year) == 0 or len(_title)==0:
		continue
	if _year[0] == "2015":
		write_cvs(_author,_title,_year,'2015')
	if _year[0] == "2016":	
		write_cvs(_author,_title,_year,'2016')
	if _year[0] == "2017":	
		write_cvs(_author,_title,_year,'2017')
	if _year[0] == "2018":	
		write_cvs(_author,_title,_year,'2018')
	if _year[0] == "2019":	
		write_cvs(_author,_title,_year,'2019')



