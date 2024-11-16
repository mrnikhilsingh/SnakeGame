import turtle  # Import the turtle graphics module
import time  # Import the time module for handling delays
import random  # Import the random module for generating random positions for the food

# Initial delay for the game speed
delay = 0.1

# Initial score values
score = 0  # Current score of the player
high_score = 0  # Highest score achieved

# Setting up the screen
wn = turtle.Screen()  # Create a screen object
wn.title("Snake Game")  # Set the title of the window
wn.bgcolor("lightblue")  # Set the background color of the window
wn.setup(width=600, height=600)  # Set the dimensions of the window
wn.tracer(0)  # Turn off automatic screen updates to manually control updates

# Creating the snake's head
head = turtle.Turtle()  # Create a turtle object for the snake's head
head.speed(0)  # Animation speed of the turtle (0 = fastest)
head.shape("square")  # Set the shape of the head to square
head.color("black")  # Set the color of the head
head.penup()  # Prevent drawing lines as the head moves
head.goto(0, 0)  # Start the head at the center of the screen
head.direction = "stop"  # Initial direction of the head is stopped

# Creating the food
food = turtle.Turtle()  # Create a turtle object for the food
food.speed(0)  # Animation speed of the turtle (0 = fastest)
food.shape("circle")  # Set the shape of the food to circle
food.color("red")  # Set the color of the food
food.penup()  # Prevent drawing lines as the food moves
food.goto(0, 100)  # Start the food at a fixed position on the screen

# List to hold snake segments (body parts)
segments = []

# Creating the pen for displaying the score
pen = turtle.Turtle()  # Create a turtle object for the pen
pen.speed(0)  # Animation speed of the turtle (0 = fastest)
pen.shape("square")  # Set the shape of the pen (not visible)
pen.color("white")  # Set the color of the pen text
pen.penup()  # Prevent drawing lines
pen.hideturtle()  # Hide the turtle cursor
pen.goto(0, 260)  # Position the pen at the top center of the screen
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))  # Initial score display

# Functions to handle snake movement
def go_up():
    if head.direction != "down":  # Prevent the snake from moving in the opposite direction
        head.direction = "up"  # Change the direction to up

def go_down():
    if head.direction != "up":  # Prevent the snake from moving in the opposite direction
        head.direction = "down"  # Change the direction to down

def go_left():
    if head.direction != "right":  # Prevent the snake from moving in the opposite direction
        head.direction = "left"  # Change the direction to left

def go_right():
    if head.direction != "left":  # Prevent the snake from moving in the opposite direction
        head.direction = "right"  # Change the direction to right

# Function to move the snake
def move():
    if head.direction == "up":  # If the direction is up
        y = head.ycor()  # Get the current y-coordinate
        head.sety(y + 20)  # Move the head up by 20 pixels

    if head.direction == "down":  # If the direction is down
        y = head.ycor()  # Get the current y-coordinate
        head.sety(y - 20)  # Move the head down by 20 pixels

    if head.direction == "left":  # If the direction is left
        x = head.xcor()  # Get the current x-coordinate
        head.setx(x - 20)  # Move the head left by 20 pixels

    if head.direction == "right":  # If the direction is right
        x = head.xcor()  # Get the current x-coordinate
        head.setx(x + 20)  # Move the head right by 20 pixels

# Keyboard bindings to control the snake
wn.listen()  # Listen for keyboard input
wn.onkeypress(go_up, "w")  # Call go_up when "w" is pressed
wn.onkeypress(go_down, "s")  # Call go_down when "s" is pressed
wn.onkeypress(go_left, "a")  # Call go_left when "a" is pressed
wn.onkeypress(go_right, "d")  # Call go_right when "d" is pressed

# Adding bindings for arrow keys
wn.onkeypress(go_up, "Up")  # Call go_up when the up arrow key is pressed
wn.onkeypress(go_down, "Down")  # Call go_down when the down arrow key is pressed
wn.onkeypress(go_left, "Left")  # Call go_left when the left arrow key is pressed
wn.onkeypress(go_right, "Right")  # Call go_right when the right arrow key is pressed

# Main game loop
while True:
    wn.update()  # Update the screen

    # Check for collision with the borders
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)  # Pause the game for a second
        head.goto(0, 0)  # Move the head back to the starting position
        head.direction = "stop"  # Stop the head's movement

        # Hide the body segments
        for segment in segments:
            segment.goto(1000, 1000)  # Move the segment off the screen

        segments.clear()  # Clear the segments list

        # Reset the score and delay
        score = 0
        delay = 0.1

        # Update the score display
        pen.clear()  # Clear the previous score
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for collision with the food
    if head.distance(food) < 20:
        # Move the food to a random position
        x = random.randint(-290, 290)  # Generate a random x-coordinate
        y = random.randint(-290, 290)  # Generate a random y-coordinate
        food.goto(x, y)  # Move the food to the new position

        # Add a new segment to the snake's body
        new_segment = turtle.Turtle()  # Create a new turtle object
        new_segment.speed(0)  # Animation speed of the turtle (0 = fastest)
        new_segment.shape("square")  # Set the shape of the segment to square
        new_segment.color("grey")  # Set the color of the segment
        new_segment.penup()  # Prevent drawing lines
        segments.append(new_segment)  # Add the segment to the list

        # Shorten the delay to increase the game speed
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:  # Check if the current score is greater than the high score
            high_score = score  # Update the high score

        pen.clear()  # Clear the previous score display
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()  # Get the x-coordinate of the previous segment
        y = segments[index - 1].ycor()  # Get the y-coordinate of the previous segment
        segments[index].goto(x, y)  # Move the current segment to the previous segment's position

    # Move segment 0 to the position of the head
    if len(segments) > 0:
        x = head.xcor()  # Get the x-coordinate of the head
        y = head.ycor()  # Get the y-coordinate of the head
        segments[0].goto(x, y)  # Move segment 0 to the head's position

    move()  # Move the snake

    # Check for collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:  # Check if the head collides with any segment
            time.sleep(1)  # Pause the game for a second
            head.goto(0, 0)  # Move the head back to the starting position
            head.direction = "stop"  # Stop the head's movement

            # Hide the body segments
            for segment in segments:
                segment.goto(1000, 1000)  # Move the segment off the screen

            segments.clear()  # Clear the segments list

            # Reset the score and delay
            score = 0
            delay = 0.1

            # Update the score display
            pen.clear()  # Clear the previous score display
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)  # Pause the loop to control the game speed

wn.mainloop()  # Keep the window open
