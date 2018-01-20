from pandas import read_csv
from matplotlib import pyplot

def test():
    filename = "iris.csv"
    data = read_csv(filename,skiprows=[1])
    data.plot(title="line plot")         #by default kind is line
    pyplot.show()
    data.plot(kind="box",title="box plot")
    pyplot.show()
    data.plot(kind="density",title="density plot")
    pyplot.show()

if __name__ == "__main__":
    test()
