import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100,1)
x = x * 2 - 1


#この式を推定（次数は隠されているとする）
y = 4 * x**3 - 3 * x**2 + 2 * x - 1


y += np.random.randn(100,1)


#データを分割
x_train = x[:30]
y_train = y[:30]

x_test = x[30:]
y_test = y[30:]



#学習
from sklearn import linear_model


#次数がわからないので9次式としてみてみる
X_TRAIN = np.c_[x_train**9,x_train**8,x_train*7,x_train**6,x_train**5,x_train**4,x_train**3,x_train**2,x_train]
model=linear_model.LinearRegression()
model.fit(X_TRAIN, y_train)



print(model.coef_)
print(model.intercept_)
print(model.score(X_TRAIN,y_train))

plt.subplot(2,1,2)
plt.scatter(x_train,y_train,marker='+')
plt.scatter(x_train,model.predict(X_TRAIN), marker='o')
plt.title('trained')






#評価
X_TEST=np.c_[x_test**9,x_test**8,x_test**7,x_test**6,x_test**5,x_test**4,x_test**3,x_test**2,x_test]

print(model.score(X_TEST,y_test))
plt.subplot(2,1,1)
plt.scatter(x_test,y_test,marker='+')
plt.scatter(x_test,model.predict(X_TEST),marker='o')
plt.title('test')


plt.show()
