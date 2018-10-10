
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
#Making various functions

#what can the function do and what can it return

def create_title(number_of_items, source_titles):
    aggregate_titles = []
    for titles in range(number_of_items):
        title_string = source_titles[titles]
        aggregate_titles.append(title_string)
    return aggregate_titles

def create_img_url(number_of_items, source_img):
    aggregate_img = []
    for images in range(number_of_items):
        img_src= 'http://www.umart.com.au' + source_img[images]
        aggregate_img.append(img_src)
    return aggregate_img

def create_price(number_of_items, source_prices):
    aggregate_price = []
    for prices in range(number_of_items):
        item_price = source_prices[prices]
        aggregate_price.append(item_price)
    return aggregate_price

def html_creator():
    if int(monitors_spinbox.get()) > 0:
        for number in range(int(monitors_spinbox.get())):
            pass#print to the html th title, img and price
    if int(skateboards_spinbox.get()) >0:
        for number in range(int(skateboards_spinbox.get())):
            return           
    if int(scarves_spinbox.get()) >0:
        for number in range(int(scarves_spinbox.get())):
            print "hello scarves"        
    if int(shirts_spinbox.get()) >0:
        for number in range(int(shirts_spinbox.get())):
            print "hello shirts"           

def print_invoice():
    umart_title
    umart_spinbox.get()
    html_head = """<!DOCTYPE html>

<html>

    <head>
    <style>
    table, tr, td {
    border:1px solid black;
    border-collapse: collapse;
    }
    </style>
            

        <meta charset="utf-8">

        <title>Your invoice</title>

        <link rel="stylesheet" link="css/style.css">

    </head>



    <body>

        <div id="container">

            <header>

                <div id="logo_title">

                    <div id="logo">

                        <a href="index.html">

                            <img src="https://s-media-cache-ak0.pinimg.com/736x/c5/04/15/c50415d22e95ac75c925333ef37b85d2.jpg" alt="logo">

                        </a>

                    </div>

                    <div id="title">

                        <h1>Thank you for participating in Capitalism</h1>

                    </div>

                </div>

            </header>
"""
    html_table = """
    <table>
    
    """
    item_count = 0
    total = 0.0
    for count in range(int(umart_spinbox.get())):
        html_table = html_table + """
        <tr>
        <td>"""+umart_title[item_count]+"""</td>"""+"""<td><img src= 'https://www.umart.com.au"""+umart_img[item_count]+"""'></td><td>"""+umart_price[item_count]+"""AUD</td>"""
        total += float(umart_price[item_count])
        item_count = item_count + 1
    """</tr>"""

    item_count = 0
    for count in range(int(amazon_spinbox.get())):
        html_table = html_table + """
        <tr>
        <td>"""+amazon_title[item_count]+"""</td>"""+"""<td><img src="""+amazon_img[item_count]+"""'></td><td>"""+amazon_price[item_count]+"""AUD</td>"""
        total += float(amazon_price[item_count])
        item_count = item_count + 1
    """</tr>"""
    

    html_table = html_table + "</table>"
    
    reciept = open('invoice.html', 'w')

##    for count in shirts_spinbox.get():
##        invoice.write(html_body.format(title[count], image[count], price[count]))
    total_price = """<h3> Your total is """ + str(total) + """AUD </h3>"""
    html_footer = """
<nav>

<ul>

<li><a href="http://www.umart.com.au/newsite/category.php?id=680">Umart</a></li>

<li><a href="https://www.amazon.com/b/ref=lp_11051398011_sk_ln_0_0?node=3416381&ie=UTF8&qid=1495158270">Amazon (US)</a></li>

<li><a href="https://www.ebay.com.au/b/Theme-Metallica/15687/bn_57338821">Ebay</a></li>

<li><a href="contact_us.html">Contact Us</a></li>

</ul>

</nav>

<footer>

<p>Copyright &copy; 2016 | All Rights Reserved</p>

</footer>

</div>

</body>

</html>
"""
    content = html_head + html_table + total_price + html_footer
    reciept.write(content)

def make_grid():
    column_number = 0
    for each in range(10):
        holder.grid(row=0, column=column_number)
        column_number = column_number + 1

#Open and Download webpage using a python script.

umart = 'http://www.umart.com.au/newsite/category.php?id=680'
amazon = 'https://www.amazon.com/b/ref=lp_11051398011_sk_ln_0_0?node=3416381&ie=UTF8&qid=1495158270'
ebay = 'https://www.ebay.com.au/b/Theme-Metallica/15687/bn_57338821'
watches = 'http://www.ebay.com.au/rpp/preowned-picks/C2C-Luxury-Watches-070317'

umart_data = urlopen(umart).read()
amazon_data = urlopen(amazon).read()
ebay_data = urlopen(ebay).read()
watches_data = urlopen(watches).read()
# Searching the webpages and extracting the information
umart_title = findall('ng soon"[\s].........(.*)"\s', umart_data)
umart_img = findall('/newsite/images/201[0-9][0-9]{2}/[a-z]{5}_img/[0-9]{5}_thumb_G_[0-9]{13}.jpg', umart_data)
umart_price = findall('Price:\$([0-9]*\.[0-9])', umart_data)

amazon_title = findall('<a class="a-link-normal" title="(.*)" href', amazon_data)
amazon_img = findall('window.uet && uet.call && uet\("cf"\);\'\s src="(.*)"\s',amazon_data)
amazon_price = findall('a-text-strike\"\>\$([0-9]*)', amazon_data)
##amazon_price = 

#print amazon_title


# Creating the Tk Window
gui_window = Tk()
# Give it a name
gui_window.title('Super Lucky Fun Prize!')
#need set size, dont want to irritate the user of buttons move etc...*mumbles about powerpoint
#gui_window.geometry('400x400')

# Functions





###########################################################################################


##content = (html_head + html_body + html_footer)
##if int(monitors_spinbox.get()) > 0:
##    for number in range(int(monitors_spinbox.get())):
##        print "hello"
##if int(skateboards_spinbox.get()) >0:
##    for number in range(int(skateboards_spinbox.get())):
##        print "Hello skaters"           
##if int(scarves_spinbox.get()) >0:
##    for number in range(int(scarves_spinbox.get())):
##        print "hello scarves"        
##if int(shirts_spinbox.get()) >0:
##    for number in range(int(shirts_spinbox.get())):
##        print "hello shirts"



    
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
umart_label = Label(gui_window, text = 'Monitors')
shirts_label = Label(gui_window, text = 'Shirts')
amazon_label = Label(gui_window, text = 'Skateboards')
scarves_label = Label(gui_window, text = 'Scarves')
watches_label = Label(gui_window, text = 'Watches')

# Making Spinboxes
umart_spinbox = Spinbox(gui_window, from_=0,to=10, width = 1)
shirts_spinbox = Spinbox(gui_window, from_=0,to=10, width = 1)
amazon_spinbox = Spinbox(gui_window, from_=0,to=10, width = 1)
scarves_spinbox = Spinbox(gui_window, from_=0,to=10, width = 1)
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
amazon_spinbox.grid(row=5, column=3)
amazon_label.grid(row=5, column=2)
scarves_spinbox.grid(row=6, column=3)
scarves_label.grid(row=6, column=2)
umart_spinbox.grid(row=5, column=6)
umart_label.grid(row=5, column=5)
shirts_spinbox.grid(row=6, column=6)
shirts_label.grid(row=6, column=5)
step_two.grid(row=7, column=0, columnspan=10)
invoice.grid(row=8, column=0, columnspan=10)
step_three.grid(row=9, column=0, columnspan=10)
progress.grid(row=10, column=0, columnspan=10)

print amazon_img

# Name of the invoice file. To simplify marking, your program should
# produce its results using this  file name.
file_name = 'file:///Users/alexholm/Documents/IFB104/N9918205.Assignment2/invoice.html'

gui_window.mainloop()


