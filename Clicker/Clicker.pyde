def setup():
    # Change the size of the screen
    size(250, 250)

def draw():
    # Check whether a mouse button has been pressed
    if mousePressed:
        # Check whether the right mousebutton is down
        if mouseButton == RIGHT:
            # Change the fill to black
            fill(0)
        # Check whether the left mousebutton is down
        elif mouseButton == LEFT:
            # Change the fill to white
            fill(255)
    else:
        # Make the fill grey
        fill(126)
        
    # Draw a rectangle
    rect(15, 15, 220, 220)
        
    
    
        
