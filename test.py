# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys
import requests
import codecs
from video import Video
from scraper1 import Scraper1

fromPage  = input("from page n°: ")
countPage = input("number of pages : ")

if not fromPage:
    fromPage = 1
if not countPage:
    countPage = 1

scraper1 = Scraper1()
scraper1.scrap(int(fromPage), int(countPage))

print("\n\n\n\n")
print("==================================================")
print("||                                              ||")
print("||                    TOP TEN                   ||")
print("||                                              ||")
print("==================================================")
print("\n")

sorted_vids = sorted(scraper1.vid_list, key=lambda video: video.rating, reverse=True)
for i in range(0,10):
    print(i+1, "- (", sorted_vids[i].rating, "% )", sorted_vids[i].title)