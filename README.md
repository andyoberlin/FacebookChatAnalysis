FacebookChatAnalysis
====================

There are three scripts here to allow for nice error handling in the Facebook APIs. After about
7000+ messages you will get throttled. So breaking this up into the scripts was the bets idea.


Script One -- fetchMessages.py
---------------------------------------
This creates a json file filled with all the messages it can find by paginating backward form the
start of the conversation. To use this do the following:

Go here: https://developers.facebook.com/tools/explorer/?method=GET&path=me%2Finbox&version=v2.0
Click the "Get User Access Token" option under the "Get Access Token" dropdown
Request "read_malibox" permissions under "Extended Permissions"
Copy the access token from the input and put it in the access_token.dat file
On the same site, grab the conversation id of the conversation you are interested in

Run the script:

python fetchMessages.py -m <name of json file to write> -c <conversation id>

This script will likely say something about "being throttled" and output a restart.dat file
Repeat above process to get a new access token
Edit the restart.dat file by removing the "access_token" query parameter
Add "&access_token=<new access token>" to the end of the file

Run the script:

python fetchMessages.py -m <same name of json file as before> -r restart.dat

Repeat until all messages are downloaded.


Script Two -- createMessagesDB.py
----------------------------------------
Run the script: python createMessagesDB.py -d <name of database to create>.db -m <json file from before>



Script Three -- analyzeMessages.py
----------------------------------------
Run the script: python analyzeMessages.py -d <name of database>.db

Profit!
