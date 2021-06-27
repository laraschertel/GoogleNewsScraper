import pickle
import matplotlib.pyplot as plt
import numpy as np
import statistics as s
from headline import Headline

headlines_list = []
years_list = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
zeitungen = ['t-online','n-tv', 'spiegel', 'welt', 'focus', 'bild']

open_file = open("HeadlinesSubListNeu.pkl", "rb")
headlines_list = pickle.load(open_file)
open_file.close()

def plotBarChart():
    sentimentValuesPerYear = []
    for zeitung in zeitungen:
        sentimentValuesPerYear.append([countPosSentiment(zeitung), countNegSentiment(zeitung)])

    zeitungenPosNeg = ['t-online+','t-online-', 'n-tv+', 'n-tv-', 'spiegel+', 'spiegel-', 'welt+', 'welt-', 'focus+', 'focus-', 'bild+', 'bild-']
    plt.bar(zeitungenPosNeg,sentimentValuesPerYear)
    plt.title('Positiv-/Negativ-Verteilung')
    plt.xlabel('Zeitungen')
    plt.ylabel('Anzahl Artikel')
    plt.show()

def countPosSentiment(zeitung):
    counter = 0
    for headline in headlines_list:
        if zeitung in headline.link and headline.sentimentWert > 0:
            counter = counter + 1
    return counter

def countNegSentiment(zeitung):
    counter = 0
    for headline in headlines_list:
        if zeitung in headline.link and headline.sentimentWert < 0:
            counter = counter + 1
    return counter

def plotLineChart():
    for zeitung in zeitungen:
        amountPerYear = []
        for year in years_list:
            amountPerYear.append(countSingleNewspaperPublishesPerYear(zeitung,str(year)))
        plt.plot(years_list,amountPerYear,label=zeitung)
        print(amountPerYear)




    plt.title('Anzahl Artikel aller Zeitungen')
    plt.xlabel('Jahre')
    plt.ylabel('Anzahl Artikel')
    plt.legend()
    plt.show()

def countSingleNewspaperPublishesPerYear(zeitung, jahr):
    counter = 0
    for headline in headlines_list:
        if zeitung in headline.link and jahr in headline.published:
            counter = counter + 1
    return counter

plotLineChart()


