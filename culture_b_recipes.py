from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(r"assets\frame3")

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
image_1 = canvas.create_image(639.0, 73.0, image=image_image_1)

canvas.create_rectangle(
    -2.0,
    150.00003079305475,
    1280.0001220703125,
    152.0509033203125,
    fill="#F36302",
    outline=""
)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(68.0, 74.0, image=image_image_2)

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

canvas.create_window(68.0, 74.0, window=home_button)

from data.recipes_b import recipes

for recipe_index, recipe in enumerate(recipes):
    recipe_x_position = 300 + recipe_index * 400 - 80
    recipe_y_position = 300

    canvas.create_text(
        recipe_x_position, recipe_y_position,
        text=recipe['name'],
        fill="black",
        font=("Samarkan", 14, "bold"),
        anchor="center"
    )
    
    ingredients_list = recipe['ingredients'].split(', ')
    for i, ingredient in enumerate(ingredients_list):
        canvas.create_text(
            recipe_x_position-80, recipe_y_position + (i + 1) * 20 + 30,
            text=ingredient,
            fill="black",
            font=("Segoe Script", 12),
            anchor="w"
        )

window.resizable(False, False)
window.mainloop()
