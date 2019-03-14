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

def change_label( t ):
    a_label.config( text = "You pressed button {}".format( t )  )


for i in range( 3 ):
    for j in range( 3 ):
        new_button = tk.Button( a_frame , text = '( {} , {} )'.format( i , j ) )

        new_button.grid( row = 2 + j  , column = i )

        new_button.config( command = ft.partial( change_label, ( i , j ) ) )

        grid_of_buttons.append( new_button )       



a_button.config( bg = "powder blue" )


#root.columnconfigure( 0 , weight = 1 )
#root.rowconfigure( 1 , weight = 1 )

tk.mainloop()
