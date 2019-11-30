# bocfx ![](https://img.shields.io/badge/License-MIT-green.svg) ![](https://img.shields.io/badge/Python-3-blue.svg) ![](https://img.shields.io/badge/PyPI-0.7.0-orange.svg)
An easy-to-use python package for getting foreign exchange rate from Bank of China (BOC).  
一个帮你快速获取中国银行外汇牌价的 Python 应用（也可作API)。  
Author: [**Bob Lee**](https://boblee.cn)
<br>
<br>

# Features

* [x] **Multithreading 多线程**
* [x] **As a command-line application 支持命令行应用模式**
* [x] **As a python module 支持模块导入模式（导入到你自己的项目里就能作API了）**
* [x] **Foreign exchange selection 支持多种外汇币种同时输出（默认是英、欧、美、加、澳）**
* [x] **Foreign exchange quotation filter 支持外汇牌价种类同时输出（买入、卖出、现钞、现汇）**
* [x] **Date selection (Realtime/History) 支持按时间/时间段筛选**
* [x] **Line graph generation 支持生成历史波动曲线**
* [x] **.csv generation 支持导出csv格式表格文件**
* [x] **Set output path 支持导出到指定路径**
* [ ] **Database connection 支持导出到数据库（开发中）**

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
- [Limitation 局限性](#limitation)
- [MIT Licence](#mit-licence)
<br>

# Installation

```
# (Discarded) Required packages will be installed automatically
# (Discarded) pip3 install -U requests scrapy tqdm prettytable numpy matplotlib

# pip install bocfx
pip3 install bocfx 
```
<br>
<br>

# Basic Usage
<br>

## As a command-line application

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

## As a python module

```
>>> from bocfx import bocfx

>>> output = bocfx('GBP,USD','SE,ASK')
100%|████████████████████████████████████████████| 5/5 [00:00<00:00, 532.87it/s]

>>> output # The latest foreign exchange rate
['879.96', '672.28']
```
<br>
<br>

# Advanced Usage
<br>

## As a command-line application

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
<br>

## Option 1 `-f`/`--fx`

`-f`/`--fx` is the BOC foreign excahnge selector. This opinion supports **multi-parameter**.

`,` is the separator of each parameter.
<br>
<br>

#### Common foreign currency:

Parameter | Currency | Country (Region) | Alias
:-|:-|:-|:-
`GBP` | Pound | The United Kingdom | `gbp`/`UK`/`uk`
`EUR` | Euro | European Union | `eur`/`EU`/`eu`
`USD` | Dollar | The United States | `usd`/`USA`/`usa`/`US`/`us`
`CAD` | Canadian Dollar | Canada | `cad`/`CA`/`ca`
`AUD` | Australian Dollar | Australia | `aud`/`AU`/`au`
`RUB` | Russian Ruble | Russia | `rub`/`RU`/`ru`
`HKD` | Hong Kong Dollar | Hong Kong | `hdk`/`HK`/`hk`
`MOP` | Macao Pataca | Macao | `mop`
`NTD` | New Taiwan Dollar | Taiwan | `ntd`/`TW`/`tw`
`JPY` | Japanese Yen | Japan | `jpy`/`JP`/`jp`/`Yen`
`KRW` | South Korean Won | South Korean | `krw`/`KR`/`kr`
`THB` | Thai Baht | Thailand | `thb`/`Thai`
`PHP` | Philippine Peso | Philippines | `php`/`Peso`
`MYR` | Malaysian Ringgit | Malaysia | `myr`/`Sen`
`SGD` | Singapore Dollar | Singapore | `sgd`
`NZD` | New Zealand Dollar | New Zealand | `nzd`/`Kiwi`
`INR` | Indian Rupee | India | `inr`
`TRY` | Turkish Lira | Turkey | `try`/`YTL`/`ytl`
`BRL` | Brazilian Real | Brazil | `brl`
`IDR` | Indonesian Rupiah | Indonesia | `idr`
`ZAR` | South African Rand | South Africa | `zar`
`AED` | United Arab Emirates Dirham | United Arab Emirates | `aed`
`SAR` | Saudi Riyal | Saudi Arabia | `sar`

If not using this option, the default parameters will be `GBP, EUR, USD, CAD, AUD`.
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

`-s`/`--sort` is the filter of foreign exchange quotation. This opinion supports **multi-parameter**.

`,` is the separator of each parameter.

`-s`/`--sort` | `SE` Spot Exchange | `BN` Banknote
 :-|:-|:-
 `BID` Bid Price | `SE,BID` SE_BID | `BN,BID` BN_BID 
 `ASK` Ask Price | `SE,ASK` SE_ASK | `BN,ASK` BN_ASK

If not using this option, the default output will include all prices.
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

`-t`/`--time` can filter the date of foreign exchange quotation.

There are 3 ways to write parameter.

 No. | Example | Definition
 :-|:-|:-
 1 | `6` | Get data from 6 days ago to today
 2 | `2019-02-20` | Get data from 2019-02-20 to today
 3 | `2019-02-20,2019-02-21` | Get data from 2019-02-20 to 2019-02-21
 
If not using this option, **only the latest quotation** will be output.
<br>
<br>
<br>

## Option 4 `-p`/`--plot`

Using `-p`/`--plot` can generate a line graph with .png format.

The default output path is `~/bocfx_output/`
<br>
<br>
<br>

## Option 5 `-c`/`--csv`

Using `-c`/`--csv` can output data in .csv format.

The default output path is `~/bocfx_output/`
<br>
<br>
<br>

## Option 6 `-o`/`--op`

Using `-o`/`--op` can change default output path.

Example: `-o '~/desktop/example/'`
<br>
<br>
<br>

# Limitation

This package is no-database design.   

All data are captured from http://srh.bankofchina.com/search/whpj/search.jsp in real time.  

**Thus, the speed of spider will be strongly influenced by the connectation quality!**
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
