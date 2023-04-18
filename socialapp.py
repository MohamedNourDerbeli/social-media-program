from tkinter import *
import webview
app = Tk()
app.geometry('1000x600+200+50')
app.title('Social Media')
app.configure(background='whitesmoke')
app.resizable(False, False)
def Facebook():
    url= 'https://www.facebook.com'
    webview.create_window("Facebook", url,
                      width=815, 
                      height=560, 
                      resizable=True,
                      background_color='#D8D8D8',
                      x= 390,y=120,
                      zoomable=True,
                          
                      )
    webview.start()
def Instagram():
    url1= 'https://www.instagram.com'
    webview.create_window("Instagram", url1,
                      width=815, 
                      height=560, 
                      resizable=True,
                      background_color='#D8D8D8',
                      x= 390,y=120,
                      zoomable=True,
                        
                      )
    webview.start()
def Twitter():
    url2= 'https://www.twitter.com'
    webview.create_window("Twitter", url2,
                      width=815, 
                      height=560, 
                      resizable=True,
                      background_color='#D8D8D8',
                      x= 390,y=120,
                      zoomable=True,
                
                      )
    webview.start()
def TikTok():
    url3= 'https://www.tiktok.com'
    webview.create_window("TikTok", url3,
                      width=815, 
                      height=560, 
                      resizable=True,
                      background_color='#D8D8D8',
                      x= 390,y=120,
                      zoomable=True,
                        
                      )
    webview.start()
    

# Top title
title1 = Label(app, text="Social Application",
               fg='white', bg='#1f1e2d',width=85,
              height=2,
               font=('Noumal', 16,'bold'),
               bd=0,
               )
title1.place(x=0,y=0)

Logo = PhotoImage(file='image/SocialMedia.png')
pan = Label(app, image=Logo)
pan.place(x=240, y=85, width=700, height=400)

textlogo = Label(app, text="Social Media Application Program",
                 fg='black', bg='whitesmoke',
                 font=('Courier', 16, 'bold'),
                 )
textlogo.place(x=380, y=520,)

# Sidebar
side = Frame(app, width=170, height=610, bg='#1f1e2d', bd=0, relief=FLAT)
side.place(x=0, y=0)

side_title1 = Label(side, text=" Shadow ",
                    fg='white',
                    bg='#1f1e2d',
                    font=('Nourmal', 10, 'bold'),
                    )
side_title1.place(x=50, y=20)

home_image = PhotoImage(file='image/globe-network.png')
facebook_image = PhotoImage(file='image/facebook.png')
instagram_image = PhotoImage(file='image/instagram.png')
twitter_image = PhotoImage(file='image/twitter.png')
tiktok_image = PhotoImage(file='image/tiktok.png')

button_width = 120  # Set button width
button_height = 65  # Set button height
button_font = ('Courier', 10, 'bold')  # Set button font

user = Button(side, text='Home',
              fg='white',
                bg='#1f1e2d',
              cursor='hand2',
              image=home_image,

              compound=TOP,
              relief=FLAT,
            width=button_width,  # Set button width
            height=button_height,  # Set button height
            font=button_font,  # Set button font
              )
user.place(x=15, y=50)

side_title2 = Label(side,text="Social App",
                    fg='white',
                    bg='#1f1e2d',
                    font=( 'Nourmal',10, 'bold'),
                    )
side_title2.place(x=40, y=125)

facebook1 = Button(side,
                   cursor='hand2',
                   image=facebook_image,
                   compound=TOP,
                   relief=FLAT,
                   fg='white',
                    bg='#1f1e2d',
                   width=button_width,  # Set button width
                   height=button_height,  # Set button height
                   font=button_font,  # Set button font
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
                    width=button_width,  # Set button width
                    height=button_height,  # Set button height
                    font=button_font,  # Set button font
                    command=Instagram,
                    )
instagram1.place(x=15, y=220)

twitter1 = Button(side,
                  cursor='hand2',
                  image=twitter_image,
                  compound=TOP, relief=FLAT,
                  fg='white',
                    bg='#1f1e2d',
                  width=button_width,  # Set button width
                  height=button_height,  # Set button height
                  font=button_font,  # Set button font
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
                 width=button_width,  # Set button width
                 height=button_height,  # Set button height
                 font=button_font,  # Set button font
                 command=TikTok,
                 )
tiktok1.place(x=15, y=360)
main_app = Frame(app, width=840, height=610,
                 bg='whitesmoke', bd=0, relief=RAISED)
main_app.place(x=160, y=50)

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

app.mainloop()
