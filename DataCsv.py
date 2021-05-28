import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import csv
from datetime import datetime

sample_data = pd.read_csv('California_Fire_Incidents.csv')
californiaCounties = []
acresBurned = []
county_acre_burn_dict = {}


def initialize_data():
    return dict(zip(sample_data.Counties, sample_data.AcresBurned))


def csv_file():
    with open('California_Fire_Incidents.csv', 'r', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            acresBurned.append([line[9],line[0]])


class DataCsv:

    def __init__(self):
        self.sample_data = None


print(initialize_data())
csv_file()
print(acresBurned)
# res = dict(zip(sample_data.Counties, sample_data.AcresBurned))
# print(str(res))
