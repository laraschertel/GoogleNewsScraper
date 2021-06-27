import pickle
import pandas as pd
from tabulate import tabulate


open_file = open("WordsCount2015.pkl", "rb")
words_count_2015_list = pickle.load(open_file)
open_file.close()

words_count_2015_min1_list = filter(lambda x: x[1] > 2, words_count_2015_list)

print(tabulate(words_count_2015_min1_list, headers='keys', tablefmt='fancy_grid'))

