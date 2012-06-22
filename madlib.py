#!/usr/bin/env python

from random import randint

class MadLibGen(object):

	def __init__(self, story, verbFile, adverbFile, nounFile, adjectiveFile):
		self.verbs = self.loadFile(verbFile)
		self.adverbs = self.loadFile(adverbFile)
		self.nouns = self.loadFile(nounFile)
		self.adjectives = self.loadFile(adjectiveFile)
		self.story = self.loadStoryFile(story)
		self.toFill = []

	def loadFile(self, filePath):
		f = open(filePath, 'r')
		data = f.read().split()
		f.close()
		return data

	def rollDice(self):
		roll = randint(0,1)
		if(roll):
			return True
		return False

	def loadStoryFile(self, filePath):
		f = open(filePath, 'r')
		data = f.read()
		f.close()
		return data

	def makeMadlib(self):
		print '[*] Replacing verbs ...'
		count = 0
		for word in self.verbs:
			if word in self.story:
				self.findReplace(word, "verb", count)
				self.toFill.append("verb "+str(count)+":_____")
				count +=1
		print '[*] Replacing adverbs ...'
		count = 0
		for word in self.adverbs:
			if word in self.story:
				self.findReplace(word, "adverb", count)
				self.toFill.append("adverb "+str(count)+":_____")
				count +=1
		print '[*] Replacing nouns ...'
		count = 0
		for word in self.nouns:
			if word in self.story:
				self.findReplace(word, "noun", count)
				self.toFill.append("noun "+str(count)+":_____")

				count +=1
		print '[*] Replacing adjectives ...'
		count = 0
		for word in self.adjectives:
			if word in self.story:
				self.findReplace(word, "adjective", count)
				self.toFill.append("adjective "+str(count)+":_____")
				count +=1

	def findReplace(self, word, wordType, count):
		if(self.rollDice()):
			self.story = self.story.replace(word, " __%s_%d__ " % (wordType, count))

	def saveFile(self):
		print '[*] Saving file ...'
		f = open('madlibs.out', 'w')
		f.write(self.story)
		f.close()

	def saveFillFile(self):
		print "[*] Saving Fill File"
		f = open('fillFile.out', 'w')
		f.write('\n'.join(self.toFill))
		f.close()

if __name__ == '__main__':
	gen = MadLibGen("story.txt", "verbs.list", "adverb.txt", "nouns.list", "adjective.list")
	gen.makeMadlib()
	gen.saveFile()
	gen.saveFillFile()
	print '[*] All done!'

