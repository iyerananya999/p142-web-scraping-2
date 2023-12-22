from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape(url):
    try:
        page= requests.get(url)
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        temp_list = []
        for tr_tag in soup.find_all('tr', attrs={"class": 'fact_row'}):
            td_tags  = tr_tag.find_all("tt")
            for td_tag in (td_tags):
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append('')
            planets_data.append(temp_list)
    except:
        time.sleep(1)
        scrape(url)
# Calling Method    
planet_df = pd.read_csv('')
for index, row in planet_df.iterrows():
     scrape(row['url'])
    
scrape_data =[]
for i in planets_data:
    replaced = []
    for r in row:
      r = r.replace('\n', '')
      replaced.append(r)
    scrape_data.append(replaced)
     

# Define Header
headers = ["confirmed_brown_dwarfs_orbiting_primary_stars", "unconfirmed_brown_dwarfs", "field_brown_dwarfs", "former_brown_dwarfs"]


# Define pandas DataFrame   
planet_df = pd.DataFrame(planets_data, columns = headers)
planet_df.to_csv('scraped_data.csframe', index = True, index_label='id')