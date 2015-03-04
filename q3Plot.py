import numpy as np
import matplotlib.pyplot as plt

N = 6

##Values obtained from the output of the second part
number_of_tweets = (108411, 11659, 4255, 349, 64, 122)

ind = np.arange(N)  # the x locations for the groups
width = 0.75       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, number_of_tweets, width, color='#FF6666')

xlabels = ['','','','','','']

# add some text for labels, title and axes ticks
plt.ylabel('Number of tweets')
plt.xlabel('Hashtags')
plt.title('Number of tweets per Hashtag')
plt.xticks(ind+width/2.,xlabels)

name = ['#SuperBowl', '#NFL', '#DeflateGate', '#DeflatedBalls', '#SNL', '#Colts']

plt.yscale("symlog")

##Function to add text in the bar of the graph
def autolabel(rects):
    for ii,rect in enumerate(rects):
        height = rect.get_height()
        #height = 1
        plt.text(rect.get_x()+rect.get_width()/2., 1, '%s'% (name[ii]),ha='center', va='bottom',rotation='vertical')
        plt.text(rect.get_x()+rect.get_width()/2., 1.2*height, '%d'% (int(height)),ha='center', va='bottom')

autolabel(rects1)

plt.show()
