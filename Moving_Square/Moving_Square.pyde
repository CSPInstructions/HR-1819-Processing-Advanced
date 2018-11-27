def setup():
    # Make sure that variables are accesible everywhere
    global square, isDragging, dragStart
    
    # Create a square
    square = { 'positionX': 15, 'positionY': 15, 'size': 200 }
    
    # Initialize dragging variables
    isDragging = False
    dragStart = None
    
    # Change the size of the screen
    size(500, 500)
    
def draw():
    # Reset the screen
    clear()
    
    # Draw the square
    rect(square['positionX'], square['positionY'], square['size'], square['size'])
    
def mousePressed():
    # Make sure that we can edit variables
    global isDragging, dragStart
    
    # Check whether the X's collide
    if square['positionX'] < mouseX < square['positionX'] + square['size']:
        # Check whether the Y's collide
        if square['positionY'] < mouseY < square['positionY'] + square['size']:
            # Change the dragging variables
            isDragging = True
            dragStart = (square['positionX'], square['positionY'], mouseX, mouseY)
        
def mouseReleased():
    # Make sure that we can edit variables
    global isDragging, dragStart
    
    # Change the dragging variables
    isDragging = False
    mouseStart = None
    
def mouseDragged():
    # Check whether we are dragging the square
    if isDragging:
        # Change the position of the square
        square['positionX'] = dragStart[0] - (dragStart[2] - mouseX)
        square['positionY'] = dragStart[1] - (dragStart[3] - mouseY)
