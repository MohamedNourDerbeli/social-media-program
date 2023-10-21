# Import necessary libraries
from tkinter import *
import webview

# Create the main application window
app = Tk()
app.geometry('1000x600+200+50')
app.title('Social Media')
app.configure(background='whitesmoke')
app.resizable(False, False)

# Define functions for launching social media web pages

def Facebook():
    # Open a Facebook web page using the webview library
    url = 'https://www.facebook.com'
    webview.create_window("Facebook", url,
                      width=815,
                      height=560,
                      resizable=True,
                      background_color='#D8D8D8',
                      x=390, y=120,
                      zoomable=True,
                      )
    webview.start()

def Instagram():
    # Define a function to open the Instagram web page
    url = 'https://www.instagram.com'
    webview.create_window("Instagram", url,
                      width=815,
                      height=560,
                      resizable=True,
                      background_color='#D8D8D8',
                      x=390, y=120,
                      zoomable=True,
                      )
    webview.start()

def Twitter():
    # Define a function to open the Twitter web page
    url = 'https://www.twitter.com'
    webview.create_window("Twitter", url,
                      width=815,
                      height=560,
                      resizable=True,
                      background_color='#D8D8D8',
                      x=390, y=120,
                      zoomable=True,
                      )
    webview.start()

def TikTok():
    # Define a function to open the TikTok web page
    url = 'https://www.tiktok.com'
    webview.create_window("TikTok", url,
                      width=815,
                      height=560,
                      resizable=True,
                      background_color='#D8D8D8',
                      x=390, y=120,
                      zoomable=True,
                      )
    webview.start()

# Create labels, buttons, and images for the user interface

# Top title
title1 = Label(app, text="Social Application",
               fg='white', bg='#1f1e2d', width=85,
               height=2,
               font=('Noumal', 16, 'bold'),
               bd=0,
               )
title1.place(x=0, y=0)

# Load a logo image
Logo = PhotoImage(file='image/SocialMedia.png')
pan = Label(app, image=Logo)
pan.place(x=240, y=85, width=700, height=400)

# Create a label for the text logo
textlogo = Label(app, text="Social Media Application Program",
                 fg='black', bg='whitesmoke',
                 font=('Courier', 16, 'bold'),
                 )
textlogo.place(x=380, y=520)

# Create the sidebar

side = Frame(app, width=170, height=610, bg='#1f1e2d', bd=0, relief=FLAT)
side.place(x=0, y=0)

# Add a title in the sidebar
side_title1 = Label(side, text=" Shadow ",
                    fg='white',
                    bg='#1f1e2d',
                    font=('Nourmal', 10, 'bold'),
                    )
side_title1.place(x=50, y=20)

# Load images for buttons
home_image = PhotoImage(file='image/globe-network.png')
facebook_image = PhotoImage(file='image/facebook.png')
instagram_image = PhotoImage(file='image/instagram.png')
twitter_image = PhotoImage(file='image/twitter.png')
tiktok_image = PhotoImage(file='image/tiktok.png')

# Set button dimensions and font
button_width = 120
button_height = 65
button_font = ('Courier', 10, 'bold')

# Create the Home button
user = Button(side, text='Home',
              fg='white',
              bg='#1f1e2d',
              cursor='hand2',
              image=home_image,
              compound=TOP,
              relief=FLAT,
              width=button_width,
              height=button_height,
              font=button_font,
              )
user.place(x=15, y=50)

# Add a title for the social media section
side_title2 = Label(side, text="Social App",
                    fg='white',
                    bg='#1f1e2d',
                    font=('Nourmal', 10, 'bold'),
                    )
side_title2.place(x=40, y=125)

# Create buttons to launch different social media platforms
facebook1 = Button(side,
                   cursor='hand2',
                   image=facebook_image,
                   compound=TOP,
                   relief=FLAT,
                   fg='white',
                   bg='#1f1e2d',
                   width=button_width,
                   height=button_height,
                   font=button_font,
                   command=Facebook,
                   )
facebook1.place(x=15, y=150)

instagram1 = Button(side,
                    cursor='hand2',
                    image=instagram_image,
                    compound=TOP,
                    relief=FLAT,
                    fg='white',
                    bg='#1f1e2d',
                    width=button_width,
                    height=button_height,
                    font=button_font,
                    command=Instagram,
                    )
instagram1.place(x=15, y=220)

twitter1 = Button(side,
                  cursor='hand2',
                  image=twitter_image,
                  compound=TOP,
                  relief=FLAT,
                  fg='white',
                  bg='#1f1e2d',
                  width=button_width,
                  height=button_height,
                  font=button_font,
                  command=Twitter,
                  )
twitter1.place(x=15, y=290)

tiktok1 = Button(side,
                 cursor='hand2',
                 image=tiktok_image,
                 compound=TOP,
                 relief=FLAT,
                 fg='white',
                 bg='#1f1e2d',
                 width=button_width,
                 height=button_height,
                 font=button_font,
                 command=TikTok,
                 )
tiktok1.place(x=15, y=360)

# Create the main application frame
main_app = Frame(app, width=840, height=610,
                 bg='whitesmoke', bd=0, relief=RAISED)
main_app.place(x=160, y=50)

# Add a main title and a description in the main application frame
main_title = Label(main_app, text="Welcome to Social Media App!",
                   fg='black', bg='whitesmoke',
                   font=('Courier', 16, 'bold'),
                   )
main_title.place(x=230, y=20)

main_text = Label(main_app, text="Select a social media platform from the sidebar to launch it.",
                  fg='black', bg='whitesmoke',
                  font=('Courier', 12),
                  )
main_text.place(x=120, y=80)

# Start the Tkinter main loop
app.mainloop()
