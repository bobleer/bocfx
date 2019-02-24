
## Installation

```
### Required packages
# pip3 install -U requests scrapy tqdm prettytable numpy matplotlib

pip3 install bocfx
```

## Basic Usage
###### As stand-alone	 application

```
~
❯ bocfx                        
100%|████████████████████████████████████████████| 5/5 [00:00<00:00, 471.66it/s]


+-----+--------+--------+--------+--------+---------------------+
|  5  | SE_BID | BN_BID | SE_ASK | BN_ASK |         Time        |
+-----+--------+--------+--------+--------+---------------------+
| GBP | 873.83 | 846.68 | 880.27 | 882.41 | 2019-02-24 10:30:00 |
| EUR | 758.58 | 735.01 | 764.18 | 765.87 | 2019-02-24 10:30:00 |
| USD | 670.24 | 664.79 | 673.08 | 673.08 | 2019-02-24 10:30:00 |
| CAD | 508.86 | 492.79 | 512.61 | 513.85 | 2019-02-24 10:30:00 |
| AUD | 477.14 | 462.31 | 480.65 | 481.82 | 2019-02-24 10:30:00 |
+-----+--------+--------+--------+--------+---------------------+
(SE = Spot Exchange, BN = Banknote)

~
❯ 
```

###### As module

```
>>> from bocfx import bocfx

>>> output = bocfx()
100%|████████████████████████████████████████████| 5/5 [00:00<00:00, 532.87it/s]

>>> output
[[5, 'SE_BID', 'BN_BID', 'SE_ASK', 'BN_ASK', 'Time'], ['GBP', '873.83', '846.68', '880.27', '882.41', '2019-02-24 10:30:00'], ['EUR', '758.58', '735.01', '764.18', '765.87', '2019-02-24 10:30:00'], ['USD', '670.24', '664.79', '673.08', '673.08', '2019-02-24 10:30:00'], ['CAD', '508.86', '492.79', '512.61', '513.85', '2019-02-24 10:30:00'], ['AUD', '477.14', '462.31', '480.65', '481.82', '2019-02-24 10:30:00']]
```

## Advanced Usage
###### As stand-alone	 application

```
bocfx -f -s -t -p -c -o
```

###### As module

```
from bocfx import bocfx

bocfx(FX=0, sort=0, time=-1, plot=0, csv=0, pt=0, op='~/bocfx')
```

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

