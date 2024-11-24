from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(r"assets\frame7")

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
image_1 = canvas.create_image(640.0, 71.0, image=image_image_1)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(96.0, 71.0, image=image_image_7)

def cal_button_click():
    print("Home Button clicked!")
    window.destroy()
    subprocess.run(["python", "calendar_page.py"])

cal_button = Button(
    window,
    image=image_image_7,
    bg="#FBE85B",
    activebackground="#FBE85B",
    command=cal_button_click,
    relief="flat",
    width=421,
    height=153,
    bd=0,
    highlightthickness=0
)
canvas.create_window(96.0, 71.0, window=cal_button)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(324.0, 495.0, image=image_image_3)

def koli_button_click():
    print("Koli Button clicked!")
    window.destroy()
    subprocess.run(["python", "culture_a.py"])

koli_button = Button(
    window,
    image=image_image_3,
    bg="#FBE85B",
    activebackground="#FBE85B",
    command=koli_button_click,
    relief="flat",
    width=421,
    height=153,
    bd=0,
    highlightthickness=0
)
canvas.create_window(324.0, 495.0, window=koli_button)

canvas.create_rectangle(
    -2.0,
    149.99990872274202,
    1280.0001220703125,
    152.05078125,
    fill="#F36302",
    outline=""
)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(983.0, 495.0, image=image_image_5)

def konk_button_click():
    print("Konk Button clicked!")
    window.destroy()
    subprocess.run(["python", "culture_b.py"])

konk_button = Button(
    window,
    image=image_image_5,
    bg="#FBE85B",
    activebackground="#FBE85B",
    command=konk_button_click,
    relief="flat",
    width=421,
    height=153,
    bd=0,
    highlightthickness=0
)
canvas.create_window(983.0, 495.0, window=konk_button)

window.resizable(False, False)
window.mainloop()
