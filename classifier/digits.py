import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import tree
from sklearn import metrics


digits = datasets.load_digits()


#3,8のデータを取得している
flag_3_8 = (digits.target == 3) + (digits.target == 8)


#イメージとラべルを取得
images = digits.images[flag_3_8]
labels = digits.target[flag_3_8]

print(flag_3_8[flag_3_8])


#画像を一次元化
images= images.reshape(images.shape[0],-1)


#データの分割
n_samples = len(flag_3_8[flag_3_8])
train_size = int(n_samples * 3 / 5)



#決定木を使って分類
classifier = tree.DecisionTreeClassifier()
classifier.fit(images[:train_size], labels[:train_size])



expected = labels[train_size:]
predicted= classifier.predict(images[train_size:])




print('accuracy:\n', metrics.accuracy_score(expected,predicted))





