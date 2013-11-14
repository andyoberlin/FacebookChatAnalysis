import json
import sqlite3
from optparse import OptionParser

def averageMessageLen(db):
    query = 'SELECT F.name, AVG(LENGTH(M.message)) FROM message M JOIN friend F ON M.sender = F.id WHERE M.message != "NULL" GROUP BY M.sender;'
    

def printOutput(key, value, form):
    print str(key) + "\t" + str(value)

if __name__ == '__main__':
    parser = OptionParser()
    
    parser.add_option("-d", "--database", dest="database", default="messages.db",
                      help="Filename for the sqlite database for the messages")
    #parser.add_option("-f", "--format", dest="format", default="tabbed",
    #                  help="The format in which to output the data to the console: csv, tabbed")
    
    (options, args) = parser.parse_args()
    
    


