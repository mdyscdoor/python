##四国電力の日ごとの消費電力を散布図として出力したい


import pandas as pd


a = pd.read_csv(
    '../../data/shikoku_electricity_2012.csv',
    skiprows = 3,
    names = ['DATE', 'TIME', 'CONSUMPTION'],
    parse_dates = {'date_hour':['DATE', 'TIME']},
    index_col = 'date_hour'

)







#四国電力の年ごとの消費電力を配列にする
E = [pd.read_csv(
    '../../data/shikoku_electricity_{}.csv'.format(year),
    skiprows = 3,
    names = ['date', 'time', 'consumption'],
    parse_dates = {'date_hour':['date', 'time']},
    index_col = 'date_hour'
    )
    for year in [2012,2013,2014,2015,2016]
]


#データフレームを結合
elec_data= pd.concat(E)







#読み込んだデータをグラフ化
import matplotlib.pyplot as plt
plt.figure(figsize = (10,8))



#7月1日からの経過日数に、データフレームのtimeを書き換える
delta = elec_data.index - pd.to_datetime('2012/07/01 00:00:00')
elec_data['time'] = delta.days + delta.seconds / 3600.0 / 24.0


plt.subplot(2,1,1)
plt.scatter(elec_data['time'],elec_data['consumption'], s=0.1)
plt.xlabel('days from 2012/07/01')
plt.ylabel('electricity_consumption (*10000 kWh)')
plt.title('elec_consumption per day (chronological)')



plt.subplot(2,1,2)
plt.hist(elec_data['consumption'], bins=50)
plt.xlabel('elec_consumption(*10000kWh) per day')
plt.ylabel('count')


plt.show()





##
           


    
