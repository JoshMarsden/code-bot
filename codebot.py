"""

URL: http://geekswipe.net/2014/10/code-python-twitter-bot-in-ten-minutes/
Author: Karthikeyan KC
Name: Funzoned Twitter Bot
Description: A Twitter bot that tweets one liners every fifteen minutes.
Comment: This bot is created for learning purposes and is full of 'novice' bugs. It might evolve soon. The process runs on my laptop from a terminal and it will be on and off at times.
Twitter: http://twitter.com/funzoned
Bitbucket: https://bitbucket.org/karthikeyankc/funzoned-twitter-bot/src/

Modified by: Joshua Marsden
Modifications: Created another python file to hide credentials from GitHub

"""

from twython import Twython, TwythonError
import time
import credentials as creds


twitter = Twython(creds.APP_KEY,
                  creds.APP_SECRET,
                  creds.OAUTH_TOKEN,
                  creds.OAUTH_TOKEN_SECRET)

try:
	with open('samples.txt', 'r+') as tweetfile:
		buff = tweetfile.readlines()

	for line in buff[:]:
		line = line.strip(r'\n')
		if len(line)<=140 and len(line)>0:
			print ("Tweeting...")
			twitter.update_status(status=line)
			with open ('samples.txt', 'w') as tweetfile:
				buff.remove(line)
				tweetfile.writelines(buff)
			#time.sleep(900)
			time.sleep(300)
		else:
			with open ('samples.txt', 'w') as tweetfile:
				buff.remove(line)
				tweetfile.writelines(buff)
			print ("Skipped line - Char length violation")
			continue
	print ("No more lines to tweet...")


except TwythonError as e:
	print (e)
