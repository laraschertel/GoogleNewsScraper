class Headline:
    def __init__(self, title, published, link, sentimentWert, sentimentSubjektivity ):
        self.title = title
        self.published = published
        self.link = link
        self.sentimentWert = sentimentWert
        self.sentimentSubjektivity = sentimentSubjektivity
    def get_data(self):
        print(self.title, self.published, self.link, self.sentimentWert, self.sentimentSubjektivity)