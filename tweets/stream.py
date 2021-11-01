import datetime
import os
import pika
from pika import channel
import tweepy
from tweepy import StreamListener

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET_KEY"]
consumer_key = os.environ["CONSUMER_KEY"]
consumer_token = os.environ["CONSUMER_SECRET"]

'''
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost'
    )
)
'''

class MyStreamListener(StreamListener):
    def __init__(self) -> None:
        super().__init__()
    
    def on_status(self,status):
        print(status)
    
    def on_error(self,status_code):
        print(status_code)



#channel = connection.channel()
#channel.queue_declare(queue="tweeter")

auth = tweepy.OAuthHandler(consumer_key,consumer_token)
auth.set_access_token(api_key,api_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True, compression=True)

stream_listener =  MyStreamListener()
stream = tweepy.Stream(auth=api.auth,listener=stream_listener)
stream.filter(track=['python'],languages=['en'])

