#!/usr/bin/python3
"""
subs module
"""

import requests
import json


def number_of_subscribers(subreddit):
    """
    queries the Reddit API
    and returns the number of subscribers
    """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent': 'RimJoudi'}
    request = requests.get(url, headers=user_agent, allow_redirects=False)
    if request.status_code == 200:
        request = request.json()
        data = request.get('data')
        subscribers = data.get('subscribers')
        if data is not None and subscribers is not None:
            return subscribers
    return 0
