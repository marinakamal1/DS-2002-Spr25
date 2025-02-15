import requests

url = "https://api.github.com/events"
response = requests.get(url)

if response.status_code == 200:
    print("GitHub Events:")
    print(response.json()[:5])  # Print the first 5 events
else:
    print("Failed to retrieve events")

