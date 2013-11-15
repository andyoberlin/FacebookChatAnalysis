import sqlite3
import json
from optparse import OptionParser

def makeSchema(db):
    schemaFile = open('messages.sql', 'r')
    schema = schemaFile.read()
    schemaFile.close()

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.executescript(schema)

    cursor.close()
    conn.close()

def loadMessages(messages):
    messagesFile = open(messages, 'r')
    result = messagesFile.read()
    messagesFile.close()

    return json.loads(result)

def addMessageToDB(message, db):
    name = message['from']['name']
    text = message['message'] if message.has_key('message') else 'NULL'
    time = message['created_time'] 
    
    # add the user for the message
    conn = sqlite3.connect(db)
    cursor = conn.cursor()    

    cursor.execute("INSERT OR IGNORE INTO friend(name) VALUES (?);", (name, ))
    
    conn.commit()
    
    userID = cursor.execute("SELECT id FROM friend WHERE name=?;", (name, )).fetchone()[0]
    cursor.execute("INSERT OR IGNORE INTO message(sender, message, time) VALUES (?, ?, ?);",
            (userID, text, time))

    conn.commit()

    cursor.close()
    conn.close()



if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-d", "--database", dest="database", default="messages.db", help="Filename for the sqlite3 database")
    parser.add_option("-m", "--messages", dest="messages", default="messages.json", help="Filename for the messages in json")

    (options, args) = parser.parse_args()

    makeSchema(options.database)
    messages = loadMessages(options.messages)
    for message in messages:
        addMessageToDB(message, options.database)
