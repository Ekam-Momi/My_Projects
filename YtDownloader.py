import tkinter
import customtkinter
from pytube import YouTube

                                    #FUNCTIONS

# This function will start the downloading of the youtube video
def start_download():
    try:
        yT_link = link.get()
        ytObj = YouTube(yT_link)
        heading.configure(text  = ytObj.title)
        video = ytObj.streams.get_highest_resolution()
        fin_lable.configure(text = "")
        video.download()
        fin_lable.configure(text = "Download complete.", text_color = "green")
    except:
        fin_lable.configure(text = "Invalid link, video could not be downloaded.", text_color = "red")
    

# Settings
customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")

# App frame
my_app = customtkinter.CTk()
my_app.geometry("740x480")
my_app.title("Youtube Video Downloader")

                                        # USER INTERFACE ELEMENTS

# Instructional title
heading = customtkinter.CTkLabel(my_app, text = "Enter YouTube link below")
heading.pack(padx = "10", pady = "10")

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(my_app, width = 400, height = 40, textvariable = url_var)
link.pack()

# Finished message for user
fin_lable = customtkinter.CTkLabel(my_app, text = "")
fin_lable.pack(padx = "10", pady = "10")

# Button for downloading video in maximum resoulution
dnld_btn = customtkinter.CTkButton(my_app, text = "Download", command = start_download)
dnld_btn.pack(padx = "10", pady = "10")

# Running the app
my_app.mainloop()