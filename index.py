import csv;
from matplotlib import pyplot as plt;
import numpy as np;
from collections import Counter;
# read csv file
lang =[]
popularity = []
with open('survey_results_public.csv') as file_reader:
	data = csv.DictReader(file_reader)
	lang_counter = Counter()
	i= 0
	for row in range(0,14):
		lang_counter.update(next(data)['LanguageWorkedWith'].split(';'))
		i+=1
	# print(lang_counter.most_common())
	for item in lang_counter.most_common():
		lang.append(item[0])
		popularity.append(item[1])
	lang.reverse()
	popularity.reverse()
plt.barh(lang,popularity)
plt.title("lang bars")
plt.xlabel('Popularity')
plt.show()