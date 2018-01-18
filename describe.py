from pandas import read_csv
from pandas import set_option
from matplotlib import pyplot

def des():
    filename = "iris.csv"
    data= read_csv(filename,skiprows=[1])
    set_option('display.width',100)
    set_option('precision',3)
    d= data.describe()          #gives basic info about columns like mean max etc
    class_counts = data.groupby('class').size()
    print(d)
    print(data.shape)
    print(class_counts)

if __name__ == '__main__':
    des()
