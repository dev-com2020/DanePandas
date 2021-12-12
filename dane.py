import pandas as pd

"""
pip install pandas
pip install xlwt openpyxl xlrd
"""

# w = pd.read_excel('imiona.xlsx',sheet_name='Wynik2',header=None,names=["Imię","Nazwisko","Wynik"])
# w.to_html('imiona_nowe.html')

# oceny = [[1, 3, 5, 6], [22, 33, 44, 55]]
# zbior = pd.DataFrame(oceny)
# zbior.columns = ['Pierwszy','Drugi','Trzeci','Czwarty']
# print(zbior)

# slownik = {'Imię': ['Marcin', 'Alan', 'Tomek'], 'Wiek': [17, 18, 38]}
# zbior = pd.DataFrame(slownik)
# print(zbior)

# s = pd.Series([11, 22, 33, 44])
# print(s)

# miasta = pd.read_csv('worldcities.csv')
# print(miasta)
# print(miasta.head())
# print(miasta.tail())
# print(miasta[0:5])
# print(miasta[-5:-1])
# print(miasta.city.is_unique)
# print(miasta[0:5]['city'])
# print(miasta.info())
# print(miasta.describe())
# print(miasta.isnull())
# print(miasta.isnull().sum())
# print(miasta.duplicated().sum())
# miasta.drop_duplicates()
kostium = pd.read_csv('Halloween.csv', header=2)

# print(kostium[:10][['region', '1']])
# kostium.set_index('region', inplace=True)
# print(kostium[:10][['1']])
# kostium.reset_index()
# print(kostium.loc['Arizona'])
# kostium.loc['Arizona','1']='Batman'
# print(kostium.loc['Arizona'])
# print(kostium.iloc[3, 2])

# for index, zawartosc in kostium.iterrows():
#     if zawartosc['1'] == 'Rabbit':
#         print(zawartosc['region'])

# print(kostium['1'] == 'Rabbit')


# print(kostium[ kostium['1']=='Rabbit'])
# print(kostium[ (kostium['1']=='Rabbit') | (kostium['1'] =='Dinosaur')])
# print(kostium[ (kostium['1']=='Rabbit') & (kostium['1'] =='Dinosaur')])

kostium['6'] = 0
kostium.loc[kostium['1'] == 'Harley Quinn', '6'] = 'TAK'

# print(kostium.rename( columns={'1':'Najpopularniejsze'}))
print(kostium.drop('6', axis=1))
