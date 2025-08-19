from tkinter import *
import random
import time
from practice_texts import practice_texts

GREY = "#5C6672"
GREEN = "#49E750"
FONT = ("Arial", 14)
PRACTICE_TEXT_FONT = ("Arial", 24)
RESULT_FONT = ("Arial", 18, "bold")

practice_text = ""
disable_writing = None
announce_result = None


# ---------------------------------------------- CENTER WINDOW ON SCREEN -----------------------------------------------
def center_window(window, width, height):
    """Gets screen size and positions program window in the middle of the screen"""

    # Get screen Width and Height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate position X and Y coordinates
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set window size and its position
    window.geometry(f"{width}x{height}+{x}+{y}")


# ------------------------------------------------- TYPING SPEED TEST --------------------------------------------------
def refresh_text():
    """Refreshes test practice text and clears textarea"""
    global practice_text, disable_writing, announce_result

    # Cancel scheduled events if they exist
    if 'disable_writing' in globals() and disable_writing:
        app.after_cancel(disable_writing)
        disable_writing = None
    if 'announce_result' in globals() and announce_result:
        app.after_cancel(announce_result)
        announce_result = None

    practice_text = random.choice(practice_texts)
    practice_text_message.config(text=practice_text)
    practice_text_textfield.config(state="normal")
    practice_text_textfield.delete(1.0, END)
    results_label.config(text="")


def on_first_key(event):
    """Start timer on first keystroke in the text area,
    then after 60 seconds disables text area and calls announcement"""
    global disable_writing, announce_result

    disable_writing = app.after(60000, lambda: practice_text_textfield.config(state="disabled"))
    announce_result = app.after(62000, announcement)


def announcement():
    """Checks accuracy and announce result"""
    global practice_text

    # Check typing accuracy by taking the number of written words into account
    typed_words = practice_text_textfield.get(1.0, END).split()
    nr_of_typed_words = len(typed_words)
    practice_words = practice_text.split()[:nr_of_typed_words]
    correct_words = sum(1 for a, b in zip(typed_words, practice_words) if a == b)
    accuracy = (correct_words / len(practice_words)) * 100
    results_label.config(text=f"Your WPM is: {nr_of_typed_words}   Accuracy: {accuracy:.1f} % ")


# ------------------------------------------------------ UI SETUP ------------------------------------------------------
app = Tk()
app.title("Typing Speed Test")
app.config(padx=10, pady=10, bg=GREY)
app.resizable(width=False, height=False)
center_window(app, 1000, 600)

# Practice Text  and Text Field
practice_text_message = Message(text="", font=PRACTICE_TEXT_FONT, background=GREY, foreground="white", width=950)
practice_text_textfield = Text(bg="white", fg="black", font=PRACTICE_TEXT_FONT, padx=5, pady=5, wrap="word")
practice_text_message.place(x=0, y=0, anchor='nw')
practice_text_textfield.place(x=5, y=395, anchor='w', width=970, height=280)
practice_text_textfield.bind("<Key>", on_first_key)

# Refresh Text Button
refresh_text_button = Button(text="Refresh Text", command=refresh_text, font=FONT, highlightbackground=GREY)
refresh_text_button.place(x=5, y=560, anchor='w', width=120)

# Results Label
results_label = Label(font=RESULT_FONT, background=GREY, foreground=GREEN)
results_label.place(x=150, y=560, anchor='w')

# Load practice text when program loads
refresh_text()

app.mainloop()

