import csv
import plotly.figure_factory as ff
import pandas as pd

list1 = []
dataf = pd.read_csv('./data.csv')
list1 = dataf["Height(Inches)"].tolist()


figure = ff.create_distplot([list1],["Height"])
figure.show()