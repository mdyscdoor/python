import matplotlib.pyplot as plt
from sklearn import datasets



digits = datasets.load_digits()


for label,img in zip(digits.target[:10], digits.images[:10]):
    plt.subplot(2,5,label + 1)

    #軸を消す
    plt.axis('off')
    plt.imshow(img, cmap = plt.cm.gray_r,interpolation = 'nearest')
    plt.title('Digit:{0}'.format(label))


plt.show()
