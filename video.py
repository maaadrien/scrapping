class Video:

    def __init__(self, link, title, duration, views, rating):
        self.link     = link
        self.title    = title
        self.duration = duration
        self.views    = views
        self.rating   = rating

    def __repr__(self):
        return repr((self.link, self.title, self.duration, self.views, self.rating))

    def printVid(self):
        print("")
        print("==================================================")
        print(self.title)
        print(self.link)
        print("Duration: ", self.durationToTime())
        print("Views:    ", self.views)
        print("Rating:   ", self.rating, "% ")

    def durationToTime(self):
        sec = self.duration
        hrs = sec // 3600
        sec -= 3600*hrs
        mins = sec // 60
        sec -= 60*mins
        if not mins:
            return str(sec)+'s'
        elif not hrs:
            return str(mins)+'m'+str(sec)+'s'
        else:
            return str(hrs)+'h'+str(mins)+'m'+str(sec)+'s'