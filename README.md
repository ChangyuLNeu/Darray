# Darray
## Introduction
The Darray is a 2-dimensional data structure which is used for data preprocessing. It is inspired by Dataframe in Pandas

It is built by a two-levels nested(两层嵌套??) list(as list of lists). Every column is stored in a inner list and all of columns are store in a outer list. 

The type of data in Darray is numeric. 

You can you use Darray to complement following functions:

###**1.initialize Darray:by a list or csv file**

###**2.index and slice Darray; set value**

**3.Handle Na and outliers**

**4.Arrange data by ascending, descending or random order**

**5.concate data by column and row**

**6.summarize statistical information**

**7.....other calculation **

## Install
Use pip to install the package.

Note:the url is the website of the package on github
```
pip install git+https://github.com/ChangyuLNeu/Darray.git
```


## Usage(example of functions)
`1.` **initialize Darray**
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

`2.` **index and slice Darray**
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

`5.` **concate data by column and row**
```
b = Darray([[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8]], colnames=['name','sex','no'])
c = Darray([[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8]], colnames=['name','gender','no'])
d = Darray([[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8],[1,2,3,4,5,6]], colnames=['name','sex','no','age'])
e = Darray([[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8],[1,2,3,4,5,6]], colnames=['name','sex','no','age'])
f = Darray([[1,2,3,4,5,6,7],[2,3,4,5,6,7,8],[3,4,5,6,7,8,9],[1,2,3,4,5,6,7]], colnames=['name','sex','no','age'])

#concate data by row
e.concat_rows(f) #correct
b.concat_rows(c) #ValueError: column names are not same
b.concat_rows(d) #ValueError: amount of columns is not same

#concate data by column
c.merge_cols(d) #correct
e.merge_cols(f) #ValueError: rows number are not same
```






















## Authors
Changyu Liu, Zihan Zhao, Yishui Tian, Jiaran Kang, Jie Ji
