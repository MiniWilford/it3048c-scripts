# Project 1 dependencies (Email / API calls)
import requests
import json
import smtplib
import ssl

# Project 2 dependencies (GUI)
import tkinter as tkgui

# Import the email modules
from email.message import EmailMessage as email_message

# References Project 1:
# https://stackoverflow.com/questions/61977076/how-to-fetch-data-from-api-using-python (Kriti Pawar)
# https://www.weatherapi.com/docs/#intro-request
# https://stackoverflow.com/questions/6270782/how-to-send-an-email-with-python
# https://mailtrap.io/blog/python-send-email-gmail/
# https://stackoverflow.com/questions/64505/sending-mail-from-python-using-smtp
# https://stackoverflow.com/questions/1483429/how-do-i-print-an-exception-in-python
# https://stackoverflow.com/questions/37224073/smtp-auth-extension-not-supported-by-server
# https://www.geeksforgeeks.org/how-to-capitalize-first-character-of-string-in-python/

# References Project 2:
# https://www.askpython.com/python-modules/top-best-python-gui-libraries
# https://www.pythontutorial.net/tkinter/tkinter-hello-world/
# https://www.pythontutorial.net/tkinter/tkinter-window/
# https://webstockreview.net/explore/clipart-clouds-bitmap/  ## Get cloud icon
# https://www.pythontutorial.net/tkinter/tkinter-entry/  ## Get user input
# https://www.bing.com/videos/riverview/relatedvideo?q=tkinter+seet+background+color+of+window&mid=F0B05B9715FD9CA3489BF0B05B9715FD9CA3489B&FORM=VIRE ## Learn to change background color
# https://www.youtube.com/watch?v=ls3BAhPV06M ## Button and options in Tkinter
# https://www.geeksforgeeks.org/python-tkinter-entry-widget/  ## Help with structure
# https://stackoverflow.com/questions/3819354/in-tkinter-is-there-any-way-to-make-a-widget-invisible ## Hiding widget
# https://stackoverflow.com/questions/67251284/how-to-display-function-output-to-tkinter-gui

# Get Weather API base URL
base_url = "http://api.weatherapi.com/v1"

def display_information(location, time, temp_f, temp_c):
    print()

def hide_widget(widget):
    widget.widget.pack_forget()

def show_widget(widget):
    widget.pack()

def submit_city():
    """
       Get User information entered in get_city entry textbox
    """
    # Retrieve entry input
    city = get_city.get()
    
    # Convert user string into API readable input (first capital letter)
    user_location = city[0].upper() + city[1:].lower()
    
    # WebAPI URI 
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
        
        # Display label in window
        data = tkgui.Label(main_window, 
                           text=display_information(location, time, temp_f, temp_c))
        data.grid(row=1, column=1)

# Create tkinter window class instance (main)
main_window = tkgui.Tk()

# Change main_window icon
#main_window.iconbitmap('./images/cloud_clipart_free.ico')

# Set window dimensions
main_window.geometry('665x400+25+25')

# Set Window background color
main_window['background'] = 'lightblue' # "sky feeling"

# Window named 'Retrieve City'
main_window.title("Retrieve Weather")

# Place dedicated question label for main_window 
question_label = tkgui.Label(main_window, text="What city would you like to check the weather at? (E.g. Cincinnati):", font=('ariel', 12, 'bold'))
question_label.pack()

# Place textbox for user entry
get_city = tkgui.StringVar() # ensure it is in string format
question_textbox = tkgui.Entry(main_window, textvariable=get_city, font=('ariel', 10, 'normal'))

# Create 'submit' button
submit_button = tkgui.Button(main_window, text='Submit', relief='raised', command=submit_city) 

# hidden data, unveils when submit is clicked
data = tkgui.Label(main_window, text="")

# Place label/entry/button
question_label.grid(row=0, column=0)
question_textbox.grid(row=0, column=1)
submit_button.grid(row=1, column=1)
data.grid(row=0, column=0)

# Ensure main window shown is persistent during runtime
main_window.mainloop()




'''
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

# Get Weather API base URL
base_url = "http://api.weatherapi.com/v1"

# Persist Program
running = True
while (running):
    # Ask user for location
    print("") # Empty string for better legibility on continues
    user_location = str(input("What city would you like to check the weather at? (E.g. Cincinnati): "))
    
    # Convert user string into API readable input (first capital letter)
    user_location = user_location[0].upper() + user_location[1:].lower()
    
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
'''