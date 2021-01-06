import pandas as pd
area = (10.0 * 10.0) * 10.0
spa_sec = 0.33 * 0.6
std_sec = 0.33 * 0.3


raw = pd.read_csv(
        'rawdata2020.csv',
        encoding = "utf-8_sig",
        skiprows = 1,
        names= ['class', 'id', 'type', 'ears', 'paddies', 'valid-paddies','weight', 'water-ratio'],
        index_col = 'id')

types=['疎植', '少肥', '標準', '多肥']
classes=['月曜','水曜']
sort = raw.sort_values(['class','type'])




for day in classes:
    for type in types:
        
        type_list= raw[raw['type'] == type]
        data = type_list[type_list['class'] == day]

        if type == '疎植' :
            section = spa_sec
        else:
            section = std_sec
            
        browns = (data.ears * data.weight / 3.0) * (area / section) / 1000.0
        ave = browns.mean()

        print(day + 'クラス ' + type + '条件の10aあたり収量は ' + str('{:.1f}'.format(ave)) + ' kg/10a です。') 










