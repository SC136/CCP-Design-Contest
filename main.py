import tkinter as tk
# from home import HomePage
import subprocess

def main():
    # root = tk.Tk()
    # root.title("Cultural App")
    # root.geometry("1280x720")
    
    # # Load the home page
    # HomePage(root)
    # root.mainloop()
    subprocess.run(["python", "home.py"])

if __name__ == "__main__":
    main()
