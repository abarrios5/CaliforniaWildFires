from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sample_data = pd.read_csv('California_Fire_Incidents.csv')

root = Tk()
root.title("California")
root.geometry("400x200")


def graph():
    plt.hist(sample_data.AcresBurned, 50)
    plt.show()


def gra():
    plt.plot(sample_data.AcresBurned)
    plt.show


my_button = Button(root, text="GraphIt", command=graph)
my_button.pack()

root.mainloop()
