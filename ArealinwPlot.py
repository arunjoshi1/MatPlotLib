from matplotlib import pyplot as plt
from numpy.core.multiarray import where
import pandas as pd
dataset = pd.read_csv('./data.csv')
ages = dataset['Age']
python_sal = dataset['Python']

js_sal = dataset['JavaScript']
plt.plot(ages, python_sal, label='python')
plt.plot(ages, js_sal, label='javascript')
plt.fill_between(ages, js_sal, python_sal, alpha=0.25, color='red',
                 interpolate=True,
                 where=(python_sal < js_sal))
plt.fill_between(ages, js_sal, python_sal, alpha=0.25, color='green',
                 interpolate=True,
                 where=(python_sal > js_sal))
#  style
plt.legend()
plt.savefig('./fillarea.png')
plt.show()
