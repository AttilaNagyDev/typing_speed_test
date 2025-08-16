from tkinter import *
import random
import time
from practice_texts import practice_texts

GREY = "#5C6672"
FONT = ("Arial", 14)
PRACTICE_TEXT_FONT = ("Arial", 24)

start_time = None


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


# ------------------------------------------------- TYPING SPEED TEST --------------------------------------------------
def refresh_text():
    """Refreshes test practice text and clears textarea"""
    practice_text = practice_texts[random.randint(0, len(practice_texts)-1)]
    practice_text_label.config(text=practice_text)
    practice_text_textfield.delete(1.0, END)


def on_first_key(event):
    """Start timer on first keystroke in the text area"""
    global start_time

    if start_time is None:
        start_time = time.time()
        print(start_time)


# ------------------------------------------------------ UI SETUP ------------------------------------------------------
app = Tk()
app.title("Typing Speed Test")
app.config(padx=15, pady=25, bg=GREY, width=800, height=400)
app.resizable(width=False, height=False)
center_window(app, 800, 400)

# Practice Text  and Text Field
practice_text_label = Label(text="", font=PRACTICE_TEXT_FONT, background=GREY, foreground="white")
practice_text_textfield = Text(bg="white", fg="black", font=PRACTICE_TEXT_FONT, padx=5, pady=5)
refresh_text()
practice_text_label.place(x=340, y=40, anchor='center')
practice_text_textfield.place(x=0, y=200, anchor='w', width=770, height=150)
practice_text_textfield.bind("<Key>", on_first_key)

# Refresh Text Button
refresh_text_button = Button(text="Refresh Text", command=refresh_text, font=FONT, highlightbackground=GREY)
refresh_text_button.place(x=0, y=300, anchor='w', width=150)

app.mainloop()

