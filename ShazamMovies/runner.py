#!/usr/bin/python
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
from movieObj import movieObj

model 		= pickle.load(open("model.p","rb"))
movieDict 	= pickle.load(open("dict.p","rb"))


	

class SearchThread(threading.Thread):
    def __init__(self, listWidget,searched):
    	super(SearchThread, self).__init__()
    	self.listWidget = listWidget
    	self.searched = searched
    	self.quit = False

    def run(self):
        counter = 0
       	self.listWidget.clear()
        while True:
			results = model.search(str(self.searched), n_docs = 10)
			
			print results
			for r in results:
				#resultStr += r[0] + "\n"
				self.listWidget.addItem(r[0])
			break


class SpeechThread(threading.Thread):
    def __init__(self, lineEdit):
    	super(SpeechThread, self).__init__()
    	self.lineEdit = lineEdit
    	self.quit = False

    def run(self):
        counter = 0
        while True:
			#gobject.idle_add(self.update_label, counter)
			r = sr.Recognizer()
			
			with sr.Microphone() as source:
				print 'listening'
				audio = r.listen(source)
			try:
				transcribe = r.recognize_google(audio)
				print transcribe
				self.lineEdit.setText(transcribe)
			except sr.UnknownValueError:
				print 'Google Speech could not understand'
			except sr.RequestError as e:
				print 'Could get results from Google'	 
			break



class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
	def onStart(self): 
		self.progressBar.setRange(0,100)
	
	def search(self):
		self.progressBar.setRange(0,100)
		newThread =  SearchThread(self.listWidget,self.lineEdit.text())
		newThread.start()
		count = 0
		while True:
			time.sleep(.1)
			count += 5
			self.helperObj.valueUpdated.emit(count)
			if count == 100:
				count =0
			#print newThread
			if newThread.is_alive() == False:
				break
		print 'finished'
		self.progressBar.setValue(100)
		
		
	def audioTranslate(self):
		self.progressBar.setRange(0,100)
		newThread =  SpeechThread(self.lineEdit)
		newThread.start()
		count = 0
		while True:
			time.sleep(.1)
			count += 5
			self.helperObj.valueUpdated.emit(count)
			if count == 100:
				count =0
			#print newThread
			if newThread.is_alive() == False:
				break
		print 'finished'
		self.progressBar.setValue(100)	
	
	def onProgress(self, i):
		self.progressBar.setValue(i)
		print i


	def radioclicked(self):
		#print 'radio'
		print 'radio1' + str(self.radioButton.isChecked())
		print 'radio2' + str(self.radioButton_2.isChecked())

		if(self.radioButton_2.isChecked()):
			self.lineEdit.setEnabled(False)
			self.pushButton_2.setEnabled(True)
			
		if(self.radioButton.isChecked()):
			self.lineEdit.setEnabled(True)
			self.pushButton_2.setEnabled(False)
	
	

	
	
	def __init__(self):
		super(self.__class__, self).__init__()
		self.valueUpdated = QtCore.pyqtSignal(int)
		print self.valueUpdated
		self.setupUi(self) 
		self.pushButton.clicked.connect(self.search)
		
		self.pushButton_2.clicked.connect(self.audioTranslate)
		#self.radio1.toggled.connect(self.radio1_clicked)
        #self.radio2.toggled.connect(self.radio2_clicked)
		
		self.progressBar.setValue(0)
		
		self.listWidget.currentItemChanged.connect(self.on_item_changed)

		
		self.radioButton.setChecked(True)
		self.radioButton.toggled.connect(self.radioclicked)
		#self.radioButton_2.toggled.connect(self.radioclicked)
		
		self.pushButton_2.setEnabled(False)
		
		#self.valueUpdated.connect(self.handleValueUpdated)	
		self.helperObj = HelperClass(self)
		self.helperObj.valueUpdated.connect(self.handleValueUpdated)

		
		

	
	def on_item_changed(self,curr, prev):
		print curr
		movieObj =  movieDict[str(curr.text())]
		picFileName = movieObj.movieImageFileLocation
		picmap  = QPixmap("moviePics/"+picFileName)
		pixmap4 = picmap.scaled(120, 120)
		
		self.movieTitle.setText(movieObj.movieName)
		self.picLabel.setPixmap(pixmap4)
		
		
		try:
			subs = pysrt.open('subtitles/'+str(curr.text()), encoding='cp1252')
		except:
				subs = pysrt.open('subtitles/'+str(curr.text()), encoding='utf8')
		
		
		self.subtitle.setText(subs.text)
		cursor = self.subtitle.textCursor()
        # Setup the desired format for matches
		format = QtGui.QTextCharFormat()
		format.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))
        # Setup the regex engine
		patterns = self.lineEdit.text().split(" ")
		print patterns
		for pattern in patterns:
			regex = QtCore.QRegExp(pattern)
        # Process the displayed document
			pos = 0
			index = regex.indexIn(self.subtitle.toPlainText(), pos)
			while (index != -1):
				# Select the matched text and apply the desired format
				cursor.setPosition(index)
				cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
				cursor.mergeCharFormat(format)
            # Move to the next match
				pos = index + regex.matchedLength()
				index = regex.indexIn(self.subtitle.toPlainText(), pos)
		
		
		#w.resize(pixmap.width(),pixmap.height())
	
	def handleValueUpdated(self, value):
		self.progressBar.setValue(value)
		QtGui.qApp.processEvents()
	 


from PyQt4 import QtCore

class HelperClass(QtCore.QObject):
    valueUpdated = QtCore.pyqtSignal(int)


def main():
	app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
	form = ExampleApp()                 # We set the form to be our ExampleApp (design)
	form.show()                         # Show the form
	app.exec_()                         # and execute the app
	


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()     