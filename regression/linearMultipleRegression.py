##重回帰分析

import matplotlib.pyplot as plt
import numpy as np


x1 = np.random.rand(100,1)
x1 = x1 * 4 - 2

x2 = np.random.rand(100,1)
x2= x2 * 4- 2


#この変数を求める
y = 3 * x1 - 2 * x2 + 1

y += np.random.randn(100,1)



from sklearn import linear_model

#(x1_1,x2_1),(x1_2,x2_2)...の形に変換
x1_x2 = np.c_[x1,x2]

model= linear_model.LinearRegression()
model.fit(x1_x2,y)


yp = model.predict(x1_x2)







plt.subplot(1,2,1)

plt.scatter(x1, y, marker='+')
plt.scatter(x1, yp, marker='o')
plt.xlabel('x1')
plt.ylabel('y')


plt.subplot(1,2,2)
plt.scatter(x2, y, marker='+')
plt.scatter(x2, yp, marker='o')
plt.xlabel('x2')
plt.ylabel('y')


plt.tight_layout()
print(model.score(x1_x2,y))
print(model.coef_)
print(model.intercept_)






plt.show()
