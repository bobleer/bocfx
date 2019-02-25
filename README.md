# bocfx
A python package for getting foreign exchange rate from Bank of China (BOC).

## Features

1. Foreign exchange selection.
2. Foreign exchange quotation filter.
3. Date selection.
4. Line graph output.
5. .csv output.

## Installation

```
### Required packages
### pip3 install -U requests scrapy tqdm prettytable numpy matplotlib

pip3 install bocfx
```

## Basic Usage
#### As command-line application

```
~
❯ bocfx                        
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

#### As python module

```python
>>> from bocfx import bocfx

>>> output = bocfx('GBP,USD','SE,ASK')
100%|████████████████████████████████████████████| 5/5 [00:00<00:00, 532.87it/s]

>>> output # Latest foreign exchange rate
['879.96', '672.28']
```

## Advanced Usage
#### As command-line application

```Bash
bocfx [-f|--fx] [-s|--sort] [-t|--time] (-p|--plot) (-c|--csv) {-o|--op}
```

###### Example:

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

#### As python module

```python
from bocfx import bocfx

bocfx(FX=0, sort=0, time=-1, plot=0, csv=0, pt=0, op='~/bocfx_output')
```

###### Example:

```
>>> from bocfx import bocfx

### Equivalent command
### example01 = bocfx(FX='GBP,USD', sort='SE', time=1)
>>> example01 = bocfx('GBP,USD','SE',1)
100%|█████████████████████████████████████████████| 2/2 [00:01<00:00,  1.49it/s]

>>> type(example01)
<class 'list'>
>>> print(example01)
[[2, 'SE_BID', 'SE_ASK', 'Time'], ['USD', '669.74', '672.58', '2019-02-25 09:25:23'], ['GBP', '874.18', '880.62', '2019-02-25 09:25:13'], ... , ['GBP', '873.83', '880.27', '2019-02-24 00:00:05'], ['USD', '670.24', '673.08', '2019-02-24 00:00:05']]
```

```
>>> from bocfx import bocfx

### Equivalent command
### example02 = bocfx(FX='GBP,USD', sort='SE', time='2018-08-01,2018-08-02', plot=1, csv=1, pt=0, op='~/desktop/example/')
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

## Option and parameter
#### Option 1 `-f`/`--fx`

`-f`/`--fx` is the BOC foreign excahnge selector. This opinion supports **multi-parameter**.

`,` is the separator of each parameter.

Common foreign currency:

Parameter | Currency | Country (Region) | Fault-tolerant
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

If not using this option, the default parameters will be `GBP,EUR,USD,CAD,AUD`.

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

#### Option 2 `-s`/`--sort`

`-s`/`--sort` is the filter of foreign exchange quotation. This opinion supports **multi-parameter**.

`,` is the separator of each parameter.

`-s`/`--sort` | `SE` Spot Exchange | `BN` Banknote
 :-|:-|:-
 `BID` Bid Price | `SE,BID` SE_BID | `BN,BID` BN_BID 
 `ASK` Ask Price | `SE,ASK` SE_ASK | `BN,ASK` BN_ASK

If not using this option, the default output will include all prices.

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

#### Option 3 `-t`/`--time`

`-t`/`--time` can filter the date of foreign exchange quotation.

`,` is the separator of each parameter.





## MIT Licence

Copyright (c) 2018 The Python Packaging Authority

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

