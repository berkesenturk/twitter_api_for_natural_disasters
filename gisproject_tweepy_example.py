import tweepy
def home_timeline():
    """
    -----------
    Description
    -----------

    Gathers the home stream of the current time 
    """
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

if __name__ == "__main__":
    
    twitter_api_credential_kwargs={
                        "api_key":"ouCXfxtlieyI1LinIGYaM7kzo",
                        "api_secret_key":"SdmMWT5px27PlpQP7DPkT812xH51M97qiaWAWwVVXliYVM5Yog",
                        "bearer_token":"AAAAAAAAAAAAAAAAAAAAAAxNKQEAAAAA%2B1ilngVTZTf6cutmuKqOGf0OyWs%3DkhySUrBcn11XYtW8stKpgNkroJVKX6ECpO2B06UZtux71g1qjv",
                        "access_token":"946198081-Tm5YDvPNKOxU0uuf6OHv6pl9cwkFUojDXcDSkppL",
                        "access_token_secret":"fUx8Xkr2WERJTA5BaBzZ1KanwQvLs7CvgdpLjj1t5qEtd"                        
                        }


    #credentials
    consumer_key=twitter_api_credential_kwargs["api_key"]
    consumer_secret=twitter_api_credential_kwargs["api_secret_key"]
    access_token=twitter_api_credential_kwargs["access_token"]
    access_token_secret=twitter_api_credential_kwargs["access_token_secret"]

    #authorization
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    home_timeline()







    