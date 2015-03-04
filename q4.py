import urllib
import httplib
import json
import datetime, time
import ast
import numpy as np
import matplotlib.pyplot as plt
import math

f = open('tweets.txt','r')
tweets = []
i = 0
dictCount = dict()
tweetIds = []
UniqueTweetIndex = []

for line in f:    
    tweets.append(ast.literal_eval(line))
    tid = tweets[i]['tweet']['id']
    if tid in tweetIds:
       pass  
    else:
        tweetIds.append(tid)
        UniqueTweetIndex.append(i)
        count = tweets[i]['metrics']['citations']['total']
        if count in dictCount:
            dictCount[count] = dictCount[count] + 1
        else:    
            dictCount[count] = 1
    i = i+1

k = dictCount.keys()
maxK = max(k)
xVals = range(1,maxK+1)
yVals = []
for x in xVals:
    if x in dictCount:
        yVals.append(dictCount[x])
    else:
        yVals.append(0)

#xVals has all the k's, even the ones for which there are no retweets
#newK are only the k's for which there are retweets, except 0

newK = k[1:]
newY = []
for x in newK:
    newY.append(dictCount[x])

#xv_ are the logs of newK
#yv_ are the logs of the number of tweets with newK retweets
xv_ = map(lambda x: math.log(x), newK)
yv_ = map(lambda x: math.log(x) if x!=0 else x, newY)


###Just to remove all the newK for which the corresponding newY are 1 or log(newY) = 0###
###This is just to see how much is the linear relation affected by the 0 values###
xv = list(xv_)
yv = list(yv_)
zr = []
for i in range(0,yv.__len__()):
    if yv[i] == 0:
        zr.append(i)

zr.reverse()
for x in zr: yv.pop(x)

for x in zr: xv.pop(x)


#xv = map(lambda x: math.log(x), xVals)
#yv = map(lambda x: math.log(x) if x!=0 else x, yVals)
plt.plot(xv,yv,'ro')
plt.show()

p = np.polyfit(xv,yv,1)
plt.plot(xv,yv,'ro')
plt.plot(xv,np.polyval(p,xv),'r-')
plt.show()

plt.plot(xv_,yv_,'ro')
plt.show()

p = np.polyfit(xv_,yv_,1)
plt.plot(xv_,yv_,'ro')
plt.plot(xv_,np.polyval(p,xv_),'r-')
plt.show()

plt.plot(xVals,yVals,'ro')
plt.ylim(-50,max(yVals)+100)
plt.show()
plt.plot(xVals,yVals,'ro')
plt.ylim(-5,50)
plt.show()

plt.plot(newK,newY,'ro')
plt.ylim(-50,max(newY)+100)
plt.show()

p = np.polyfit(newK,newY,1)
plt.plot(newK,newY,'ro')
plt.plot(newK,np.polyval(p,newK),'r-')
plt.show()

plt.plot(newK,newY,'ro')
plt.ylim(-5,50)
plt.show()

f.close()
