import tkinter as tk

root = tk.Tk()
root.geometry( '200x200' )

class MyButton( tk.Frame ):
    def __init__( self , parent ):

        # Initialize
        
        tk.Frame.__init__( self , parent )

        # Give weightings to columns and rows
        
        self.grid_columnconfigure( 0 , weight = 1 )
        self.grid_rowconfigure( 0 , weight = 1 )
        self.grid_rowconfigure( 1 , weight = 1 )

        # Make label
        
        self.my_label = tk.Label( self , text = 'Hello World' )

        # Place label
        
        self.my_label.grid( column = 0 , row = 0 )

        # Make button
        
        self.my_button = tk.Button( self , text = 'Press' , command = self.do_change )

        # Place button
        
        self.my_button.grid( column = 0 , row = 1 )

    def do_change( self ):
        self.my_label.config( text = 'You pressed the button!' )

MyButton( root ).pack()

root.mainloop()
