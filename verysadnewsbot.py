import feedparser
import requests
from time import sleep

discord_webhook_url = "" #put ur discord webhook url here
feed = feedparser.parse("https://www.reddit.com/r/news/.rss") # put rss feed here

def sendMessage(webhook_url, message):
    requests.post(webhook_url, data=message)


for i in range(0, len(feed.entries)-1):
    thing_to_say = {"content": "guys i cant believe " + feed.entries[i].title + "😭😭😭2021 is such a bad year😭😭😭😭😭😭😭😭"} #message goes here
    sendMessage(discord_webhook_url, thing_to_say)
    sleep(300)
