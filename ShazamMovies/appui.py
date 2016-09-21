from time import sleep
import pygtk
pygtk.require('2.0')
import gtk
import pickle
from LanguageModel import LanguageModel
import speech_recognition as sr
import gobject
import threading,logging
from tran import speechToText
from os import listdir

from threading import Thread

if 'model.p' in listdir("../IRP"):
	model = pickle.load(open("model.p","rb"))
	print 'model already exists'
else:
	import generateModel
	'generate model'
	model = pickle.load(open("model.p","rb"))

gobject.threads_init()

class SpeechThread(threading.Thread):
    def __init__(self, spinner, textbox):
        super(SpeechThread, self).__init__()
        self.spinner = spinner
        self.textbox = textbox
        self.quit = False

    def update_label(self, counter):
        self.spinner.start()
        return False

    def run(self):
        counter = 0
        while True:
			counter += 1
			gobject.idle_add(self.update_label, counter)
			r = sr.Recognizer()
			with sr.Microphone() as source:
				print 'listening'
				audio = r.listen(source)
			try:
				transcribe = r.recognize_google(audio)
				print transcribe
			except sr.UnknownValueError:
				print 'Google Speech could not understand'
			except sr.RequestError as e:
				print 'Could get results from Google'	 
			
			print('finished thread')
			self.spinner.stop()
			self.textbox.set_text(transcribe)
			break

class SearchThread(threading.Thread):
	def __init__(self,spinner,search, textbox1):
		super(SearchThread, self).__init__()
		self.spinner 	= spinner
		self.search 	= search
		self.textbox1 	= textbox1
		self.quit = False
	
	def update_label(self, counter):
		self.spinner.start()
		return False

	def run(self):
		counter = 0
		while True:
			counter += 1
			gobject.idle_add(self.update_label, counter)
			results = model.search(self.search, n_docs = 10)
			resultStr  = ''
			for r in results:
				resultStr += r[0] + "\n"
			print r
			buffer = self.textbox1.get_buffer()
			buffer.set_text(resultStr)
			self.textbox1.set_buffer(buffer)	
			print('finished thread')
			self.spinner.stop()
			break
	

class IRSys: 
	
    def callback(self, widget, data=None):
		print "%s was toggled %s" % (data, ("OFF", "ON")[widget.get_active()])
		if data == 'b1':
			self.on_button_clicked1(widget)
		else:
			self.on_button_clicked2(widget)
			
		
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        #self.window.set_position(gtk.WIN_POS_MOUSE)
        self.window.set_border_width(10)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(800, 600)
        self.window.set_title("Information Retrieval System")
        self.window.set_tooltip_text("This Project has done By:\n Dan Moony & Nazar Al-Wattar\n Supervised By: Professor Yacci Paul")

        button = gtk.RadioButton()
        self.radioButton1 = gtk.RadioButton(button)
        self.radioButton1.connect("toggled", self.callback,'b1')
        self.radioButton1.set_active(True)

        self.label1 = gtk.Label("Enter Your Text ")
        self.label2 = gtk.Label("Search Result are:  ")

        self.textbox1 = gtk.Entry()
        self.textbox1.connect("changed", self.textEntered)

        self.radioButton2 = gtk.RadioButton(button)
        self.radioButton2.connect("toggled", self.callback,'b2')

        self.voicerecordingbutton = gtk.Button("Record Your Voice")
        self.voicerecordingbutton.connect("pressed", self.press)
        self.voicerecordingbutton.connect("released", self.release)
        self.voicerecordingbutton.set_tooltip_text("This Button Will Record Your Voice")

        self.textbox1.set_tooltip_text("Enter Your Text Here")

        self.spinner = gtk.Spinner()
        self.spinner.size(100,100)

        self.searchbutton = gtk.Button("Search")
        self.searchbutton.connect("clicked", self.mysearchbutton)
        self.searchbutton.set_tooltip_text("This Button Will Start Search and return the result to the combobox")

        #self.combo = gtk.combo_box_entry_new_text()
        #self.combo.connect("changed", self.combo_text)
        #self.combo.append_text("This is my first result")
        #self.combo.append_text("This is my second result")

        self.combo = gtk.TextView()
        self.combo.set_size_request(width=250, height=150)
        self.combo.set_editable(False)
        buffer = gtk.TextBuffer()
        buffer.set_text("Test Results here!")
        self.combo.set_buffer(buffer)
       	
        fixed = gtk.Fixed()
        fixed.put(self.radioButton1, 100, 50)
        fixed.put(self.label1, 150, 50)
        fixed.put(self.label2, 150, 350)
        fixed.put(self.textbox1, 550, 50)

        fixed.put(self.radioButton2, 100, 150)
        fixed.put(self.voicerecordingbutton, 150, 150)
        fixed.put(self.spinner, 500, 100)

        fixed.put(self.searchbutton, 570, 270)
        fixed.put(self.combo, 525, 350)

        self.window.add(fixed)
        self.window.show_all()
        self.hidevoicerecordingbutton(False)
        self.hidesearchbutton(True)
        self.hidecombobox(True)
	
	    	
    def press(self,widget):
    	self.spinner.start()
    
    
    def release(self, widget, data=None):
		speechThread = SpeechThread(spinner = self.spinner, textbox = self.textbox1)
		speechThread.start()
		print 'finished release'
    	
    		
    	
    	
    	
    	#thread1 = myThread(1, "Thread-1", 1)
    	#thread1.start()
    	#thread2 = myThread(1, "Thread-1", 1)
    	#thread2.start()
    	#voice = speechToText() 
    	#self.search(voice)
    	#test = Thread(target=download, args=(self,)).start()
    	#test.start()      
	
	
		
    	
    
	
    #def search(self,query):
		#results = model.search(query)
		#resultStr  = ''
		#or r in results:
		#	resultStr += r[0] + "\n"
		#	print r
		#buffer = self.combo.get_buffer()
		#buffer.set_text(resultStr)
		#self.combo.set_buffer(buffer)		
    	
        	
    
        
    def mysearchbutton(self, widget, data=None):
		self.showcombo(True)
		print ("You Clicked the search button")
		print self.textbox1.get_text()
		searchedText = self.textbox1.get_text()
		newThread =  SearchThread(self.spinner, searchedText, self.combo)
		newThread.start()
        #self.search(searchedText)
        
        

    def hidetextbox(self, sen):
        self.textbox1.set_sensitive(sen)

    def hidevoicerecordingbutton(self, sen):
        self.voicerecordingbutton.set_sensitive(sen)

    def hidesearchbutton(self, sen):
        self.searchbutton.set_sensitive(sen)

    def hidecombobox(self, sen):
        self.combo.set_sensitive(sen)

    def showtextbox(self, sen):
        self.textbox1.set_sensitive(sen)

    def showvoicerecordingbutton(self, sen):
        self.voicerecordingbutton.set_sensitive(sen)

    def showsearchbutton(self, sen):
        self.searchbutton.set_sensitive(sen)

    def showcombo(self, sen):
        self.combo.set_sensitive(sen)

    def textEntered(self, widget):
        print ("I got your text")

    def on_button_clicked1(self, button):
        sen = False
        if button.get_active():
            self.hidevoicerecordingbutton(sen)
            self.spinner.stop()
            sen = True
            self.showtextbox(sen)
            self.showsearchbutton(sen)
            print ("active")

    def on_button_clicked2(self, button):
        sen = False
        if button.get_active():
            self.hidetextbox(sen)
            sen = True
            self.showvoicerecordingbutton(sen)
            self.showsearchbutton(sen)
            print ("active")

    def combo_text(self, widget):
        self.textbox1.set_text(widget.get_active_text)

    def main(self):
        gtk.main()
        


if __name__ == "__main__":
    base = IRSys()
    base.main()