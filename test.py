# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys
import requests
import codecs
from video import Video


# url = input("Enter a website to extract the URL's from: ")
f = open('url.txt', 'r')
url = f.read()


for page in range(1,5):
    print("")
    print("")
    print("==================================================")
    print("                  GETTING PAGE ", page)
    print("==================================================")
    r  = requests.get("http://" +url+str(page))
    data = r.text
    soup = BeautifulSoup(data)
    boxes = soup.find_all("li", {"class": "videoBox"})
    for box in boxes:
        
        linkElem = box.find("a", {"class": "videoTitle"})
        viewsElem = box.find("div", {"class": "views"})
        viewsElem.span.decompose()
        durationElem = box.find("div", {"class": "duration"})
        durationElem.span.decompose()
        ratingElem = box.find("div", {"class": "rating"})
        ratingElem.span.decompose()

        link = url + linkElem['href'].strip()
        title = linkElem.text.strip().encode(sys.stdout.encoding, errors='replace').decode('cp850')
        duration = durationElem.text.strip()
        views = viewsElem.text.strip()
        rating = ratingElem.text.strip()
        
        
        
        
        
        # print(link.text.strip().encode(sys.stdout.encoding, errors='replace').decode('cp850'))
        # print(url + link['href'].strip())
        # print(duration.text.strip())
        # print(views.text.strip())
        # print(rating.text.strip())
        vid = Video(link, title, duration, views, rating)
        vid.printVid()