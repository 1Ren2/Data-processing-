import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np
useful_dictionary = {"Day": [1, 2, 3, 4, 5, 6], "visitors": [1000, 700, 6000, 2000, 1000, 500],
                     "Bounce rate": [20, 23, 23, 24, 15, 14]}
useful_dictionary1 = {"Day": [1, 2, 3, 4, 5, 6], "visitors": [1000, 700, 6000, 2000, 1000, 500],
                      "Bounce rate": [20, 23, 23, 24, 15, 14]}
df = pd.DataFrame(useful_dictionary)
df1 = pd.DataFrame(useful_dictionary1)

merge = pd.merge(df, df1, on="Day")
print(merge)
dg = pd.read_csv("Symmetry_Energy_for_each_different_paper.csv", skiprows=2,
                 names=["Atomic mass", "Tian", "Mei", "Jiang", "VM Kolomotiez",
                        "Min Lui", "Ma Chang"])
fig,ax =  plt.subplots()
dg.plot(kind="scatter",x="Atomic mass",y="Tian",ax=ax)
dg.plot(kind="scatter",x="Atomic mass",y="Mei",ax=ax)
dg.plot(kind="scatter",x="Atomic mass",y="Jiang",ax=ax)
dg.plot(kind="scatter",x="Atomic mass",y="VM Kolomotiez",ax=ax)
 
# Don't allow the axis to be on top of your data
ax.set_axisbelow(True)

# Turn on the minor TICKS, which are required for the minor GRID
ax.minorticks_on()

# Customize the major grid
ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.legend()


plt.show()

