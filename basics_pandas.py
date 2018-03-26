import pandas as pd
from matplotlib import pyplot
import numpy as np
def try1():
    print(pd.__version__)
    """
    DataFrame, which you can imagine as a relational data table, with rows and named columns.
    Series, which is a single column. A DataFrame contains one or more Series and a name for each Series.
    """
    city = pd.Series(['San Fransico','San Jose','Sacramento'])
    pop = pd.Series([82569,1015785,485199])
    cp = pd.DataFrame({'City name':city,'Population':pop})
    print(cp)
    df = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
    print(df.describe())
    df.hist()
    pyplot.show()
    print(df.head())

    #accessing data from dataframes using python dict style
    print(type(cp['City name']))
    print(cp['City name'][1])
    print(cp[0:2])

    #Python's basic arithmetic operations to Series
    print("poplation divided by 100\n",pop/100)
    print("log on population\n",np.log(pop))
    print(pop.apply(lambda val:val >82569))
    cp['Area square miles']= pd.Series([46.87,176.53,97.92])
    cp['Population density']= cp['Population']/cp['Area square miles']
    print(cp)
    cp['boolean'] =( cp['Area square miles'].apply(lambda val: val>50) & cp['City name'].apply(lambda s: s.startswith('San')))
    print(cp)
    print(cp.index)
    print(cp.reindex([2,0,1]))
    print(cp.reindex(np.random.permutation(cp.index)))

if __name__ == '__main__':
    try1()
