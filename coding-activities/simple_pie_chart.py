import matplotlib.pyplot as plt
import seaborn as sns

data = [15, 25, 25, 30, 5]
labels = ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5"]

colors = sns.color_palette("pastel")[0 : len(labels)]

plt.pie(data, labels=labels, colors=colors, autopct="%.0f%%")
plt.savefig("simple_pie_chart.png")
