import tkinter as tk

root = tk.Tk()
root.geometry( '200x200' )

label_text = tk.StringVar()
label_text.set( 'Hello World' )

root.grid_columnconfigure( 0 , weight = 1 )
root.grid_rowconfigure( 0 , weight = 1 )
root.grid_rowconfigure( 1 , weight = 1 )
my_label = tk.Label( root , textvariable = label_text ,  ).grid( column = 0 , row = 0 )

def do_change():
    label_text.set( 'You pressed the button!' )

my_button = tk.Button( root , text = 'Press' , command = do_change ). grid( column = 0 , row = 1 )
root.mainloop()
