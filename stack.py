from matplotlib import pyplot as plt
time = [1, 2, 3, 4, 5, 6, 7, 8]
player_1 = [1, 2, 1, 4, 5, 4, 7, 6]
player_2 = [1, 2, 1, 4, 5, 4, 7, 6]
player_3 = [1, 2, 1, 4, 5, 4, 7, 6]
labels = ['player one', 'player two', 'player three']
plt.stackplot(time, player_1, player_2, player_3, labels=labels)
plt.savefig('./stackPlot.png')
plt.legend(loc=(0.01, .30))
plt.show()
