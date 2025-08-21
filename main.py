from tkinter import *
import random
import math
from practice_texts import practice_texts

GREY = "#5C6672"
GREEN = "#49E750"
FONT = ("Arial", 14)
PRACTICE_TEXT_FONT = ("Arial", 24)
RESULT_FONT = ("Arial", 20, "bold")
TIMER_FONT = ("Arial", 22, "bold")
practice_text = ""
disable_writing = None
announce_result = None
timer = "None"


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


def start_timer(event):
    countdown(60)
    practice_text_textfield.unbind("<Key>")


def reset_timer():
    app.after_cancel(timer)
    timer_label.config(text="1:00")


def countdown(count):
    """Counts down 60 seconds then stops the typing speed test"""

    global disable_writing, announce_result

    count_min = math.floor(count / 60)

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    timer_label.config(text=f"{count_min}:{count_sec}")  # Display the formatted time

    if count > 0:
        global timer
        timer = app.after(1000, countdown, count - 1)
    else:
        practice_text_textfield.config(state="disabled")
        announcement()


def refresh_text():
    """Refreshes test practice text and clears textarea"""
    global practice_text, disable_writing, announce_result

    # Reset timer
    reset_timer()

    # Pick another practice text and reset app to normal
    practice_text = random.choice(practice_texts)
    practice_text_message.config(text=practice_text)
    practice_text_textfield.config(state="normal")
    practice_text_textfield.delete(1.0, END)
    results_label.config(text="")
    practice_text_textfield.bind("<Key>", start_timer)


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

# Refresh Text Button
refresh_text_button = Button(text="Refresh Text", command=refresh_text, font=FONT, highlightbackground=GREY)
refresh_text_button.place(x=5, y=560, anchor='w', width=120)

# Results Label
results_label = Label(font=RESULT_FONT, background=GREY, foreground=GREEN)
results_label.place(x=500, y=547, anchor='n')

# Timer label
timer_label = Label(text="1:00", font=TIMER_FONT, background=GREY, foreground="#FF4D4D")
timer_label.place(x=925, y=559, anchor='w')

# Load practice text when program loads
refresh_text()

app.mainloop()
