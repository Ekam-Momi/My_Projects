import tkinter
import customtkinter
from pytube import YouTube

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

# Button for downloading



# Running the app
my_app.mainloop()