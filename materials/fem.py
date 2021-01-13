##はりのたわみ・たわみ角を求める問題
##有限要素法




import numpy as np

#全体の長さ
wLength = 1
#曲げ剛性
ei = 1

###   節点の数を入力   ###                              #
nd =int(input('節点の数を入力してください：'))
#nd = 101



#分布荷重ベクトル
load = np.zeros((nd*2,1))
#変位・たわみベクトル
d = np.zeros((nd*2,1))
#分割区間の長さ
lth = wLength / (nd - 1)



###   拘束節点を設定   ###                              #
#偶数点で並進拘束
#奇数店で回転拘束
rtrP = []
rtrR = []
rtr=[]
print('拘束する接点番号を入力してください')

tmp = ''

while(True):
    tmp = input('並進拘束番号(1 ～ '+ str(nd) + ' 、入力なしで次に進む)：')        
    if tmp == '':
        break
    rtrP.append(int(tmp))
while(True):
    tmp = input('並進拘束番号(1 ～ '+ str(nd) + ' 、入力なしで次に進む)：')                 
    if tmp == '':
        break
    rtrR.append(int(tmp))


for i in rtrP:
    rtr.append(2*(i-1))
for i in rtrR:
    rtr.append(2*i-1)
rtr.sort()
print(rtr)
                



##rtr = [0,100,200,201]
#残りを自由節点に設定
free = list(range(nd*2))
print(free)
print(nd*2)
for i in rtr:
    if i in free:
        free.remove(i)




#グラフ描画用の拘束フラグ
supported = []
gerber = []
cantilever = []

for i in range(0,nd*2,2):
    if i in rtr:    
        supported.append(int(i/2))
for i in range(1,nd*2,2):
    if i in rtr:
        if int((i-1)/2) in supported:
            cantilever.append(int((i-1)/2))
            supported.remove(int((i-1)/2))
        else:
            gerber.append(int((i-1)/2))





###   荷重を設定   ###                                  #
load[51] = 800

#剛性行列
ke = np.array([[12*ei/lth**3, 6*ei/lth**2, -12*ei/lth**3,6*ei/lth**2],
               [6*ei/lth**2, 4*ei/lth, -6*ei/lth**2,2*ei/lth],
               [-12*ei/lth**3, -6*ei/lth**2, 12*ei/lth**3,-6*ei/lth**2],
               [6*ei/lth**2, 2*ei/lth, -6*ei/lth**2,4*ei/lth]
])


#節点に応じて全体剛性行列を生成
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


#一次的に変位・荷重ベクトルを求める
xv=np.array([])
lv=[]

for i in free:
    lv.append(float(load[i]))
for i in free:
    dv= np.dot(np.array(lv),kInv)


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
ax1.scatter(range(101),y,s=0.5)

#曲げる前の棒を表示
ax1.plot(list(range(101)),list(np.zeros((1,101)).flatten()),c='gray', marker='s',markevery=cantilever)
ax1.plot(list(range(101)),list(np.zeros((1,101)).flatten()),c='gray', marker='^',markevery=supported)
ax1.plot(list(range(101)),list(np.zeros((1,101)).flatten()),c='gray', marker='o',markevery=gerber)
ax1.set_xlabel('node number')
ax1.set_ylabel('displacement')

plt.show()














