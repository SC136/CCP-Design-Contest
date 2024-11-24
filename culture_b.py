from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(r"assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1280x720")
window.configure(bg="#FBE85B")
window.title("Cultural App")

canvas = Canvas(
    window,
    bg="#FBE85B",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(640.0, 66.0, image=image_image_1)

canvas.create_rectangle(
    -2.0,
    150.00003079305463,
    1280.0001220703125,
    152.0509033203125,
    fill="#F36302",
    outline=""
)

canvas.create_rectangle(137.0, 360.0, 513.0, 480.0, fill="#F36302", outline="")
canvas.create_rectangle(708.0, 360.0, 1144.0, 480.0, fill="#F36302", outline="")

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_2 = canvas.create_image(349.0, 419.0)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_3 = canvas.create_image(931.0, 420.0)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(106.0, 80.0, image=image_image_4)

def recipe_button_click():
    print("recipe Button clicked!")
    window.destroy()
    subprocess.run(["python", "culture_b_recipes.py"])

recipe_button = Button(
    window,
    image=image_image_5,
    bg="#FBE85B",
    activebackground="#FBE85B",
    command=recipe_button_click,
    relief="flat",
    width=376,
    height=125,
    bd=0,
    highlightthickness=0
)
canvas.create_window(325.0, 419.0, window=recipe_button)

def info_button_click():
    print("info Button clicked!")
    window.destroy()
    subprocess.run(["python", "culture_b_info.py"])

info_button = Button(
    window,
    image=image_image_6,
    bg="#FBE85B",
    activebackground="#FBE85B",
    command=info_button_click,
    relief="flat",
    width=440,
    height=125,
    bd=0,
    highlightthickness=0
)
canvas.create_window(925.0, 419.0, window=info_button)

def home_button_click():
    print("Button clicked!")
    window.destroy()
    subprocess.run(["python", "home.py"])

home_button = Button(
    window,
    image=image_image_4,
    bg="#FBE85B",
    activebackground="#FBE85B",
    command=home_button_click,
    relief="flat",
    width=80,
    height=80,
    bd=0,
    highlightthickness=0
)
canvas.create_window(106.0, 80.0, window=home_button)

window.resizable(False, False)
window.mainloop()
