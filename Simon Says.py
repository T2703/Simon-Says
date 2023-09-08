import random
import time
from tkinter import *
from tkinter import messagebox

# Variables
score = 0 
player_answer = ""
player_count = 0 
simon_choice = ["R", "G", "B", "Y"]
simon_answer = ""
simon_ready = True # Keep this true because we need it true and so simon can go first yeah? No questions!counter 
counter = 0 # The Count of MC

# This function checks for what button has been clicked.
# It returns the player's answer. 
def button_clicked(color):
    global player_answer, player_count, simon_ready 
    
    if simon_ready == False and player_count < 4:
        if color == "green":
            player_answer += "G"
            player_count += 1
        elif color == "red":
            player_answer += "R"
            player_count += 1
        elif color == "yellow":
            player_answer += "Y"
            player_count += 1
        elif color == "blue":
            player_answer += "B"
            player_count += 1

        if player_count == 4:  # Player's sequence complete
            # Disable the player's buttons after the sequence is complete
            green_button.config(state=DISABLED)
            red_button.config(state=DISABLED)
            yellow_button.config(state=DISABLED)
            blue_button.config(state=DISABLED)

            simon_ready = True  # Allow player's turn

            check_answer(player_answer, simon_answer)
            player_answer = "" # Clear everytime it is called & after the checkanswer 
            player_count = 0 

# This function checks the answer of the player and Simon.
# Simple enough.
def check_answer(player_answer: str, simon_answer: str) -> int:
    global score
    if player_answer == simon_answer:
        score += 1
        simon_turn()
        update_score_label()  # Update the score label

    elif player_answer != simon_answer:
        messagebox.showinfo("Game Over", f"Your score is {score}")
        quit()

    return score

def simon_turn():
    global simon_answer, simon_ready

    simon_answer = ""
    
    if counter < 5:  # Check if counter is less than 5:
        for _ in range(4):
            chosen_color = random.choice(simon_choice)

            if chosen_color == "G":
                simon_answer += "G"
                green_button.config(bg="black")
                time.sleep(1)
                window.update()
                time.sleep(1)
                green_button.config(bg="green")
                window.update()
            elif chosen_color == "R":
                simon_answer += "R"
                red_button.config(bg="black")
                time.sleep(1)
                window.update()
                time.sleep(1)
                red_button.config(bg="red")
                window.update()
            elif chosen_color == "Y":
                simon_answer += "Y"
                yellow_button.config(bg="black")
                time.sleep(1)
                window.update()
                time.sleep(1)
                yellow_button.config(bg="yellow")
                window.update()
            elif chosen_color == "B":
                simon_answer += "B"
                blue_button.config(bg="black")
                time.sleep(1)
                window.update()
                time.sleep(1)
                blue_button.config(bg="blue")
                window.update()

    
    simon_ready = False

    # Enable the player's buttons after Simon's turn
    green_button.config(state=NORMAL)
    red_button.config(state=NORMAL)
    yellow_button.config(state=NORMAL)
    blue_button.config(state=NORMAL)
    
    return simon_answer

def start_simon_turn(event=None):
    global simon_ready, counter

    if simon_ready:
        simon_ready = False
        counter = 0  # Reset the counter to 0
        simon_turn()

# Function to update the score label
def update_score_label():
    score_label.config(text="Score: " + str(score))
    window.update()

# Create the window
window = Tk()
window.title("Simon Says")
window.configure(bg = 'lightgray')
window.resizable(False, False)
    
canvas = Canvas(window, width = 600, height = 600)
canvas.pack()

square_size = 150  # Adjust the size of the squares as needed

canvas_width = canvas.winfo_reqwidth()
canvas_height = canvas.winfo_reqheight()

# Calculate center coordinates for the grid
center_x = (canvas_width - 2 * square_size) / 2
center_y = (canvas_height - 2 * square_size) / 2

# Create clickable square buttons
green_button = Button(canvas, bg="green", command=lambda: button_clicked("green"), state=DISABLED if simon_ready else NORMAL)
green_button.place(x=center_x, y=center_y, width=square_size, height=square_size)

red_button = Button(canvas, bg="red", command=lambda: button_clicked("red"), state=DISABLED if simon_ready else NORMAL)
red_button.place(x=center_x + square_size, y=center_y, width=square_size, height=square_size)

yellow_button = Button(canvas, bg="yellow", command=lambda: button_clicked("yellow"), state=DISABLED if simon_ready else NORMAL)
yellow_button.place(x=center_x, y=center_y + square_size, width=square_size, height=square_size)

blue_button = Button(canvas, bg="blue", command=lambda: button_clicked("blue"), state=DISABLED if simon_ready else NORMAL)
blue_button.place(x=center_x + square_size, y=center_y + square_size, width=square_size, height=square_size)


# Create a label for the score display
score_label = Label(window, text="Score: " + str(score), font=("Arial", 24))
score_label.pack()

# Bind the Enter keypress event to start Simon's turn
window.bind("<Return>", start_simon_turn)

window.mainloop()