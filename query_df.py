import pandas as pd
from matplotlib import pyplot
import numpy as np
def test():
    filename= "iris.csv"
    df = pd.read_csv(filename,skiprows=[1])
    print(df.head(2))
    print(df.tail(2))
    print(df.iloc[[2,3,6,5,8]]) #to get particular rows
    print(df.iloc[1,1]) #to access a particular location
    print(df.iat[1,1])  #same but faster
    print(df["sepallength"].mean())
    print(df[df["sepallength"] > df["sepallength"].mean()]) #prints rows where sepallength is greater than mean sepal length
    






if __name__ == '__main__':
        test()
