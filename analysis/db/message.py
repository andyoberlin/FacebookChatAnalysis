'''
Created on Nov 14, 2013

@author: andyisaballa
'''

from datetime import datetime

class Message(object):
    def __init__(self, ID, sender, message, time):
        self.ID = ID
        self.sender = sender
        self.text = message
        self.time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S+0000')
        
    @staticmethod
    def fromTuple(tup):
        return Message(tup[0], tup[1], tup[2], tup[3])
