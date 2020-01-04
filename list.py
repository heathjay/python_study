import os
import glob
import pandas as pd


def listdir_nohidden(path):
    return glob.glob(os.path.join(path, '*'))

def mergeCvs(file,dest):
	fr=open(file)
	data=pd.read_csv(fr)
	data.to_csv(dest,mode='a',index=False)

def delDuplicate(file):
	df = pd.read_csv(file,header=0)
	datalist=df.drop_duplicates()
	datalist.to_csv(file,index=False)


#path = "/home/jay/桌面/Assignment_4_ieee_acm_dblp/ieee_robert"
path = "/home/jay/桌面/Assignment_4_ieee_acm_dblp/mixup3"

files = listdir_nohidden(path)
s = []
year=['2015.csv','2016.csv','2017.csv','2018.csv','2019.csv']
des = [path+'/'+ y for y in year]
for file in files:
	if os.path.isdir(file):
		temp1_files = listdir_nohidden(file)
		compare_year_cvs=[file + '/' + y for y in year]
		for temp2 in temp1_files:	
			if temp2 == compare_year_cvs[0]:
				mergeCvs(temp2,des[0])
				delDuplicate(des[0])
			elif temp2 == compare_year_cvs[1]:
				mergeCvs(temp2,des[1])
				delDuplicate(des[1])
			elif temp2 == compare_year_cvs[2]:
				mergeCvs(temp2,des[2])
				delDuplicate(des[2])
			elif temp2 == compare_year_cvs[3]:
				mergeCvs(temp2,des[3])
				delDuplicate(des[3])
			elif temp2 == compare_year_cvs[4]:
				mergeCvs(temp2,des[4])
				delDuplicate(des[4])
			
