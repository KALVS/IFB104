
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
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  Online Shopper
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for aggregating product data published by a variety of
#  online shops.  See the instruction sheet accompanying this file
#  for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution.)
from urllib import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from Tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression.  (You do NOT need to
# use these functions in your solution, although you will find
# it difficult to produce a robust solution without using
# regular expressions.)
from re import findall, finditer

# Import the standard SQLite functions just in case they're
# needed.
from sqlite3 import *

#
#--------------------------------------------------------------------#


#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#
#Download webpage using a python script.
rss_feeds = ['http://www.specialoffers.com/rss/computers-coupons.xml']
#https://www.etsy.com/shop/MagM8z/rss', 'https://www.etsy.com/shop/GoodGear69/rss', 'https://www.etsy.com/shop/AestheticsRL.rss ']

rss_feed_files = open('rss_feeds.html', 'w')

rss_feed_files.write('<!DOCTYPE html>\n')
rss_feed_files.write('<html>\n')
rss_feed_files.write('<body>\n')

rss_feed_files.write(' <ul>\n')

for feeds in rss_feeds:
    html_source = urlopen(feeds).read()
    extracted_elements = findall('<title>(.*)</title>', html_source)
    print extracted_elements
    
rss_feed_files.write('  </ul>\n')
rss_feed_files.write('</body>\n')
rss_feed_files.write('</html>')

rss_feed_files.close()

# Creating the Tk Window
gui_window = Tk()
# Give it a name
gui_window.title('Super Lucky Fun Prize!')
#need set size, dont want to irritate the user of buttons move etc...*mumbles about powerpoint
#gui_window.geometry('400x400')

# Functions
def openwebpage():
    url = 'https://www.popcultcha.com.au/rss/catalog/new/store_id/1/'
    web_content = urlopen(url).read()
    print web_content
    findall('hats',web_content)

def down_button():
    print "press down"

def progress_report():
    pass

def print_invoice():
    file_name = 'file:///Users/alexholm/Documents/IFB104/N9918205.Assignment2/invoice.html' # Put your web page address here

    # Read the contents of the web page as a character string
    web_page_contents = urlopen(file_name).read()

    # Display the downloaded web page
    print web_page_contents

#make header
def make_grid():
    column_number = 0
    for each in range(10):
        holder.grid(row=0, column=column_number)
        column_number = column_number + 1
    
    
# Creating the Top Label - Welcome the customer
label_heading = Label(gui_window, text = 'Do you want random trash?',
                 font = ('Arial, 28'), justify = 'center', fg = 'red')

#Secondary Top label - Explain what we do
label_subhead = Label(gui_window, text = "If you said 'yes', than step right up!",
                      font = ('Arial, 20'), justify = 'center', fg = 'maroon')
#first step label - Giving an indication of the qualtity of products
step_one = Label(gui_window, text = 'Step 1: Choose products! \n Spending yourself better feeling', 
                 font = ('Arial, 20'), fg = 'blue')
#second step label - Opening a link to a html document
step_two = Label(gui_window, text = 'Step 2: Join the capitalist machine and buy. \n C O N S U M E',
                 font = ('Arial, 20'), fg = 'cyan')
# third step label - Observe the progress of the order.
step_three = Label(gui_window, text = 'Step 3: Await treats from industry at the expense of others.',
                   font = ('Arial, 20'), fg = 'orange')
### need 4 labels, text entry fields, up and down buttons.

#These are creating the labels for the spin boxes
hats_label = Label(gui_window, text = 'Hats')
socks_label = Label(gui_window, text = 'Socks')
lanyard_label = Label(gui_window, text = 'Lanyards')
scarfs_label = Label(gui_window, text = 'Scarfes')
watches_label = Label(gui_window, text = 'Watches')

# Making Spinboxes
hats_spinbox = Spinbox(gui_window, from_=0,to=10, width = 1)
socks_spinbox = Spinbox(gui_window, from_=0,to=10, width = 1)
lanyard_spinbox = Spinbox(gui_window, from_=0,to=10, width = 1)
scarfs_spinbox = Spinbox(gui_window, from_=0,to=10, width = 1)
watches_spinbox = Spinbox(gui_window, from_=0,to=10, width = 1)

#making a button that prints the invoice
invoice = Button(gui_window, text = "Do you want to print your invoice?",
                 command = print_invoice)

# Let the customer see the order status and track progress
progress = Label(gui_window, text = 'Avaiable for use', font = ('Arial, 16'), fg = 'green')

#need a placeholder for things..I dunno I should fix this
holder = Label(gui_window, text=' ', font = ('Arial'))
#Unpacking

###need to place these


make_grid()
label_heading.grid(row=1, column=0, columnspan = 10)
label_subhead.grid(row=2, column=0, columnspan = 10)
step_one.grid(row=3, column=0, columnspan=10, rowspan=2)
lanyard_spinbox.grid(row=5, column=3)
lanyard_label.grid(row=5, column=2)
scarfs_spinbox.grid(row=6, column=3)
scarfs_label.grid(row=6, column=2)
hats_spinbox.grid(row=5, column=6)
hats_label.grid(row=5, column=5)
socks_spinbox.grid(row=6, column=6)
socks_label.grid(row=6, column=5)
step_two.grid(row=7, column=0, columnspan=10)
invoice.grid(row=8, column=0, columnspan=10)
step_three.grid(row=9, column=0, columnspan=10)
progress.grid(row=10, column=0, columnspan=10)

# Name of the invoice file. To simplify marking, your program should
# produce its results using this  file name.
file_name = 'file:///Users/alexholm/Documents/IFB104/N9918205.Assignment2/invoice.html'

gui_window.mainloop()


