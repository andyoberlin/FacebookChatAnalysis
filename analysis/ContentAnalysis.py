'''
Created on Nov 15, 2013

@author: andyisaballa
'''

from db import DatabaseUtil
from Analysis import Analysis, AnalysisRunner

class ContentAnalysis(Analysis):

    @AnalysisRunner
    def generateTotalReport(self):
        friends = self._getFriends()
        
        print "Generating Total Report............."
        
        for friend in friends:
            messages = DatabaseUtil.getMessagesByFriend(self.db, friend.ID, DatabaseUtil.STICKERS_ENABLED)
            print "\t", friend.name, ": ", len(messages)

    @AnalysisRunner
    def generateStickerReport(self):
        friends = self._getFriends()
        
        print "Generating Sticker Report............."
        
        for friend in friends:
            messages = DatabaseUtil.getMessagesByFriend(self.db, friend.ID, DatabaseUtil.STICKERS_ONLY)
            print "\t", friend.name, ": ", len(messages)
            
    @AnalysisRunner
    def generateStickerRatioReport(self):
        friends = self._getFriends()
        
        print "Generating Sticker Ratio Report............."
        
        for friend in friends:
            stickers = DatabaseUtil.getMessagesByFriend(self.db, friend.ID, DatabaseUtil.STICKERS_ONLY)
            messages = DatabaseUtil.getMessagesByFriend(self.db, friend.ID, DatabaseUtil.STICKERS_ENABLED)
            print "\t", friend.name, ": ", "{0:.2f}".format(100 * float(len(stickers)) / len(messages)), "%"
            
            
            
