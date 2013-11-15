import sqlite3
from message import Message
from friend import Friend

'''
Created on Nov 14, 2013

@author: andyisaballa
'''
STICKERS_ENABLED = 0
STICKERS_DISABLED  = 1
STICKERS_ONLY = 2


def getMessagesByFriend(db, name, stickers=STICKERS_DISABLED):
    conn = sqlite3.connect(db)
    cursor = conn.cursor() 
    if isinstance(name, str):
        nameQ = 'SELECT id FROM friend WHERE name=?;'
        name = cursor.execute(nameQ, (name, )).fetchone()[0]
        
    if stickers == STICKERS_DISABLED:
        query = "SELECT * FROM message WHERE sender=? AND message != 'NULL';"
    elif stickers == STICKERS_ONLY:
        query = "SELECT * FROM message WHERE sender=? AND message == 'NULL';"
    else:
        query = 'SELECT * FROM message WHERE sender=?;'
    
    messages = cursor.execute(query, (name, )).fetchall()
    
    cursor.close()
    conn.close() 
    
    return [Message.fromTuple(m) for m in messages]
    
def getFriends(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    people = cursor.execute('SELECT * FROM friend;').fetchall()
    
    cursor.close()
    conn.close() 
    
    return [Friend.fromTuple(f) for f in people]

