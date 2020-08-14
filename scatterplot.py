from typing import ChainMap
from matplotlib import pyplot as plt

import pandas as pd
#  style for plot
plt.style.use('seaborn')
plt.xscale('log')
plt.yscale('log')
#  plt info
plt.title('like to the  view count ')
plt.xlabel('view Count')
plt.ylabel('likes')

# data for program
dataset = pd.read_csv('./scatterdata.csv')
viewCount = dataset['view_count']
likes = dataset['likes']
ratio = dataset['ratio']
plt.scatter(viewCount, likes, s=100, c=ratio, marker='o', edgecolor='black',
            linewidths=1, alpha=.75, cmap='summer')

# side bar
cbar = plt.colorbar()
cbar.set_label('check here !')
#  save as image
plt.savefig('./plots/scatter.png')
plt.show()
