import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import html
import lxml


def get_views(url):
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')
    count_container = soup.find(class_="watch-view-count")
    print(count_container.text)

    return count_container.text


video_details = ()
data = pd.read_excel("Links.xlsx")
for i in data.index:
    d = ()
    d = data.values[i]
    for url in d:
        print("")
        print(url)
        try:
            views = get_views(url)
        except:
            try:
                views = get_views(url)
            except:
                try:
                    views = get_views(url)
                except:
                    print("Failed to fetch")

