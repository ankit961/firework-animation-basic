import turtle
import random
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fireworks Animation")
screen.setup(width=800, height=600)

# Create turtle for fireworks
firework = turtle.Turtle()
firework.speed(0)
firework.hideturtle()

colors = ["red", "blue", "green", "yellow", "purple", "orange", "white", "pink"]

def explode_firework(x, y):
    """Function to create a firework explosion at given coordinates (x, y)."""
    firework.penup()
    firework.goto(x, y)
    firework.pendown()
    color = random.choice(colors)
    firework.color(color)
    
    # Create explosion effect
    for _ in range(36):  # 36 particles
        firework.forward(50)
        firework.backward(50)
        firework.right(10)

def random_fireworks():
    """Generate fireworks at random positions on the screen."""
    for _ in range(10):  # 10 fireworks in total
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        explode_firework(x, y)
        time.sleep(0.5)  # Pause between each firework

# Main loop
random_fireworks()

# End program on click
screen.exitonclick()
