import urllib
import httplib
import json
import datetime, time
import codecs

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv

#########   create UNIX timestamps
start_date = datetime.datetime(2015,02,01, 18,50,0)
end_date = datetime.datetime(2015,02,01, 20,00,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))

API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
host = 'api.topsy.com'
url = '/v2/content/tweets.json'

hashtag = raw_input('Hashtag: ')
lim = int(raw_input('Limit: '))

#hashtag = '#SuperBowl'
#lim = 500

#########   set query parameters
params = urllib.urlencode({'apikey' : API_KEY, 'q' :hashtag,
                           'mintime': str(mintime), 'maxtime': str(maxtime),
                           'new_only': '1', 'include_metrics':'1', 'limit': lim})

#########   create and send HTTP request
req_url = url + '?' + params
req = httplib.HTTPConnection(host)
req.putrequest("GET", req_url)
req.putheader("Host", host)
req.endheaders()
req.send('')


#########   get response and print out status
resp = req.getresponse()
print resp.status, resp.reason


#########   extract tweets
resp_content = resp.read()
ret = json.loads(resp_content,object_hook=_decode_dict)
tweets = ret['response']['results']['list']

f = open('top_tweets.txt','w')
for i in range(0,5):
	f.write(repr(tweets[i])+'\n')
	print 'Tweet Text: ' + tweets[i]['tweet']['text']
	print 'User: ' + tweets[i]['tweet']['user']['name']
	postingdate = datetime.datetime.fromtimestamp(tweets[i]['firstpost_date'])
	print 'Posting Date: ' + postingdate.__str__() 
	print '\n'
f.close()
