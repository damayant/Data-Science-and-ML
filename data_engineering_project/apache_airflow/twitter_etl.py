import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs
import requests
from requests_oauthlib import OAuth1Session


consumer_key =  "1725511661761503232-f0M1lEVrdMGQNrKwJb1gUWeLYcbuwZ"
consumer_secret = "G93tCjMDIx8fmfOf3jUFlFbUD5KxCuslw7VPZigHcoHml"
access_key = "qW8v4yCbl5GEbHguEEJZR1VfI"
access_secret  = "0IAIXEQvrPVdpdvb0SDdcR2uRHRgmef5hKImdJDUfd1dQgjWTZ"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAC5IrAEAAAAATIoftZRLKOYiPLYj66bkk%2FcJZyk%3DEgXsoOiSiXE5a0kpBS5sTwSnirPyeBLy3paILspTvCbSug1yFd"





#Twitter authentication
auth = tweepy.OAuthHandler(access_key,access_secret)
auth.set_access_token(consumer_key,consumer_secret)

print(auth)


#Creating an api object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('authentication is correct')
except:
    print('error during suthentication')

# print(api)
username = 'elonmusk'
url = 'https://api.twitter.com/2/usage/tweets'
url_1 = 'https://api.twitter.com/1.1/statuses/home_timeline.json'

headers={'Authorization':'Bearer {}'.format(bearer_token), 'User-Agent':'v2UsageTweetsPython'}
# print(headers)
response = requests.request('GET',url,headers=headers)
print(response)

# tweets =  api.user_timeline(screen_name='@elonmusk',count=10,include_rts=False,tweet_mode = 'extended')

# print(tweets)