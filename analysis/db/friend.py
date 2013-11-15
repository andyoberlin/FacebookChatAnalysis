'''
Created on Nov 15, 2013

@author: andyisaballa
'''

class Friend(object):

    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
    
    
    @staticmethod
    def fromTuple(tup):
        return Friend(tup[0], tup[1])