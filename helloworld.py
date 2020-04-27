#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time
import sys

argfile = str(sys.argv[1])

# enter the corresponding information from your Twitter application:
# keep the quotes, replace this with your consumer key
CONSUMER_KEY = ''
# keep the quotes, replace this with your consumer secret key
CONSUMER_SECRET = ''
# keep the quotes, replace this with your access token
ACCESS_KEY = ''
# keep the quotes, replace this with your access token secret
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(180)  # Tweet every 15 minutes
