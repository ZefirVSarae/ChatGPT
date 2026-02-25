import tkinter as tk
from tkinterweb import HtmlFrame
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os
import sys

class GeminiApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gemini Desktop")
        self.root.geometry("1200x800")
        
        try:
            self.set_app_icon("https://www.gstatic.com/lamda/images/favicon_v2_180x180.png")
        except:
            pass
        
        self.frame = HtmlFrame(self.root)
        self.frame.load_website("https://gemini.google.com")
        self.frame.pack(fill="both", expand=True)

    def set_app_icon(self, url):
        response = requests.get(url, timeout=5)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        self.photo = ImageTk.PhotoImage(img)
        self.root.iconphoto(False, self.photo)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GeminiApp()
    app.run()
  
