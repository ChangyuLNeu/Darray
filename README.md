# Darray
## Introduction
The Darray is a data-frame-like 2-dimensional data structure used for data preprocessing inspired by Dataframe in Pandas with variables as columns and observation as rows.

It is built by a two-level nested list(i.e.[[inner_list1],[inner_list2],...]). Every column in a table is stored in an inner list and all of columns are stored in an outer list. 

Darray includes two attributes: data and colnames. The attribute 'data' stores the data of varibles as a two-level nested list and the attribute 'colnames' stores the names of variables as a list.

The type of data in Darray is numeric. 

You can you use Darray to complement following functions:

**1. Initialize Darray:by a list or csv file**

**2. Index and slice Darray; set value**

**3. Handle Na and outliers**

**4. Arrange data by ascending, descending or random order**

**5. Concat data by columns or rows**

**6. Summarize statistical information**

**7. Operations on Darray**

## Install
Use pip to install the package.

Note:the url is the website of the package on github
```
pip install git+https://github.com/ChangyuLNeu/Darray.git
```


## Usage(example of functions)
`1.` **Initialize Darray**
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
a = Darray.read_csv('test.csv')    #download 'test.csv' from this repository

print(a)
```

`2.` **Index and slice Darray**
```
#index one cell by indexes
a[1,0]

#index by colnames
a[1,'id']
a[1,['id', 'age']]

#index by boolean
a[[True, False, False, False, False, False, False, True],0]

#slice Darray
a[1:5,0:2]
a[1:5,:]
a[1:3,['id', 'age']]
```

`3.` **Handle Na and outliers**
```
#count all nan in Darray
a.countna()

#count nan by column 
a.countna_col()

#count nan by row 
a.countna_row()

#replace nan with a number
a.fillna(0)

#replace nan with mean of the column
a.fillna('mean')

#replace nan with median of the column
a.fillna('median')

#delete rows with nan
a.deletena()

#delete columns with nan
a.deletena_col()

#replace outlier use
a.replace_outliers()         #这里测试会把nan值，按照lower outlier填充掉。是有问题的
```

`4.` **Arrange data by ascending, descending or random order**
```
#ascending order(by column index)
a.order(1,'asc') 

#ascending order(by column name)
a.order('age','asc') 

#descending order(by column index)
a.order(1,'dec')        

#random order(by column index)
a.order(1,'random')      
```    

`5.` **Concat data by columns or rows**
```
b = Darray([[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8]], colnames=['apple','banana','orange'])
c = Darray([[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8]], colnames=['apple','peach','orange'])
d = Darray([[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8],[1,2,3,4,5,6]], colnames=['apple','banana','orange','pear'])
e = Darray([[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8],[1,2,3,4,5,6]], colnames=['apple','banana','orange','pear'])
f = Darray([[1,2,3,4,5,6,7],[2,3,4,5,6,7,8],[3,4,5,6,7,8,9],[1,2,3,4,5,6,7]], colnames=['apple','banana','orange','pear'])

#concate data by row
e.concat_rows(f) #correct
b.concat_rows(c) #ValueError: column names are not same
b.concat_rows(d) #ValueError: amount of columns is not same

#concate data by column
c.merge_cols(d) #correct
e.merge_cols(f) #ValueError: rows number are not same
```

`6` **Summarize statistical information**
```
a.summary()
```

`7.` **Operations on Darray**
```
#add operation with a single number
b + 1

#add operation with another Darray with the same shape
d + e

#subtract operation with a single number
b - 2

#subtract operation with another Darray with the same shape
d - e

#multiply operation with a single number
b * 3 

#multiply operation with another Darray with the same shape
d * e

#division operation with a single number
b / 2

#division operation with another Darray with the same shape
d / e

#calculate sum of each element in a Darray
b.sum()
```

## Authors
Changyu Liu, Zihan Zhao, Yishui Tian, Jiaran Kang, Jie Ji
