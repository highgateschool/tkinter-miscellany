import tkinter as tk
import functools as ft

root = tk.Tk()

root.geometry( "400x300" )


a_button = tk.Button( root , text = "Alyssa's button" )
a_label = tk.Label( root , text = "Vivika's label" )
a_frame = tk.Frame( root )

a_button.grid()
a_label.grid()
a_frame.grid()

grid_of_buttons = []

def make_button( parent , button_text , callback_label ):
    new_button = tk.Button( parent , text = button_text )

    def button_func():
        callback_label.config( text = 'You pressed button ' + button_text )

    new_button.config( command = button_func )

    return new_button

for i in range( 3 ):
    for j in range( 3 ):
        grid_button = make_button( a_frame , '( {} , {} )'.format( i , j ) , a_label )

        grid_button.grid( row = j  , column = i )

        grid_of_buttons.append( grid_button )       



a_button.config( bg = "powder blue" )


#root.columnconfigure( 0 , weight = 1 )
#root.rowconfigure( 1 , weight = 1 )

tk.mainloop()
