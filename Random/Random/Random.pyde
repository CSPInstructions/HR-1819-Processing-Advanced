# Get access to bibliotheken
import random

# Make sure that the randomint function is easy to access
newRandom = random.randint

def setup():
    # Change the size of the screen
    size(250, 250)

def draw():
    # Create random values for a square
    randomX = newRandom(0, 50)
    randomY = newRandom(0, 50)
    randomWidth = newRandom(0, 200)
    randomHeight = newRandom(0, 200)
    
    # Create random values for colors
    randomColorR = newRandom(0, 255)
    randomColorG = newRandom(0, 255)
    randomColorB = newRandom(0, 255)
    
    # Fill the figures with the random color
    fill(randomColorR, randomColorG, randomColorB)
    
    # Draw a rectangle with the random values
    rect(randomX, randomY, randomWidth, randomHeight)
