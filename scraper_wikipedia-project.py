from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
#import requests as req

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome('chromedriver.exe')
browser.get(START_URL)

time.sleep(10)
headers = ["name", "distance", "mass", "radius", "luminosity"]
stars_data = list()

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for table in soup.find_all("table", attrs={"class", "wikitable sortable jquery-tablesorter"}):
        tbody = table.find("tbody")
        tmpry_list = list()
        for tr_tags in tbody.find_all("td"):
            td_tags = tr_tags.find_all("tr")
            for index, td_tag in enumerate(td_tags):
                if index == 0:
                    tmpry_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        tmpry_list.append(td_tag.contents[0])
                    except:
                        tmpry_list.append("")
        stars_data.append(tmpry_list)

with open("stars.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(stars_data)

scrape()