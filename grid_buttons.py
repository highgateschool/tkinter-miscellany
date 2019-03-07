import tkinter as tk

class MyFirstGUI:
    def __init__( self , master ):
        self.master = master
        master.title("A simple GUI")

        # Create buttons
        self.button_a = tk.Button( master , text = 'Choice a' , command = self.raiseA )
        self.button_b = tk.Button( master , text = 'Choice b' , command = self.raiseB )

        # Create menus to associate with frames

        self.frame_a = tk.Frame( self.master , background = "Blue"  )
        self.frame_b = tk.Frame( self.master , background = "Red"  )

        # Populate menus

        self.menu_a = MenuA( self.frame_a )
        self.menu_b = MenuB( self.frame_b )

        # And another button

        self.button_c = tk.Button( master , text = 'Exit' )

        # Layout the screen

        self.button_a.grid( row = 0 , column = 0 , sticky = 'ew' , padx = 3 , pady = 3 )
        self.button_b.grid( row = 0 , column = 1 , sticky = 'ew' , padx = 3 , pady = 3 )
        self.frame_a.grid( row = 1 , column = 0 , columnspan = 2)
        self.button_c.grid( row = 2 , column = 0 , columnspan = 2 , pady = 3 )

        # Now describe the rows and columns
        master.grid_columnconfigure( 0 , weight = 1 )
        master.grid_columnconfigure( 1 , weight = 1 )
        master.grid_columnconfigure( 0 , weight = 1 )
        master.grid_rowconfigure( 1 , weight = 1 )
        master.grid_rowconfigure( 2 , weight = 0 )


    def raiseA( self ):
        self.frame_b.grid_forget()
        self.frame_a.grid( row = 1 , column = 0 , columnspan = 2)
        
    def raiseB( self ):
        self.frame_a.grid_forget()
        self.frame_b.grid( row = 1 , column = 0 , columnspan = 2)
 

class MenuA:
    def __init__( self , master ):
        self.master = master

        # Create content

        self.label = tk.Label( master , text = 'This is menu A' )
        self.entry = tk.Entry( master )

        # Layout the frame

        self.label.grid( row = 0 )
        self.entry.grid( row = 1 )

        # Now describe the rows and columns
        
        master.grid_rowconfigure( 0 , weight = 1 )
        master.grid_rowconfigure( 1 , weight = 0 )



class MenuB:
    def __init__( self, master ):
        self.master = master

        # Create label

        self.label = tk.Label( master , text = 'This is menu B' )
        self.label.grid()

        # Layout the frame



root = tk.Tk()
my_gui = MyFirstGUI( root )
root.mainloop()
