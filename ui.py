import customtkinter as ctk
import ctypes
from browser import main as browserMain
from pytubeinteraction import get_titles, get_id, get_tracks
import threading
import os

screen_width = ctypes.windll.user32.GetSystemMetrics(0)
screen_height = ctypes.windll.user32.GetSystemMetrics(1)

window_width = int(screen_width / 3)
window_height = int(screen_height / 3)

posX = int(screen_width / 2 - window_width / 2)
posY = int(screen_height / 2 - window_height / 2)

root = ctk.CTk()
root.title("TrackSnatcher | EscapedShadows")
root.geometry(f"{window_width}x{window_height}+{posX}+{posY}")
root.resizable(False,False)

def handle_browser():
    usebrowser.configure(state="disabled")
    links = browserMain()
    titles = get_titles(links)
    usebrowser.configure(state="normal")
    for i, title in enumerate(titles):

        max_length = window_width // 8
        if len(title) > max_length:
            title = title[:max_length-3] + "..."

        label = ctk.CTkLabel(songlist, text=title)
        label.custom_data = {}
        label.custom_data["url"] = links[i]
        check = ctk.CTkCheckBox(songlist, text="Use")
        check.select()

        row = songlist.grid_size()[1]
        label.grid(row=row, column=0, sticky='w', padx=10)
        check.grid(row=row, column=1, sticky='w', padx=10)

def prepare_playlist():
    links = []

    elements = songlist.winfo_children()

    for i in range(0,len(elements),2):
        temp1, temp2 = elements[i].custom_data.get("url"),elements[i+1].get()

        if temp2 == 0:
            pass
        else:
            links.append(temp1)

    if not os.path.isdir(rf"C:\Users\{os.getlogin()}\Documents\EscapedShadows"):
        os.mkdir(rf"C:\Users\{os.getlogin()}\Documents\EscapedShadows")

    if not os.path.isdir(rf"C:\Users\{os.getlogin()}\Documents\EscapedShadows\PlaylistCreator"):
        os.mkdir(rf"C:\Users\{os.getlogin()}\Documents\EscapedShadows\PlaylistCreator")

    if not os.path.isdir(rf"C:\Users\{os.getlogin()}\Documents\EscapedShadows\PlaylistCreator\{playlistname.get()}"):
        os.mkdir(rf"C:\Users\{os.getlogin()}\Documents\EscapedShadows\PlaylistCreator\{playlistname.get()}")

    for link in links:
        vId = get_id(link)
        if os.path.isfile(rf"C:\Users\{os.getlogin()}\Documents\EscapedShadows\PlaylistCreator\{playlistname.get()}\{vId}.mp3"):
            links.remove(link)

    return links

def create_playlist_handler():
    feedbacklabel.set(0)
    threading.Thread(target=create_playlist).start()

def create_playlist():
    links = prepare_playlist()

    ids = []

    for link in links:
        ids.append(get_id(link))

    streams = get_tracks(links)

    intervalls = 1 / len(ids)

    current = 0

    for i, stream in enumerate(streams):
        mp4_file = stream.download(output_path=rf"C:\Users\{os.getlogin()}\Documents\EscapedShadows\PlaylistCreator\{playlistname.get()}")
        os.rename(mp4_file, rf"C:\Users\{os.getlogin()}\Documents\EscapedShadows\PlaylistCreator\{playlistname.get()}\{ids[i]}.mp3")
        current += intervalls
        feedbacklabel.set(current)

    os.system(rf"explorer C:\Users\{os.getlogin()}\Documents\EscapedShadows\PlaylistCreator\{playlistname.get()}")

def add_song():

    title = get_titles([addsong.get()])

    title = title[0]

    max_length = window_width // 8
    if len(title) > max_length:
        title = title[:max_length-3] + "..."

    label = ctk.CTkLabel(songlist, text=title)
    label.custom_data = {}
    label.custom_data["url"] = addsong.get()
    check = ctk.CTkCheckBox(songlist, text="Use")
    check.select()

    row = songlist.grid_size()[1]
    label.grid(row=row, column=0, sticky='w', padx=10)
    check.grid(row=row, column=1, sticky='w', padx=10)

def use_browser():
    threading.Thread(target=handle_browser).start()

playlistname = ctk.CTkEntry(root, placeholder_text="Enter Playlist Name")
playlistname.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

createplaylist = ctk.CTkButton(root, text="Create Playlist", command=create_playlist_handler)
createplaylist.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

addsong = ctk.CTkEntry(root, placeholder_text="Add Song URL here...")
addsong.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

addsongbutton = ctk.CTkButton(root, text="Add Song", command=add_song)
addsongbutton.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

usebrowser = ctk.CTkButton(root, text="Use Browser", command=use_browser)
usebrowser.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

feedbacklabel = ctk.CTkProgressBar(root)
feedbacklabel.grid(row=3, column=0, columnspan=2, padx=10, sticky='ew')

songlist = ctk.CTkScrollableFrame(root, height=window_height, width=window_width - 50)
songlist.grid(row=4, column=0, columnspan=2, pady=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(4, weight=1)

root.mainloop()