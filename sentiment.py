import tweepy #alows use to access the twitter api
from textblob import TextBlob # library for processing textual data

#accesing twitter developer app
consumer_key = '1T83eLPjQR5YSDRBOp0dqTkDQ'
consumer_secret =  'YIOng7bm2sR2nivpEcwjnICZquDcf1Fru9EqO0FzaSZxef7mRT'
access_token = '1345711940-QLWm1wNLCN0PiKPBT5PyjToVqNAUmdiCRIQCSZF'
access_token_secret = 's8oAAlfYAJEW5WUG9sNisywkGlTECI2byH2gDbFkt9jc2'

#authenticating the app
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#getting tweets and printing sentiment value
tweets = api.search('21 Savage')
for tweet in tweets: 
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('\n')


