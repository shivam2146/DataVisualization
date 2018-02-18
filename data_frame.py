import pandas as pd
from matplotlib import pyplot

def test():
    filename= "iris.csv"
    df = pd.read_csv(filename,skiprows=[1])
    print(df.sepallength)
    print("length",len(df))
    print("shape",df.shape)
    print("columns",df.columns)
    print("dtypes\n",df.dtypes)
    print("index",df.index)
    print(df.values[2])


if __name__ == '__main__':
    test()
