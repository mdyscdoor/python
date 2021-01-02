import pandas as pd

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



import matplotlib.pyplot as plt

plt.figure(figsize=(6,10))

plt.subplot(2,1,1)
delta = tmp.index - pd.to_datetime('2012/07/01 00:00:00')
tmp['time'] = delta.days + delta.seconds / 3600.0 / 24.0



plt.scatter(tmp['time'], tmp['temperature'], s=0.1)
plt.xlabel('days from 2012/7/1')
plt.ylabel('temperature(c degree/ chronological)')



plt.subplot(2,1,2)
plt.hist(tmp['temperature'], bins=80)
plt.xlabel('temperature(c degree)')
plt.ylabel('count')
plt.show()
