### 3x-2 の単回帰

import matplotlib.pyplot as plt
import numpy as np


#-2から2
x = np.random.rand(100,1)
x = x * 4 - 2


y = 3 * x - 2
y += np.random.randn(100,1)



##線形回帰の呼び出しと訓練
##最小二乗法を用いる
from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(x,y)


plt.scatter(x,y, marker='+')
plt.scatter(x,model.predict(x), marker='o')


##推測した切片と傾き、決定係数を表示
print(model.coef_)
print(model.intercept_)
print(model.score(x,y))

plt.show()
