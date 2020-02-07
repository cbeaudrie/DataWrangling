#%% TWITTER API
from __future__ import print_function
import tweepy

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

def get_config():
    # Return my config object
    config = ConfigParser()
    config.read('config/CB_production.cfg')
    return config

config = get_config()
config.sections() # Confirm config is read properly


# %%
# Create authentication handler

auth = tweepy.OAuthHandler(config.get('twitter', 'consumer_key'), config.get('twitter', 'consumer_secret'))
auth.set_access_token(config.get('twitter', 'access_token'), config.get('twitter', 'access_token_secret'))

#Create API endpoint
api = tweepy.API(auth)

# %%
#Search Twitter
python_tweets = api.search('Python')

for tweet in python_tweets:
    print(tweet.text)

# %%
