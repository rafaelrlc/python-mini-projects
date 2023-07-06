from tkinter import *
import math, time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


def cronometro_pomodoro(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds == 0:
        count_seconds = f"0{count_seconds}"
    if count_minutes == 0:
        count_seconds = f"0{count_minutes}"
    cronometro.itemconfig(timer, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global loop_timer
        loop_timer = window.after(1000, cronometro_pomodoro, count - 1)
    else:
        timer_type()



def reset():
    global reps
    reps = 0
    window.after_cancel(loop_timer)
    cronometro.itemconfig(timer, text="00:00")
    upper_text.config(text="Timer")
    #resetar check marks



def timer_type():
    time.sleep(0.5)
    global reps
    reps += 1
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        upper_text.config(text="Work", foreground=GREEN)
        cronometro_pomodoro(WORK_MIN * 60)

        # check mark
    elif reps == 2 or reps == 4 or reps == 6:
        upper_text.config(text="Break", foreground=PINK)

        cronometro_pomodoro(SHORT_BREAK_MIN * 60)
    elif reps == 8:
        upper_text.config(text="Break", foreground=PINK)
        cronometro_pomodoro(LONG_BREAK_MIN * 60)
        reps = 0  # reseta reps


# WINDOW
window = Tk()
window.title("Pomorodoaaa")
window.config(padx=100, pady=80, background=YELLOW)

# LABELS
upper_text = Label(text="Timer", font=("Courier", 50), background=YELLOW, foreground=PINK)
upper_text.grid(column=1, row=0)

cronometro = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
cronometro.create_image(100, 112, image=tomato_img)
timer = cronometro.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
cronometro.grid(column=1, row=1)



# BUTTONS
start_button = Button(text="Start", highlightbackground=YELLOW, command=timer_type, width=3, height=1)
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset, width=3, height=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

# CHECK MARK
check_marks = Label(text="", foreground=GREEN, background=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
