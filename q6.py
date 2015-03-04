import urllib
import httplib
import json
import datetime, time
import ast

f = open('tweets.txt','r')
tweets = []
i = 0
for line in f:
    tweets.append(ast.literal_eval(line))
    postingdate = datetime.datetime.fromtimestamp(tweets[i]['firstpost_date'])
    print 'Posting Date: ' + postingdate.__str__() 	
    print 'Tweet Text: ' + tweets[i]['tweet']['text']
    print 'Number of Retweets: ' + str(tweets[i]['metrics']['citations']['total'])
    print 'User: ' + tweets[i]['tweet']['user']['name']
    print '\n'
    i = i+1

f.close()
