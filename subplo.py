from matplotlib import pyplot as plt
import pandas as pd

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)


dataset = pd.read_csv('./data.csv')
ages = dataset['Age']
dev_sal = dataset['All_Devs']
py_sal = dataset['Python']
js_sal = dataset['JavaScript']

ax1.plot(ages, dev_sal, label='all dev sal')

ax2.plot(ages, py_sal, label='py sal')
ax2.plot(ages, js_sal, label='js sal')
ax2.legend()
ax1.legend()
ax1.set_title('dev sal 2020')
ax1.set_xlabel('Ages')
ax1.set_ylabel('sal')
ax2.set_xlabel('Ages')
ax2.set_ylabel('sal')
plt.savefig('./plots/subplots.png')
plt.show()
