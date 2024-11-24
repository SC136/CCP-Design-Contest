from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(r"assets\frame4")

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
image_1 = canvas.create_image(683.0, 77.0, image=image_image_1)

canvas.create_rectangle(
    -2.0,
    149.99990872274202,
    1280.0001220703125,
    152.05078125,
    fill="#F36302",
    outline=""
)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(58.0, 76.0, image=image_image_2)

def home_button_click():
    print("Button clicked!")
    window.destroy()
    subprocess.run(["python", "home.py"])

home_button = Button(
    window,
    image=image_image_2,
    bg="#FBE85B",
    activebackground="#FBE85B",
    command=home_button_click,
    relief="flat",
    width=80,
    height=80,
    bd=0,
    highlightthickness=0
)

long_text = (
    "The Kokani community, native to the Konkan region of Maharashtra, Goa,\n and parts of Karnataka,"
    "has a rich cultural heritage tied to fishing, agriculture, and coastal life.\n"
    "They celebrate festivals like Narli Purnima, Ganesh Chaturthi, and Kokani New Year,\n"
    "marked by vibrant rituals, folk dances, and music.\n"
    "The cuisine, including dishes like Kokani Fish Curry and Sol Kadhi,\n"
    "reflects their coastal environment.\n"
    "The Kokanis are known for their strong sense of community and deep respect for nature,\n"
    "maintaining traditions passed down through generations."
)

wrapped_text = "\n".join(long_text.split("\n"))

canvas.create_text(
    640, 360,
    text=wrapped_text,
    fill="black",
    font=("Tempus Sans ITC", 22, "bold"),
    anchor="center"
)

canvas.create_window(58.0, 74.0, window=home_button)

window.resizable(False, False)
window.mainloop()
