#!/usr/bin/env python

#By Alexandra Robin, this is the stupidest program I have ever written.

import urllib2, urllib
import re, os

pageURL = "http://icanhascheezburger.com/page/"
currentPage = 2 # there is no /page/1 :(
maximumPage = 3502
#maximumPage = 3

imageCount = 0

while currentPage < maximumPage:
	print "Page: " + str(currentPage) + " images so far: "+str(imageCount)
	
	# Grab the HTML	
	url = pageURL + str(currentPage)
	pageContent = urllib2.urlopen(url).read()
	
	#Parse it looking for the string <img class='event-item-lol-image' and grabbing src='blah'
	#<img class='event-item-lol-image' src='https://i.chzbgr.com/maxW500/6394246400/hEAEB10B8/' id='_r_a_6394246400'   width="500" height="398" alt="What &quot;Meow&quot; Means" title="What &quot;Meow&quot; Means" />
	imageURLList = re.findall("""<img class='event-item-lol-image' src=["'](.*?)["']""", pageContent, re.DOTALL)
	
	#Download the images to the current folder
	for i in range(0, len(imageURLList)):
		imageCount += 1
		#print imageURLList[i]
		tmpURL = imageURLList[i]
		#fileData = tmpURL.split('/')
		#fileName = "cat-"+str(imageCount)+"-"+fileData[4]+"-"+fileData[5]+".jpg"
		fileName = "cat-"+str(imageCount)+".jpg"
		print fileName
		try:
			urllib.urlretrieve(tmpURL, fileName)
		except:
			print "Failed to get "+tmpURL

	currentPage += 1
