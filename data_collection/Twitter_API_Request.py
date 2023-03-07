# Twitter_API_Request.py
# Author: Cheng XU
# Date created: 15/01/2023
# Last modified: 06/03/2023
# Github page for this code: https://github.com/chengxuphd/AROT-COV23
#
# Description: A Python script for accessing the Twitter API to collect data.
#
# Acknowledgments:
# - Parts of this code were adapted from the tutorial: 
#   https://towardsdatascience.com/an-extensive-guide-to-collecting-tweets-from-twitter-api-v2-for-academic-research-using-python-3-518fcb71df2a


# For sending GET requests from the API
import requests
# For saving access tokens and for file management when creating and adding to the dataset
import os
# For dealing with json responses we receive from the API
import json
#To add wait time between requests
import time

# Set the workspace path here
workspace = '/content/drive/MyDrive/'

# Replace 'NaN' to your Twitter API token
os.environ['TOKEN'] = 'NaN'

def auth():
    return os.getenv('TOKEN')

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, start_date, end_date, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/all" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)


def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def add_data(json_response, file):
  with open(workspace + file, 'a') as f:
    json.dump(json_response, f)
    f.write('\n')


#Inputs for the request
bearer_token = auth()
headers = create_headers(bearer_token)
keyword = "(COVID-19 OR مرض فيروس كورونا OR فيروس كوفيد) lang:ar -is:nullcast -is:retweet -is:reply"


# Set the time range for data collection

# start_time = "2019-12-01T00:00:00.000Z"
# end_time = "2023-01-01T00:00:00.000Z"

start_list = [
        # '2019-01-01T00:00:00.000Z',
        # '2020-01-01T00:00:00.000Z',
        # '2020-02-01T00:00:00.000Z',
        # '2020-03-01T00:00:00.000Z',
        # '2020-04-01T00:00:00.000Z',
        # '2020-05-01T00:00:00.000Z',
        # '2020-06-01T00:00:00.000Z',
        # '2020-07-01T00:00:00.000Z',
        # '2020-08-01T00:00:00.000Z',
        # '2020-09-01T00:00:00.000Z',
        # '2020-10-01T00:00:00.000Z',
        # '2020-11-01T00:00:00.000Z',
        # '2020-12-01T00:00:00.000Z',
        # '2021-01-01T00:00:00.000Z',
        # '2021-02-01T00:00:00.000Z',
        # '2021-03-01T00:00:00.000Z',
        # '2021-04-01T00:00:00.000Z',
        # '2021-05-01T00:00:00.000Z',
        # '2021-06-01T00:00:00.000Z',
        # '2021-07-01T00:00:00.000Z',
        # '2021-08-01T00:00:00.000Z',
        # '2021-09-01T00:00:00.000Z',
        # '2021-10-01T00:00:00.000Z',
        # '2021-11-01T00:00:00.000Z',
        # '2021-12-01T00:00:00.000Z',
        # '2022-01-01T00:00:00.000Z',
        # '2022-02-01T00:00:00.000Z',
        # '2022-03-01T00:00:00.000Z',
        # '2022-04-01T00:00:00.000Z',
        # '2022-05-01T00:00:00.000Z',
        # '2022-06-01T00:00:00.000Z',
        # '2022-07-01T00:00:00.000Z',
        # '2022-08-01T00:00:00.000Z',
        # '2022-09-01T00:00:00.000Z',
        # '2022-10-01T00:00:00.000Z',
        # '2022-11-01T00:00:00.000Z',
        # '2022-12-01T00:00:00.000Z',
        # '2023-01-01T00:00:00.000Z',
        ]
        
end_list =  [
        # '2019-12-31T00:00:00.000Z',
        # '2020-01-31T00:00:00.000Z',
        # '2020-02-29T00:00:00.000Z',
        # '2020-03-31T00:00:00.000Z',
        # '2020-04-30T00:00:00.000Z',
        # '2020-05-31T00:00:00.000Z',
        # '2020-06-30T00:00:00.000Z',
        # '2020-07-31T00:00:00.000Z',
        # '2020-08-31T00:00:00.000Z',
        # '2020-09-30T00:00:00.000Z',
        # '2020-10-31T00:00:00.000Z',
        # '2020-11-30T00:00:00.000Z',
        # '2020-12-31T00:00:00.000Z',
        # '2021-01-31T00:00:00.000Z',
        # '2021-02-28T00:00:00.000Z',
        # '2021-03-31T00:00:00.000Z',
        # '2021-04-30T00:00:00.000Z',
        # '2021-05-31T00:00:00.000Z',
        # '2021-06-30T00:00:00.000Z',
        # '2021-07-31T00:00:00.000Z',
        # '2021-08-31T00:00:00.000Z',
        # '2021-09-30T00:00:00.000Z',
        # '2021-10-31T00:00:00.000Z',
        # '2021-11-30T00:00:00.000Z',
        # '2021-12-31T00:00:00.000Z',
        # '2022-01-31T00:00:00.000Z',
        # '2022-02-28T00:00:00.000Z',
        # '2022-03-31T00:00:00.000Z',
        # '2022-04-30T00:00:00.000Z',
        # '2022-05-31T00:00:00.000Z',
        # '2022-06-30T00:00:00.000Z',
        # '2022-07-31T00:00:00.000Z',
        # '2022-08-31T00:00:00.000Z',
        # '2022-09-30T00:00:00.000Z',
        # '2022-10-31T00:00:00.000Z',
        # '2022-11-30T00:00:00.000Z',
        # '2022-12-31T00:00:00.000Z',
        # '2023-01-07T00:00:00.000Z',
        ]


# Total number of tweets we collected from the loop
total_tweets = 0

# The maximum number of tweets per request
max_results = 500


for i in range(0,len(start_list)):

    # Inputs
    count = 0 # Counting tweets per time period
    max_count = 99999999 # Max tweets per time period
    flag = True
    next_token = None
    
    # Check if flag is true
    while flag:
        # Check if max_count reached
        if count >= max_count:
            break
        print("-------------------")
        print("Token: ", next_token)
        url = create_url(keyword, start_list[i],end_list[i], max_results)
        json_response = connect_to_endpoint(url[0], headers, url[1], next_token)
        result_count = json_response['meta']['result_count']

        if 'next_token' in json_response['meta']:
            # Save the token to use for next call
            next_token = json_response['meta']['next_token']
            print("Next Token: ", next_token)
            if result_count is not None and result_count > 0 and next_token is not None:
                print("Start Date: ", start_list[i])
                add_data(json_response, "data.json")
                count += result_count
                total_tweets += result_count
                print("Total # of Tweets added: ", total_tweets)
                print("-------------------")
                time.sleep(3)                
        # If no next token exists
        else:
            if result_count is not None and result_count > 0:
                print("-------------------")
                print("Start Date: ", start_list[i])
                add_data(json_response, "data.json")
                count += result_count
                total_tweets += result_count
                print("Total # of Tweets added: ", total_tweets)
                print("-------------------")
                time.sleep(3)
            
            #Since this is the final request, turn flag to false to move to the next time period.
            flag = False
            next_token = None
        time.sleep(3)
print("Total number of results: ", total_tweets)