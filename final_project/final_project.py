# Project 1 dependencies (Email / API calls)
from tkinter import filedialog as fd
import requests
import json
import smtplib
import ssl

# Project 2/3 dependencies (GUI / Operations)
import tkinter as tkgui

# Project 3 Dependencies
import os


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
# https://www.tutorialspoint.com/how-to-clear-the-entry-widget-after-a-button-is-pressed-in-tkinter

# References Project 3:
# https://stackoverflow.com/questions/11295917/how-to-select-a-directory-and-store-the-location-using-tkinter-in-python
# https://pythonspot.com/tk-file-dialogs/
# https://stackoverflow.com/questions/58855112/finding-the-biggest-folder-within-a-directory-tree
# https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python

# Get Weather API base URL
base_url = "http://api.weatherapi.com/v1"

def display_city_information(location, time, temp_f, temp_c):
    data.delete(0, 'end') # Remove previous text
    data.insert(0, f"At {location} it is {time}. Fahrenheit: {temp_f}, Celcius: {temp_c} ")

def storage_window():
    #
    # Retrieve highest consuming folders from PC storage (SSD/HDD)
    #
    
    def get_folder_size(path):
        #
        # Get Size of directory selected / specified
        #
        size_of_folder = 0
        for (root, dirs, files) in os.walk(path): # Get each item in OS specificed path
            for file in files: # Join file to initial path and getsize of folder with each file and its size
                filename = os.path.join(root, file)
                size_of_folder += os.path.getsize(filename)
        return size_of_folder
    
    # Setup storage window
    storage_window = tkgui.Tk()
    storage_window.geometry('400x400+25+25')
    storage_window.title("Storage Results")
    storage_window['background'] = 'beige'
    storage_window.focus() # Supposed to "focus" the window, but askdirectory below overwrites (I guess)
    
    # Get Directory to search through from User's PC
    # Will display "select folder" dialog and search for user selected directory
    # https://stackoverflow.com/questions/11295917/how-to-select-a-directory-and-store-the-location-using-tkinter-in-python
    rootPC = tkgui.Tk()
    rootPC.withdraw()
    selected_folder = fd.askdirectory()
    
    # Parse user's selected directory
    # https://stackoverflow.com/questions/58855112/finding-the-biggest-folder-within-a-directory-tree
    # https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python
    # https://stackoverflow.com/questions/6748791/top-5-folders-consuming-the-most-space?rq=33
    directory_size_bytes = get_folder_size(selected_folder)
    directory_size_mbytes = directory_size_bytes / 1000000
    directory_size_Gbytes = directory_size_bytes / 1000000000
    
    
    # Display this information
    print(directory_size_bytes)
    print(directory_size_mbytes)
    print(directory_size_Gbytes)
    
    # GUI label / printing
    # Bytes
    display_bytes_label = tkgui.Label(storage_window, text="Byte(s): ", background="red", font=('ariel', 12, 'bold'))
    display_bytes = tkgui.Entry(storage_window, width=30)
    display_bytes.delete(0, 'end') # Remove previous text
    display_bytes.insert(0, f"{directory_size_bytes}")
    
    # Megabytes
    display_mbytes_label = tkgui.Label(storage_window, text="Megabyte(s): ", background="red", font=('ariel', 12, 'bold'))
    display_mbytes = tkgui.Entry(storage_window, width=30)
    display_mbytes.delete(0, 'end') # Remove previous text
    display_mbytes.insert(0, f"{directory_size_mbytes}")
    
    # Gigabytes
    display_Gbytes_label = tkgui.Label(storage_window, text="Gigabyte(s): ", background="red", font=('ariel', 12, 'bold'))
    display_Gbytes = tkgui.Entry(storage_window, width=30)
    display_Gbytes.delete(0, 'end') # Remove previous text
    display_Gbytes.insert(0, f"{directory_size_Gbytes}")
    
    # Place labels/buttons/texbox
    display_bytes_label.grid(row=0, column=0)
    display_bytes.grid(row=0, column=1)
    
    display_mbytes_label.grid(row=1, column=0)
    display_mbytes.grid(row=1, column=1)
    
    display_Gbytes_label.grid(row=1, column=0)
    display_Gbytes.grid(row=1, column=1)
    

    
    


def email(subject, body, sender, to, password, user_smtp_server):
    try:   
        message = email_message()
        message.set_content = body
        message['Subject'] = subject
        message['From'] = sender
        message['To'] = to
        ssl_context = ssl.create_default_context()  # answered Nov 22, 2019 at 16:02 by Asaga
        with smtplib.SMTP(user_smtp_server, 587) as smtp_server:
            smtp_server.connect(user_smtp_server, 587)
            smtp_server.starttls(context= ssl_context)
            smtp_server.login(user= sender, password= password)
            smtp_server.send_message(message)
        return "Message sent!"
    except Exception as error:
        print("\nMessage Failed, check account settings or smtp server availability...")
        print("Error: {error}".format(error = error))
        return str(error)

def email_window():
    
    def send_email():
        # Get variables
        subject = email_subject.get()
        to = email_to.get()
        sender = email_sender.get()
        password = email_password.get()
        body = data.get()
        user_smtp_server = smtp_server.get()
        
        # Send email
        confirmation = email(subject, body, sender, to, password, user_smtp_server)
        display_email_confirmation(confirmation)
        
    def display_email_confirmation(message):
        display_confirmation.delete(0, 'end') # Remove previous text
        display_confirmation.insert(0, f"{message}")
    
    # Setup email window
    email_window = tkgui.Tk()
    email_window.geometry('190x400+25+25')
    email_window.title("Email Results")
    email_window['background'] = 'gray'
    
    # Get Sender email (e.g., coolemail@yahoo.com)
    email_sender = tkgui.StringVar()
    sender_label = tkgui.Label(email_window, text="Email Username", background="gray", font=('ariel', 12, 'bold'))
    sender_textbox = tkgui.Entry(email_window, textvariable=email_sender)
    
    # Get Sender password
    email_password = tkgui.StringVar()
    password_label = tkgui.Label(email_window, text="Email Password", background="gray", font=('ariel', 12, 'bold'))
    password_textbox = tkgui.Entry(email_window, textvariable=email_password, show="X")
    
    # Get subject
    email_subject = tkgui.StringVar()
    subject_label = tkgui.Label(email_window, text="Email Subject", background="gray", font=('ariel', 12, 'bold'))
    subject_textbox = tkgui.Entry(email_window, textvariable=email_subject)
    
    # Get "to"
    email_to = tkgui.StringVar()
    to_label = tkgui.Label(email_window, text="Email To", background="gray", font=('ariel', 12, 'bold'))
    to_textbox = tkgui.Entry(email_window, textvariable=email_to)
    
    # Get SMTP server
    # 3 options (Ex: 'smtp.mail.yahoo.com' or 'smtp.gmail.com')
    smtp_server = tkgui.StringVar()
    google = tkgui.Radiobutton(email_window, text='GMAIL', value='smtp.gmail.com', background="gray", variable=smtp_server)
    yahoo = tkgui.Radiobutton(email_window, text='YAHOO', value='smtp.mail.yahoo.com', background="gray", variable=smtp_server)
    outlook = tkgui.Radiobutton(email_window, text='OUTLOOK', value='smtp.office365.com', background="gray", variable=smtp_server)
    
    
    # Email Button
    send_email_button = tkgui.Button(email_window, text="SEND", relief="raised", padx=15, background="lightgreen", command=send_email)
    
    # Display If email sent
    display_confirmation_label = tkgui.Label(email_window, text="Confirmation", background="gray", font=('ariel', 12, 'bold'))
    display_confirmation = tkgui.Entry(email_window, width=30)
    
    # Place labels/buttons/texbox
    sender_label.grid(row=0, column=1)
    sender_textbox.grid(row=1, column=1)
    password_label.grid(row=2, column=1)
    password_textbox.grid(row=3, column=1)
    subject_label.grid(row=4, column=1)
    subject_textbox.grid(row=5, column=1)
    to_label.grid(row=6, column=1)
    to_textbox.grid(row=7, column=1)
    google.grid(row=8, column=1)
    yahoo.grid(row=9, column=1)
    outlook.grid(row=10, column=1)
    send_email_button.grid(row=11, column=1)
    display_confirmation_label.grid(row=12, column=1)
    display_confirmation.grid(row=13, column=1)

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
        display_city_information(location, time, temp_f, temp_c)

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
question_textbox = tkgui.Entry(main_window, textvariable=get_city, font=('ariel', 10, 'normal'), width=20)

# Create 'submit' button
submit_button = tkgui.Button(main_window, text='Submit', relief='raised', command=submit_city) # command=submit_city() 

# hidden data, unveils when submit is clicked
data = tkgui.Entry(main_window, width=80)

# Add button to open email window to email results
email_button = tkgui.Button(main_window, text="Email Results", relief="raised", background="lightgreen", command=email_window)

# Add button to check PC data consumption
storage_button = tkgui.Button(main_window, text="Check PC Storage", relief="raised", background="lightgray", command=storage_window)

# Place label/entry/button
question_label.grid(row=0, column=0)
question_textbox.grid(row=0, column=1)
submit_button.grid(row=1, column=1)
data.grid(row=2, column=0)
email_button.grid(row=3, column=0)
storage_button.grid(row=4, column=0)

# Ensure main window shown is persistent during runtime
main_window.mainloop()
