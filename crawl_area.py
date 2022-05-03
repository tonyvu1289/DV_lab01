from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from datetime import date
import datetime
url = "https://www.worldometers.info/geography/largest-countries-in-the-world/"
data_html = requests.get(url).text
data_html = re.sub(r'<.*?>', lambda g: g.group(0).upper(), data_html)

df = pd.read_html(data_html)

df[0].reset_index().drop(columns=['index','#'])
df[0].to_csv('./data/area'+'.csv')

