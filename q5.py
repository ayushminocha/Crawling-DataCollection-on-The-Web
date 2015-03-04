import urllib
import httplib
import json
import datetime, time
import matplotlib.pyplot as plt

API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
host = 'api.topsy.com'
url = '/v2/content/tweets.json'

#hashtags = ['#SuperBowl','#NFL','#DeflateGate','#DeflatedBalls','#SNL','#Colts']
hashtags = ['#SuperBowl','#NFL']
tweetsPs = []
tweetsPs.append([])
tweetsPs.append([])
#total = [0] * hashtags.__len__()
#f = open('tweets.txt','w')
#sLog = open('search_log.txt','w')

for i in range(0,hashtags.__len__()):

        startHr = 18
        startMin = 50
        startSec = 0
        endHr = 18
        endMin = 50
        endSec = 0
        timeStep = 10
        revert = 0

        while endHr != 20:
            if revert == 0:
                timeStep = 1
            endSec = endSec+timeStep
            if endSec >= 60:
                endSec = endSec-60
                endMin = endMin+1
                if endMin >= 60:
                    endMin = endMin-60
                    endHr = endHr+1
            
            #########   create UNIX timestamps
            start_date = datetime.datetime(2015,02,01, startHr,startMin,startSec)
            end_date = datetime.datetime(2015,02,01, endHr,endMin,endSec)
            mintime = int(time.mktime(start_date.timetuple()))
            maxtime = int(time.mktime(end_date.timetuple()))

            #########   set query parameters
            params = urllib.urlencode({'apikey' : API_KEY, 'q' :hashtags[i],
                    'mintime': str(mintime), 'maxtime': str(maxtime),
                    'new_only': '1', 'include_metrics':'1', 'limit': 500})



            #########   create and send HTTP request
            req_url = url + '?' + params
            req = httplib.HTTPConnection(host)
            req.putrequest("GET", req_url)
            req.putheader("Host", host)
            req.endheaders()
            req.send('')


            #########   get response and print out status
            resp = req.getresponse()
            #print resp.status, resp.reason


            #########   extract tweets
            resp_content = resp.read()
            ret = json.loads(resp_content)
            tweets = ret['response']['results']['list']
            if tweets.__len__() >= 500:
                print hashtags[i]
                print str(startHr) + ':' + str(startMin) + ':' + str(startSec)               
                print str(endHr) + ':' + str(endMin) + ':' + str(endSec) + '\n' 
                endHr = startHr
                endMin = startMin
                endSec = startSec
                if timeStep == 10:
                    timeStep = 5
                    revert = 2
                elif timeStep == 5:
                    timeStep = 1
                    revert = 5
                continue

            tweetsPs[i].append(tweets.__len__())
            
            startHr = endHr
            startMin = endMin
            startSec = endSec

xVals = tweetsPs[0][:]
yVals = tweetsPs[1][:]
plt.plot(xVals,yVals,'ro')
plt.show()
#print tweetsPs.__len__()
