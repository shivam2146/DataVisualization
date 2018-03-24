from pandas import read_csv
from matplotlib import pyplot

def test():
    filename = "iris.csv"
    data = read_csv(filename,skiprows=[1])
    data.plot(kind="density",y="petallength");
    pyplot.show()


if __name__ == "__main__":
    test()
