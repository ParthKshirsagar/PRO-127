from bs4 import BeautifulSoup
import requests
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

def scrape():
    headers = ['magnitude', 'name', 'bayer_designation', 'distance', 'spectral_class', 'mass', 'radius', 'luminosity']
    planet_data = []
    page = requests.get(START_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    for tr_tag in soup.find_all("tr"):
        td_tags = tr_tag.find_all('td')
        temp_list = []
        for index, td_tag in enumerate(td_tags):
            if(index == 0):
                temp_list.append(td_tag.find_all("a")[0].contents[0])
            else:
                try: 
                    temp_list.append(td_tag.contents[0])
                except: 
                    temp_list.append("")
        planet_data.append(temp_list)
    with open('scraper.csv', 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(planet_data)
scrape()