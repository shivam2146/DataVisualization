from pandas import read_csv
#Better way to import pyplot from matplotlib
from matplotlib.pyplot import plt

def test():
    filename = "iris.csv"
    data = read_csv(filename,skiprows=[1])
    data.plot(kind="density",y="petallength");
    plt.show()
    #To save the plot figure
    plt.savefig('fig_data_plot.png')


if __name__ == "__main__":
    test()
