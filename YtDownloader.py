import tkinter
import customtkinter
from pytube import YouTube

                                    #FUNCTIONS

# This function will start the downloading of the youtube video
def start_download():
    try:
        yT_link = link.get()
        ytObj = YouTube(yT_link, on_progress_callback = progress_func)
        heading.configure(text  = ytObj.title)
        video = ytObj.streams.get_highest_resolution()
        fin_label.configure(text = "")
        video.download()
        fin_label.configure(text = "Download complete.", text_color = "green")
    except:
        fin_label.configure(text = "Invalid link, video could not be downloaded.", text_color = "red")
    

# This funtion will update the progress label and the progress bar
def progress_func(stream, chunck, bytes_remaining):
    # Updating the label
    total_size = stream.filesize
    amount_downloaded = total_size - bytes_remaining
    percent_completed = amount_downloaded / total_size * 100
    percent_val = str(int(percent_completed))
    prcnt_lbl.configure(text = percent_val + "%")
    prcnt_lbl.update()

    # Updating the bar
    prcnt_bar.set(float(percent_completed) / 100) 


                                        #  APP SETTINGS

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
heading.pack(padx = 10, pady = 10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(my_app, width = 400, height = 40, textvariable = url_var)
link.pack()

# Finished message for user
fin_label = customtkinter.CTkLabel(my_app, text = "")
fin_label.pack(padx = 10, pady = 10)

# Progress Percentage Label and Bar
prcnt_lbl = customtkinter.CTkLabel(my_app, text = "0%") # Label
prcnt_lbl.pack()

prcnt_bar = customtkinter.CTkProgressBar(my_app, width = 400) # Bar
prcnt_bar.set(0)
prcnt_bar.pack(padx = 10, pady = 10)

# Button for downloading video in maximum resoulution
dnld_btn = customtkinter.CTkButton(my_app, text = "Download", command = start_download)
dnld_btn.pack(padx = 10, pady = 10)

# Running the app
my_app.mainloop()