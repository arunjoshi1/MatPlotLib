from matplotlib import pyplot as plt
ages = [20, 21, 23, 13, 7, 40, 41, 26, 28, 37, 55]
bins = [10, 20, 30, 40, 50, 60]
plt.hist(ages, bins=bins, edgecolor='white')
plt.xlabel('ages of dev')
plt.ylabel('Count per age')
plt.savefig('./hist.png')
plt.show()
