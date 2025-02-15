#!/usr/bin/python3

import os
import json
import requests

# Get GitHub username from environment variable
GHUSER = os.getenv('GITHUB_USER')

# Construct API URL
url = 'https://api.github.com/users/{0}/events'.format(GHUSER)

# Fetch GitHub events
response = requests.get(url)

# Parse JSON response
if response.status_code == 200:
    events = json.loads(response.text)
    print("Recent GitHub Events for:", GHUSER)
    for event in events[:5]:  # Print first 5 events
        print(event['type'], "::", event['repo']['name'])
else:
    print("Failed to fetch events. Status Code:", response.status_code)

