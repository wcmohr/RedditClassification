import pandas as pd
import requests

def get_reddit_submissions(subreddits: list, max_num: int):
    base_url = "https://api.pushshift.io/reddit/search/submission"
    all_posts = []
    
    for subreddit in subreddits:
        params = {
            'subreddit': subreddit,
            'size': 1000 #doesn't appear to be working
        }
        
        count = 0 #keep track of posts/subreddit
        
        while count < max_num:
            res = requests.get(base_url, params)
            
            if res.status_code == 200:
                posts = pd.DataFrame(res.json()['data'])
                count += len(posts)
                
                all_posts.append(posts)
                
                if len(posts) == 0: 
                    break #break loop if request successful but nothing retrieved
                    
                #get sequential posts from most recent to least    
                params['before'] = posts['created_utc'].min()
            else:
                print(f'status: {res.status_code}')
        print(f'scraped from {subreddit}: {count}')
    
    return pd.concat(all_posts)