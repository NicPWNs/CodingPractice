#!/usr/bin/env python3
# Author: Nic Jones (NicPWNs)
# web-scraper.py

import requests

# Get target from user input and make request
target = str(input("Enter a URL to scrape: ") or "youtube.com")
# Add HTTP scheme if not present
if "http" not in target:
    target = "http://" + target

# Set headers for request
headers = {
    'User-Agent': 'NicPWNs Scraper 1.0',
}

# Make request
page = requests.get(target)