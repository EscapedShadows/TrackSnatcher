import customtkinter as ctk
import ctypes

screen_width = ctypes.windll.user32.GetSystemMetrics(0)
screen_height = ctypes.windll.user32.GetSystemMetrics(1)

window_width = int(screen_width / 3)
window_height = int(screen_height / 3)

posX = int(screen_width / 2 - window_width / 2)
posY = int(screen_height / 2 - window_height / 2)

root = ctk.CTk()
root.title("TrackSnatcher | EscapedShadows")
root.geometry(f"{window_width}x{window_height}+{posX}+{posY}")

def create_playlist():
    print("Create Playlist button clicked")

def add_song():
    print("Add Song button clicked")

def use_browser():
    print("Use Browser button clicked")

playlistname = ctk.CTkEntry(root, placeholder_text="Enter Playlist Name")
playlistname.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

createplaylist = ctk.CTkButton(root, text="Create Playlist", command=create_playlist)
createplaylist.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

addsong = ctk.CTkEntry(root, placeholder_text="Add Song URL here...")
addsong.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

addsongbutton = ctk.CTkButton(root, text="Add Song", command=add_song)
addsongbutton.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

userbrowser = ctk.CTkButton(root, text="Use Browser", command=use_browser)
userbrowser.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

feedbacklabel = ctk.CTkLabel(root, text="")
feedbacklabel.grid(row=3, column=0, columnspan=2, padx=10, sticky='ew')

songlist = ctk.CTkScrollableFrame(root, height=window_height, width=window_width - 50)
songlist.grid(row=4, column=0, columnspan=2, pady=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(4, weight=1)

root.mainloop()