
"""
Plot the results of human vs deep learning on high-resolution AG-MNIST
"""

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(6, 11))
hor4 = np.array([0.99,0.99,0.97])*100
ver4 = np.array([0.98,0.99,0.96])*100
ul4 = np.array([0.99,0.98,0.99])*100
ur4 = np.array([1,0.98,0.98])*100
hor8 = np.array([0.99,0.98,0.99])*100
ver8 = np.array([0.94,0.91,0.99])*100
ul8 = np.array([0.95,0.99,0.94])*100
ur8 = np.array([0.98,0.97,0.98])*100
plt.ylim(0,100)
# 人类结果
plt.scatter([1,1,1],hor4, s=100,color='orange',alpha=0.5, label='I=4, human performance')
plt.scatter([2,2,2],ver4, s=100,color='orange', alpha=0.5)
plt.scatter([3,3,3],ul4, s=100,color='orange', alpha=0.5)
plt.scatter([4,4,4],ur4, s=100,color='orange', alpha=0.5)

plt.scatter([1,1,1],hor8, s=50,color='green', alpha=0.5, label='I=8, human performance')
plt.scatter([2,2,2],ver8, s=50,color='green', alpha=0.5)
plt.scatter([3,3,3],ul8, s=50,color='green', alpha=0.5)
plt.scatter([4,4,4],ur8, s=50,color='green', alpha=0.5)

#模型结果
plt.scatter(1,22.43, s=100,color='orange',alpha=0.5, marker='^', label='I=4, deep learning performance') #hor4
plt.scatter(1,23.69, s=50,color='green',alpha=0.5, marker='^', label='I=8, deep learning performance') #hor8
plt.scatter(2,24.14, s=100,color='orange',alpha=0.5, marker='^') #ver4
plt.scatter(2,22.55, s=50,color='green',alpha=0.5, marker='^') #ver8
plt.scatter(3,38.18, s=100,color='orange',alpha=0.5, marker='^') #ul4
plt.scatter(3,19.11, s=50,color='green',alpha=0.5, marker='^') #ul8
plt.scatter(4,27.18, s=100,color='orange',alpha=0.5, marker='^') #ur4
plt.scatter(4,22.76, s=50,color='green',alpha=0.5, marker='^') #ur8

#plt.axhline(100,color='red',linestyle='--')
plt.axhline(10,color='blue',linestyle='--', label = 'Random level')
plt.xticks([0,1,2,3,4,5], labels=['','hor','ver','ul','ur',''],fontsize=15)
plt.yticks(np.arange(0, 105, step=5),fontsize=15)
plt.xlabel('Direction of gratings',fontsize=15)
plt.ylabel('Accuracy(%)',fontsize=15)
plt.legend(loc='center',bbox_to_anchor=(0.5,1.07),frameon=False)
plt.show()
