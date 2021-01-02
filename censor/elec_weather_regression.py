##電力と気温の関係の回帰
##気温から電力消費量を回帰できるか




import pandas as pd


#電力消費量
E = [pd.read_csv(
    '../../data/shikoku_electricity_{}.csv'.format(year),
    skiprows = 3,
    names = ['date', 'time', 'consumption'],
    parse_dates = {'date_hour':['date', 'time']},
    index_col = 'date_hour'
    )
    for year in [2012,2013,2014,2015,2016]
]

elec_data= pd.concat(E)


##気象情報
tmp = pd.read_csv(
    u'../../data/47891_高松.csv',
    parse_dates={'date_hour': ['日時']},
    index_col='date_hour',
    na_values='×'

)

del tmp['時']
columns = {
    '降水量(mm)': 'rain',
    '気温(℃)':'temperature',
    '日照時間(h)':'sunhour',
    '湿度(％)':'humid'
}

tmp.rename(columns=columns, inplace=True)




##開始日時時刻が異なるため、結合してから再分割
takamatsu = elec_data.join(tmp['temperature']).dropna().values

taka_elec = takamatsu[:,0:1]
taka_wthr = takamatsu[:,1:]








##気温と電力の関係をプロット

import matplotlib.pyplot as plt

plt.figure()
plt.scatter(taka_wthr,taka_elec,s=0.1)
plt.xlabel('temperature(c degree)')
plt.ylabel('electricity_consumption (*10000 kWh)')
#plt.show()





##サポートベクターマシンを使い、
##５分割交差検証を行う



from sklearn.model_selection import KFold
import sklearn.svm

#長さと分割数を指定
data_count = len(taka_elec)
kf = KFold(n_splits = 5)


#交差検証を実施
for train, test in kf.split(taka_wthr, taka_elec):
    x_train = taka_wthr[train]
    x_test = taka_wthr[test]
    y_train = taka_elec[train]
    y_test = taka_elec[test]


    model = sklearn.svm.SVR()
    y_train = y_train.flatten()
    y_test=y_test.flatten()


    model.fit(x_train,y_train)
    print('SVR: training_score = {}, testing_score = {}' .format(model.score(x_train,y_train),model.score(x_test,y_test)))
    



    





