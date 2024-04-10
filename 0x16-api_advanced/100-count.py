#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursive function to count the occurrences of given keywords in the titles of hot articles for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.
    word_list (list): A list of keywords to count occurrences.
    after (str): A token used for pagination to get the next page of results. Default is None.
    word_count (dict): A dictionary to store the count of each keyword. Default is an empty dictionary.

    Returns:
    None
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
            
            # Counting occurrences of keywords in titles
            for post in posts:
                title = post.get('data', {}).get('title', '').lower()
                for word in word_list:
                    if ' ' + word.lower() + ' ' in title:
                        if word.lower() in word_count:
                            word_count[word.lower()] += 1
                        else:
                            word_count[word.lower()] = 1
            
            # Recursively calling the function for pagination
            after = data.get('data', {}).get('after')
            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                # Sorting and printing the results
                sorted_results = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_results:
                    print(f"{word}: {count}")
        else:
            # If the subreddit is invalid or any other error occurs, print nothing
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# Example usage:
subreddit = "learnpython"
word_list = ["python", "java", "javascript"]
print(f"Keyword counts in r/{subreddit}:")
count_words(subreddit, word_list)
