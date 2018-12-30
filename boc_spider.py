#!/usr/bin/env python3
# coding:utf-8 

import time
import datetime
import requests
from scrapy.selector import Selector
import re

nums = 0
error_times = 0
lasttime = ''

def spider(erectDate,nothing,fex_sl,page):
	try:
		input = requests.post('http://srh.bankofchina.com/search/whpj/search.jsp', data = {'erectDate':erectDate, 'nothing':nothing, 'pjname':fex_sl, 'page':page})
	except:
		global error_times
		error_times += 1
		print("出现错误, 5秒后重试(第%i次)"%(error_times))
		time.sleep(5)
		spider(erectDate,nothing,fex_sl,page)

	else:
		body = input.text
		for row in range(2,22):
			rate_output = Selector(text=body).xpath('//tr[%i]/td[4]/text()' %(row)).extract()
			time_output = Selector(text=body).xpath('//tr[%i]/td[7]/text()' %(row)).extract()
			global lasttime
			try:
				if time_output[0] == lasttime:
					#print("重复数据")
					continue
				outrow = time_output[0]+","+rate_output[0]+"\n"
				out.write(outrow)
				#print(time_output[0]+','+rate_output[0])
				global nums
				nums += 1
				lasttime = time_output[0]
			except IndexError:
				break
		print("已抓取至第%i/%i页, %i条数据" %(page,pages,nums))

today_noFormat = datetime.date.today()
lastweek_noFormat = today_noFormat - datetime.timedelta(days=6)
today = str(today_noFormat)
lastweek = str(lastweek_noFormat)
print("---------------------------------------------------")
print("| 中行外汇牌价抓取脚本 | Made by Bob | 2018.09.19 |")
print("---------------------------------------------------")
fex = input("请选择要抓取的外汇种类:\n1.英镑\n2.美元\n3.澳元\n4.欧元\n")

while True:
	if fex == '1':
		fex_sl = 1314
		fex_name = 'GBP'
		break
	elif fex == '2':
		fex_sl = 1316
		fex_name = 'USD'
		break
	elif fex == '3':
		fex_sl = 1325
		fex_name = 'AUD'
		break
	elif fex == '4':
		fex_sl = 1326
		fex_name = 'EUR'
		break
	else:
		fex = input("输入有误,请重新选择:\n1.英镑\n2.美元\n3.澳元\n4.欧元\n")

print("输入抓取汇率的起始日期(回车默认7天前:%s):"%(lastweek))
erectDate = str(input())
if not len(erectDate.strip()):
	erectDate = str(lastweek)

print("输入抓取汇率的结束日期(回车默认今天:%s):"%(today))
nothing = str(input())
if not len(nothing.strip()):
	nothing = str(today)

input = requests.post('http://srh.bankofchina.com/search/whpj/search.jsp', data = {'erectDate':erectDate, 'nothing':nothing, 'pjname':fex_sl, 'page':'1'})
body = input.text
searchOBJ = re.search(r'var m_nRecordCount = (.*);',body)
pages = (int(searchOBJ.group(1))//20)+1

out = open('/Users/bob/Desktop/[%s]%s_%s.csv'%(fex_name,erectDate,nothing),'a',newline='')
for page in range(1,(pages+1)):
	spider(erectDate,nothing,fex_sl,page)

out.close()
print("")
print('-' * 28,"\n")
print("抓取完毕, 共%i条数据"%(nums))
print("共出现错误%i次"%(error_times))
print("结果已保存至 ~/Desktop/boc-s.csv")