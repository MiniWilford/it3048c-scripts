# it3048c Project1 - "`Check temperature and time`"


## The Goal
The goal of the script is to automate the process of finding the weather and time of a location selected by the user and to enable them to email any results via a SMTP (simple mail transfer protocol) server like GMAIL or Yahoo to the person of their choosing.

## Before Using
Before conducting any usage of the script, you will need to ensure the email smtp server provider (E.g. smtp.mail.yahoo.com) has third-party access enabled. 

Please Refer to the following sites to figure out how to proceed:

Gmail: https://support.google.com/accounts/answer/3466521?hl=en

Yahoo: https://help.yahoo.com/kb/SLN15241.html

Outlook: https://support.microsoft.com/en-us/account-billing/add-a-trusted-device-to-your-microsoft-account-fe3860c8-bc04-9770-e218-b4fd6b767f4b#TXT

## How to use:
Download the script and ensure Python (https://www.python.org/downloads/release/python-3120/ or > v3.0) is installed and correctly set up with the Python PATH variable created on your machine. The default libraries that come with Python should be more than sufficient to run the script. 

During the initial launch you will be prompted to enter a location with an example. The script will automatically turn the first letter capital and everything after into lowercase, this is to enable a functional query parameter with the WeatherAPI being used.

Once you have entered a location, a prompt will ask you to select [yes] or [no] to email results (the case does not matter, it will be lowercase no matter what). 

If the message is failed due to any closed connection, or wrong typed smtp server name, then the error will be printed in the console displaying the root issue to what went wrong, then ask if the user if they would like to try the program again.

## Where is the data coming from?
An API is being utilized to retrieve weather data from https://WeatherAPI.com and is limited to 1 million requests monthly.

## My Email won't send...?
This is because you don't have third party access enabled by your SMTP provider or there is a firewall issue. Ensure everything is working correctly before trying again.