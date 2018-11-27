# Create variables for the position of the star
starX = 0
starY = 0

def setup():
    # Create a local variable for photo
    global photo
    
    # Change the size of the screen
    size(250, 250)
    
    # Load the star image
    photo = loadImage("star.png")
    
def draw():
    # Make sure that we can edit the global variables
    global starX, starY
    
    # Clear the screen
    clear()

    # Draw the star
    image(photo, starX, starY, 75, 75)
    
    # Check for keyboardinput
    if (keyPressed):
        # Check for W
        if (key in ["w", "W"]):
            # Make the star go up
            starY = starY - 1
        
        # Check for S
        if (key in ["s", "S"]):
            # Make the star go down
            starY = starY + 1
        
        # Check for A
        if (key in ["a", "A"]):
            # Make the star go left
            starX = starX - 1
            
        # Check for D
        if (key in ["d", "D"]):
            # Make the star go right
            starX = starX + 1
    
    
    
