'''
Created on Nov 15, 2013

@author: andyisaballa
'''

from inspect import ismethod
from db import DatabaseUtil
def AnalysisRunner(fn):
    fn.analysisMethod = True
    return fn

class Analysis(object):
    
    def __init__(self, db):
        self.db = db
        self.friends = None
    
    def analyze(self):
        for name in dir(self):
            attribute = getattr(self, name)
            if ismethod(attribute) and hasattr(attribute, 'analysisMethod') and attribute.analysisMethod:
                attribute()
                print "\n"
                
    def _getFriends(self):
        if self.friends:
            return self.friends
        
        self.friends = DatabaseUtil.getFriends(self.db)
        return self.friends
        