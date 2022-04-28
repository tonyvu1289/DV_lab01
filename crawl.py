from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from datetime import date
import datetime
url = "https://www.worldometers.info/coronavirus/"
data_html = requests.get(url).text
data_html = re.sub(r'<.*?>', lambda g: g.group(0).upper(), data_html)

df = pd.read_html(data_html)

for i in range(1,3):
    df[i].reset_index().drop(columns=['index','#'])
    df[i].to_csv('./data/'+str(date.today()-datetime.timedelta(i))+'.csv')