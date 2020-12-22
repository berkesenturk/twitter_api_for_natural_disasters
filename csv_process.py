import pandas as pd



def csv_process(csv_name):

    csv_example=pd.read_csv(csv_name, sep=" ", header=None)
    result=csv_example.drop(columns=['user_created_at','favorite_count','media','in_reply_to_screen_name','user_description','place','possibly_sensitive',
                        'in_reply_to_status_id','id','retweet_count','retweet_id','retweet_screen_name','source','user_default_profile_image',
                        'user_description','user_screen_name.1','user_listed_count','user_location','user_time_zone',
                        'tweet_url','user_screen_name','user_statuses_count','user_verified','user_urls','user_screen_name','user_name','lang','urls',
                        'user_followers_count','user_friends_count','user_favourites_count'])  
    result.to_csv("result.csv")

    print("Columns are cleaned")
     

csv_process(csv_name='hydrate_ex.txt')

   
