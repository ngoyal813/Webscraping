import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import html
import lxml

video_details = ()
data = pd.read_excel("V1.xlsx")
for i in data.index:
 d=()
 d = data.values[i]
 for url in d:
     r = requests.get(url).text
     c = BeautifulSoup(r,'lxml')
     #print("data is", repr(c.find(class_= 'watch-view-count')))
     try:
         for div in c.find(class_= 'watch-view-count'):
           video_details = div.replace(",", "").rstrip('views')
           print(video_details)
     except:
         try:
             for div in c.find(class_= 'watch-view-count'):
                video_details = div.replace(",", "").rstrip('views')
                print(video_details)
         except:
            print(" ")