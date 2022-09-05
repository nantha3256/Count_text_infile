"""
==============
Twitter authentication file
==============

This file to authenticate twitter account and web scraping from twitter.

Reference:
`


"""
import twitter
from twitter import Twitter,OAuth
import json



twitter = Twitter(auth=OAuth(token='_______________________________________________',
                             token_secret='_____________________________________________',
                             consumer_key='_________________________',
                             consumer_secret='__________________________________________________')
                  )

def get_tweet_from_id():
    return print(twitter.statuses.home_timeline())
def get_search():
    return (twitter.search.tweets(q='arsenal'))

def saved_file():
    saved_file = 'save_1.json'
    with open (saved_file,'w') as f:
        return json.dump(get_search(),f)
saved_file()
