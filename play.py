import tkinter as tk

# My Grid inherits from the Frame class

class SmallGrid( tk.Frame ):
    def __init__( self , master ):
        tk.Frame.__init__( self , master )

        # Pack into master, extending in both horizontally and vertically
        # tk.X for just horizontal and tk.Y for just vertical
        
        self.pack( fill = tk.BOTH , expand = 1 )

        # Choose my background
        
        self.config( background = "blue" )

        # Create some widgets
        
        self.action = tk.Button( self , text = "Go" , command = self.amend )
        self.label = tk.Label( self , text = "Again" )

        # Set up grid

        self.grid_rowconfigure( 0 , weight = 1)
        self.grid_columnconfigure( 0 , weight = 1)
        self.grid_columnconfigure( 1 , weight = 1)

        # Place widgets in grid
        
        self.action.grid( row = 0 , column = 0 , sticky = "" )
        self.label.grid( row = 0 , column = 1 ,sticky = "" )

    # Show that the button does something and the frame resizes

    def amend( self ):
        self.label.config( text = "And again" )

# My Big Grid is also a frame

class BigGrid( tk.Frame ):
    def __init__( self , master ):
        tk.Frame.__init__( self , master )

        # Pack into master

        self.pack( fill =tk.BOTH , expand = 1 )


        # Create some widgets, one of which is a frame which will contain my small grid

        self.label = tk.Label( self , text = "Title" )
        self.wrapper_frame = tk.Frame( self )
        self.small_grid = SmallGrid( self.wrapper_frame )
        self.button = tk.Button( self , text = "Another button" , command = self.small_grid.amend  )
        

        # Layout grid
        
        self.grid_rowconfigure( 0 , weight = 1)
        self.grid_rowconfigure( 1 , weight = 1)
        self.grid_rowconfigure( 2 , weight = 1)
        self.grid_columnconfigure( 0 , weight = 1)
        
        # Place widgets in grid

        self.label.grid( row = 0 , column = 0 , sticky = "" )
        self.wrapper_frame.grid( row = 1 , column = 0 , sticky = "news" )
        self.button.grid( row = 2 , column = 0 , sticky = "" )

def show_hierarchy( win ):
    print( win  )
    
    for w in win.winfo_children():
        show_hierarchy( w )

                        

root = tk.Tk()


my_big_grid = BigGrid( root )

show_hierarchy( root )


root.mainloop()
