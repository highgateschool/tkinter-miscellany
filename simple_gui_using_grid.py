import tkinter as tk

root = tk.Tk()
root.geometry( "400x300" )

def boo():
    global my_label
    print( "Hello, you pressed a button!" )
    my_label.config( text = "Well done!" )

# Create objects

my_button = tk.Button( root , text = "A word on it that says Button" , command = boo )
my_frame =tk.Frame( root , background = "blue" )
my_label = tk.Label( root , text = "Text" )

# Button on grid

new_label = tk.Label( my_frame , text = "Different text" )

# Stick to grid

my_button.grid( row = 1 , column = 1 , sticky = "" )
my_frame.grid( row = 2 , column = 0 , columnspan = 3 , sticky = "NESW" )
my_label.grid( row = 0 , column = 0 , columnspan = 3 , sticky = "" )

# Describe grid

root.rowconfigure( 0 , weight = 1 )
root.rowconfigure( 1 , weight = 10 )
root.rowconfigure( 2 , weight = 1 )

root.columnconfigure( 0 , weight = 1 )
root.columnconfigure( 1 , weight = 1 )
root.columnconfigure( 2 , weight = 1 )



new_label.grid()
