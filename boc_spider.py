#!/usr/bin/env python3
# coding:utf-8 

import time
import datetime
import requests
from scrapy.selector import Selector
import re

nums = 0
error_times = 0

def spider(erectDate,nothing,page):
	try:
		input = requests.post('http://srh.bankofchina.com/search/whpj/search.jsp', data = {'erectDate':erectDate, 'nothing':nothing, 'pjname':'1314', 'page':page})
	except:
		global error_times
		error_times += 1
		print("出现错误, 5秒后重试(第%i次)"%(error_times))
		time.sleep(5)
		spider(erectDate,nothing,page)

	else:
		body = input.text
		for row in range(2,22):
			rate_output = Selector(text=body).xpath('//tr[%i]/td[4]/text()' %(row)).extract()
			time_output = Selector(text=body).xpath('//tr[%i]/td[8]/text()' %(row)).extract()
			try:
				outrow = time_output[0]+","+rate_output[0]+"\n"
				out.write(outrow)
				print(time_output[0]+','+rate_output[0])
				global nums
				nums += 1
			except IndexError:
				break
		print("已抓取第%i页, 共%i条数据\n" %(page,nums))

today_noFormat = datetime.date.today()
lastweek_noFormat = today_noFormat - datetime.timedelta(days=6)
today = str(today_noFormat)
lastweek = str(lastweek_noFormat)

print("中行英镑牌价抓取脚本 Ver:0.8")
print("输入抓取汇率的起始日期(回车默认为7天前:%s):"%(lastweek))
erectDate = input()
if not len(erectDate.strip()):
	erectDate = lastweek

print("输入抓取汇率的结束日期(回车默认为今天:%s):"%(today))
nothing = input()
if not len(nothing.strip()):
	nothing = today

input = requests.post('http://srh.bankofchina.com/search/whpj/search.jsp', data = {'erectDate':erectDate, 'nothing':nothing, 'pjname':'1314', 'page':'1'})
body = input.text
searchOBJ = re.search(r'var m_nRecordCount = (.*);',body)
pages = (int(searchOBJ.group(1))//20)+1

out = open('/Users/bob/Desktop/boc-s.csv','a',newline='')
for page in range(1,(pages+1)):
	spider(erectDate,nothing,page)

out.close()
print("")
print('-' * 28,"\n")
print("抓取完毕!")
print("共出现错误%i次"%(error_times))