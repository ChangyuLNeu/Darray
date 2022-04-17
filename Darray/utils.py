# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:20:06 2022

@author: Administrator
"""

import math


def median(x):
    """
    Calculate the median value of an iterable
    Parameters
    ----------
    x : An iterable to calculate the median value

    Returns
    -------
    The median value.

    """
    x=[x_ for x_ in x if x_==x_]                      #ignore np.nan
    half = len(x) // 2
    x.sort()
    if not len(x) % 2:
        return (x[half - 1] + x[half]) / 2.0
    return x[half]

def mean(x):
    """
    Calculate the average of an iterable
    Parameters
    ----------
    x : An iteralbe to take the average of the values

    Returns
    -------
    The average

    """
    x=[x_ for x_ in x if x_==x_]
    number_count=0
    sum_number=0
    for i in x:
            number_count= number_count+1
            sum_number=sum_number+i
    if number_count==0:
        return None
    else:
        means=sum_number/number_count
        return means

def imax(x):
    """
    Get the maximum value of an iterable
    Parameters
    ----------
    x : An iteralbe to find the maximum

    Returns
    -------
    The maximum

    """
    x=[x_ for x_ in x if x_==x_]
    max_num=-math.inf
    max_index=None
    for i in range(len(x)):
            if(x[i]>max_num):
                max_num=x[i]
                max_index=i
    return x[max_index]
   
   

def min(x):
    """
    Get the minimum of an iterable
    Parameters
    ----------
    x :  An iteralbe to find the minimum

    Returns
    -------
    The minimum

    """
    x=[x_ for x_ in x if x_==x_]
    min_num=math.inf
    min_index=None
    for i in range(len(x)):
        if(x[i]<min_num):
            min_num=x[i]
            min_index=i
            
    return x[min_index]


def count(x):
    """
    Return a dictionary of unique values and their counts in a list 
    
    Parameters
    ----------
    x : list

    Returns
    -------
    cnt : dictionary
        count of every element in the list x

    """
    x=[x_ for x_ in x if x_==x_]
    #define an empty dictionary first 
    cnt={}
    #for every element in x: if it appears once, return 1 for its count; else, plus one to its count every time it appears again.
    for v in x:
        if v in cnt:
            cnt[v] += 1
        else:
            cnt[v] = 1
            
    return cnt


def max_index(x):
    """
    Finds and returns the index of the maximum numeric value (float/int) in an iterable x 
    Non-numeric values are silently skipped over and ignored

    Parameters
    ----------
    x : list
        may contain non-numeric values.

    Returns
    -------
    idx : index of the maximum numeric value (float/int) in an iterable x 
    Returns None if no numeric values are encountered   

    """
    x=[x_ for x_ in x if x_==x_]
    #define the initial value of the maximum value
    val=-math.inf
    #define the inital value of the index (Returns None if no numeric values are encountered)
    idx=None
    for i in range(len(x)):
        if isinstance(x[i],(int,float)) and x[i] > val:
            #keep updating the maximum and the index of the maximum till the last element in x
            val=x[i]
            idx=i
    #return the index of the maximum 
    #if the maximum value appears more than once in the list, this function only returns the minimum index for the value
    return idx

def mode_1(x):
    """
    Calculates and returns the most common value (mode)  in an iterable x (not sensitive to ties)
    
    Parameters
    ----------
    x : list

    Returns
    -------
    list(count(x).keys())[idx] : mode element

    """
    x=[x_ for x_ in x if x_==x_]
    #find the index of the maximum value of the dictionary which is created by count() function
    idx=max_index(list(count(x).values()))
    #return the key for the index
    #since the imax() function only returns the minimum index for the maximum, it is not sensitive to ties.
    return list(count(x).keys())[idx]



def variance(x):
    '''
    variance of a list

    Parameters
    ----------
    x : a list of numbers 
        

    Returns
    -------
    var : the variance

    '''
    x=[x_ for x_ in x if x_==x_]
    var=0
    
    for i in range(len(x)):
        var=var+(x[i]-mean(x))**2
        
    return var       


def q1q3(x):
    """
    Calculates and returns Q1 and Q3 (the first and third quartiles) of an iterable x

    Parameters
    ----------
    x : list
        contains only numeric elements

    Returns
    -------
    q1q3: a list of 2 elements[Q1,Q3]

    """
    x=[x_ for x_ in x if x_==x_]
    x = sorted(x)
    n = len(x)
    i = math.floor(n/2)
    q1q3 = []
    if n % 2 == 0:
        small = x[0:i]
        Q1 = median(small)
        large = x[i:n]
        Q3 = median(large)
    else:
        small = x[0:i+1]
        Q1 = median(small)
        large = x[i:n]
        Q3 = median(large)
    q1q3.append(Q1)
    q1q3.append(Q3)
    return q1q3  



def method(elem):
    """
    A self defined sorthing method that 
    let sort function sort according to the first element of the list. 

    Parameters
    ----------
    elem : LIST
        The list we are going to sort.

    Returns
    -------
    The first element of the list.

    """
    return elem[0]
    
