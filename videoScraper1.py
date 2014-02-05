from bs4 import BeautifulSoup
import sys
from videoScraper import VideoScraper

class VideoScraper1(VideoScraper):

    def __init__(self):
        print("Lauching Scraper1...")
        self.fileUrl = "url.txt"
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
    def formatLinkDOM(self, linkDOM):
        return self.url + linkDOM['href'].strip()

    def formatTitleDOM(self, titleDOM):
        return titleDOM.text.strip().encode(sys.stdout.encoding, errors='replace').decode('cp850')

    def formatDurationDOM(self, durationDOM):
        durationDOM.span.decompose()
        return int(self.splitToSec(durationDOM.text.strip(), ":"))

    def formatViewsDOM(self, viewsDOM):
        viewsDOM.span.decompose()
        return int(viewsDOM.text.strip().replace(',',""))

    def formatRatingDOM(self, ratingDOM):
        ratingDOM.span.decompose()
        return int(ratingDOM.text.strip().replace('%',""))