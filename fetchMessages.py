import urllib2
import json
from optparse import OptionParser

def addAccessToken(url, token):
    return url + "?access_token=" + token

def cleanData(raw):
    data = json.loads(raw)
    
    nextPage = data['paging']['next'] if data.has_key('paging') else None
    prevPage = data['paging']['previous'] if data.has_key('paging') else None

    return data['data'], nextPage, prevPage

def getFacebookMessages(url, token=None):
    print "Fetching message data again..."
    print ("\t URL: " + url)

    if token:
        url = addAccessToken(url, token)
    
    try:
        messages, nextUrl, prevUrl = cleanData(urllib2.urlopen(url).read())
    except urllib2.URLError:
        print "Blocked by Facebook rate limit... restart the script using:"
        print "\tpython fetchMessages.py --restart=restart.dat -messages=messages.json"
        
        with open('restart.dat', 'w') as restart:
            restart.write(url)
        
        return []

    nextMessages = getFacebookMessages(nextUrl) if len(messages) > 0 else []
    
    messages = nextMessages + messages

    return messages

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-r", "--restart", dest="restart",
       help="File with paginated url for restarting if something goes wrong")

    parser.add_option("-s", "--start", dest="start", help="File with url to follow")

    parser.add_option("-a", "--access_token", dest="accessToken", help="Token to append to url for accessing the data")

    parser.add_option("-m", "--messages", dest="messages", help="Filename to output the messages to. Also used with restart to read in")

    (options, args) = parser.parse_args()
    
    # get the file for the messages to be stored in
    messagesFilename = options.messages if options.messages else 'messages.json'

    # get the access token if it exists
    accessToken = None
    if options.accessToken:
        with open(options.accessToken, 'r') as token:
            accessToken = token.read()
    else:
        with open('token.dat', 'r') as token:
            accessToken = token.read()

    # run the program
    if options.restart:
        with open(options.restart, 'r') as restart:
            restart = restart.read()
        with open(messagesFilename, 'r') as messagesFile:
            messages = json.loads(messagesFile.read())
        messages = getFacebookMessages(restart, None) + messages
        with open(messagesFilename, 'w') as messagesFile:
            messagesFile.write(json.dumps(messages))
    elif options.start:
        with open(options.start, 'r') as start:
            start = start.read()
        messages = getFacebookMessages(start, accessToken)
        with open(messagesFilename, 'w') as messagesFile:
            messagesFile.write(json.dumps(messages))
    else:
        data = getFacebookMessages('https://graph.facebook.com/159341617595013/comments', accessToken)
        with open(messagesFilename, 'w') as output:
            output.write(json.dumps(data))
