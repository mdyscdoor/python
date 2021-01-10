import numpy as np
wLength = 1
ei = 2

#接点の数を入力
##ndof = input('接点の数を入力してください')
nd = 101
##
##while(!str.isdigit(ndof) or ndof < 2):
##    ndof = input('接点の数を入力してください')
##ndof = int(ndof)


#分布荷重ベクトル
load = np.zeros((nd*2,1))
#変位・たわみベクトル
d = np.zeros((nd*2,1))
#分割区間の長さ
lth = wLength / (nd - 1)

##for i in range(ndof):
##    for j in (0,1):
##        print(i +  '番目の並進方向の自由度を入力してください:')     




#拘束接点を設定
rtr = [200,201]
#残りを自由接点に設定
free = list(range(nd*2))
for i in rtr:
    free.remove(i)
print(free)


#荷重を設定
#load[101]=500
load[51] = 800



#剛性行列
ke = np.array([[12*ei/lth**3, 6*ei/lth**2, -12*ei/lth**3,6*ei/lth**2],
               [6*ei/lth**2, 4*ei/lth, -6*ei/lth**2,2*ei/lth],
               [-12*ei/lth**3, -6*ei/lth**2, 12*ei/lth**3,-6*ei/lth**2],
               [6*ei/lth**2, 2*ei/lth, -6*ei/lth**2,4*ei/lth]

])


#接点数に応じて全体剛性行列を生成
k = np.pad(ke,[0,(nd - 2)*2])
for i in range(nd - 2):
    k += np.pad(ke,[(i+1)*2, (nd - i - 3)*2])









#計算のため拘束点の剛性行列を削る
k= np.delete(k,rtr, axis=0)
k= np.delete(k,rtr, axis=1)


#分布荷重行列と全体剛性行列の逆行列の積で変位ベクトルを求める
kInv = np.linalg.inv(k)
print(k)
print(kInv)


#一次的な変位・荷重ベクトルを求める
xv=np.array([])
lv=[]

for i in free:
    lv.append(float(load[i]))
for i in free:
    dv= np.dot(np.array(lv),kInv)

print(lv)
print(dv)


#全体変位ベクトルに反映
count = 0
for i in range(nd*2):
    if i in rtr:
        continue
    d[i] = dv[count]
    count += 1
print(d)







#たわみとたわみ角に分割
y = []
theta = []

for i in range(0, nd*2,2):
    y.append(float(d[i]))
for i in range(1, nd*2,2):
    theta.append(float(d[i]))
print(y)
print(theta)
    





#グラフを描画
import matplotlib
import matplotlib.pyplot as plt


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
#plt.subplots_adjust(hspace= , wspace = )
ax1.scatter(range(101),y)
##ax1.scatter(range(101),np.zeros((1,101)),s='0.5')
ax1.set_xlabel('接点番号')
ax1.set_ylabel('変位')

plt.show()














