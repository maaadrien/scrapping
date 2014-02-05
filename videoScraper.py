from bs4 import BeautifulSoup
import sys
import requests
import codecs
from video import Video

class VideoScraper:

    def __init__(self):
        self.vid_list = []
        self.loadUrl()

    def __repr__(self):
        return repr((self.link, self.title, self.duration, self.views, self.rating))
    
    #FUNCS
    def splitToSec(self, strDur, sep):
        duration = strDur.split(sep)
        nbParts = len(duration)
       
        if nbParts == 1:
            duration = int(duration[0])
        elif nbParts == 2:
            duration = int(duration[0]) * 60 + int(duration[1])
        elif nbParts == 3:
            duration = int(duration[0]) * 3600 + int(duration[1]) * 60 + int(duration[2])
        return duration

    #SCRAP
    def scrap(self, fromPage, nbPages):
        for page in range(fromPage, fromPage + nbPages):
            print("==================================================")
            print("               SCRAPING PAGE ", page)
            print("==================================================")
            self.scrapPage(page)

    def scrapPage(self, page):
        videoDOMs = self.findVideoDOMs(self.requestPage(page))
        for videoDOM in videoDOMs:
            link     = self.formatLinkDOM(self.findLinkDOM(videoDOM))
            title    = self.formatTitleDOM(self.findTitleDOM(videoDOM))
            duration = self.formatDurationDOM(self.findDurationDOM(videoDOM))
            views    = self.formatViewsDOM(self.findViewsDOM(videoDOM))
            rating   = self.formatRatingDOM(self.findRatingDOM(videoDOM))
            
            vid = Video(link, title, duration, views, rating)
            vid.printVid()
            self.vid_list.append(vid)
        
    def loadUrl(self):
        f = open(self.fichierUrl, 'r')
        self.url = f.readline().strip()
        self.urlToPage = f.readline().strip()

    def requestPage(self, page):
        r  = requests.get("http://" + self.url + self.urlToPage + str(page))
        data = r.text
        return BeautifulSoup(data)

    def findVideoDOMs(self, soup):
        pass
    
    #FIND
    def findLinkDOM(self, videoDOM):
        pass

    def findTitleDOM(self, videoDOM):
        pass

    def findDurationDOM(self, videoDOM):
        pass

    def findViewsDOM(self, videoDOM):
        pass

    def findRatingDOM(self, videoDOM):
        pass

    #FORMAT
    def formatLinkDOM(self, videoDOM):
        pass

    def formatTitleDOM(self, videoDOM):
        pass

    def formatDurationDOM(self, videoDOM):
        pass

    def formatViewsDOM(self, videoDOM):
        pass

    def formatRatingDOM(self, videoDOM):
        pass