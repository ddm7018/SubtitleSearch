import sys, os, operator, pysrt, threading
from os 			import listdir
from os.path 		import isfile,join
from collections 	import defaultdict
from math 			import log, sqrt
import re




class LanguageModel:
	def __init__(self, datafolder):
		
		self.corpus = [f for f in listdir(datafolder) if isfile(join(datafolder,f))]
		self.text = []
		for file in self.corpus:
			print file
			try:
				subs = pysrt.open(datafolder+"/"+file, encoding='cp1252')
			except:
				subs = pysrt.open(datafolder+"/"+file, encoding='utf8')
			subtext = ''
			for ele in subs:
				subtext += ele.text 
			self.text.append(subtext)
		
		allWords = []
		allDocs = self.text
		for d in allDocs:
			for ele in re.split(",|!| ",d):
				allWords.append(ele)
		self.vocab = allWords
		
		self.wordDict =  self.word_freq(allWords)
		
	def words(self, document):
		words = document.split()
		words = [x.lower() for x in words]
		words = [x for x in words if len(x) >= 2and not x.isdigit()]
		return words	

	def word_freq(self, wordlist):
		wordFreq = defaultdict(int)
		for w in wordlist:
			wordFreq[w] += 1
		return wordFreq

	'''
	def vocab(self):
		allWords = []
		allDocs = self.text
		for d in allDocs:
			for ele in re.split(",|!| ",d):
				allWords.append(ele)
		return allWords
		
	def wordDict(self):
		allWords = self.vocab()
		
		return self.word_freq(allWords)
	'''
	def document_logScore(self, document, query):
		docWords 			= self.words(document)
		docWordFrequency 	= self.word_freq(docWords)
		corpusVocablury 	= self.wordDict
		normalizingFactor 	= len(self.vocab)
		logProb 			= 0
		queryWords = self.words(query)
		for q in queryWords:
			try:
				qFreq = docWordFrequency[q]
			except:
				qFreq = 0	
			try:
				 qCount = corpusVocablury[q] 
			except:
				qCount = 0
			
			#print qFreq,qCount,normalizingFactor
			
			alpha = float(qFreq + 1)/float(qCount + normalizingFactor)

			logContribution 	= log(alpha)
			logProb 			+= logContribution

		return logProb


	
	
	def logScoreDict(self, query):
		
		
		rakingDict 	= {}
		allDocs 	= range(len(self.corpus ))	
		count 		= 0
		
		self.query = query
		
		for ele in allDocs:
			docText 	= self.text[count]
			logScore 	= self.document_logScore(docText, query)
			#print self.corpus[count],logScore
			rakingDict[self.corpus[count]]	= logScore
			count 		+= 1 
			
		#pool = Pool(1)
		#iterable = self.text
		#func = partial(f,self)
		#results =pool.map(func, allDocs)
		#pool.close()
		#pool.join()
		
	
		
		#for ele in results:
			
		#	rakingDict[self.corpus[ele[0]]]	= ele[1]
		
		return rakingDict
		
	def search(self, query, n_docs = 2):
		relevantDocs = []
		rankings 		= self.logScoreDict(query)
		rankingSort 	= sorted(rankings.iteritems(), key=lambda (k,v): (v,k))
		rankingRev		= rankingSort[::-1]
		return rankingRev[0:n_docs]
		return rankings
