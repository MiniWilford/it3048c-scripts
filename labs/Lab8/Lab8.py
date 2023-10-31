import requests as req
import re as regex

# Grab site 
request = req.get('https://www.w3schools.com/html/html5_geolocation.asp')

# Get Site content
site = str(request.content)

# Extract data
page_title = regex.compile('<h1>(.*?)</h1>')
page_description = regex.compile('<h2>(.*?)</h2>')

# Print "content" for title
# Credit: https://www.delftstack.com/howto/python/python-remove-html-tags/
title = page_title.search(site).group()
remove_tags = regex.compile("<.*?>")
clean_title = regex.sub(remove_tags, "", title)

# Print "content" for description
description = page_description.search(site).group()
remove_tags = regex.compile("<.*?>")
clean_description = regex.sub(remove_tags, "", description)
cleaner_description = str(clean_description.replace('\\', ''))

print("The page is about " + clean_title)
print("The description of the page is: " + cleaner_description)