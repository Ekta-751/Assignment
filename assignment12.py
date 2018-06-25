#Short note on Access Token and Write your own Access Token.
#anuswer:
# print("An access_token is a unique string of letters and numbers that you pass with every API call, so WePay knows you are authorized to make that call.
       # Each access_token is associated with:
       # Your API application.
       # The user you are acting on behalf of (for merchants, this is yourself).
       # The permissions your app has for that user.
       # If you include an access_token in an API call, we automatically know the API application and the WePay user for whom the call is being made.
       # The access token should be passed in the ‘Authorization’ HTTP request header. It should look like this:
       # Authorization: Bearer <access-token>
      # (Just make sure to replace <access-token> with the appropriate access_token.)")

#Get IP Address Of some Websites google and facebook.
#google
# $ nslookup google.com
# Non-authoritative answer:
# Server:  google-public-dns-a.google.com
# Address:  8.8.8.8

# Name:    google.com
# Addresses:  2404:6800:4002:803::200e
          # 172.217.24.238
#facebook
# $ nslookup facebook.com
# Non-authoritative answer:
# Server:  google-public-dns-a.google.com
# Address:  8.8.8.8

# Name:    facebook.com
# Addresses:  2a03:2880:f10c:283:face:b00c:0:25de
          # 157.240.13.35

#Extract Tweets By the help Of Tweepy Library.
import tweepy
consumer_key='#'
cosumer_secret='#'
access_token='#'
access_token_secret='#'
auth=tweepy.OAuthHandler(consumer_key,cosumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweets=api.search('#Coding',lang="en",count=5,tweet_mode="extended")
#print(tweets)
for tweet in tweets:
     print("--------------")
     print(tweet.full_text)
     print("--------------")

#Difference between Library and API.
# library:A library is a collection of functions / objects that serves one particular purpose.
# you could use a library in a variety of projects. (Various specialized services in our case)
# API:An API is an interface for other programs to interact with your program or library  without having direct access. 
# ( giving specifications for our need to various vendors in our case)
# API is a part of library which defines how an application communicates with external code
# .API can be written in any language.
# Library is written in same language which is a collection of all the functionalities required for the use case.
# For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, 
# along with a large collection of high-level mathematical functions to operate on these arrays.
