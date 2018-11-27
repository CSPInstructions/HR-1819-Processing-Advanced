def setDragging(dragStartValue):
    # Access global variables
    global isDragging, dragStart
    
    # Change the values
    isDragging = dragStartValue != None
    dragStart = dragStartValue
    
def changeSquarePosition(positionX, positionY, size = 200):
    # Access global variables
    global square
    
    # Change the square
    square = { 'positionX': positionX, 'positionY': positionY, 'size': size }

def setup():
    # Set the square to the starting position
    changeSquarePosition(15, 15)
    
    # Change the dragging settings
    setDragging(None)
    
    # Change the size of the screen
    size(500, 500)
    
def draw():
    # Reset the screen
    clear()
    
    # Draw the square
    rect(square['positionX'], square['positionY'], square['size'], square['size'])
    
def mousePressed():
    # Check whether the X's collide
    if square['positionX'] < mouseX < square['positionX'] + square['size']:
        # Check whether the Y's collide
        if square['positionY'] < mouseY < square['positionY'] + square['size']:
            # Change the dragging settings
            setDragging( (square['positionX'], square['positionY'], mouseX, mouseY) )
        
def mouseReleased():
    # Change the dragging settings
    setDragging(None)
    
def mouseDragged():
    # Check whether we are dragging the square
    if isDragging:
        # Change the position of the square
        changeSquarePosition(dragStart[0] - (dragStart[2] - mouseX), dragStart[1] - (dragStart[3] - mouseY))
