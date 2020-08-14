from matplotlib import pyplot as plt
d =[200,100,300]
lables = ['200','100','300']
colors = ['red','blue','green']
explode=[0,0.1,0]
plt.pie(d,labels=lables,autopct='%1.1f%%',explode=explode,shadow=True,startangle=60,wedgeprops={'edgecolor':'#49599a'})
plt.savefig('./pie.png')

plt.show()