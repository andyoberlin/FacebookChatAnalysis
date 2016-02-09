'''
Created on Nov 15, 2013

@author: andyisaballa
'''
from db import DatabaseUtil
from Analysis import Analysis, AnalysisRunner
import string

class WordAnalysis(Analysis):

    @AnalysisRunner
    def generateHahaCountReport(self):
        friends = self._getFriends()

        print "Generating Haha Report............."

        for friend in friends:
            hahaCount = 0
            messages = DatabaseUtil.getMessagesByFriend(self.db, friend.ID, DatabaseUtil.STICKERS_DISABLED)
            for message in messages:
                #tokenize the message
                tokens = message.text.split()
                hahaCount += sum([1 for token in tokens if WordAnalysis.isHaha(WordAnalysis.stripPunctuation(token))])
            print "\t", friend.name, ": ", hahaCount

    @AnalysisRunner
    def generateLolCountReport(self):
        friends = self._getFriends()

        print "Generating Lol Report............."

        for friend in friends:
            lolCount = 0
            messages = DatabaseUtil.getMessagesByFriend(self.db, friend.ID, DatabaseUtil.STICKERS_DISABLED)
            for message in messages:
                #tokenize the message
                tokens = message.text.split()
                lolCount += sum([1 for token in tokens if WordAnalysis.isLol(WordAnalysis.stripPunctuation(token))])
            print "\t", friend.name, ": ", lolCount

    @AnalysisRunner
    def generateMessageLenReport(self):
        friends = self._getFriends()

        print "Generating Word Average Report............."

        for friend in friends:
            messages = DatabaseUtil.getMessagesByFriend(self.db, friend.ID, DatabaseUtil.STICKERS_DISABLED)

            avg = [len(message.text.split()) for message in messages]

            if len(avg) > 0:
                avg = float(sum(avg)) / len(avg)
                print "\t", friend.name, ": ", "{0:.2f}".format(avg) + " words"
            else:
                print "\t", friend.name, ": No messages"

    @AnalysisRunner
    def generateCussWordCountReport(self):
        friends = self._getFriends()

        print "Generating Cuss Word Report............."

        for friend in friends:
            cussCount = 0
            messages = DatabaseUtil.getMessagesByFriend(self.db, friend.ID, DatabaseUtil.STICKERS_DISABLED)
            for message in messages:
                #tokenize the message
                tokens = message.text.split()
                cussCount += sum([1 for token in tokens if WordAnalysis.isCussWord(WordAnalysis.stripPunctuation(token))])
            print "\t", friend.name, ": ", cussCount

    @AnalysisRunner
    def generateAmazonCountReport(self):
        friends = self._getFriends()

        print "Generating \"Amazon\" Count Report............."

        for friend in friends:
            amazonCount = 0
            messages = DatabaseUtil.getMessagesByFriend(self.db, friend.ID, DatabaseUtil.STICKERS_DISABLED)
            for message in messages:
                #tokenize the message
                tokens = message.text.split()
                amazonCount += sum([1 for token in tokens if WordAnalysis.isAmazon(WordAnalysis.stripPunctuation(token))])
            print "\t", friend.name, ": ", amazonCount

    @staticmethod
    def isCussWord(word):
        return False

    @staticmethod
    def isAmazon(word):
        return "amazon" == word.lower()

    @staticmethod
    def isHaha(word):
        return len(word) > 1 and 'ha' in word and len(set(word.lower()) - {'h', 'a'}) == 0

    @staticmethod
    def isLol(word):
        if len(word) < 3:
            return False
        word = word.lower()
        missingLO = set(word) - {'l', 'o'}
        empty = len(missingLO) == 0
        if empty:
            return True
        else:
            return word[-1] == 'z' and len(set(word[:-1]) - {'l', 'o'}) == 0

    @staticmethod
    def stripPunctuation(word):
        punct = set(string.punctuation)
        return "".join([c for c in word if not c in punct])
