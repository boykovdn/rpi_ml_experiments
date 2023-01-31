import matplotlib.pyplot as plt
import pandas as pd

result_path = "./test.csv"

data = pd.read_csv(result_path)
col_names = data.columns

plt.scatter(data[col_names[0]], 1/data[col_names[1]], label="fps")
plt.scatter(data[col_names[0]], data[col_names[2]], label="temperature / C")
plt.legend()
#plt.hlines(80, col_names[0][0], col_names[0][-1], linestyle="--", label="Temperature limit / C")
plt.xlabel("time/s")
#plt.ylim(0,90)
plt.show()
