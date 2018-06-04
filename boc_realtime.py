#!/usr/bin/env python3
# coding:utf-8 

import time
import os
import requests
from scrapy.selector import Selector
#from scrapy.http import HtmlResponse

last_time=''
last_rate=0
error_times=0

def getrate(last_time,last_rate,error_times):
	while True:

		try:
			r = requests.post('http://srh.bankofchina.com/search/whpj/search.jsp', data = {'erectDate':'', 'nothing':'', 'pjname':'1314'})

		except requests.exceptions.ConnectionError:
			error_times += 1
			print("网络错误, 第%i次.\n"%(error_times))
			time.sleep(10)
			continue

		body = r.text

		rate_output = Selector(text=body).xpath('//tr[2]/td[4]/text()').extract()
		time_output = Selector(text=body).xpath('//tr[2]/td[8]/text()').extract()

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
				print(time_output[0],"-",rate_output[0],"▼","\a\n")
			elif float(rate_output[0]) > float(last_rate):
				print(time_output[0],"-",rate_output[0],"▲","\n")
			else:
				print(time_output[0],"-",rate_output[0],"○","\n")

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

		time.sleep(120)

try:
	getrate(last_time,last_rate,error_times)
except KeyboardInterrupt:
	print("\n用户中止程序")

