# %%
""" Simple tweepy stream listener for twitter API. """
from __future__ import print_function
import tweepy
import time

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

myFilename = 'fetched_tweets.txt'

# %%
#Authenticate
def get_config():
    """ Return my config object. """
    conf = ConfigParser()
    conf.read('config/CB_production.cfg')
    return conf

config = get_config()
auth = tweepy.OAuthHandler(config.get('twitter', 'consumer_key'),
                           config.get('twitter', 'consumer_secret'))

auth.set_access_token(config.get('twitter', 'access_token'),
                      config.get('twitter', 'access_token_secret'))

# %%
#Define PythonListener and get_config function
class PythonListener(tweepy.StreamListener):
    """ Very simple tweepy stream listener. """
    # def on_status(self, tweet):
    #     print(tweet.text)

    def on_data(self, data):
        try:
            print('\n Printing data...\n ')
            print(data)
            # with open(myFilename, 'a') as tf:
            #     tf.write(data)
            saveFile = open(myFilename, 'a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except(BaseException, e):
            print('failed on_data, ', str(e))
            time.sleep(5)

    def on_error(self, msg):
        print('Error: %s', msg)
        if msg == 420:
            #returning False in on_error disconnects the stream
            return False

    def on_timeout(self):
        print('tweepy timeout. waiting before next poll')
        sleep(30)

# %%
#Create listener and stream from Twitter
my_listener = PythonListener()

my_stream = tweepy.Stream(auth = auth, listener=my_listener)
my_stream.filter(track=['#python', 'python'], is_async=True)

setTime = 60

print('** Will disconnect in ', setTime, ' seconds ** \n')
time.sleep(setTime) # Python will sleep while streaming

print('\n** Disconnecting **')

my_stream.disconnect() # Disconnect the stream

# Should do something like this:
# myFile = open('testDoc.txt', 'a')
# myFile.write('\n Something to add to the file...')
# myFile.close()

# %%
