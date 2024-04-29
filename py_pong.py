import tkinter as tk
from tkinter import ttk
import random

# Constants
WIDTH = 600
HEIGHT = 400
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_SIZE = 20
INITIAL_BALL_SPEED = 2
BALL_SPEED_INCREMENT = 0.5
INITIAL_LIVES = 2
MAX_LIVES = 3
POINTS_TO_EXTRA_LIFE = 50

# Initialize the tkinter window
root = tk.Tk()
root.title("PyPong")

# Create a canvas for drawing
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Create the paddle
paddle = canvas.create_rectangle(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT,
                                 WIDTH // 2 + PADDLE_WIDTH // 2, HEIGHT, fill="white")

# Initialize ball position and velocity
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.choice([-1, 1]) * INITIAL_BALL_SPEED
ball_dy = -INITIAL_BALL_SPEED

# Create the ball
ball = canvas.create_oval(ball_x - BALL_SIZE // 2, ball_y - BALL_SIZE // 2,
                          ball_x + BALL_SIZE // 2, ball_y + BALL_SIZE // 2, fill="white")

# Difficulty selection
selected_difficulty = tk.StringVar()
selected_difficulty.set("Medium")  # Default value
difficulty_frame = tk.Frame(root, bg="black")
difficulty_frame.pack(pady=10)
difficulty_label = tk.Label(difficulty_frame, text="Select Difficulty:", fg="white", bg="black")
difficulty_label.grid(row=0, column=0)
difficulties = ["Low", "Medium", "Hard"]
for i, difficulty in enumerate(difficulties):
    tk.Radiobutton(difficulty_frame, text=difficulty, variable=selected_difficulty, value=difficulty, bg="black", fg="white").grid(row=0, column=i+1)

# Function to start the game
def start_game():
    # Hide landing page elements
    highest_score_label.pack_forget()
    play_button.pack_forget()
    difficulty_frame.pack_forget()
    lives_label.pack()
    score_label.pack()
    # Start the game
    move_ball()

# Play button
play_button = tk.Button(root, text="Play", command=start_game)
play_button.pack()

# Highest score
highest_score = 0
highest_score_label = tk.Label(root, text=f"Highest Score: {highest_score}", fg="white", bg="black")

# Score and lives
score = 0
score_label = tk.Label(root, text=f"Score: {score}", fg="white", bg="black")
lives = INITIAL_LIVES
lives_label = tk.Label(root, text=f"Lives: {lives}", fg="white", bg="black")

# Function to move the ball
def move_ball():
    global ball_x, ball_y, ball_dx, ball_dy, score, lives
    ball_x += ball_dx
    ball_y += ball_dy
    # Bounce off the walls
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1
    # Bounce off the paddle
    if ball_y >= HEIGHT - PADDLE_HEIGHT and ball_x >= canvas.coords(paddle)[0] and ball_x <= canvas.coords(paddle)[2]:
        ball_dy *= -1
        score += 1
        score_label.config(text=f"Score: {score}")
        # Increase speed every 5 points
        if score % 5 == 0:
            ball_dx *= 1.1
            ball_dy *= 1.1
        # Check for extra life
        if score % POINTS_TO_EXTRA_LIFE == 0 and lives < MAX_LIVES:
            lives += 1
            lives_label.config(text=f"Lives: {lives}")
    # Check for game over
    if ball_y >= HEIGHT:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")
        if lives == 0:
            game_over()
        else:
            reset_ball()
    # Update ball position
    canvas.coords(ball, ball_x - BALL_SIZE // 2, ball_y - BALL_SIZE // 2,
                  ball_x + BALL_SIZE // 2, ball_y + BALL_SIZE // 2)
    # Move the ball again after a delay
    canvas.after(10, move_ball)

# Function to move the paddle
def move_paddle(event):
    if event.keysym == "Left" and canvas.coords(paddle)[0] > 0:
        canvas.move(paddle, -10, 0)
    elif event.keysym == "Right" and canvas.coords(paddle)[2] < WIDTH:
        canvas.move(paddle, 10, 0)

# Bind arrow keys to move the paddle
canvas.bind_all("<KeyPress-Left>", move_paddle)
canvas.bind_all("<KeyPress-Right>", move_paddle)

# Function to reset the ball position
def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_dx = random.choice([-1, 1]) * INITIAL_BALL_SPEED
    ball_dy = -INITIAL_BALL_SPEED

# Function for game over
def game_over():
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 24), anchor="center")
    # Record score as recent score
    recent_score = score
    if recent_score > highest_score:
        highest_score_label.config(text=f"Highest Score: {recent_score}")
    # Show landing page elements
    highest_score_label.pack()
    play_button.pack()
    difficulty_frame.pack()

root.mainloop()
