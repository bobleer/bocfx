#!/usr/bin/env python
# coding: utf-8

import getopt
import sys
import time
import os
import requests
from scrapy.selector import Selector
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

import datetime
import re

def asexec():
	FX = 0
	sort = 0
	time = -1
	plot = 0
	csv = 0
	pt = 1
	op = '~/bocfx_output'
	opts, args = getopt.getopt(sys.argv[1:],'hf:s:t:pco:',['help','FX=','sort=','time=','plot','csv','op='])

	for opt, arg in opts:
		if opt in ('-h','--help'):
			print("A python package for getting foreign exchange rate from Bank of China (BOC).\nGet detailed help from https://github.com/bobleer/bocfx")
			sys.exit()

		elif opt in ('-f','--FX'):
			FX = arg

		elif opt in ('-s','--sort'):
			sort = arg

		elif opt in ('-t','--time'):
			time = arg

		elif opt in ('-p','--plot'):
			plot = 1

		elif opt in ('-c','--csv'):
			csv = 1

		elif opt in ('-o','--op'):
			op = arg

	output = main(FX, sort, time, plot, csv, pt, op)
	sys.exit() 


def bocfx(FX=0, sort=0, time=-1, plot=0, csv=0, pt=0, op='~/bocfx_output'):

	output = main(FX, sort, time, plot, csv, pt, op)

	return output


def page_get(output, sort, FX_or, erectDate, nothing, FX, i, page, end):
	error_times = 0
	try:
		r = requests.post('http://srh.bankofchina.com/search/whpj/search.jsp', data = {'erectDate':erectDate, 'nothing':nothing, 'pjname':str(FX[i]), 'page':str(page)})
	except:
		print("Internet Error, waiting 2s.\n")
		error_times += 1
		time.sleep(2)
		while error_times <= 3:
			r = requests.post('http://srh.bankofchina.com/search/whpj/search.jsp', data = {'erectDate':erectDate, 'nothing':nothing, 'pjname':str(FX[i]), 'page':str(page)})
		else:
			print("Retry 3 times, break!")
			exit()

	html = r.text
	lasttime = ''
	for row in range(2,end):
		try:
			SE_B = Selector(text=html).xpath('//tr[%i]/td[2]/text()' % (row)).extract()[0]
			BN_B = Selector(text=html).xpath('//tr[%i]/td[3]/text()' % (row)).extract()[0]
			SE_A = Selector(text=html).xpath('//tr[%i]/td[4]/text()' % (row)).extract()[0]
			BN_A = Selector(text=html).xpath('//tr[%i]/td[5]/text()' % (row)).extract()[0]
			time = Selector(text=html).xpath('//tr[%i]/td[7]/text()' % (row)).extract()[0].replace('.','-')
			if time != lasttime:
				#continue
				output.append(eval(sort))
				lasttime = time
		except IndexError:
			break


def main(FX, sort, time, plot, csv, pt, op):
	if FX != 0:
		FXdict = {'GBP':'1314','gbp':'1314','UK':'1314','uk':'1314','HKD':'1315','hkd':'1315','HK':'1315','hk':'1315','USD':'1316','usd':'1316','USA':'1316','usa':'1316','US':'1316','us':'1316','CHF':'1317','chf':'1317','FS':'1317','Fr':'1317','DM':'1318','dm':'1318','FF':'1319','ff':'1319','SGD':'1375','sgd':'1375','SEK':'1320','sek':'1320','DKK':'1321','dkk':'1321','NOK':'1322','nok':'1322','kr':'1322','JPY':'1323','jpy':'1323','JP':'1323','jp':'1323','Yen':'1323','CAD':'1324','cad':'1324','CA':'1324','ca':'1324','AUD':'1325','aud':'1325','AU':'1325','au':'1325','EUR':'1326','eur':'1326','EU':'1326','eu':'1326','MOP':'1327','mop':'1327','PHP':'1328','php':'1328','Peso':'1328','THB':'1329','thb':'1329','Thai':'1329','NZD':'1330','nzd':'1330','Kiwi':'1330','KRW':'1331','krw':'1331','KR':'1331','kr':'1331','RUB':'1843','rub':'1843','RU':'1843','ru':'1843','MYR':'2890','myr':'2890','Sen':'2890','TWD':'2895','twd':'2895','NTD':'2895','ntd':'2895','TW':'2895','tw':'2895','ESP':'1370','esp':'1370','ITL':'1371','itl':'1371','NLG':'1372','nlg':'1372','BEF':'1373','bef':'1373','FIM':'1374','fim':'1374','IDR':'3030','idr':'3030','BRL':'3253','brl':'3253','AED':'3899','aed':'3899','DH':'3899','Dhs':'3899','INR':'3900','inr':'3900','ZAR':'3901','zar':'3901','SAR':'4418','sar':'4418','TRY':'4560','try':'4560','YTL':'4560','ytl':'4560'}

		FX = FX.split(',')
		FX_ed = []

		for i in FX:
			try:
				FX_ed.append(FXdict[i])
			except:
				print('FX Value error!')
				exit()
		FX_or = FX.copy()
		FX = FX_ed

	else:
		FX = ['1314', '1326', '1316', '1324', '1325']
		FX_or = ['GBP', 'EUR', 'USD', 'CAD', 'AUD']


	if sort != 0:
		sort = sort.split(',')
		if 'SE' in sort or 'se' in sort or 'Se' in sort:
			if 'BID' in sort or 'bid' in sort or 'Bid' in sort:
				sort = '[FX_or[i],SE_B,time]'
				output = [[len(FX),'SE_BID','Time']]
			elif 'ASK' in sort or 'ask' in sort or 'Ask' in sort:
				sort = '[FX_or[i],SE_A,time]'
				output = [[len(FX),'SE_ASK','Time']]
			else:
				sort = '[FX_or[i],SE_B,SE_A,time]'
				output = [[len(FX),'SE_BID','SE_ASK','Time']]
		elif 'BN' in sort or 'bn' in sort or 'Bn' in sort:
			if 'BID' in sort or 'bid' in sort or 'Bid' in sort:
				sort = '[FX_or[i],BN_B,time]'
				output = [[len(FX),'BN_BID','Time']]
			elif 'ASK' in sort or 'ask' in sort or 'Ask' in sort:
				sort = '[FX_or[i],BN_A,time]'
				output = [[len(FX),'BN_ASK','Time']]
			else:
				sort = '[FX_or[i],BN_B,BN_A,time]'
				output = [[len(FX),'BN_BID','BN_ASK','Time']]
		elif 'BID' in sort or 'bid' in sort or 'Bid' in sort:
			sort = '[FX_or[i],SE_B,BN_B,time]'
			output = [[len(FX),'SE_BID','BN_BID','Time']]
		elif 'ASK' in sort or 'ask' in sort or 'Ask' in sort:
			sort = '[FX_or[i],SE_A,BN_A,time]'
			output = [[len(FX),'SE_ASK','BN_ASK','Time']]
		else:
			print("Sort Value error!")
			exit()

	else:
		sort = '[FX_or[i],SE_B,BN_B,SE_A,BN_A,time]'
		output = [[len(FX),'SE_BID','BN_BID','SE_ASK','BN_ASK','Time']]


	if time != -1:
		if len(str(time)) < 5:
			today_nof = datetime.date.today()
			tegart_nof = today_nof - datetime.timedelta(days=int(time))
			erectDate = str(tegart_nof)
			nothing = str(today_nof)
			
		elif ',' in time:
			time = time.split(",")
			erectDate = str(time[0])
			nothing = str(time[1])

		else:
			today_nof = datetime.date.today()
			erectDate = str(time)
			nothing = str(today_nof)

		for i in tqdm(range(len(FX))):
			r = requests.post('http://srh.bankofchina.com/search/whpj/search.jsp', data = {'erectDate':erectDate, 'nothing':nothing, 'pjname':FX[i], 'page':'1'})
			r = r.text
			searchOBJ = re.search(r'var m_nRecordCount = (.*);',r)
			pages = (int(searchOBJ.group(1))//20)+1

			ex = ThreadPoolExecutor(max_workers=20)
			all_task = [ex.submit(page_get, output, sort, FX_or, erectDate, nothing, FX, i, page, 22) for page in tqdm(range(1,(pages+1)))]

		ex.shutdown(wait=True)

		output.sort(reverse=True,key=lambda ele:ele[-1])
		filename = '['+'+'.join(FX_or)+']'+'+'.join(output[0][1:-1])+'_'+erectDate+'_'+nothing

	else:
		ex = ThreadPoolExecutor(max_workers=20)
		all_task = [ex.submit(page_get, output, sort, FX_or, '', '', FX, i, '1', 3) for i in tqdm(range(len(FX)))]

		ex.shutdown(wait=True)
		
		t=[output[0]]
		for i in range(len(FX_or)):
			for f in range(len(output)):
				if output[f][0] == FX_or[i]:
					t.append(output[f])
		output = t
		filename = '[Basic]'+output[1][-1].replace(' ','_')


	if pt != 0:
		from prettytable import PrettyTable

		pt = PrettyTable(output[0])
		for i in output[1:]:
			pt.add_row(i)

		print('\n')
		print(pt)
		print("(SE = Spot Exchange, BN = Banknote)")

	else:
		pass
		#print(output)


	if csv != 0:
		op = os.path.expanduser(op)
		if not os.path.exists(op):
			os.makedirs(op)
		csvpath = os.path.join(op,filename)+'.csv'

		with open(csvpath, 'w')  as f:
			for i in output:
				f.write(','.join(map(str,i))+'\n')
		print('\n.csv has already saved to '+csvpath)


	if plot != 0:
		import numpy as np
		import matplotlib.pyplot as plt

		p = np.array(output)
		fl = len(FX_or)
		plt.figure(figsize=(13, 8.5))

		for f in range(fl):
			plt.subplot(fl,1,f+1)
			sd = p[np.where(p[:][:,0] == FX_or[f])]
			x = sd[:,-1][:].astype(np.datetime64)

			for i in range(1,len(output[0])-1):
				plt.plot(x,sd[:,i][:].astype(float),label='['+FX_or[f]+']'+str(p[:,i][0])+': '+str(sd[:,i][0]))

			plt.legend(loc=2)

		op = os.path.expanduser(op)
		if not os.path.exists(op):
			os.makedirs(op)
		plotpath = os.path.join(op,filename)+'.png'
		
		plt.savefig(plotpath, dpi=150)
		print('\nPlot has already saved to '+plotpath)
		plt.show()

	simple_output = []
	if len(output[1])==3 and time==-1 and plot==0 and csv==0 and pt==0:
		for i in output[1:]:
			simple_output.append(i[1])
		output = simple_output

	return output

if __name__ == '__main__':

	asexec()
