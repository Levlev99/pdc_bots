import requests
from bs4 import BeautifulSoup
import re

# URL to scrape
url = "https://hertie-scraping-website.vercel.app/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all visible flags in text (matching "flag-[number]")
flags = soup.find_all(text=re.compile(r'flag-\d+'))

# Also, find flags embedded in HTML attributes (id and class attributes)
flags += soup.find_all(id=re.compile(r'flag-\d+'))
flags += soup.find_all(class_=re.compile(r'flag-\d+'))

# Clean up and store unique flags in a set to remove duplicates
unique_flags = set()

# Extract flags from text and attributes
for item in flags:
    if isinstance(item, str):
        unique_flags.add(item.strip())
    else:
        # Check and add flags from 'id' attributes
        if 'id' in item.attrs and re.match(r'flag-\d+', item['id']):
            unique_flags.add(item['id'])
        # Check and add flags from 'class' attributes
        if 'class' in item.attrs:
            for cls in item['class']:
                if re.match(r'flag-\d+', cls):
                    unique_flags.add(cls)

# Print all unique flags sorted numerically
print(sorted(unique_flags))


import requests
from bs4 import BeautifulSoup
import re

# URL to scrape
url = "https://hertie-scraping-website.vercel.app/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all visible flags in text (matching "flag-[number]")
flags = soup.find_all(text=re.compile(r'flag-\d+'))

# Also, find flags embedded in HTML attributes (id and class attributes)
flags += soup.find_all(id=re.compile(r'flag-\d+'))
flags += soup.find_all(class_=re.compile(r'flag-\d+'))

# Clean up and store unique flags in a set to remove duplicates
unique_flags = set()

# Extract flags from text and attributes
for item in flags:
    if isinstance(item, str):
        unique_flags.add(item.strip())
    else:
        # Check and add flags from 'id' attributes
        if 'id' in item.attrs and re.match(r'flag-\d+', item['id']):
            unique_flags.add(item['id'])
        # Check and add flags from 'class' attributes
        if 'class' in item.attrs:
            for cls in item['class']:
                if re.match(r'flag-\d+', cls):
                    unique_flags.add(cls)

# Print all unique flags sorted numerically
print(sorted(unique_flags))

