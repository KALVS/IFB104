
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N9918205
#    Student name: Alex Holm
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  BUILDING BLOCKS
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "stack_blocks".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a pile of building blocks
#  whose arrangement is determined by data stored in a list which
#  specifies the blocks' locations.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.
global block_size
block_size = 250 # pixels
top_and_bottom_border = 75 # pixels
left_and_right_border = 150 # pixels
canvas_width = (block_size + left_and_right_border) * 2
canvas_height = (block_size + top_and_bottom_border) * 2

#
#--------------------------------------------------------------------#



#-----Functions for Managing the Canvas------------------------------#
#
# The functions in this section are called by the main program to
# set up the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():

    # Set up the drawing canvas
    setup(canvas_width, canvas_height)

    # Set the coordinate system so that location (0, 0) is centred on
    # the point where the blocks will be stacked
    setworldcoordinates(-canvas_width / 2, -top_and_bottom_border,
                        canvas_width / 2, canvas_height - top_and_bottom_border)

    # Draw as fast as possible
    tracer(False)

    # Colour the sky blue
    bgcolor('sky blue')

    # Draw the ground as a big green rectangle (sticking out of the
    # bottom edge of the drawing canvas slightly)
    overlap = 50 # pixels
    penup()
    goto(-(canvas_width / 2 + overlap), -(top_and_bottom_border + overlap)) # start at the bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(top_and_bottom_border + overlap)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(top_and_bottom_border + overlap)
    end_fill()
    penup()

    # Draw a friendly sun peeking into the image
    goto(-canvas_width / 2, block_size * 2)
    color('yellow')
    dot(250)

    # Reset everything ready for the student's solution
    color('black')
    width(1)
    penup()
    home()
    setheading(0)
    tracer(True)


# As a debugging aid, mark the coordinates of the centres and corners
# of the places where the blocks will appear
def mark_coords(show_corners = False, show_centres = False):

    # Go to each coordinate, draw a dot and print the coordinate, in the given colour
    def draw_each_coordinate(colour):
        color(colour)
        for x_coord, y_coord in coordinates:
            goto(x_coord, y_coord)
            dot(4)
            write(' ' + str(x_coord) + ', ' + str(y_coord), font = ('Arial', 12, 'normal'))

    # Don't draw lines between the coordinates
    penup()

    # The list of coordinates to display
    coordinates = []

    # Only mark the corners if the corresponding argument is True
    if show_corners:
        coordinates = [[-block_size, block_size * 2], [0, block_size * 2], [block_size, block_size * 2],
                       [-block_size, block_size], [0, block_size], [block_size, block_size],
                       [-block_size, 0], [0, 0], [block_size, 0]]
        draw_each_coordinate('dark blue')

    # Only mark the centres if the corresponding argument is True
    if show_centres:
        coordinates = [[-block_size / 2, block_size / 2], [block_size / 2, block_size / 2],
                       [-block_size / 2, block_size + block_size / 2], [block_size / 2, block_size + block_size / 2]]
        draw_each_coordinate('red')

    # Put the cursor back how it was
    color('black')
    home()


# End the program by hiding the cursor and releasing the window
def release_drawing_canvas():
    tracer(True)
    hideturtle()
    done()

#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# the building blocks:
#
# 1. The name of the block, from 'Block A' to 'Block D'
# 2. The place to put the block, either 'Top left', 'Top right',
#    'Bottom left' or 'Bottom right'
# 3. The block's orientation, meaning the direction in which the top
#    of the block is pointing, either 'Up', 'Down', 'Left' or 'Right'
# 4. An optional mystery value, 'X' or 'O', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily mention all four blocks.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#

# The following data set doesn't require drawing any blocks
# at all.  You may find it useful as a dummy argument when you
# first start developing your "draw_attempt" function.

arrangement_00 = []

# Each of the following data sets specifies drawing just one block
# in an upright orientation.  You may find them useful when
# creating your individual pieces.

arrangement_01 = [['Block A', 'Bottom left', 'Up', 'O']]
arrangement_02 = [['Block B', 'Bottom right', 'Up', 'O']]
arrangement_03 = [['Block C', 'Bottom left', 'Up', 'O']]
arrangement_04 = [['Block D', 'Bottom right', 'Up', 'O']]

# Each of the following data sets specifies drawing just one block
# in non-upright orientations.  You may find them useful when
# ensuring that you can draw all the blocks facing in different
# directions.

arrangement_10 = [['Block A', 'Bottom left', 'Down', 'O']]
arrangement_11 = [['Block A', 'Bottom right', 'Left', 'O']]
arrangement_12 = [['Block A', 'Bottom left', 'Right', 'O']]

arrangement_13 = [['Block B', 'Bottom left', 'Down', 'O']]
arrangement_14 = [['Block B', 'Bottom right', 'Left', 'O']]
arrangement_15 = [['Block B', 'Bottom left', 'Right', 'O']]

arrangement_16 = [['Block C', 'Bottom left', 'Down', 'O']]
arrangement_17 = [['Block C', 'Bottom right', 'Left', 'O']]
arrangement_18 = [['Block C', 'Bottom left', 'Right', 'O']]

arrangement_19 = [['Block D', 'Bottom left', 'Down', 'O']]
arrangement_20 = [['Block D', 'Bottom right', 'Left', 'O']]
arrangement_21 = [['Block D', 'Bottom left', 'Right', 'O']]

# The following data sets all stack various numbers of
# blocks in various orientations

arrangement_30 = [['Block C', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Top right', 'Up', 'O']]
arrangement_31 = [['Block A', 'Bottom left', 'Up', 'O'],
                  ['Block C', 'Bottom left', 'Up', 'O']]

arrangement_32 = [['Block B', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Bottom left', 'Up', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]
arrangement_33 = [['Block B', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Bottom left', 'Up', 'O'],
                  ['Block A', 'Top left', 'Up', 'O']]
arrangement_34 = [['Block B', 'Bottom left', 'Up', 'O'],
                  ['Block A', 'Bottom right', 'Up', 'O'],
                  ['Block D', 'Top left', 'Up', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]

arrangement_40 = [['Block C', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top right', 'Right', 'O']]
arrangement_41 = [['Block A', 'Bottom left', 'Down', 'O'],
                  ['Block C', 'Bottom left', 'Up', 'O']]

arrangement_42 = [['Block B', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block C', 'Top right', 'Down', 'O']]
arrangement_43 = [['Block B', 'Bottom right', 'Right', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block A', 'Top left', 'Right', 'O']]
arrangement_44 = [['Block B', 'Bottom left', 'Down', 'O'],
                  ['Block A', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top left', 'Right', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]

arrangement_50 = [['Block B', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block C', 'Top right', 'Down', 'X']]
arrangement_51 = [['Block B', 'Bottom right', 'Right', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block A', 'Top left', 'Right', 'X']]
arrangement_52 = [['Block B', 'Bottom left', 'Down', 'O'],
                  ['Block A', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top left', 'Right', 'O'],
                  ['Block C', 'Top right', 'Up', 'X']]

arrangement_60 = [['Block B', 'Bottom right', 'Left', 'X'],
                  ['Block D', 'Bottom left', 'Left', 'O'],
                  ['Block C', 'Top right', 'Down', 'O']]
arrangement_61 = [['Block B', 'Bottom right', 'Right', 'O'],
                  ['Block D', 'Bottom left', 'Left', 'X'],
                  ['Block A', 'Top left', 'Right', 'O']]
arrangement_62 = [['Block B', 'Bottom left', 'Down', 'X'],
                  ['Block A', 'Bottom right', 'Left', 'X'],
                  ['Block D', 'Top left', 'Right', 'O'],
                  ['Block C', 'Top right', 'Up', 'O']]

# The following arrangements create your complete image, but
# oriented the wrong way

arrangement_80 = [['Block C', 'Bottom right', 'Left', 'O'],
                  ['Block D', 'Top right', 'Left', 'X'],
                  ['Block A', 'Bottom left', 'Left', 'O'],
                  ['Block B', 'Top left', 'Left', 'O']]

arrangement_81 = [['Block B', 'Bottom right', 'Right', 'X'],
                  ['Block D', 'Bottom left', 'Right', 'X'],
                  ['Block A', 'Top right', 'Right', 'O'],
                  ['Block C', 'Top left', 'Right', 'O']]

arrangement_89 = [['Block A', 'Bottom right', 'Down', 'O'],
                  ['Block C', 'Top right', 'Down', 'O'],
                  ['Block B', 'Bottom left', 'Down', 'O'],
                  ['Block D', 'Top left', 'Down', 'O']]

# The following arrangements should create your complete image
# (but with the blocks stacked in a different order each time)

arrangement_90 = [['Block C', 'Bottom left', 'Up', 'O'],
                  ['Block D', 'Bottom right', 'Up', 'O'],
                  ['Block B', 'Top right', 'Up', 'X'],
                  ['Block A', 'Top left', 'Up', 'O']]

arrangement_91 = [['Block D', 'Bottom right', 'Up', 'X'],
                  ['Block C', 'Bottom left', 'Up', 'X'],
                  ['Block A', 'Top left', 'Up', 'O'],
                  ['Block B', 'Top right', 'Up', 'O']]

arrangement_92 = [['Block D', 'Bottom right', 'Up', 'X'],
                  ['Block B', 'Top right', 'Up', 'O'],
                  ['Block C', 'Bottom left', 'Up', 'O'],
                  ['Block A', 'Top left', 'Up', 'O']]

arrangement_99 = [['Block C', 'Bottom left', 'Up', 'O'],
                  ['Block D', 'Bottom right', 'Up', 'O'],
                  ['Block A', 'Top left', 'Up', 'O'],
                  ['Block B', 'Top right', 'Up', 'O']]
arrangement_100 = [['Block C', 'Bottom left', 'Up', 'X'],
                  ['Block D', 'Bottom right', 'Up', 'O'],
                  ['Block A', 'Top left', 'Up', 'O'],
                  ['Block B', 'Top right', 'Up', 'O']]

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "stack_blocks" function.
#
######################################################################
######################################################################
## D E F I N I N G . F U N C T I O N S ##
########################################################
## H E R E . W E . H A V E . R E U S E D . C O D E ##
##
# Code needs to be logical and in order.

#This is so satisfying when I copied these varaibles here. 

bottom_left = -block_size / 2, block_size / 2
bottom_right = block_size / 2, block_size / 2
top_left = -block_size / 2, block_size + block_size / 2
top_right = block_size / 2, block_size + block_size / 2

#Hopefully the function names are easy to understand. Aaanyway

#### Draws a white...background
def white_background():
    pu()
    right(90)
    forward(125)
    right(90)
    forward(125)
    pd()
    right(90)
    begin_fill()
    color('white')
    forward(block_size)
    right(90)
    forward(block_size)
    right(90)
    forward(block_size)
    right(90)
    forward(block_size)
    end_fill()
    pu()
#### WOOOOAH! A Black border to individualize the blocks
def black_border():
    global blockhome
    pu()
    goto(blockhome)
    setheading(blockhead)
    color('black')
    width(5)
    forward(block_size/2)
    right(90)
    forward(block_size/2)
    right(90)
    pd()
    forward(block_size)
    right(90)
    forward(block_size)
    right(90)
    forward(block_size)
    right(90)
    forward(block_size)
    width(1)
#### Where we go and stuff
def location_finder():
    global location
    global bottom_left
    global bottom_right
    global top_left
    global top_right

    
    if location == 'Bottom left':
        goto(bottom_left)
    elif location == 'Bottom right':
        goto(bottom_right)
    elif location == 'Top left':
        goto(top_left)
    elif location == 'Top right':
        goto(top_right)
#### Sets rotation...
def set_rotation():
    if rotation == 'Up':
        pass
    if rotation == 'Left':
        left(90)
    if rotation == 'Right':
        right(90)
    if rotation == 'Down':
        right(180)
#### Drawing the bad boyzz
def drawing():
    if block == 'Block A':
        draw_block_a()
        pu()
    elif block == 'Block B':
        draw_block_b()
        pu()
    elif block == 'Block C':
        draw_block_c()
        pu()
    elif block == 'Block D':
        draw_block_d()
        pu()
#### I must admit I did shortcut this but I couldn't use pass or break but return works so...
#### I bet you won't read this
#### something to return instead of a block
def draw_X():
    return "hello, world"
#### Nice addition to the assignment, had a great day smashing this out
#### This moves the blocks and checks for X 
def myth_buster():
    global bottom_left
    global bottom_right
    global top_left
    global top_right
    global location

    if mystery == 'O':
        if location == 'Bottom left':
            goto(bottom_left)
        elif location == 'Bottom right':
            goto(bottom_right)
        elif location == 'Top left':
            goto(top_left)
        elif location == 'Top right':
            goto(top_right)
        set_rotation()

        drawing()
    elif mystery =='X':
        draw_X()
        if location == 'Bottom left':
            top_left = bottom_left
        elif location == 'Bottom right':
            top_right = bottom_right

################# B U I L D I N G B L O C K S
def draw_block_a():
    width(2)
    global blockhome
    blockhome = position()
    global blockhead
    blockhead = heading()

#### White Background
    white_background()
#### Drawing his head
    begin_fill()
    pu()
    color('yellow')
    forward(-111)
    pd()
    right(80)
    forward(80)
    for numbers in range(6):
        right(5)
        forward(12)
    hair_a_pos = position()
    hair_a_head = heading()
    for each in range(3):
        right(5)
        forward(12)
    hair_b_pos = position()
    hair_b_head = heading()
    for each in range(11):
        right(5)
        forward(12)
    forward(10)
    right(90)
    forward(234)
    right(90)
    forward(139)
    end_fill()


#### Drawing the eye
    pu()
    color('white')
    goto(blockhome)
    setheading(blockhead)
    right(90)
    forward(125)
    left(90)
    forward(125)
    right(180)
    forward(57)
    right(90)
    pd()
    begin_fill()
    for each in range(90):
        forward(1)
        right(1)
    right(90)
    forward(57.79)
    end_fill()
    right(90)
    forward(57)
    right(90)
    color('black')
    width(3)
    for each in range(90):
        forward(1)
        right(1)
    width(2)


#### PUPIL (please disregard the lazy eye)

    pu()
    right(115)
    forward(45)
    pd()
    begin_fill()
    circle(4)
    end_fill()


#### AND LET US REMEMEBER THE HOLY HAIR OF HOMER

    pu()
    goto(hair_a_pos)
    setheading(hair_a_head)
    left(20)
    pd()
    forward(-20)
    forward(20)
    for each in range(45):
        forward(3)
        right(3)
    pu()
    goto(hair_b_pos)
    setheading(hair_b_head)
    left(35)
    pd()
    forward(-20)
    forward(20)
    for each in range(45):
        forward(3)
        right(3)

#### Black border function
#(uses the AHEM...global...method)
    black_border()


def draw_block_b():
    
    width(2)
    global blockhome
    blockhome = position()
    global blockhead
    blockhead = heading()


#### White background
    white_background()


#### The skull
    goto(blockhome)
    setheading(blockhead)
    left(90)
    forward(125)
    left(90)
    forward(125)
    left(90)
    forward(16)
    left(90)
    pd()
    color('yellow')
    begin_fill()
    for each in range(50):
        forward(4)
        right(1.5)
    forward(25)
    left(45)
    for each in range(60):
        forward(1)
        right(2)
    right(25)
    forward(156.39)
    end_fill()
    pu()
#### and also the eye outline
    goto(blockhome)
    setheading(blockhead)
    right(90)
    forward(125)
    right(90)
    forward(125)
    right(90)
    forward(57)
    right(90)
    pd()
#### insert eye part
    color('white')
    begin_fill()
    for each in range(50):
        forward(1)
        right(1)
    right_eye_home = position()
    right_eye_head =  heading()
    for each in range(38):
        forward(1)
        right(1)
    right(90)
    forward(57)
    end_fill()
    pu()
    goto(right_eye_home)
    setheading(right_eye_head)
    pd()
    begin_fill()
    right(265)
    forward(25)
    for each in range(145):
        forward(1.1)
        right(1)
    pu()
    end_fill()
    goto(blockhome)
    setheading(blockhead)
    right(90)
    forward(125)
    right(90)
    forward(125)
    right(90)
    forward(57)
    right(90)
    pd()
    color('black')
    width(3)
    for each in range(50):
        forward(1)
        right(1)
    right_eye_home = position()
    right_eye_head =  heading()
    for each in range(40):
        forward(1)
        right(1)
    pu()
    goto(right_eye_home)
    setheading(right_eye_head)
    pd()
    right(265)
    forward(25)
    for each in range(145):
        forward(1.1)
        right(1)
    pu()
    left(105)
    forward(-50)
    left(90)
    forward(20)
    begin_fill()
    circle(5)
    end_fill()
    width(2)

#### Black border
    black_border()

def draw_block_c():
#to make rotation and orientation easy, I used the centre to class as 'home'
#these first lines are to draw the white background
    width(2)
    global blockhome
    blockhome = position()
    global blockhead
    blockhead = heading()
    white_background()


#### This block uses a variable that needs a point for the beard.
#### This is just placing the variable in its spot.
    forward(-block_size)
    left(90)
    forward(-130)
    beard = position()
    forward(130)
    right(90)
    forward(block_size)

#### We now draw the neck etc.
    pu()
    color('yellow')
    forward(-block_size)
    pd()
    begin_fill()
    forward(139)
    right(90)
    forward(block_size)
    right(90)
    forward(139)
    right(90)
    end_fill()
    forward(90)
    right(90)
    forward(95)
    right(90)
    begin_fill()

#### Yellow ear
    circle(30)
    end_fill()
    for each in range(30):
        forward(1)
        left(2)

#### The ear
    color('black')
    width(2)
    for each in range(140):
        forward(1)
        left(2)
    right(90)
    forward(7)
    forward(-14)
    forward(7)
    right(270)
    come_back = position()
    pu()
    left(70)
    forward(25)
    pd()
    forward(15)
    right(90)
    for each in range(7):
        forward(2)
        right(2)
    for each in range(15):
        forward(-2)
        left(2)
    pu()
    goto(come_back)
    left(4)

#### The hair that makes the M
    left(25)
    forward(49)
    pd()
    forward(50)
    left(150)
    forward(50)
    right(130)
    forward(48)
    left(150)
    forward(50)
    pu()
    goto(beard)

#### Starting to Draw the beard
    right(25)
    color('brown')
    pd()
    begin_fill()
    for each in range(64):
        forward(2)
        left(1)
    left(54)
    end_fill()


#### Re-centre turtle to draw eye
    pu()
    goto(blockhome)
    setheading(blockhead)
    forward(125)
    left(90)
    forward(75)
    left(90)
    eye_start = position()
    eye_head = heading()
#### Drawing eye
    pd()
    color('white')
    begin_fill()
    for each in range(84):
        forward(1)
        right(1)
    right(96)
    forward(57)
    right(90)
    forward(50)
    end_fill()
    pu()
    goto(eye_start)
    setheading(eye_head)
    color('black')
    width(3)
    pd()
    for each in range(84):
        forward(1)
        right(1)


#### Black border
    black_border()




def draw_block_d():
#### Getting into position
    width(2)
    global blockhome
    blockhome = position()
    global blockhead
    blockhead = heading()
    white_background()
    color('yellow')
    begin_fill()
#### Starting from the neck
    forward(-125)
    right(90)
    forward(block_size)
    left(90)
    forward(125)
    left(90)
    forward(block_size)
    end_fill()
    color('brown')
    pu()
    forward(-12)
    left(71)
    pd()
#### Bottom jaw
    begin_fill()
    for each in range(13):
        forward(11)
        left(3)
    left(15)
    forward(10)
    for each in range(13):
        forward(3)
        left(4)
    right(85)
    pd()
    for each in range(6):
        forward(4)
        left(10)
    for each in range(4):
        forward(3)
        left(2.5)
    forward(10)
    right(75)
    bottom_lip_xy = position()
    bottom_lip_head = heading()
    for each in range(11):
        forward(5)
        left(3)
    left(65)
    for each in range(7):
        forward(7)
        left(1)
    right(15)
    forward(5)
    left(5)
    for each in range(8):
        forward(4)
        left(2)
    for each in range(10):
        forward(5)
        left(3)
    left(90)
    for each in range(10):
        forward(1)
        right(5)
    for each in range(6):
        forward(12)
        left(3)
    nose_start = position()
    nose_head = heading()
    for each in range(7):
        forward(12)
        left(3)
    forward(72)
    end_fill()
    goto(bottom_lip_xy)
    setheading(bottom_lip_head)
    color('black')
    for each in range(30):
        forward(-5)
        left(-1)
    stamp()
    pu()
#### Drawing the nose
    goto(nose_start)
    setheading(nose_head)
    right(180)
    pd()
    forward(-20)
    begin_fill()
    color('yellow')
    forward(55)
    right(25)
    forward(35)
    for each in range(42):
        forward(1.5)
        left(5)
    right(21)
    forward(80)
    pu()
    end_fill()

#### Drawing the eye in the top left
    pu()
    color('white')
    goto(blockhome)
    setheading(blockhead)
    forward(-125)
    left(90)
    forward(75)
    right(90)
    pd()
    begin_fill()
    for each in range(83):
        forward(1)
        left(1)
    left(97)
    forward(57.31)
    left(90)
    forward(50)
    end_fill()
    color('black')
    width(3)
    left(90)
    for each in range(83):
        forward(1)
        left(1)
#### Black border
    black_border()

# Draw the stack of blocks as per the provided data set
# drawing Homer
def stack_blocks(arrangements):
    for each_option in arrangements:
        #for each different option inside the arrangement list we do something
        # I have names the 4 items inside each sublist where the turtle
        #will interpret the information inside the list and be able to
        # understand the english language
        global blockhome
        global blockhead
        global location
        global block_size
        global rotation
        global mystery
        global block
        mystery = each_option[3]
        rotation = each_option[2]
        location = each_option[1]
        block = each_option[0]

        setheading(0)
        set_rotation()
        location_finder()
        myth_buster()


#
#--------------------------------------------------------------------#




#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by stacking your blocks correctly
title('Live for the weekend')

# Display the corner and centre coordinates of the places where
# the blocks must be placed
# ***** If you don't want to display the coordinates change the
# ***** arguments below to False
mark_coords(False, False)

### Call the student's function to display the stack of blocks
### ***** Change the argument to this function to test your
### ***** code with different data sets
stack_blocks(arrangement_99)

# Exit gracefully
release_drawing_canvas()

#
#--------------------------------------------------------------------#
