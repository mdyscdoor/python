##y=ax^2 + b の線形単回帰


import numpy as np
import matplotlib.pyplot as plt

x= np.random.rand(100,1)
x = x * 4 - 2


#y = 3xx -2  の切片と傾きを求める
y = 3 * x**2 - 2
y += np.random.randn(100,1)


from sklearn import linear_model


#xを二乗した線形単回帰なので、xを二乗して渡す
model =linear_model.LinearRegression()
model.fit(x**2 ,y)



plt.scatter(x,y,marker='+', label='expected y')
plt.scatter(x,model.predict(x**2), label='predicted y')

print(model.coef_)
print(model.intercept_)
print(model.score(x**2,y))


plt.legend()
plt.show()
