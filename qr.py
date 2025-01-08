import qrcode
# import tkinter as tk
img = qrcode.make("https://i.pinimg.com/736x/22/3a/2b/223a2b9e3de478e34ebe308748015f71.jpg")
img.save('thepotatoeaters.png')