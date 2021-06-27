import csv
import pickle
import statistics as s
from collections import namedtuple

from headline import Headline

headlinesSub_list  = []

open_file = open("HeadlinesSubListNeu.pkl", "rb")
headlinesSub_list = pickle.load(open_file)
open_file.close()

countneg = 0
countpos = 0

for headline in headlinesSub_list:
    if headline.sentimentWert > 0:
       countpos += 1
    if headline.sentimentWert < 0:
        countneg += 1
print(countpos)
print(countneg)


######################################### Statistics Values ################################

sentiment_list = [headline.sentimentWert for headline in headlinesSub_list]

sentiment_list_not_neutral = [headline.sentimentWert for headline in headlinesSub_list if headline.sentimentWert != 0]

# get the average value of all the sentiments
print('Average value of all the sentiment polarities: ' + str(s.mean(sentiment_list)))
print('Mode (most common value) of all the sentiment polarities: ' + str(s.mode(sentiment_list)))


# get the average value from all non neutral values
print('Average value of all the non neutral sentiment polarities: ' + str(s.mean(sentiment_list_not_neutral)))
print('Mode (most common value) of all the non neutral sentiment polarities: ' + str(s.mode(sentiment_list_not_neutral)))


headlines2015_2016 = [headline for headline in headlinesSub_list if '2021' in headline.published]
words_2015 = []

for headline in headlines2015_2016:
    for word in headline.title.split():
         word =  word.replace('-', '').replace(':', '').replace('.', '').replace('!', '').replace('?', '').replace(',', '').replace(';', '')
         if word not in words_2015 and word.istitle():
            words_2015.append(word)

#print(words_2015)

#class WordCount:
 #   def __init__(self, word, count):
  #      self.word = word
   #     self.count = count
   # def get_data(self):
    #    print(self.word, self.count)


words_count_2015 = []

#WordCount = namedtuple('word', 'count')


for word in words_2015:
    count = 0
    for headline in headlines2015_2016:
        for w in headline.title.split():
            w = w.replace('-', '').replace(':', '').replace('.', '').replace('!', '').replace('?', '').replace(',', '').replace(';', '')
            if word == w:
               count += 1
    words_count_2015.append((word, count))

words_count_2015.sort(key = lambda x: x[1],  reverse = True)



open_file = open("WordsCount2021.pkl", "wb")
pickle.dump(words_count_2015, open_file)
open_file.close()

