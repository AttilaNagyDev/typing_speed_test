from tkinter import *

GREY = "#5C6672"
FONT = ("Arial", 14)


# ---------------------------------------------- CENTER WINDOW ON SCREEN -----------------------------------------------
def center_window(window, width, height):
    """Gets screen size and positions program window in the middle of the screen"""

    # Get screen Width and Height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate position X and Y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    # Set window size and its position
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


# ------------------------------------------------------ UI SETUP ------------------------------------------------------
app = Tk()
app.title("Typing Speed Test")
app.config(padx=25, pady=35, bg=GREY, width=800, height=400)
app.resizable(width=False, height=False)
center_window(app, 800, 400)

app.mainloop()
