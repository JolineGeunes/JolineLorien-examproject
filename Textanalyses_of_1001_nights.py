##############################
#Text analyses of 1001-nights#
##############################

# Make a corpus of the ten volumes:
from os import listdir

def list_10_volumes(directory):
	volumes = []
	for volume in listdir(directory):
		if volume.startswith('arabian'):
			volumes.append(directory + '/' + volume)
	return volumes

corpus = list_10_volumes('data')
print(corpus)

# How many characters does each volume in the corpus have? 
# and how many characters does the entire corpus have?
def calculate_characters(corpus):
	counter = 0
	for volume in corpus:
		f = open(volume, 'rt', encoding='utf-8') 
		text = f.read()
		f.close()
		print(volume + ' has ' + str(len(text)) + ' characters.')	
		counter+= len(text)
	print('Together, the ten volumes have ' + str(counter) + ' characters.' )

print(calculate_characters(corpus))	

# How many lines does the entire corpus have?
def calculate_lines(corpus):
	count = 0
	for volume in corpus:
		f = open(volume, 'rt', encoding='utf-8') 
		for line in f:
			count += 1
		f.close()	
	print('The corpus of ten volumes has ' + str(count) + ' lines.')	
			
print(calculate_lines(corpus))	

# How many lines does each volume have?
def calculate_lines_II(file):
	count = 0
	f = open (file, 'rt', encoding='utf-8') 
	for line in f:
		count += 1
	f.close()
	return file + ' has ' + str(count) + ' lines.'

for volume in corpus: 
	print(calculate_lines_II(volume))		

# In order to calculate the amount of words and sentences in each volume,
# I made a new corpus of the volumes using the nltk PlaintextCorpusReader
# which has some easy tools that can split a text into a list of words or sentences.

from nltk.corpus import PlaintextCorpusReader
corpus_root= 'data'
volumes = PlaintextCorpusReader(corpus_root, 'arabian.*')

list_of_sentences = volumes.sents()
print('The ten volumes consist of ' + str(len(list_of_sentences)) + ' sentences')

list_of_words = volumes.words()
print('The ten volumes consist of ' + str(len(list_of_words)) + ' words')

for item in volumes.fileids(): #calculate the amount of words in each volume
	print(item,':', len(volumes.words(item)), 'words')

for item in volumes.fileids(): #calculate the amount of sentences in each volume
	print(item,':', len(volumes.sents(item)), 'sentences')	

####################################################################################
#<<<<<<< HEAD
#Now that we know some of the statistics about each volume and the entire corpus, we
#want to have a look at the individual nights. 
####################################################################################


#visualization of the statistiscs with basic plotting techniques

import matplotlib.pyplot as plt #pyhton library for plotting data
import numpy as np
#%matplotlib inline #only necessary when you need to use the code in Jupyter Notebook

#visualize the characters per volume
#make a list of the total characters per volume ---> lijst maken van de counters die def(calculate_characters) teruggeeft
#characters_per_volume= []
#for volume in corpus:
	#characters_per_volume.append(calculate_characters(corpus)) #ik weet niet hoe ik hier een lijst van kan maken
#dit klopt niet, de aparte counters zonder tekst komen niet in een lijst, wel de tekst en de counters
#print(characters_per_volume)

characters_per_volume = [719626, 713975, 740002, 608981, 805537, 620786, 816219, 728202, 743379, 130715] #nu heb ik handmatig een lijst gemaakt
 #van de aantallen characters per volume
x = [1,2,3,4,5,6,7,8,9,10]
y = characters_per_volume
x_labels = ["vol1","vol2","vol3","vol4","vol5","vol6","vol7","vol8","vol9","vol10"]
y_labels = [719626, 713975, 740002, 608981, 805537, 620786, 816219, 728202, 743379, 130715]
width = 0.8 # width of the bars
fig, ax = plt.subplots() #make subplots, so that their will be labels above the bars
rects1 = ax.bar(x, y_labels) #rects stands for rectangles, the shape of the bar chart. 

def autolabel(rects):# attach labels above bars #zoals gevonden op matplotlib site
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom') #The placement of the text is determined by the height function, or the height of the column
        #and the number that is put on top of each column is written by: '%d' %int(height). 
        #So all you need to do is create an array of strings that you want at the top of the columns and iterate through. 
print(autolabel(rects1))

plt.bar(x,y) #plot a bar chart and attach some information to it
plt.title("total number of characters in a volume")
plt.xlabel("volume")
plt.ylabel("# of characters")
plt.xticks(x,x_labels)
plt.show()


#visualize the lines per volume
#make a list of the total lines per volume ---> lijst maken van de counters die def(calculate_lines_II(volume)) teruggeeft 
lines_per_volume = []
for volume in corpus:
	lines_per_volume.append(calculate_lines_II(volume)) #ik weet niet hoe ik hier een lijst van kan maken
#dit klopt niet, de aparte counters zonder tekst komen niet in een lijst, wel de tekst en de counters
print(lines_per_volume)

lines_per_volume = [ 12498, 12159, 13092, 10925, 14585, 10491, 13786, 13189, 12517, 2221 ] #I made this list manually
x = [1,2,3,4,5,6,7,8,9,10]
y = lines_per_volume
x_labels = ["vol1","vol2","vol3","vol4","vol5","vol6","vol7","vol8","vol9","vol10"]
y_labels = [12498, 12159, 13092, 10925, 14585, 10491, 13786, 13189, 12517, 2221 ]
width = 0.8 # width of the bars
fig, ax = plt.subplots() #make subplots, so that their will be labels above the bars
rects2 = ax.bar(x, y_labels) #rects stands for rectangles, the shape of the bar chart. 

def autolabel(rects):# attach labels above bars as recommanded by the matplotlib site
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom') #The placement of the text is determined by the height function, or the height of the column
        #and the number that is put on top of each column is written by: '%d' %int(height). 
        #So all you need to do is create an array of strings that you want at the top of the columns and iterate through. 
print(autolabel(rects2))

plt.bar(x,y) #plot a bar chart and attach some information to it
plt.title("total number of lines in a volume")
plt.xlabel("volume")
plt.ylabel("# of lines")
plt.xticks(x,x_labels)
plt.show()

#visualize the sentences per volume
sentences_per_volume = []
for item in volumes.fileids():
	sentences_per_volume.append(len(volumes.sents(item)))
print(sentences_per_volume)

x = [1,2,3,4,5,6,7,8,9,10]
y = sentences_per_volume
x_labels = ["vol1","vol2","vol3","vol4","vol5","vol6","vol7","vol8","vol9","vol10"]
y_labels = sentences_per_volume
width = 0.8 # width of the bars
fig, ax = plt.subplots() #make subplots, so that their will be labels above the bars
rects1 = ax.bar(x, y_labels) #rects stands for rectangles, the shape of the bar chart. 

def autolabel(rects):# attach labels above bars as recommanded by the matplotlib site
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom') #The placement of the text is determined by the height function, or the height of the column
        #and the number that is put on top of each column is written by: '%d' %int(height). 
        #So all you need to do is create an array of strings that you want at the top of the columns and iterate through. 
print(autolabel(rects1))

plt.bar(x,y) #plot a bar chart and attach some information to it
plt.title("total number of sentences in a volume")
plt.xlabel("volume")
plt.ylabel("# of sentences")
plt.xticks(x,x_labels)
plt.show()


#visualize the words per volume
words_per_volume = []
for item in volumes.fileids():
	words_per_volume.append(len(volumes.words(item)))
print(words_per_volume)

x = [1,2,3,4,5,6,7,8,9,10]
y = words_per_volume
x_labels = ["vol1","vol2","vol3","vol4","vol5","vol6","vol7","vol8","vol9","vol10"]
y_labels = words_per_volume
width = 0.8 # width of the bars
fig, ax = plt.subplots() #make subplots, so that their will be labels above the bars
rects1 = ax.bar(x, y_labels) #rects stands for rectangles, the shape of the bar chart. 

def autolabel(rects):# attach labels above bars as recommanded by the matplotlib site
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom') #The placement of the text is determined by the height function, or the height of the column
        #and the number that is put on top of each column is written by: '%d' %int(height). 
        #So all you need to do is create an array of strings that you want at the top of the columns and iterate through. 
print(autolabel(rects1))

plt.bar(x,y) #plot a bar chart and attach some information to it
plt.title("total number of words in a volume")
plt.xlabel("volume")
plt.ylabel("# of words")
plt.xticks(x,x_labels)
plt.show()

#visualize all the total numbers for the entire corpus (= ten volumes of The Arabian Nights)
#I would like to make a table with the following cells, but I don't know how yet
#data_matrix = [['Statistiscs', 'Total characters', 'total lines', 'total sentences', 'total words'],
               ['The Arabian Nights', 6627422 , 115463, 43094, 1459332 ]]


#########################################################################################

# Now that we know some of the statistics about each volume and the entire corpus, we
# Want to have a look at the individual nights. 

# To make sure all the volumes are automatically read. 
read_corpus = []
for volume in corpus:
	f = open(volume, 'rt', encoding='utf-8') 
	text = f.read()
	f.close()
	read_corpus.append(text)	

import re

# Two definitions that can find the starting and ending index of each night. 
def start_idex_nights(regex, text, flags=re.IGNORECASE): # So it is case insensitive.
	start_index = []
	for match in re.finditer(regex, text, flags):
		start_index.append(match.start())
	return start_index	

def start_and_end_index_nights(volume):
	start_index = start_idex_nights("When it was the.*Night,?\n", volume)
	night_indexes = []
	for i in range(len(start_index)-1): # Minus 1 because the last night of each volume is no new start index of the next night (which is in the next volume).
		night_indexes.append((start_index[i], start_index[i+1])) # You get the index of a night and the subsequent night, which is the end index of the previous night.	
	night_indexes.append((start_index[-1], len(volume) - 1)) # Here the indexes of the last night of a volume are added.
	return night_indexes

counter = 0
for volume in read_corpus:
	counter+= (len(start_and_end_index_nights(volume)))
print(counter) # It seems there are only 990 nights in the ten volumes, or at least, 990 nights are extracted. 

# The next step is to put each night in a separate file. (I will do that asap)
	


#>>>>>>> origin/master
