import tkinter as tk
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode
from PIL import Image,ImageTk


def QRCODE():
    url = Enter_URL.get()

    if url:
        QR_url = pyqrcode.create(url)
        File_Address = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG dosyaları", "*.svg")])

        if File_Address:
            with open(File_Address, 'wb') as f:  # Open the file in binary write mode
                QR_url.svg(f, scale=8)
            Ans_TAG.config(text="QRCODE IS SUCCESSFULLY CREATED!!")
            


App_Window = tk.Tk()
App_Window.title("QR_Code Maker")

Enter_TAG = tk.Label(App_Window,text="Enter URL :")
Enter_URL = tk.Entry(App_Window,width=40)
QR_CODE_Create_BTN = tk.Button(App_Window,text="Create QRCODE",command=QRCODE)
Ans_TAG = tk.Label(App_Window,text="")

Image_path = "Scan_me.jpg"
Img = Image.open(Image_path)
Img = Img.resize((100,100))
photo = ImageTk.PhotoImage(Img)
Image_label = tk.Label(App_Window,image=photo)

Enter_TAG.grid(row=0,column=0,padx=10,pady=10)
Enter_URL.grid(row=0,column=1,padx=10,pady=10)
QR_CODE_Create_BTN.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
Ans_TAG.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
Image_label.grid(row=1, column=0)


App_Window.mainloop()


