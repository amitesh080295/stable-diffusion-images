import tkinter as tk
import customtkinter as ctk
import torch

from PIL import ImageTk
from authtoken import auth_token
from diffusers import StableDiffusionPipeline

root = tk.Tk()
root.geometry('532x632')
root.title('Diffuse Dreams')
ctk.set_appearance_mode('dark')

prompt = ctk.CTkEntry(master=root, height=40, width=512, text_color='black', fg_color='white')
prompt.place(x=10, y=10)

lmain = ctk.CTkLabel(master=root, height=512, width=512)
lmain.place(x=10, y=110)

modelid = 'CompVis/stable-diffusion-v1-4'
device = 'cpu'
pipe = StableDiffusionPipeline.from_pretrained(modelid, use_auth_token=auth_token)
pipe.to(device)

def generate():
    image = pipe(prompt.get(), guidance_scale=8.5)['sample'][0]
    image.save('generatedimage.png')
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img)

trigger = ctk.CTkButton(master=root, height=40, width=120, text_color='white', fg_color='blue', command=generate)
trigger.configure(text='Generate')
trigger.place(x=206, y=60)

root.mainloop()
