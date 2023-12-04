# it3048c Final Project - "`Check temperature and time GUI`"


## The Goal
The goal of the script is to automate the process of finding the weather and time of a location selected by the user and to enable them to email any results via a SMTP (simple mail transfer protocol) server like GMAIL or Yahoo to the person of their choosing through a guided user interface.

## Before Using
Before conducting any usage of the script, you will need to ensure the email smtp server provider (E.g. smtp.mail.yahoo.com) has third-party access enabled. As well as making sure to wait for the program to full process any data when clicking the "submit" buttons.

Please Refer to the following sites to figure out how to proceed:

Gmail: https://support.google.com/accounts/answer/3466521?hl=en

Yahoo: https://help.yahoo.com/kb/SLN15241.html

Outlook: https://support.microsoft.com/en-us/account-billing/add-a-trusted-device-to-your-microsoft-account-fe3860c8-bc04-9770-e218-b4fd6b767f4b#TXT

## How to use:
Download the script and ensure Python (https://www.python.org/downloads/release/python-3120/ or > v3.0) is installed and correctly set up with the Python PATH variable created on your machine. The default libraries that come with Python should be more than sufficient to run the script. If not you will need to install PIP and install `tkinter` and `requests` libraries for main functionality.

During the initial launch you will be prompted to enter a location with an example. The script will automatically turn the first letter capital and everything after into lowercase, this is to enable a functional query parameter with the WeatherAPI being used.

Once you have entered a location, the API will retrieve the closest matching location to the city entered. Giving the fahrenheit, celsius, time, and location found.

If the message is failed due to any closed connection, or wrong typed smtp server name, then the error will be printed in the console / GUI displaying the root issue to what went wrong. 

## Where is the data coming from?
An API is being utilized to retrieve weather data from https://WeatherAPI.com and is limited to 1 million requests monthly. As well as open libraries utilized such as `os`, `requests`, and `tkinter`.

## Why is this useful?
This is useful to utilize when needing to catch up with any older relatives or close friends by sending a personal email, as well as educational usage to learn the differences in temperature when it comes to geography. In addition to the prior reasonings as well, it enables user's to become accustomed to their PC and check on their current storage issues or lack there-of. 


## My Email won't send...?
This is because you don't have third party access enabled by your SMTP provider or there is a firewall issue. Ensure everything is working correctly before trying again. As well as potentially being blocked for sending too many requests.