#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Function to get the number of subscribers for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers if the subreddit is valid, otherwise 0.
    """

    # Reddit API URL for fetching subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # Making a GET request to fetch subreddit information
        response = requests.get(url, headers=headers)

        # Checking if the response is successful (status code 200)
        if response.status_code == 200:
            # Parsing JSON response
            data = response.json()

            # Extracting number of subscribers from the JSON response
            subscribers_count = data['data']['subscribers']
            return subscribers_count
        else:
            # If the subreddit is invalid or any other error occurs, return 0
            return 0
    except Exception as e:
        print("An error occurred:", e)
        return 0

# Example usage:
subreddit = "learnpython"
print(f"The number of subscribers in r/{subreddit}: {number_of_subscribers(subreddit)}")
