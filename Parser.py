import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from decimal import Decimal

url = 'http://dmo.econ.msu.ru/teaching/ru/stat/Normal.htm'
data = requests.get(url).text

soup = bs(data, 'html.parser')

a = soup.find('tbody').find_all('tr')

df = pd.DataFrame(columns=['number', '0.00', '0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08', '0.09'])


def dona(x):
    v = []
    for i in x:
        m = list(map(lambda x: str(Decimal(x) + Decimal(0.5000) if len(x) != 3 else str(x)), i))
        v.append(m)
    return v


z = []
for i in a[1:]:
    z.append((i.text.strip()).split('\n'))

kaka = dona(z)
for i in kaka:
    df.loc[len(df.index)] = i

df.set_index('number', inplace=True)

datatoexcel = pd.ExcelWriter('Normdist3.xlsx')

df.to_excel(datatoexcel)

datatoexcel.save()

