from tkinter import *
import random
import time
from practice_texts import practice_texts

GREY = "#5C6672"
GREEN = "#49E750"
FONT = ("Arial", 14)
PRACTICE_TEXT_FONT = ("Arial", 24)
RESULT_FONT = ("Arial", 18, "bold")

start_time = None
finish_time = None
practice_text = ""


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
    global practice_text, start_time

    practice_text = random.choice(practice_texts)
    practice_text_label.config(text=practice_text)
    practice_text_textfield.delete(1.0, END)
    results_label.config(text="")
    start_time = None


def on_first_key(event):
    """Start timer on first keystroke in the text area"""
    global start_time

    if start_time is None:
        start_time = time.time()


def finish():
    """Stop timer"""
    global start_time, finish_time, practice_text

    # Check typing accuracy
    typed_words = practice_text_textfield.get(1.0, END).split()
    practice_words = practice_text.split()
    correct_words = sum(1 for a, b in zip(typed_words, practice_words) if a == b)
    accuracy = (correct_words / len(practice_words)) * 100

    # Work out the writing time and format it to display
    writing_time = None
    if start_time is not None:
        finish_time = time.time()
        writing_time = finish_time - start_time

    if writing_time is not None:

        if writing_time > 60:
            mins, secs = divmod(writing_time, 60)
            results_label.config(text=f"Finished in {int(mins)}:{int(secs):02d} / Accuracy: {accuracy:.1f} %")
        else:
            results_label.config(text=f"Finished in {round(writing_time)} seconds / Accuracy: {accuracy:.1f} % ")


# ------------------------------------------------------ UI SETUP ------------------------------------------------------
app = Tk()
app.title("Typing Speed Test")
app.config(padx=15, pady=25, bg=GREY, width=800, height=350)
app.resizable(width=False, height=False)
center_window(app, 800, 350)

# Practice Text  and Text Field
practice_text_label = Label(text="", font=PRACTICE_TEXT_FONT, background=GREY, foreground="white")
practice_text_textfield = Text(bg="white", fg="black", font=PRACTICE_TEXT_FONT, padx=5, pady=5, wrap="word")
practice_text_label.place(x=340, y=30, anchor='center')
practice_text_textfield.place(x=0, y=190, anchor='w', width=770, height=150)
practice_text_textfield.bind("<Key>", on_first_key)

# Refresh Text Button
refresh_text_button = Button(text="Refresh Text", command=refresh_text, font=FONT, highlightbackground=GREY)
refresh_text_button.place(x=0, y=290, anchor='w', width=120)

# Finish Button
finish_button = Button(text="Finish", command=finish, font=FONT, highlightbackground=GREY)
finish_button.place(x=120, y=290, anchor='w', width=120)

# Results Label
results_label = Label(font=RESULT_FONT, background=GREY, foreground=GREEN)
results_label.config(text="RRR")
results_label.place(x=250, y=290, anchor='w')

# Load practice text when program loads
refresh_text()

app.mainloop()

