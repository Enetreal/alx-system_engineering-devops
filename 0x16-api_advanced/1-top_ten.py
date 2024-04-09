#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """
    Function to print the titles of the first 10 hot posts listed for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    None
    """
    
    # Reddit API URL for fetching hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # Making a GET request to fetch hot posts
        response = requests.get(url, headers=headers)
        
        # Checking if the response is successful (status code 200)
        if response.status_code == 200:
            # Parsing JSON response
            data = response.json()
            
            # Extracting posts information
            posts = data.get('data', {}).get('children', [])
            
            # Printing titles of the first 10 hot posts
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            # If the subreddit is invalid or any other error occurs, print None
            print(None)
    except Exception as e:
        print("An error occurred:", e)
        print(None)

# Example usage:
subreddit = "learnpython"
print(f"Top 10 hot posts in r/{subreddit}:")
top_ten(subreddit)
