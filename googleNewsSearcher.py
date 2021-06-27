from pygooglenews import GoogleNews
from textblob_de import TextBlobDE as TextBlob
from headline import Headline
import csv
import pickle



gn = GoogleNews()
gn = GoogleNews(lang='de', country='DE')
data_list = []
queries_list = ["site:https://www.t-online.de/ AfD", "site:https://www.focus.de/ AfD", "site:https://www.spiegel.de/ AfD", "site:https://www.welt.de/ AfD", "site:https://www.n-tv.de/ AfD", "site:https://www.bild.de/ AfD"]
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
headline_list = []


def sentiment_analyse(text):
        blob = TextBlob(text)
        blob.sentences
        blob.tokens
        blob.tags
        blob.noun_phrases
        return blob.sentiment


for y in years:
    #divided the year in three trimesters because each search can return a maximum of 100 items, and no newspaper has had more than 100 posts about AfD in less than three months
    for query in queries_list:
        try:
            fromFirstTri = str(y)+'-%01-%01'
            toFirstTri = str(y)+'-%04-%30'
            search = gn.search(query, from_=fromFirstTri, to_=toFirstTri)
            for item in search['entries']:
                if "AfD" in  item['title'] or "Alternative für Deutschland" in item['title']:
                   sentimentPolarity = sentiment_analyse(item['title'])
                   data_list.append([item['title'] + ';;' + item['published'] + ';;' + item['link'] + ';;' + str(sentimentPolarity)])
                   headline_list.append(Headline(item['title'], item['published'], item['link'], sentimentPolarity.polarity, sentimentPolarity.subjectivity))
            fromSecondTri = str(y)+'-%05-%01'
            toSecondTri = str(y)+'-%08-%31'
            searchTwo = gn.search(query, from_=fromSecondTri, to_=toSecondTri)
            for item in searchTwo['entries']:
                if "AfD" in item['title'] or "Alternative für Deutschland" in item['title']:
                    sentimentPolarity = sentiment_analyse(item['title'])
                    data_list.append([item['title'] + ';;' + item['published'] + ';;' + item['link'] + ';;' + str(sentimentPolarity)])
                    headline_list.append(Headline(item['title'], item['published'], item['link'], sentimentPolarity.polarity, sentimentPolarity.subjectivity))
            fromThirdTri = str(y)+'-%09-%01'
            toThirdTri = str(y)+'-%12-%31'
            searchThree = gn.search(query, from_=fromThirdTri, to_=toThirdTri)
            for item in searchThree['entries']:
                if "AfD" in item['title'] or "Alternative für Deutschland" in item['title']:
                   sentimentPolarity = sentiment_analyse(item['title'])
                   data_list.append([item['title'] + ';;' + item['published'] + ';;' + item['link'] + ';;' + str(sentimentPolarity)])
                   headline_list.append(Headline(item['title'], item['published'], item['link'], sentimentPolarity.polarity, sentimentPolarity.subjectivity))
        except Exception:
            pass


with open('ZeitungenHeadlinesSentimentSubjectivityNeu.csv', 'a', newline='', encoding='utf-8') as file:
     writer = csv.writer(file)
     writer.writerows(data_list)

open_file = open("HeadlinesSubListNeu.pkl", "wb")
pickle.dump(headline_list, open_file)
open_file.close()


