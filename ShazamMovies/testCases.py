from PyQt4 import QtGui,QtCore # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication

import design # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer


from PyQt4.QtGui import QPixmap, QPicture, QLabel,QImageReader
import time
import threading
import pysrt
import speech_recognition as sr
import pickle
from os import listdir
import os
from os 			import listdir
from os.path 		import isfile,join
import random


model 		= pickle.load(open("model.p","rb"))

datafolder = 'subtitles/'

corpus =  listdir(datafolder)
bothcorrect 	= 0
firstcorrect 	= 0
secondcorrect 	= 0
total 			= 0
corpus.pop(0)
corpus.remove("Highway.srt")
for doc in corpus:
	try:
		subs = pysrt.open(datafolder + doc, encoding='cp1252')
	except:
		subs = pysrt.open(datafolder + doc, encoding='utf8')
	
	testCase = random.randint(0, len(subs.text)-200)
	testtext = subs.text[testCase:testCase+200]
	testtext = testtext.replace("\n","")
	result = model.search(testtext,n_docs=5)
		
	
	if result[0][0] == doc:
		bothcorrect += 1
		print 'matched'
		
	else:
		print "didn't match"
	
		
	total += 1
		
	#except:
	#	print doc
	#	print 'testCase not long enough'

		
		
		
		#print doc + str(len(subs.text))
	
		
print 'First Random Correct' + str((firstcorrect*100)/float(total))
print 'Second Random Correct' + str((secondcorrect*100)/float(total))
print 'First or Second Random Correct' + str((bothcorrect*100)/float(total))	