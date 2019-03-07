import tkinter as tk

# MyWindow is derived from a Frame

class MyWindow( tk.Frame ):
    def __init__( self , master ):
        tk.Frame.__init__( self , master )

        # Set background

        self.config( background = "red" )

        # Create some widgets, one of which is my small grid

        self.label = tk.Label( self , text = "This is a label" )
        self.left_frame = tk.Frame( self )
        self.small_grid = SmallGrid( self )
        self.right_frame = tk.Frame( self )
        self.button = tk.Button( self , text = "Look another button" , command = self.small_grid.amend )

        # Layout grid

        # Equal weights tell grid we want balanced rows and columns
        # uniform guarantees widths
        
        self.grid_rowconfigure( 0 , weight = 1 , uniform = "b" )
        self.grid_rowconfigure( 1 , weight = 1 , uniform = "b" )
        self.grid_rowconfigure( 2 , weight = 1 , uniform = "b" )
        
        self.grid_columnconfigure( 0 , weight = 1 , uniform = "a" )
        self.grid_columnconfigure( 1 , weight = 1 , uniform = "a" )
        self.grid_columnconfigure( 2 , weight = 1 , uniform = "a" )
      
        # Place widgets in grid

        self.label.grid( row = 0 , column = 0 , columnspan = 3 , sticky = "" )
        self.left_frame.grid( row = 1 , column = 0 , sticky = "news" )
        self.small_grid.grid( row = 1 , column = 1 , sticky = "news" )
        self.right_frame.grid( row = 1 , column = 2 , sticky = "news" )
        self.button.grid( row = 2 , column = 0 , columnspan = 3 , sticky = "" )

# SmallGrid is derived from a Frame

class SmallGrid( tk.Frame ):
    def __init__( self , master ):
        tk.Frame.__init__( self , master )

        # Create a button counter

        self.button_count = 0

        # Set background
        
        self.config( background = "blue" )

        # Create some widgets
        
        self.action = tk.Button( self , text = "This is a button" , command = self.amend )
        self.label = tk.Label( self , text = "And this is a label" )

        # Layout grid

        self.grid_rowconfigure( 0 , weight = 1)
        
        self.grid_columnconfigure( 0 , weight = 1)
        self.grid_columnconfigure( 1 , weight = 1)

        # Place widgets in grid
        
        self.action.grid( row = 0 , column = 0 , sticky = "" )
        self.label.grid( row = 0 , column = 1 ,sticky = "" )

    # Show that the button does something and the frame resizes

    def amend( self ):
        self.button_count += 1
        self.label.config( text = "You pressed a button: " + str( self.button_count ) )


def show_hierarchy( win ):
    print( win  )
    
    for w in win.winfo_children():
        show_hierarchy( w )

# Create root window

root = tk.Tk()

# Give root a title and some geometry

root.title( "Main Window" )
root.geometry( "640x480" )

# Create my window (which is usually a frame inside root)

my_window = MyWindow( root )

# Pack into root

my_window.pack( fill = tk.BOTH , expand = 1 )

# Show my widget hierarchy!

show_hierarchy( root )

# Enter event loop

root.mainloop()
