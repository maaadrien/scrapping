# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys
import requests
import codecs
from video import Video

#==========FUNC=========
def splitToSec(strDur, sep):
    duration = strDur.split(sep)
    print(strDur)
    nbParts = len(duration)
    print(nbParts)
    
    if nbParts == 1:
        duration = int(duration[0])
    elif nbParts == 2:
        duration = int(duration[0]) * 60 + int(duration[1])
    elif nbParts == 3:
        duration = int(duration[0]) * 3600 + int(duration[1]) * 60 + int(duration[2])
    return duration

#=======================



# url = input("Enter a website to extract the URL's from: ")
f = open('url.txt', 'r')
url = f.read()

vid_list = []

for page in range(1,2):
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
        durationElem = box.find("div", {"class": "duration"})
        ratingElem = box.find("div", {"class": "rating"})

        durationElem.span.decompose()
        ratingElem.span.decompose()
        viewsElem.span.decompose()

        link = url + linkElem['href'].strip()
        title = linkElem.text.strip().encode(sys.stdout.encoding, errors='replace').decode('cp850')
        duration =  splitToSec(durationElem.text.strip(), ":")
        views = viewsElem.text.strip().replace(',',"")
        rating = ratingElem.text.strip().replace('%',"")
        
        vid = Video(link, title, duration, views, rating)
        vid.printVid()
        vid_list.append(vid)


print(sorted(vid_list, key=lambda video: video.rating, reverse=True))

