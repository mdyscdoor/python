import numpy as np
import matplotlib
import matplotlib.pyplot as plt



x_max = 1
x_min = -1

y_max = 2
y_min = -1



SCALE = 50
TEST_RATE = 0.3


data_x = np.arange(x_min, x_max, 1/float(SCALE)).reshape(-1,1)



data_ty= data_x ** 2
data_vy = data_ty + np.random.randn(len(data_ty),1) * 0.5




#分割する関数
def split_train_test(array):


    length = len(array)
    n_train = int(length * (1 - TEST_RATE))


    #インデックスをシャッフルしている
    indices = list(range(length))
    np.random.shuffle(indices)

    #シャッフルされたインデックスから分割
    idx_train = indices[:n_train]
    idx_test = indices[n_train:]

    #シャッフルを正し、分割おわり
    #戻り値はインデックスの割り当て方
    return sorted(array[idx_train]), sorted(array[idx_test])





#インデックスを生成し、分割している
indices = np.arange(len(data_x))
idx_train, idx_test = split_train_test(indices)


#訓練・てすとに分割
x_train = data_x[idx_train]
x_test = data_x[idx_test]

y_train = data_vy[idx_train]
y_test = data_vy[idx_test]


#ノイズデータとグラフをプロット
##plt.scatter(data_x, data_vy, label='target')
plt.plot(data_x, data_ty, linestyle=':', label='non noise curve')










##分類問題


CLASS_RADIUS = 0.6

#ラベルの定義
labels = (data_x ** 2 + data_vy ** 2) < CLASS_RADIUS ** 2


#ラベルを分割したインデックスに割り当てている
#データにラベルを指定すれば、trueのもののみが表示されるようになる
label_train = labels[idx_train]
label_test = labels[idx_test]



#閾値にあるかどうかで分類
plt.scatter(x_train[label_train], y_train[label_train], c='black', s=30, marker='*', label='near train')
plt.scatter(x_train[label_train != True], y_train[label_train != True], c='black', s=30, marker = '+', label= 'far train')

plt.scatter(x_test[label_test], y_test[label_test], c='black', s=30, marker = '^', label = 'near test')
plt.scatter(x_test[label_test != True], y_test[label_test != True], c='black', s=30, marker = 'x', label = 'far test')


#分離円
circle = plt.Circle((0,0), CLASS_RADIUS, alpha = 0.1, label = 'near area')
ax = plt.gca()
ax.add_patch(circle)

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)










#サポートベクターマシンを利用した分離

from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score


#分類のための結合
data_train = np.c_[x_train, y_train]
data_test = np.c_[x_test,y_test]



#分類器の定義
classifier = svm.SVC(gamma = 1)

#学習
classifier.fit(data_train, label_train.reshape(-1))


#評価
pred_test = classifier.predict(data_test)


#accuracy,混同行列を表示
print('accuracy_score:\n', accuracy_score(label_test.reshape(-1), pred_test))

print('confusion_matrix:\n',confusion_matrix(label_test.reshape(-1), pred_test))









#グラフを表示
plt.show()
