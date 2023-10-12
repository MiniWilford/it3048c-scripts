import requests
import json
import smtplib
import ssl

# Import the email modules
from email.message import EmailMessage as email_message

# References:
# https://stackoverflow.com/questions/61977076/how-to-fetch-data-from-api-using-python (Kriti Pawar)
# https://www.weatherapi.com/docs/#intro-request
# https://stackoverflow.com/questions/6270782/how-to-send-an-email-with-python
# https://mailtrap.io/blog/python-send-email-gmail/
# https://stackoverflow.com/questions/64505/sending-mail-from-python-using-smtp
# https://stackoverflow.com/questions/1483429/how-do-i-print-an-exception-in-python
# https://stackoverflow.com/questions/37224073/smtp-auth-extension-not-supported-by-server


def email(subject, body, sender, to, password, user_smtp_server):
    try:
        message = email_message()
        message.set_content = body
        message['Subject'] = subject
        message['From'] = sender
        message['To'] = to
        ssl_context = ssl.create_default_context()  # answered Nov 22, 2019 at 16:02 by Asaga
        with smtplib.SMTP(user_smtp_server, 587) as smtp_server:
            smtp_server.starttls(context= ssl_context)
            smtp_server.login(user= sender, password= password)
            smtp_server.send_message(message)
        print("Message sent!")
    except Exception as error:
        print("\nMessage Failed, check account settings or smtp server availability...")
        print("Error: {error}".format(error = error))

# Get Weather From Cincinnati
base_url = "http://api.weatherapi.com/v1"

# Persist Program
running = True
while (running):
    # Ask user for location
    print("") # Empty string for better legibility on continues
    user_location = str(input("Where would you like to check the weather at? \nPlease ensure there is a capital at the beginning (E.g. Cincinnati): "))
    weather_url = "/current.json?key=eec84d47224a4fefb6402059231110&q=" + user_location + "&aqi=no"
    
    # Call The Weather API
    weather_response = requests.get(base_url + weather_url) 
    
    # If Succeeds
    if(weather_response.status_code == 200):
        # Json Content
        json_response = json.loads(weather_response.text)
        
        
        # Variable Initialization
        location = json_response["location"]["name"] + ", " + json_response["location"]["region"]
        time = json_response["location"]["localtime"]
        temp_f = json_response["current"]["temp_f"]
        temp_c = json_response["current"]["temp_c"]
        
        # Results
        weather_info = print(
            """\n{location}: {time}. \nIt is [{temp_f}] degrees Fahrenheit or [{temp_c}] degress celsius.
            
            """.format(location = location, 
                       time = time, 
                       temp_f = temp_f,
                       temp_c = temp_c))
        
        # Ask if to email results
        user_response = str(input("\nWould you like to email the results? [yes] or [no]: ")).lower()
        if(user_response == "y" or user_response == "yes"):
            # Set up Email Proponents
            subject = input("Enter an email subject: ")
            user_message = input("Enter a message to send with weather information: ")
            body = "{weather_info} \n\n\n {user_message}".format(weather_info = weather_info, user_message = user_message)
            sender = input("Enter your email: ")
            to = input("Email to send to: ")
            password = str(input("Email Password: "))
            user_smtp_server = str((input("Please Enter an SMTP email server and ensure third-party access is enabled (Ex: 'smtp.mail.yahoo.com' or 'smtp.gmail.com'): ")))
            # Send Email
            email(subject, body, sender, to, password, user_smtp_server)        
        
        # Continue Program...?
        response = str(input("\nWould you like to continue? [yes] or [no] "))
        response = str(response.lower())
        if(response == "yes" or response == "y"):
            print("\nContinuing")
            continue
        else:
            running = False
            print("\nGoodbye!")
            break
    else:
        # Failed Response
        print("Failure to connect to weather service API")
        response = str(input("\nWould you like to continue [yes] or [no]? "))
        response = str(response.lower())
        if(response == "yes" or response == "y"):
            continue
        else:
            running = False
            break