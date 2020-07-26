#%%
import pandas as pd
import urllib.request
import ssl
from bs4 import BeautifulSoup
population_url = (
    "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
) #文字列を分割して記述　なぜ？

population = (
    pd.read_html(population_url)[1]
    .iloc[:-1,[1,2,4,5]]
)

population.head()

# %%
import urllib.request
import ssl
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "https://news.google.com"
Scraper(news).scrape()

# %%
