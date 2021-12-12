import pandas as pd

"""
pip install pandas
pip install xlwt openpyxl xlrd
"""

w = pd.read_excel('imiona.xlsx',sheet_name='Wynik2',header=None,names=["Imię","Nazwisko","Wynik"])
w.to_html('imiona_nowe.html')

# oceny = [[1, 3, 5, 6], [22, 33, 44, 55]]
# zbior = pd.DataFrame(oceny)
# zbior.columns = ['Pierwszy','Drugi','Trzeci','Czwarty']
# print(zbior)

# slownik = {'Imię': ['Marcin', 'Alan', 'Tomek'], 'Wiek': [17, 18, 38]}
# zbior = pd.DataFrame(slownik)
# print(zbior)

# s = pd.Series([11, 22, 33, 44])
# print(s)
