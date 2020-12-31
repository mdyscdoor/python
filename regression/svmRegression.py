import matplotlib.pyplot as plt
import numpy as np
import math

x = np.random.rand(1000,1)
x = x * 20 - 10


#この式を推定（次数は隠されているとする）
y = np.array([math.sin(v) for v in x])
y += np.random.rand(1000)



#データを分割
x_train = x[:300]
y_train = y[:300]
x_test = x[300:]
y_test = y[300:]



#学習
from sklearn import svm


#サポートベクターマシン
model=svm.SVR()
model.fit(x_train, y_train)




print(model.score(x_train,y_train))

plt.subplot(2,1,2)
plt.scatter(x_train,y_train,marker='+')
plt.scatter(x_train,model.predict(x_train), marker='o')
plt.title('trained')






#評価
print(model.score(x_test,y_test))
plt.subplot(2,1,1)
plt.scatter(x_test,y_test,marker='+')
plt.scatter(x_test,model.predict(x_test),marker='o')
plt.title('test')


plt.show()
