
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


def gui_maker():
    # Make GUI
    gui_window = Tk()
    
    # Give it a name
    gui_window.title('Super Lucky Fun Prize!')

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
    umart_label = Label(gui_window, text = 'Computer stuff')
    etsy_label = Label(gui_window, text = 'Aesthetics')
    defence_label = Label(gui_window, text = 'Self Defence')
    lux_label = Label(gui_window, text = 'Bikes')

    # Making Spinboxes
    global umart_spinbox
    global etsy_spinbox
    global defence_spinbox
    global lux_spinbox
    umart_spinbox = Spinbox(gui_window, from_=0,to=10, width = 1)
    etsy_spinbox = Spinbox(gui_window, from_=0,to=10, width = 1)
    defence_spinbox = Spinbox(gui_window, from_=0,to=10, width = 1)
    lux_spinbox = Spinbox(gui_window, from_=0,to=10, width = 1)

    #making a button that prints the invoice
    invoice = Button(gui_window, text = "Do you want to print your invoice?",
                     command = print_invoice)

    # Let the customer see the order status and track progress
    progress = Label(gui_window, text = 'Avaiable for use', font = ('Arial, 16'), fg = 'green')

    #need a placeholder for things..I dunno I should fix this
    global holder
    holder = Label(gui_window, text=' ', font = ('Arial'))
    #Unpacking

    ###need to place these


    make_grid()
    label_heading.grid(row=1, column=0, columnspan = 10)
    label_subhead.grid(row=2, column=0, columnspan = 10)
    step_one.grid(row=3, column=0, columnspan=10, rowspan=2)
    defence_spinbox.grid(row=5, column=3)
    defence_label.grid(row=5, column=2)
    lux_spinbox.grid(row=6, column=3)
    lux_label.grid(row=6, column=2)
    umart_spinbox.grid(row=5, column=6)
    umart_label.grid(row=5, column=5)
    etsy_spinbox.grid(row=6, column=6)
    etsy_label.grid(row=6, column=5)
    step_two.grid(row=7, column=0, columnspan=10)
    invoice.grid(row=8, column=0, columnspan=10)
    step_three.grid(row=9, column=0, columnspan=10)
    progress.grid(row=10, column=0, columnspan=10)
    file_name = 'file:///Users/alexholm/Documents/IFB104/N9918205.Assignment2/invoice.html'

    gui_window.mainloop()

def print_invoice():
    html_head = """<!DOCTYPE html>

<html>

    <head>
    <style>
    table, tr, td {
    border:1px solid black;
    border-collapse: collapse;
    width="80%'
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
    total = 0
    item_count = 0
    defence_price[item_count] = float(defence_price[item_count])*1.33
    for count in range(int(defence_spinbox.get())):
        html_table = html_table + """
        <tr>
        <td>"""+defence_title[item_count]+"""</td>"""+"""<td><img src="""+defence_img[item_count]+"""></td><td>"""+str(round(float(defence_price[item_count]),2))+"""AUD</td>"""
        total += float(defence_price[item_count])
        item_count = item_count + 1

    """</tr>"""

    item_count = 0
    for count in range(int(etsy_spinbox.get())):
        html_table = html_table + """
        <tr>
        <td>"""+etsy_title[item_count]+"""</td>"""+"""<td><img src="""+etsy_img[item_count]+"""></td><td>"""+str(float(etsy_price[item_count])*1.33)+"""AUD</td>"""
        total += float(etsy_price[item_count])
        item_count = item_count + 1
    """</tr>"""
    
    item_count = 0

    for count in range(int(umart_spinbox.get())):
        html_table = html_table + """
        <tr>
        <td>"""+umart_title[item_count]+"""</td>"""+"""<td><img src="""+umart_img[item_count]+"""></td><td>"""+umart_price[item_count]+"""AUD</td>"""
        total += float(umart_price[item_count])
        item_count = item_count + 1
    """</tr>"""

    item_count = 0
    for count in range(int(lux_spinbox.get())):
        html_table = html_table + """
        <tr>
        <td>"""+lux_title[item_count]+"""</td>"""+"""<td><img src=\"http://www.luxbmx.com"""+lux_img[item_count]+""""></td><td>"""+lux_price[item_count]+"""AUD</td>"""
        total += float(lux_price[item_count])
        item_count = item_count + 1
    """</tr>"""
    
    html_table = html_table + "</table>"

                       
    if total == 0:
        total = 'nothing! You have found a weakness of the machine, exploit it and seize the meeeaaaaa-yada-yada-yada </h3>'
    else:
        total = '$' + str(total) + 'AUD'

    reciept = open('invoice.html', 'w')

##    for count in shirts_spinbox.get():
##        invoice.write(html_body.format(title[count], image[count], price[count]))

    total_price = """<h3> Your total is """ + str(total)
    html_footer = """
<nav>

<ul>

<li><a href="ttps://www.umart.com.au/umart1/pro/index.phtml?bid=2'">Umart</a></li>

<li><a href="https://www.crimezappers.com/">Crime Zappers (US)</a></li>

<li><a href="https://www.etsy.com/shop/oktak/rss'">oktak on ETSY</a></li>

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

umart = 'https://www.umart.com.au/umart1/pro/index.phtml?bid=2'
umart_data = urlopen(umart).read()
umart_title = findall('spproduct\">(.*)</a>', umart_data)

defence = 'https://www.crimezappers.com/'
etsy = 'https://www.etsy.com/shop/oktak/rss'
lux = 'http://www.luxbmx.com/2017-bikes/'

umart_data = urlopen(umart).read()
defence_data = urlopen(defence).read()
etsy_data = urlopen(etsy).read()
lux_data = urlopen(lux).read()
# Searching the webpages and extracting the information
umart_title = findall('spproduct\">(.*)</a>', umart_data)
umart_img = findall('img\sborder=[0-9]\s*src=\"(.*)"\s*heigh', umart_data)
umart_price = findall('font-weight:bold;\">\s\$(.*)\s</font', umart_data)

##
defence_title = findall('\.html\"\stitle=\"(.*)"\s*class', defence_data)
defence_img = findall('image"><img\ssrc=\"(.*)"\salt',defence_data)
defence_price = findall('price\">\$(.*)</span>\s*</span', defence_data)


etsy_title = findall('<title>(.*)by\soktak</title>\s*<desc', etsy_data)
etsy_img = findall('img\ssrc=&quot;(.*)&quot;\sb', etsy_data)
etsy_price = findall('price&quot;&gt;(.*)\sUSD', etsy_data)


lux_title = findall('-image"\salt="(.*)\(2017\)', lux_data)
lux_img = findall('image">\s*<img\ssrc\="(.*)"\sclass', lux_data)
lux_price = findall('price\">\$(.*)</span', lux_data)

# Creating the Tk Window
gui_maker()
