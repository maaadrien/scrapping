from bs4 import BeautifulSoup
import sys
from scraper import Scraper

class Scraper1(Scraper):

    def __init__(self):
        print("Lauching Scraper1...")
        self.fichierUrl = "url.txt"
        super().__init__()

    def __repr__(self):
        return super().__repr__()

    #SCRAP
    def scrap(self, fromPage, nbPages):
        super().scrap(fromPage, nbPages)
        
    def findVideoDOMs(self, soup):
        return soup.find_all("li", {"class": "videoBox"})

    #FIND
    def findLinkDOM(self, videoDOM):
        return videoDOM.find("a", {"class": "videoTitle"})

    def findTitleDOM(self, videoDOM):
        return videoDOM.find("a", {"class": "videoTitle"})

    def findDurationDOM(self, videoDOM):
        return videoDOM.find("div", {"class": "duration"})

    def findViewsDOM(self, videoDOM):
        return videoDOM.find("div", {"class": "views"})

    def findRatingDOM(self, videoDOM):
        return videoDOM.find("div", {"class": "rating"})

    #FORMAT
    def formatLinkDOM(self, videoDOM):
        return self.url + videoDOM['href'].strip()

    def formatTitleDOM(self, videoDOM):
        return videoDOM.text.strip().encode(sys.stdout.encoding, errors='replace').decode('cp850')

    def formatDurationDOM(self, videoDOM):
        videoDOM.span.decompose()
        return int(self.splitToSec(videoDOM.text.strip(), ":"))

    def formatViewsDOM(self, videoDOM):
        videoDOM.span.decompose()
        return int(videoDOM.text.strip().replace(',',""))

    def formatRatingDOM(self, videoDOM):
        videoDOM.span.decompose()
        return int(videoDOM.text.strip().replace('%',""))