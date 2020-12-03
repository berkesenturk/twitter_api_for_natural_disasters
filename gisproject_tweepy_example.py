import tweepy

twitter_api_credential_kwargs={
                        "api_key":"ouCXfxtlieyI1LinIGYaM7kzo",
                        "api_secret_key":"SdmMWT5px27PlpQP7DPkT812xH51M97qiaWAWwVVXliYVM5Yog",
                        "bearer_token":"AAAAAAAAAAAAAAAAAAAAAAxNKQEAAAAA%2B1ilngVTZTf6cutmuKqOGf0OyWs%3DkhySUrBcn11XYtW8stKpgNkroJVKX6ECpO2B06UZtux71g1qjv"
                        }
consumer_key=twitter_api_credential_kwargs["api_key"]
consumer_secret=twitter_api_credential_kwargs["api_secret_key"]
access_token=


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)






    