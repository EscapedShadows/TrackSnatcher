import customtkinter as ctk
import ctypes

width, height = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
width, height = int(width/3), int(height/3)

posX, posY = int(ctypes.windll.user32.GetSystemMetrics(0)/2), int(ctypes.windll.user32.GetSystemMetrics(1)/2)
posX, posY = posX - int(width/2), posY - int(height/2)

root = ctk.CTk()
root.title("TrackSnatcher | EscapedShadows")
root.geometry(f"{width}x{height}+{width}+{height}")



root.mainloop()