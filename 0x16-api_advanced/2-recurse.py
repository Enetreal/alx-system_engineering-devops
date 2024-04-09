#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to retrieve the titles of all hot articles for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.
    hot_list (list): A list to store the titles of hot articles. Default is an empty list.
    after (str): A token used for pagination to get the next page of results. Default is None.

    Returns:
    list or None: A list containing the titles of all hot articles for the given subreddit,
                  or None if no results are found or the subreddit is invalid.
    """
    # Reddit API URL for fetching hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    
    # Custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # Parameters for pagination
        params = {'after': after} if after else {}

        # Making a GET request to fetch hot posts
        response = requests.get(url, headers=headers, params=params)
        
        # Checking if the response is successful (status code 200)
        if response.status_code == 200:
            # Parsing JSON response
            data = response.json()
            
            # Extracting posts information
            posts = data.get('data', {}).get('children', [])
            
            # Adding titles of the hot posts to the hot_list
            for post in posts:
                hot_list.append(post.get('data', {}).get('title'))
            
            # Recursively calling the function for pagination
            after = data.get('data', {}).get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list if hot_list else None
        else:
            # If the subreddit is invalid or any other error occurs, return None
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# Example usage:
subreddit = "learnpython"
print(f"All hot articles in r/{subreddit}:")
print(recurse(subreddit))

