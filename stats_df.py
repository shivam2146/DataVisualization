import pandas as pd
from matplotlib import pyplot
import numpy as np
def test():
    filename= "iris.csv"
    df = pd.read_csv(filename,skiprows=[1])
    #print(df.describe())
    print("max:",df["sepallength"].max())
    print("count:",df["sepallength"].count())
    print("mad:",df["sepallength"].mad())
    print("median:",df["sepallength"].median())
    print("min:",df["sepallength"].min())
    print("mean:",df["sepallength"].mean())
    print("s.d:",df["sepallength"].std())
    print("var:",df["sepallength"].var())
    print("skew:",df["sepallength"].skew())
    print("kurt:",df["sepallength"].kurt())

    #To descibe the dataframe
    print(df.describe())
    #To describe the data types of the columns in the data frame
    print(df.info())






if __name__ == '__main__':
        test()
