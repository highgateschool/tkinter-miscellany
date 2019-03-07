import tkinter as tk
from functools import partial

class MyFirstGUI:
    def __init__(self, master ):
        self.master = master
        master.title("A simple GUI")

        # Create my content
        self.label = tk.Label(master, text="This is our first GUI!")
        self.greet_button = tk.Button(master, text="Greet", command=self.greet)
        self.close_button = tk.Button(master, text="Close", command=self.master.quit)
        self.grid_frame = tk.Frame( master )

        # Populate grid

        my_grid = MyGrid( self.grid_frame ,self.label )
        
        # Layout using pack
##        self.label.pack()
##        self.greet_button.pack()
##        self.close_button.pack()

        # Create layout using a grid
        self.label.grid( row = 0 , column = 0 , sticky = 'ew' )
        self.grid_frame.grid( row = 1 , column = 0 , sticky = '' )
        self.greet_button.grid( row = 2 , column = 0 , sticky = 'e' )
        self.close_button.grid( row = 2 , column = 0 , sticky = 'w' )

        # Now describe rows and columns
        self.master.grid_rowconfigure( 0 , weight = 0 )
        self.master.grid_rowconfigure( 1 , weight = 1 )
        self.master.grid_rowconfigure( 2 , weight = 0 )
        self.master.grid_columnconfigure( 0 , weight = 1 )

    def greet(self):
        self.label.config( text = 'You clicked the button!' )

class MyGrid:
    def __init__( self , master , callback ):
        self.master = master
        self.callback = callback

        # Create list of lists to store buttons

        self.buttons = [ [ None ] * 10 ] * 20
        print( self.buttons )

        for i in range( 20 ):
            for j in range( 10 ):
                self.buttons[ i ][ j ] = tk.Button( master , text = str( i ) + str( j ) , command = partial( self.button_press , ( i , j ) ) )
                self.buttons[ i ][ j ].grid( row = i , column = j )


    def button_press( self , a ):
        self.callback.config( color = "Yellow" )
        self.callback.config( text = str( a ) )
    

root = tk.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
