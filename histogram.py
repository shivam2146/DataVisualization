from pandas import read_csv
from matplotlib import pyplot

def histogram():
    filename= "iris.csv"
    data = read_csv(filename,skiprows=[1])
    print(data.dtypes)      #gives details of datatypes of attributes
    data.hist()             #makes a histogram
    pyplot.show()           #displays the graph

if __name__ == '__main__':
    histogram()
