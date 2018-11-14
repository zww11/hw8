import unittest
import tweepy
import requests
import json

## SI 206 - HW
## COMMENT WITH:
## Any names of people you worked with on this assignment and what you did together

## Write code that uses the tweepy library to search for tweets with three different phrases of the
## user's choice (should use the Python input function), and prints out the Tweet text and the
## created_at value (note that this will be in GMT time) of the first FIVE tweets with at least
## 1 blank line in between each of them, e.g.

## You should cache all of the data from this exercise in a file, and submit the cache file
## along with your assignment.  So, for example, if you submit your assignment files, and you have
## already searched for tweets about "rock climbing", when we run your code, the code should use
## the CACHED data, and should not need to make any new request to the Twitter API.  But if,
## for instance, you have never searched for "bicycles" before you submitted your final files,
## then if we enter "bicycles" when we run your code, it _should_ make a request to the Twitter API.
## Because it is dependent on user input, there are no unit tests for this -- we will
## run your assignments in a batch to grade them!

##SAMPLE OUTPUT
## See: https://docs.google.com/a/umich.edu/document/d/1o8CWsdO2aRT7iUz9okiCHCVgU5x_FyZkabu2l9qwkf8/edit?usp=sharing

## **** Be sure to have twitter_info.py that contains your
## consumer_key, consumer_secret, access_token, and access_token_secret,
## in the same directory as this file.  Do NOT add and commit
## that file to your Github repo
import twitter_info

## Get your secret values to authenticate to Twitter.
consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret

## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Set up library to grab stuff from twitter with your authentication, and
# return it in a JSON-formatted way
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

## Write your code here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# string name of the file to save the cache to - must end in .json

#### Recommended order of tasks: ####
## 1. Try to read in the cache from the CACHE_FNAME file. If it doesn't exist
## set the CACHE_DICTION to an empty dictionary
## see cache_example.py for example code

## 2. Write a function to get twitter data that works with the caching pattern,
## 		so it either gets new data or caches data, depending upon what the input
##		to search for is.  See tweepy_example.py for example code that searches
##      for tweets with a given word or phrase

## 3. Loop three times.  Invoke your function.  Save the return value in a variable.

## 4. write code to print out the text and created_at values from 5 tweets,
## with a blank line after each as shown in the sample output
