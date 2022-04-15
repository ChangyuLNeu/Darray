# -*- coding: utf-8 -*-

import io  
import numbers
import numpy as np
import random
import math
from utils import * 




        
class Darray:
    def __init__(self, values, colnames=None):
        """
        initialization
        
        Parameters
        ----------
        values : list
            elements of this list are iterables, like tuple or list.
        colnames : list, optional
            contain list of name for columns

        Returns
        -------
        a Darray: 
            attributes: data, colnames

        """
        width = len(values)
        length = max([len(col) for col in values])
        
        if colnames == None:
            self.colnames = ['c_'+str(i) for i in range(width)]
        else:
            self.colnames = list(colnames)
        
        self.data = [0] * width
        for i in range(width):
            value = values[i]
            if len(value) < length:       #complement shorter column
                diff = length-len(value)
                value.extend([None]*diff)
            self.data[i] = value
            
 
    def __str__(self):
        return self.output()
 
    def __repr__(self):
        return self.output()
 
    def __getitem__(self, key):
        """
        Get a subset of Darray

        Parameters
        ----------
        key : tuple
            key[0]: index of rows. It must be int, slice or list. 
                    If it is a list, the list only contains bool values and the leng of it show be length of Darray.  
            key[1]: index of columns. It must be int, slice, str or list. 
                    If it is a list, the list only contains str values which stand for column names.

        Returns
        -------
        Darray

        """
        key_row, key_col = key[0], key[1]
        width, length = self.sizeof()
        
        #deal with key_row
        if isinstance(key_row, int):
            row_index = [key_row]
        elif isinstance(key_row, slice):
            row_index = list(range(*key_row.indices(length)))
        elif isinstance(key_row, list):
            row_index = self.get_true_index(key_row)
        else:
            raise TypeError('wrong row index')
        
        #deal with key_col
        if isinstance(key_col, int):
            col_index = [key_col]
        elif isinstance(key_col, str):
            col_index = [self.colnames.index(key_col)]
        elif isinstance(key_col, slice):
            col_index = list(range(*key_col.indices(width)))
        elif isinstance(key_col, list):
            col_index = self.get_colnames_index(key_col)
        else:
            raise TypeError('wrong column index')
            
        #print('row', row_index)
        #print('col', col_index)
        
        sub_colnames = self.get_list_elements(self.colnames, col_index)
        sub_data = []
        for col_idx in col_index:
                sub_data.append(self.get_list_elements(self.data[col_idx], row_index))
        
        return Darray(sub_data, sub_colnames)
        
        
    def __setitem__(self, key, values):
        """
        Parameters
        ----------
        key : tuple
            key[0]: index of rows. It must be int, slice or list. 
                    If it is a list, the list only contains bool values and the leng of it show be length of Darray.  
            key[1]: index of columns. It must be int, slice, str or list. 
                    If it is a list, the list only contains str values which stand for column names.

        values: Number, list, or Darray
                 If it is a list, the list should be 2d, like [[1,2,3],[1,2,3]], and every element should have the same length
        """
        
        key_row, key_col = key[0], key[1]
        width, length = self.sizeof()
        
        #deal with key_row
        if isinstance(key_row, int):
            row_index = [key_row]
        elif isinstance(key_row, slice):
            row_index = list(range(*key_row.indices(length)))
        elif isinstance(key_row, list):
            row_index = self.get_true_index(key_row)
        else:
            raise TypeError('wrong row index')
        
        #deal with key_col
        if isinstance(key_col, int):
            col_index = [key_col]
        elif isinstance(key_col, str):
            col_index = [self.colnames.index(key_col)]
        elif isinstance(key_col, slice):
            col_index = list(range(*key_col.indices(width)))
        elif isinstance(key_col, list):
            col_index = self.get_colnames_index(key_col)
        else:
            raise TypeError('wrong column index')
        
        sub_size = (len(row_index), len(col_index))
        
        #deal with values
        if isinstance(values, numbers.Number):
            self.set_single_value([row_index, col_index], values)
        elif isinstance(values, (list, Darray)):
            self.set_2d_value([row_index, col_index], values)
        else:
            raise TypeError('wrong input type')
        
        
    def output(self, num_cols=10, num_rows=100):
        """
        Get output with a format for __str__ and __repr__
        Parameters
        ----------
        num_rows :int , optional
            first num_cols columns which you want to print . The default is 10.
        num_rows : TYPE, optional
            first intnum_rows rows which you want to print . The default is 100.

        Returns
        -------
        content : str
            output content.

        """
        output = io.StringIO()
        width, length = self.sizeof()
        if num_cols < width:
            width = num_cols
        if num_rows < length:
            length = num_rows
        
        [output.write('{:>12s}'.format(name)) for name in self.colnames]
        output.write('\n')
        for i in range(length):
            for j in range(width):
                output.write('{:12.8g}'.format(self.data[j][i]))
            output.write('\n')
        content = output.getvalue()
        output.close()
        return content

        
    def sizeof(self):
        """
        Return width and length of the Darray
        Returns
        -------
        width: int
            width of Darray
        length: int
            length of Darray
        """
        width = len(self.data)
        length = len(self.data[0])
        
        return width, length     


    def concat_rows(self,new_Darry):
        """
        concat rows of Darray
        Parameters
        ----------
        row_indx : list
            list of row indices
        new_Darry : Darray
            Darray to be concated
        Returns
            concated Darray
       """
        if len(self.colnames)!=len(new_Darry.colnames):
            raise ValueError('col number is not same')
        else:
            new_data = []
            new_list = []
            for i in range(len(self.data)):
                new_list = self.data[i][:]
                new_data.append(new_list)
            for i in range(len(self.colnames)):
                for j in range (len(new_Darry.colnames)):
                    if self.colnames[i] == new_Darry.colnames[j]:
                        for num in range(len(new_Darry.data[j])):
                            new_data[i].append(new_Darry.data[j][num])
                    for colname in self.colnames:
                        if colname not in new_Darry.colnames:
                            raise ValueError('colnames are not same')
            return Darray(new_data, self.colnames)
        if len(self.colnames)!=len(new_Darry.colnames):
            raise ValueError('col number is not same')
        
            
    def merge_cols(self, new_Darry):
        
        new_data1= []
        new_list1= []
        for i in range(len(self.data)):
            new_list1 = self.data[i][:]
            new_data1.append(new_list1)
        new_list2 = []
        if len(self.data[0])==len(new_Darry.data[0]):
            for j in range(len(new_Darry.data)):
                new_list2 = new_Darry.data[j][:]
                new_data1.append(new_list2)
            for i,item in enumerate (new_Darry.colnames):
                new_Darry.colnames[i]=item + '*'
            self.colnames=self.colnames + new_Darry.colnames
            
        else:
            raise ValueError('rows number are not same')
        
        return Darray(new_data1, self.colnames)
            
    
    def replace_outliers(self):
        """
        replace outliers of Darray
        Parameters
        ----------
        list_elements : list
            list of elements
        """
        for colname in range(len(self.colnames)):
            Q1Q3=q1q3(self.data[colname])
            Q1=Q1Q3[0]
            Q3=Q1Q3[1]
            IQR=Q3-Q1
            outlier_step=1.5*IQR
            outlier_max=Q3+outlier_step
            outlier_min=Q1-outlier_step
            for i in range(len(self.data[colname])):
                if self.data[colname][i]>outlier_max:
                    self.data[colname][i]=outlier_max
                elif outlier_min<self.data[colname][i]<outlier_max:
                    self.data[colname][i]=self.data[colname][i]
                else:
                    self.data[colname][i]=outlier_min  
    
    
    def order(self,col,way):
        """
        Order the rows according to the numbers in selected column acendingly/decendingly/randomly
        
        Parameters
        ----------
        col : index
            the column where we chose to order by
        way: asc/dec/random
            the way to order the numbers


        Returns
        -------
        result : Darray
            Ordered rows according to the column selected

        """
        #change col into int
        if type(col)==int:
            col = col
        elif type(col)==str:
            if col in self.colnames:
                col = self.colnames.index(col)
            else:
                raise TypeError('wrong column index')
        else:
            raise TypeError('wrong input type')
                 
        #create a new empty list and an index list
        y = list(range(len(self.data[col])))
        mylist = [[0,0]]
        newlen = len(self.data[col])
        while (newlen)-1>0:
           mylist+=[[0,0]]
           newlen-=1
           
        #sort and creat index list
        if way == 'asc':
            new_self = self.fillna(math.inf)
            for i in range(len(self.data[col])):
                mylist[i][0]=new_self.data[col][i]
                mylist[i][1]=y[i]
            mylist.sort(key = method)
            for i in range(len(self.data[col])):
                y[i]=mylist[i][1]
        elif way == 'dec':
            new_self = self.fillna(-math.inf)
            for i in range(len(self.data[col])):
                mylist[i][0]=new_self.data[col][i]
                mylist[i][1]=y[i]
            mylist.sort(reverse=True, key=method)
            for i in range(len(self.data[col])):
                y[i]=mylist[i][1]
        elif way =='random':
            new_self = self
            numblist = []
            nplist=[]
            for i in range(len(new_self.data[col])):
                if new_self.data[col][i] is not np.nan:
                    numblist.append(i)
                else:
                    nplist.append(i)
                    
            y=random.sample(numblist,len(numblist))+nplist
  
        #create an empty list to build darray
        
        width = len(self.data)
        newlist =[[0]*len(self.data[col])]
        while (width)-1>0:
           newlist+=[[0]*len(self.data[col])]
           width-=1


           
        for i in range(len(self.data)):
            loc = 0
            for j in range(len(self.data[col])):
                    newlist[i][j]=new_self.data[i][y[loc]]
                    loc+=1
                    
        #change the -inf back
        for i in range(len(self.data)):
            for j in range(len(self.data[col])):
                if newlist[i][j] == -math.inf:
                    newlist[i][j]=np.nan
                elif newlist[i][j] == math.inf:
                    newlist[i][j]=np.nan
                    
        result = Darray(newlist,colnames=self.colnames)
                    
        return result
                   
                
    def countna_col(self):
        """
        Count the existence of nan each column you selected
        
        Parameters
        ----------
        col : index
            the column where we want to count nan


        Returns
        -------
        num : integer
            How many nan are there in the column

        """
        width = len(self.data)
        length =len(self.data[0])
        na_col= []
        
        for i in range(width):
            num=0
            for j in range(length):
                if self.data[i][j] is np.nan:
                    num+=1
            na_col.append(num)    
        return na_col
    

    def countna_row(self):
        """
        Count the existence of nan for each row 
        
        Parameters
        ----------
        row : index
            the row where we want to count nan

        Returns
        -------
        num : integer
            How many nan are there in the row

        """
        width = len(self.data)
        length =len(self.data[0])
        na_row= []
        
        for j in range(length):
            num=0
            for i in range(width):
                if self.data[i][j] is np.nan:
                    num+=1
            na_row.append(num)    
        return na_row
    

    def countna(self):
        """
        Count the existence of nan in the Whole Darray

        Returns
        -------
        num : integer
            How many nan are there in the Darray

        """
        num=0
        width, length = self.sizeof()
        for i in range(width):
            for j in range(length):
                if self.data[i][j] is np.nan:
                    num+=1
            
        return num
        

    def fillna(self,number):
        """
        Fill the nan in Darray with the number chosen
        
        Parameters
        ----------
        number : index
            the number we choose to replace nan, it can be 'mean', 'median'.

        Returns
        -------
        result : Darray
            The Darray after all nan are replaced with number selected

        """
        width, length = self.sizeof()
        
        newwid = width
        newD=[length*[0]]
        while newwid-1>0:
           newD+=[length*[0]]
           newwid-=1
        for i in range(width):
            for j in range(length):
                newD[i][j] = self.data[i][j]
        if number == 'median':
            for i in range(width):
                for j in range(length):
                    if self.data[i][j] is np.nan:
                        self.data[i][j]=median(self.data[i])
        elif number == 'mean':
            for i in range(width):
                for j in range(length):
                    if self.data[i][j] is np.nan:
                        self.data[i][j]=mean(self.data[i])
        else:
            for i in range(width):
                for j in range(length):
                    if self.data[i][j] is np.nan:
                        newD[i][j]=number
            
        
        result = Darray(newD,colnames=self.colnames)
        return result
    

    def deletena(self):
        """
        Delete the rows with nan
        
        Parameters
        -------

        Returns
        -------
        result : Darray
            The Darray after all rows which contains nan are deleted

        """
        width = len(self.data)
        length =len(self.data[0])
        newcol = self.colnames
        mylist=[]
        for j in range(length):
            for i in range(width):
                if self.data[i][j] is np.nan:
                    if j not in mylist:
                        mylist.append(j)
                   
                     
        newwid = width
        newD=[(length-len(mylist))*[0]]
        while newwid-1>0:
           newD+=[(length-len(mylist))*[0]]
           newwid-=1

        
        for a in range(width):
            loc=0
            for b in range(length):
                if b not in mylist:
                    newD[a][loc]=self.data[a][b]
                    loc+=1
        
        result = Darray(newD,colnames=newcol)
                    
        return result
    

    def deletena_col(self):
        """
        Delete the whole columns with nan
        
        Parameters
        -------

        Returns
        -------
        result : Darray
            The Darray after all columns which contains nan are deleted

        """
        width = len(self.data)
        length =len(self.data[0])
        mylist=[]
        for i in range(width):
            for j in range(length):
                if self.data[i][j] is np.nan:
                    if i not in mylist:
                        mylist.append(i)
                   
        newwid=width-len(mylist)
        newD=[[]]
        while newwid-1>0:
            newD+=[[]]
            newwid-=1
        loc = 0
        newcol = []
        for a in range(width):
            if a not in mylist:
                newD[loc]=self.data[a]
                newcol.append(self.colnames[loc])
                loc+=1
                
                
        result = Darray(newD,colnames=newcol)
        return result    


    def set_2d_value(self, index_2d, value_2d):
        if isinstance(value_2d, list):
            values = value_2d
        elif isinstance(value_2d, Darray):
            values = Darray.data
        else:
            raise TypeError('wrong input type')
            
        if (len(index_2d[0]), len(index_2d[1])) == self.get_2d_list_size(values):
            for col in range(len(index_2d[1])):
                for row in range(len(index_2d[0])):
                    self.data[index_2d[1][col]][index_2d[0][row]] = values[col][row]
        else:
            raise TypeError('wrong input size')
        
    
    
    def set_single_value(self, index_2d, value):
        length = len(index_2d[0])
        width = len(index_2d[1])
        
        value_2d = [[value] * length] * width
        self.set_2d_value(index_2d, value_2d)
    
    
    def get_2d_list_size(self, list_2d):
        width = len(list_2d)
        
        #get length of all lists
        lengths = [len(lst) for lst in list_2d]
        min_length = min(lengths)
        max_length = max(lengths)
        
        length = (min_length + max_length) / 2

        return length, width


    def get_list_elements(self, lst, idxs):
        """
        Get elements which index are idxs

        Parameters
        ----------
        lst : list
            the list where we want to get elements 
        idxs : list
            index of elements of a list

        Returns
        -------
        list_element : list
            elements we want

        """
        list_element = []
        for idx in idxs:
            list_element.append(lst[idx])
        return list_element

    
    def get_true_index(self, list_bool):
        index_list = []
        for i in range(len(list_bool)):
            if list_bool[i] ==True:
                index_list.append(i)
        return index_list


    def get_colnames_index(self, list_colnames):
        index_list = []
        for colname in list_colnames:
            index = self.colnames.index(colname)
            index_list.append(index)
        return index_list


    def read_csv(file_path, header=True):
        """
        read data from csv file and use it to initialize a new Darray
        
        Parameters
        ----------
        file_path : str
            file path of csv file.
        header : bool, optional
            Whether use first line of csv file as column names. The default is True.
    
        Returns
        -------
        Drray
            a new Darray from csv
    
        """
        list_colnames = None
        with open(file_path, 'r',) as f1:
            list_lines = f1.readlines()
        if header == True:
            list_colnames = list_lines[0].rstrip().split(',')
            list_lines = list_lines[1:]
        
        length = len(list_lines)
        width = len(list_lines[0].rstrip().split(','))
        
        data = [] 
        for i in range(width):
            data.append([None]*length)
        
        for row_idx in range(length):
            row_values_list = list_lines[row_idx].rstrip().split(',')
            for col_idx in range(width):
                if row_values_list[col_idx] == '':
                    data[col_idx][row_idx] = np.nan
                else:
                    data[col_idx][row_idx] = float(row_values_list[col_idx])
                #print(col_idx,row_idx, row_values_list[col_idx])
                #print(row_values_list[col_idx])
                #print(data[col_idx][row_idx]) 
                #print(data)
        
        return Darray(data, list_colnames)                    
