from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(r"assets\frame0")

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
image_1 = canvas.create_image(639.0, 55.0, image=image_image_1)

canvas.create_rectangle(
    -2.0,
    138.94912747274213,
    1280.0001220703125,
    141.0,
    fill="#F36302",
    outline=""
)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(70.0, 68.0, image=image_image_2)

def home_button_click():
    print("Home Button clicked!")
    window.destroy()
    subprocess.run(["python", "home.py"])

home_button = Button(
    window,
    image=image_image_2,
    bg="#FBE85B",
    activebackground="#FBE85B",
    command=home_button_click,
    width=80,
    height=80,
    bd=0,
    highlightthickness=0
)

canvas.create_window(70.0, 68.0, window=home_button)

from data.events import events

total_labels_height = len(events) * 30
canvas_height = 720
y_start_position = (canvas_height - total_labels_height) // 2
gap_between_labels = 10

for index, event in enumerate(events):
    label_text = f"{event['date']}: {event['event_name']} ({event['region']}) "
    
    label_width = 200
    canvas_width = 1280
    x_position = (canvas_width - label_width) // 4.5
    
    y_position = y_start_position + index * (50 + gap_between_labels)
    
    canvas.create_text(x_position, y_position, text=label_text, fill="black", font=("Segoe UI", 20, "bold"), anchor="w")

window.resizable(False, False)
window.mainloop()
