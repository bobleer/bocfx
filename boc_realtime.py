#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import time
import os
import requests
from scrapy.selector import Selector

#from scrapy.http import HtmlResponse

last_time=''
last_rate=0
error_times=0
sleeptime=120
print("-------------------------------------------------")
print("| 中行外汇牌价监视器 | Made by Bob | 2018.09.19 |")
print("-------------------------------------------------")

fex = input("请选择要抓取的外汇种类:\n1.英镑(默认)\n2.美元\n3.澳元\n4.欧元\n")

while True:
	if fex == '1' or fex == '':
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

def sleeptimeget(sleeptime):
	try:
		sleeptime = input("多久刷新一次(s): ")
		if sleeptime == '':
			sleeptime = 120
			print("已按照默认设置刷新(120s)\n")
		else:
			sleeptime = int(sleeptime)
	except:
		print("输入有误,请重新输入.\n")
		sleeptimeget(sleeptime)

def getrate(last_time,last_rate,error_times,sleeptime,fex_sl,fex_name):
	while True:

		try:
			r = requests.post('http://srh.bankofchina.com/search/whpj/search.jsp', data = {'erectDate':'', 'nothing':'', 'pjname':fex_sl})

		except requests.exceptions.ConnectionError:
			error_times += 1
			print("网络错误, 第%i次.\n"%(error_times))
			time.sleep(10)
			continue

		body = r.text

		rate_output = Selector(text=body).xpath('//tr[2]/td[4]/text()').extract()
		time_output = Selector(text=body).xpath('//tr[2]/td[7]/text()').extract()

		'''
		def compare():
		with open('/Users/bob/Desktop/boc.log','r') as c:
			lines = c.readlines()
			last_line = lines[0]
			last_time = last_line.rstrip('\n')
			c.close()
		'''
		
		#def printitems():
		#global last_time
		#global last_rate
		if last_time != time_output[0]:
			if float(rate_output[0]) < float(last_rate):
				print('['+fex_name+']',time_output[0],"-",rate_output[0],"▼","\a\n")
			elif float(rate_output[0]) > float(last_rate):
				print('['+fex_name+']',time_output[0],"-",rate_output[0],"▲","\n")
			else:
				print('['+fex_name+']',time_output[0],"-",rate_output[0],"○","\n")

			#def record():
			'''
			r=open('/Users/bob/Desktop/boc.log','r+')
			old = r.read()
			r.seek(0)
			r.write(time_output[0])
			r.write(",")
			r.write(rate_output[0])
			r.write("\n")
			r.write(old)
			r.close()
			'''
			last_time = time_output[0]
			last_rate = rate_output[0]

		time.sleep(sleeptime)

try:
	sleeptimeget(sleeptime)
	getrate(last_time,last_rate,error_times,sleeptime,fex_sl,fex_name)
except KeyboardInterrupt:
	print("\n用户中止程序")

