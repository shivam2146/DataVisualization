import pandas as pd
from matplotlib import pyplot
import numpy as np
def test():
    filename= "iris.csv"
    df = pd.read_csv(filename,skiprows=[1])
    sl = df['sepallength']
    print("type df",type(df))
    print("type sepal_length",type(sl))
    print("series shape",sl.shape)
    print("series values",sl.values)
    print("series index",sl.index)
    print("series name",sl.name)
    #series slicing
    print(sl[-2:])
    #print sign of last three rows using np.sign func
    print(np.sign(sl[-3:]))




if __name__ == '__main__':
        test()
