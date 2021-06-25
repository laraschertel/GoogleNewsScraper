import pickle
from headline import Headline

headlines_list = []

open_file = open("HeadlinesList.pkl", "rb")
headlines_list = pickle.load(open_file)
open_file.close()


#for headline in headlines_list:
 #   if headline.sentimentWert != 0:
  #      print(headline.title, headline.sentimentWert)
