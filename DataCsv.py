import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

sample_data = pd.read_csv('California_Fire_Incidents.csv')
# print(sample_data.AcresBurned)
# plt.plot(sample_data.AcresBurned)
# plt.show()


def plotAcres():
    return plt.plot(sample_data.AcresBurned)
