# bocfx ![](https://img.shields.io/badge/License-MIT-green.svg) ![](https://img.shields.io/badge/Python-3-3776ab.svg) ![](https://img.shields.io/badge/PyPI-0.7.6-ffd242.svg)
An easy-to-use python package for getting foreign exchange rate from Bank of China (BOC).  
一个帮你快速获取中国银行外汇牌价的 Python 爬虫（也可作外汇牌价实时查询API)。  
Author: [**Bob Lee**](https://boblee.cn)
<br>
<br>

# Features

* [x] **Multithreading 多线程**
* [x] **As a command-line application 支持命令行应用模式**
* [x] **As a python module 支持模块导入模式（import到你自己的项目里就能作API了）**
* [x] **Foreign exchange selection 支持多种外汇币种同时输出（默认是英、欧、美、加、澳）**
* [x] **Foreign exchange quotation filter 支持外汇牌价种类同时输出（买入、卖出、现钞、现汇）**
* [x] **Date selection (Realtime/History) 支持仅输出最新牌价 或 输出指定时间段内全部牌价变动**
* [x] **Line graph generation 支持生成历史波动曲线**
* [x] **.csv generation 支持导出csv格式表格文件**
* [x] **Set output path 支持导出到指定路径**
* [x] **Show or close loading bar 支持显示或关闭进度条**
* [x] **Export to database 支持导出到数据库（可使用Pandas的df.to_sql()）**

<br>

# Contents

- [Installation 安装](#installation)
- [Basic Usage 基本用法](#basic-usage)
	- [As a command-line application 作为命令行程序使用](#as-command-line-application)
	- [As a python module 作为API使用](#as-python-module)
- [Advanced Usage 进阶用法](#advanced-usage)
	- [As a command-line application 作为命令行程序使用](#as-command-line-application-1)
		- [Example](#example)
	- [As a python module 作为API使用](#as-python-module-1)
		- [Example](#example-1)
- [Option and parameter 参数选择](#option-and-parameter)
	- [Option 1 `-f`/`--fx` 外汇种类](#option-1--f--fx)
		- [Common foreign currency:](#common-foreign-currency)
		- [Example](#example-2)
	- [Option 2 `-s`/`--sort` 牌价种类](#option-2--s--sort)
		- [Example](#example-3)
	- [Option 3 `-t`/`--time` 时间、时间段](#option-3--t--time)
	- [Option 4 `-p`/`--plot` 画图](#option-4--p--plot)
	- [Option 5 `-c`/`--csv` 导出csv表格](#option-5--c--csv)
	- [Option 6 `-o`/`--op` 导出文件路径设置](#option-6--o--op)
	- [Option 7 `-b`/`--bar` 开启进度条显示](#option-7--b--bar)
- [Limitation 局限性](#limitation)
- [MIT Licence](#mit-licence)
<br>

# Installation
# 安装

Generally, one line command can perfect installation.
```
pip3 install bocfx 
```  
If your `pip` links python3, please use `pip install bocfx` to install bocfx.   
**REMEMBER**, Bocfx may not support python2.  
<br>
<br>

# Basic Usage
# 基本用法 (输出最新的牌价)
<br>

## As a command-line application
## 作为命令行工具使用

```
BOBMAC:~ bobleer$ bocfx                        
100%|████████████████████████████████████████████| 5/5 [00:00<00:00, 471.66it/s]

+-----+--------+--------+--------+--------+---------------------+
|  5  | SE_BID | BN_BID | SE_ASK | BN_ASK |         Time        |
+-----+--------+--------+--------+--------+---------------------+
| GBP | 873.53 | 846.38 | 879.96 | 882.1  | 2019-02-25 09:25:37 |
| EUR | 758.54 | 734.97 | 764.14 | 765.83 | 2019-02-25 09:25:37 |
| USD | 669.44 | 663.99 | 672.28 | 672.28 | 2019-02-25 09:25:37 |
| CAD | 509.1  | 493.03 | 512.86 | 514.1  | 2019-02-25 09:25:37 |
| AUD | 476.19 | 461.4  | 479.69 | 480.87 | 2019-02-25 10:10:35 |
+-----+--------+--------+--------+--------+---------------------+
(SE = Spot Exchange, BN = Banknote)
```
<br>
<br>

## As a Python module
## 作为 Python 模块导入使用

```
>>> from bocfx import bocfx

>>> output = bocfx('GBP,USD','SE,ASK') # 选择了英镑和美元，现汇卖出价
100%|████████████████████████████████████████████| 5/5 [00:00<00:00, 532.87it/s]

>>> output # The latest foreign exchange rate | 英镑和美元，现汇卖出价 (最新的牌价)
['879.96', '672.28'] 
```
<br>
<br>

# Advanced Usage
# 进阶用法
<br>

## As a command-line application
## 作为命令行工具使用时

`-f` | 可选外汇 | FX selection
`-s` | 可选牌价 | Quotation types selection
`-t` | 可选时间 | Time / Period selection
`-p` | 输出波动图 | Output plot
`-c` | 输出csv | Output csv table
`-o` | 指定输出路径 | Set output path

```Bash
bocfx [-f|--fx] [-s|--sort] [-t|--time] (-p|--plot) (-c|--csv) {-o|--op}
```
<br>
<br>

#### Example:

```
❯ bocfx -f GBP,USD,AUD -s ASK -t 30 -p -c -o '~/desktop/output'
100%|█████████████████████████████████████████████| 3/3 [00:03<00:00,  1.08s/it]
100%|████████████████████████████████████████| 199/199 [00:00<00:00, 422.62it/s]

+-----+--------+--------+---------------------+
|  3  | SE_ASK | BN_ASK |         Time        |
+-----+--------+--------+---------------------+
| GBP | 880.27 | 882.41 | 2019-02-24 10:30:00 |
| USD | 673.08 | 673.08 | 2019-02-24 10:30:00 |
| AUD | 480.65 | 481.82 | 2019-02-24 10:30:00 |
| GBP | 880.27 | 882.41 | 2019-02-24 05:30:00 |
| USD | 673.08 | 673.08 | 2019-02-24 05:30:00 |
| AUD | 480.65 | 481.82 | 2019-02-24 05:30:00 |
...
| GBP | 889.64 | 891.8  | 2019-01-25 00:00:05 |
| USD | 680.4  | 680.4  | 2019-01-25 00:00:05 |
| AUD | 484.37 | 485.56 | 2019-01-25 00:00:05 |
+-----+--------+--------+---------------------+
(SE = Spot Exchange, BN = Banknote)

.csv has already saved to /Users/bob/desktop/output/[GBP+USD+AUD]SE_ASK+BN_ASK_2019-01-25_2019-02-24.csv

Plot has already saved to /Users/bob/desktop/output/[GBP+USD+AUD]SE_ASK+BN_ASK_2019-01-25_2019-02-24.png
```
![](https://github.com/bobleer/bocfx/raw/master/images/%5BGBP%2BUSD%2BAUD%5DSE_ASK%2BBN_ASK_2019-01-25_2019-02-24.png)
<br>
<br>

## As a python module

```python
from bocfx import bocfx

bocfx(FX=0, sort=0, time=-1, plot=0, csv=0, pt=0, op='~/bocfx_output')
```
<br>
<br>

#### Example:

```
>>> from bocfx import bocfx

# Equivalent command
# example01 = bocfx(FX='GBP,USD', sort='SE', time=1)

>>> example01 = bocfx('GBP,USD','SE',1)
100%|█████████████████████████████████████████████| 2/2 [00:01<00:00,  1.49it/s]

>>> type(example01)
<class 'list'>

>>> print(example01)
[[2, 'SE_BID', 'SE_ASK', 'Time'], ['USD', '669.74', '672.58', '2019-02-25 09:25:23'], ['GBP', '874.18', '880.62', '2019-02-25 09:25:13'], ... , ['GBP', '873.83', '880.27', '2019-02-24 00:00:05'], ['USD', '670.24', '673.08', '2019-02-24 00:00:05']]
```

<br>

```
>>> from bocfx import bocfx

# Equivalent command
# example02 = bocfx(FX='GBP,USD', sort='SE', time='2018-08-01,2018-08-02', plot=1, csv=1, pt=0, op='~/desktop/example/')

>>> example02 = bocfx('GBP,USD','SE','2018-08-01,2018-08-02',1,1,0,op='~/desktop/example/')
100%|█████████████████████████████████████████████| 2/2 [00:02<00:00,  1.05it/s]
100%|██████████████████████████████████████████| 26/26 [00:00<00:00, 134.46it/s]

.csv has already saved to /Users/bob/desktop/example/[GBP+USD]SE_BID+SE_ASK_2018-08-01_2018-08-02.csv

Plot has already saved to /Users/bob/desktop/example/[GBP+USD]SE_BID+SE_ASK_2018-08-01_2018-08-02.png

>>> type(example02)
<class 'list'>

>>> print(example02)
[[2, 'SE_BID', 'SE_ASK', 'Time'], ['GBP', '888.85', '895.4', '2018-08-02 23:19:36'], ['USD', '683.01', '685.91', '2018-08-02 23:19:36'], ... , ['GBP', '891.33', '897.89', '2018-08-01 00:00:05'], ['USD', '680.22', '683.1', '2018-08-01 00:00:05']]
```

![](https://github.com/bobleer/bocfx/raw/master/images/%5BGBP%2BUSD%5DSE_BID%2BSE_ASK_2018-08-01_2018-08-02.png)
<br>
<br>

# Option and parameter
# 选项和参数
<br>

## Option 1 `-f`/`--fx`
## 外汇种类
`-f`/`--fx` is the BOC foreign excahnge selector. This opinion supports **multi-parameter**.

`,` is the separator of each parameter, e.g. `GBP,USD`
<br>
<br>

#### Supported foreign currency:
  
FX | ISO Code | Full Name | Alias
:-|:-|:-|:-
`英镑` | `GBP` | Great Britain Pound | `UK` 
`港币` | `HKD` | Hong Kong Dollar | `HK` 
`美元` | `USD` | United States Dollar | `US`/`USA` 
`瑞士法郎` | `CHF` | Swiss Franc | 
`德国马克` | `DEM` | Deutsche Mark | 
`法国法郎` | `FRF` | French Franc | `FF` 
`新加坡元` | `SGD` | Singapore Dollar | 
`瑞典克朗` | `SEK` | Swedish Krona | 
`丹麦克朗` | `DKK` | Danish Krone | 
`挪威克朗` | `NOK` | Norwegian Krone | 
`日元` | `JPY` | Japanese Yen | `JP` 
`加拿大元` | `CAD` | Canadian Dollar | `CA` 
`澳大利亚元` | `AUD` | Australian Dollar | `AU` 
`欧元` | `EUR` | Euro | `EU` 
`澳门元` | `MOP` | Macao Pataca | `MO`
`菲律宾比索` | `PHP` | Philippine Peso | 
`泰国铢` | `THB` | Thai Baht | 
`新西兰元` | `NZD` | New Zealand Dollar | `KIWI` 
`韩元` | `WON` | South Korean Won | `SK` 
`卢布` | `RUB` | Russian Ruble | `RU` 
`林吉特` | `MYR` | Malaysia Ringgit | `SEN` 
`新台币` | `NTD` | New Taiwan Dollar | `TW` 
`西班牙比塞塔` | `ESP` | Spain Peseta | 
`意大利里拉` | `ITL` | Italian Lira | 
`荷兰盾` | `ANG` | Nederlandse Gulden | 
`比利时法郎` | `BEF` | Belgian Franc | 
`芬兰马克` | `FIM` | Finnish Mark | 
`印度卢比` | `INR` | Indian Rupee | 
`印尼卢比` | `IDR` | Indonesian Rupee | 
`巴西里亚尔` | `BRL` | Brasil Rial | 
`阿联酋迪拉姆` | `AED` | United Arab Emirates Dirham | 
`南非兰特` | `ZAF` | South African Rand | 
`沙特里亚尔` | `SAR` | Saudi Arabian Riyal | 
`土耳其里拉` | `TRY` | Yeni Türk Lirası | `YTL` 
  
FX, ISO and Alias can be used as values of this option, e.g. `英镑`, `GBP`, `UK` are all correct.  
This parameter is case-insensitive, e.g. `GBP`, `gBp`, `UK`, `uk` will get same output.  
If not using this option, the default parameter will be `GBP, EUR, USD, CAD, AUD`.  
<br>
<br>

#### Example:

```
~
❯ bocfx            
100%|████████████████████████████████████████████| 5/5 [00:00<00:00, 612.38it/s]

+-----+--------+--------+--------+--------+---------------------+
|  5  | SE_BID | BN_BID | SE_ASK | BN_ASK |         Time        |
+-----+--------+--------+--------+--------+---------------------+
| GBP | 874.37 | 847.2  | 880.81 | 882.95 | 2019-02-25 07:28:17 |
| EUR | 759.05 | 735.47 | 764.65 | 766.35 | 2019-02-25 07:28:17 |
| USD | 670.24 | 664.79 | 673.08 | 673.08 | 2019-02-25 07:28:17 |
| CAD | 509.47 | 493.39 | 513.23 | 514.47 | 2019-02-25 07:28:17 |
| AUD | 478.68 | 463.81 | 482.21 | 483.38 | 2019-02-25 07:28:17 |
+-----+--------+--------+--------+--------+---------------------+
(SE = Spot Exchange, BN = Banknote)

~
❯ bocfx -f GBP,USD                                             
100%|███████████████████████████████████████████| 2/2 [00:00<00:00, 1818.08it/s]

+-----+--------+--------+--------+--------+---------------------+
|  2  | SE_BID | BN_BID | SE_ASK | BN_ASK |         Time        |
+-----+--------+--------+--------+--------+---------------------+
| GBP | 874.37 | 847.2  | 880.81 | 882.95 | 2019-02-25 07:28:17 |
| USD | 670.24 | 664.79 | 673.08 | 673.08 | 2019-02-25 07:28:17 |
+-----+--------+--------+--------+--------+---------------------+
(SE = Spot Exchange, BN = Banknote)
```
<br>
<br>

## Option 2 `-s`/`--sort`
## 牌价种类

`-s`/`--sort` is the filter of quotation types. This opinion supports **multi-parameter**.

`,` is the separator of each parameter.

`-s`/`--sort` | `SE` Spot Exchange 现汇价 | `BN` Banknote 现钞价
 :-|:-|:-
 `BID` Bid Price 买入价 | `SE,BID` SE_BID | `BN,BID` BN_BID 
 `ASK` Ask Price 卖出价 | `SE,ASK` SE_ASK | `BN,ASK` BN_ASK

If not using this option, the default output will include all four sorts.
<br>
<br>

#### Example:

```
~
❯ bocfx -f GBP,USD -s ASK                                  
100%|████████████████████████████████████████████| 2/2 [00:00<00:00, 443.63it/s]

+-----+--------+--------+---------------------+
|  2  | SE_ASK | BN_ASK |         Time        |
+-----+--------+--------+---------------------+
| GBP | 880.81 | 882.95 | 2019-02-25 07:28:17 |
| USD | 673.08 | 673.08 | 2019-02-25 08:35:54 |
+-----+--------+--------+---------------------+
(SE = Spot Exchange, BN = Banknote)

~
❯ bocfx -f GBP,USD -s SE,BID
100%|████████████████████████████████████████████| 2/2 [00:00<00:00, 443.26it/s]

+-----+--------+---------------------+
|  2  | SE_BID |         Time        |
+-----+--------+---------------------+
| GBP | 874.57 | 2019-02-25 08:35:54 |
| USD | 670.24 | 2019-02-25 08:35:54 |
+-----+--------+---------------------+
(SE = Spot Exchange, BN = Banknote)
```
<br>
<br>

## Option 3 `-t`/`--time`
## 时间范围选择

`-t`/`--time` can filter the date of foreign exchange quotation.

There are 3 ways to write parameter.

 No. | Example | Definition | 定义
 :-|:-|:-|:-
 1 | `6` | Get data from 6 days ago to today | 6 天之内的全部历史价格
 2 | `2019-02-20` | Get data from 2019-02-20 to today | 选定时间到今天的全部历史价格
 3 | `2019-02-20,2019-02-21` | Get data from 2019-02-20 to 2019-02-21 | 选定时间范围内全部历史价格
 
If not using this option, **only one price (the latest quotation price)** will be output.
<br>
<br>

## Option 4 `-p`/`--plot`
## 是否生成折线图

Using `-p`/`--plot` can generate a line graph with .png format.

The default output path is `~/bocfx_output/`
<br>
<br>
<br>

## Option 5 `-c`/`--csv`
## 是否生成csv表格

Using `-c`/`--csv` can output data in .csv format.

The default output path is `~/bocfx_output/`
<br>
<br>
<br>

## Option 6 `-o`/`--op`
## 自定义输出路径

Using `-o`/`--op` can change default output path.

Example: `-o '~/desktop/example/'`
<br>
<br>
<br>

## Option 7 `-b`/`--bar`
## 开启进度条显示

Using `-b`/`--bar` can show loading bar while the tasks are running.
<br>
<br>
<br>

# Limitation
# 局限性

This package is no-database design.   

All data are captured from http://srh.bankofchina.com/search/whpj/search.jsp in real time.  

**Thus, the speed of spider will be strongly influenced by the connectation quality!**  
**本脚本会受 中国银行官网接口速度 的影响！**
<br>
<br>
<br>

# MIT Licence

Copyright (c) 2019 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
<br>
