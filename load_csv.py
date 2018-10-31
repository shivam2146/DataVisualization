from pandas import read_csv
def test():
    url="https://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt"
    filename= "iris.csv"
    names=['var','skewness','curtosis','entropy','class']
    '''
    using url from where to load dataset
    '''
    data= read_csv(url,names=names)     #reads csv file into a data frame or text parser
    data1 = read_csv(url,header=None)  #as header is none it doesn't takes first row as column names it assigns names itself
    data2=read_csv(url)             #there is a argument index_col which can be used to assign a column as index
    data4 = read_csv(url,names=names,index_col=0) #to set 0th column as the index column
    print(data.head(5),"\n")
    print(data1.head(5),"\n")
    print(data2.head(5),"\n")
    print(data4.head(5),"\n")

    '''
    using csv file to load data
    '''
    data3= read_csv(filename,skiprows=[1])          #skips row no 1 as it contains datatypes and we dont need em
    print(data3.head(5))

if __name__=='__main__':
    test()
