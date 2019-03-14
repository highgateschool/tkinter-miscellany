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


for i in range( 3 ):
    for j in range( 3 ):
        button_text = '( {} , {} )'.format( i , j )
        grid_button = tk.Button( a_frame , text = button_text )

        def button_func():
            a_label.config( text = 'You pressed button ' + button_text )

        grid_button.config( command = button_func )

        grid_button.grid( row = j  , column = i )

        grid_of_buttons.append( grid_button )       



a_button.config( bg = "powder blue" )


#root.columnconfigure( 0 , weight = 1 )
#root.rowconfigure( 1 , weight = 1 )

tk.mainloop()
