import csv
import numpy as np
from numpy import loadtxt 
from urllib.request import urlopen 
from pandas import read_csv
from pandas import set_option
from matplotlib import pyplot
#names = ['plas','pres','skin','test','mass','pedi','age','class']
filename = 'pima-indians-diabetes.csv'
data = read_csv(filename,index_col=0)

def load_csv():
    filename = 'pima-indians-diabetes.data.csv'  # contains only properties
    raw_data = open(filename,'r')
    reader = csv.reader(raw_data, delimiter=',',quoting=csv.QUOTE_NONE)
    x = list(reader)
    data = numpy.array(x).astype('float')
    print(data.shape)

def load_csv_np():
    # filename = 'pima-indians-diabetes.csv'
    raw_data = open(filename,'r')
    data = loadtxt(raw_data,delimiter=',')
    print(data)
    print(data.shape)

def load_csv_np_url():
    url = 'https://goo.gl/vhm1eU'
    raw_data = urlopen(url)
    dataset = loadtxt(raw_data,delimiter=',')
    print(dataset.shape)

def load_csv_pd():
    # filename = 'pima-indians-diabetes.csv'
    names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
    data = read_csv(filename,names=names)
    print(data.shape)

def load_csv_pd_url():
    url = 'https://goo.gl/vhm1eU'
    names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
    data = read_csv(url,names=names)
    # data = read_csv(url, header=None)
    data.to_csv('pima-indians-diabetes.csv')   # storing data to csv file
    print(data.shape)

def print_csv():
    names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
    data = read_csv(filename,names=names)
    #data = read_csv(filename, index_col=0)
    peek = data.head(20)
    print(peek)
    types = data.dtypes
    print(types)
    print(data.shape)

def des_csv():
    # names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
    # data = read_csv(filename,names=names, index_col=0)
    data = read_csv(filename, index_col=0)
    #set_option('display.width',100)
    #set_option('precision',3)
    desc = data.describe()
    print(desc)

def dis_csv():
    data = read_csv(filename, index_col=0)
    class_counts = data.groupby('class').size()
    print(class_counts)

def corr_csv():
    data = read_csv(filename, index_col=0)
    set_option('display.width',100)
    set_option('precision',3)
    corr = data.corr(method='pearson')
    print(corr)

def skew_csv():
    data = read_csv(filename, index_col=0)
    skew = data.skew()
    print(skew)

def hist_csv():
    data = read_csv(filename, index_col=0)
    data.hist()
    pyplot.show()

def den_csv():
    data = read_csv(filename,index_col=0)
    data.plot(kind='density',subplots=True,layout=(3,3),sharex=False)
    pyplot.show()
