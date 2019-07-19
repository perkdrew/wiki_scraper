from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd 
from pandas import DataFrame
from time import sleep

%matplotlib inline

session = requests.Session()
header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*,q=0.8",
          "Accept-Language": "en-US",
          "Connection": "keep-alive",
          "Referrer": "https://www.google.com/",
          "User-Agent": "Chrome 75 on mac0S (Mojave)"}

# The URL we are visiting
url = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once"
page = session.get(url, headers=header).text
nobelList = BeautifulSoup(page)

nobelListTable = nobelList.find("table", {"class": ["wikitable","sortable"]})

links = dict()
for node in nobelListTable.findAll("td"): # Will contain names and links
    if node.a != None and node.a.attrs["href"][0:6] == "/wiki/": # Avoids bad links
        links[node.a.contents[0]] = node.a.attrs["href"] # Name: Link format

datadict = dict()
for name, link in links.items():
    sleep(10)
    print("Fetching: " + name)
    person_page = session.get(baseurl + links[name], headers=header).text
    ppbsObj = BeautifulSoup(person_page)
    bday_span != None:
    try:
        



