# Data_Processing.py
# Author: Cheng XU
# Date created: 15/01/2023
# Last modified: 06/03/2023
# Github page for this code: https://github.com/chengxuphd/AROT-COV23
#
# Description: A Python script for converting tweets json data to csv format.
#
# Acknowledgments:
# - Parts of this code were adapted from the tutorial: 
#   https://towardsdatascience.com/an-extensive-guide-to-collecting-tweets-from-twitter-api-v2-for-academic-research-using-python-3-518fcb71df2a


import pandas as pd
import numpy as np
import json
import csv
import dateutil.parser
import tqdm


# Set the workspace path here
workspace = '/content/drive/MyDrive/'


tweets = []
for line in open(workspace + 'data.json', 'r'):
    tweets.append(json.loads(line))


def append_to_csv(json_response, fileName):

  #A counter variable
  counter = 0

  #Open OR create the target CSV file
  csvFile = open(fileName, "a", newline="", encoding='utf-8')
  csvWriter = csv.writer(csvFile)

  #Loop through each tweet
  for i in tqdm.tqdm(range(len(json_response))):

    for j in range(len(json_response[i]['data'])):
    
      # We will create a variable for each since some of the keys might not exist for some tweets
      # So we will account for that

      # 1. Author ID
      author_id = json_response[i]['data'][j]['author_id']

      # 2. Time created
      created_at = dateutil.parser.parse(json_response[i]['data'][j]['created_at'])

      # 3. Geolocation
      # if ('geo' in tweet):   
          # geo = tweet['geo']['place_id']
      # else:
          # geo = np.NaN

      # 4. Tweet ID
      tweet_id = json_response[i]['data'][j]['id']

      # 5. Language
      lang = json_response[i]['data'][j]['lang']

      # 6. Tweet metrics
      retweet_count = json_response[i]['data'][j]['public_metrics']['retweet_count']
      reply_count = json_response[i]['data'][j]['public_metrics']['reply_count']
      like_count = json_response[i]['data'][j]['public_metrics']['like_count']
      quote_count = json_response[i]['data'][j]['public_metrics']['quote_count']

      # 7. source
      # if ('source' in tweet):
        # source = tweet['source']
      # else:
        # source = np.NaN

      # 8. Tweet text
      text = json_response[i]['data'][j]['text']
      
      for k in range(len(json_response[i]['includes']['users'])):
        if json_response[i]['includes']['users'][k]['id'] == author_id:
          user_verified = json_response[i]['includes']['users'][k]['verified']
          followers_count = json_response[i]['includes']['users'][k]['public_metrics']['followers_count']
          following_count = json_response[i]['includes']['users'][k]['public_metrics']['following_count']
          tweet_count = json_response[i]['includes']['users'][k]['public_metrics']['tweet_count']
          listed_count = json_response[i]['includes']['users'][k]['public_metrics']['listed_count']
          name = json_response[i]['includes']['users'][k]['name']
          username = json_response[i]['includes']['users'][k]['username']
          user_created_at = json_response[i]['includes']['users'][k]['created_at']
          description = json_response[i]['includes']['users'][k]['description']
          break


      # Assemble all data in a list
      res = [tweet_id, author_id, created_at, lang, like_count, quote_count, reply_count, retweet_count, 
            text, user_verified, followers_count, following_count, tweet_count, listed_count, name,
            username, user_created_at, description
            ]
      
      # Append the result to the CSV file
      csvWriter.writerow(res)
      counter += 1

    

  # When done, close the CSV file
  csvFile.close()

  # Print the number of tweets for this iteration
  print("# of Tweets added from this response: ", counter) 


# Create file
csvFile = open(workspace + "Arabic_Tweets.csv", "w", newline="", encoding='utf-8')
csvWriter = csv.writer(csvFile)

#Create headers for the data you want to save, in this example, we only want save these columns in our dataset
csvWriter.writerow(['tweet id', 'author id', 'created_at', 'lang', 'like_count', 'quote_count', 'reply_count', 'retweet_count', 'tweet', 'user_verified', 'followers_count', 'following_count', 'tweet_count', 'listed_count', 'name',
           'username', 'user_created_at', 'description'])

csvFile.close()

append_to_csv(tweets, workspace + 'Arabic_Tweets.csv')