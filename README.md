# Darray
## Introduction
The Darray is a 2-dimensional data structure which is used for data preprocessing. It is inspired by Dataframe in Pandas

It is built by a two-levels nested(嵌套的) list(as list of lists). Every column is stored in a inner list and all of columns are store in a outer list. 

The type of data in Darray is numeric. 

You can you use Darray to complement following functions:

1.initialize Darray:by a list or csv file

2.index and slice Darray; set value

3.Handle Na and outliers

4.Arrange data by ascending, descending or random order

5.concate data by column and row

6.summarize statistical information

7.....other calculation 

## Install
Use pip to install the package.

Note:the url is the website of the package on github
```
pip install git+https://github.com/ChangyuLNeu/Darray.git
```


## Usage(example of use)
1 initialize Darray
```
from darray import *

#use a nested list to initialize
a = Darray(
    values = [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
            [25.0, 21.0, 20.0, 22.0, 24.0, 23.0, 22.0, 21.0, 21.0, 25.0],
            [177.5, 180.0, 175.0, 170.0, 172.5, 177.8, np.nan, 170.5, 178.5, 181.5],
            [62.0, 70.0, 72.0, 55.0, 60.5, 72.0, np.nan, 61.0, 150.0, np.nan],
            [60.0, 70.0, 80.0, -20.0, 95.0, 85.0, np.nan, 70.0, 72.0, 90.0]],
    colnames = ['id', 'age', 'height', 'weight', 'grade'])

#use a csv file to initialize
a = Darraty.read_csv('test.csv')    #download 'test.csv' from this repository

print(a)
```

2index and slice Darray
```
#index one cell by indexes
a[1,0]

#index by colnames
a[1,'no']
a[1,['no', 'name']]

#index by boolean
a[[True, False, False, False, False, False, False, True],0]

#slice Darray
a[1:5,0:2]
a[1:5,:]
a[1:3,['no', 'name']]
```


























## Authors


'''
import numpy as np
'''

```
first push
```
