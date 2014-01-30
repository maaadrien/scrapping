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
        print(self.duration)
        print(self.views)
        print(self.rating)