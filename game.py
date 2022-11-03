# game gui

# reference: 
# What: tkinter demo for displaying a moving shape
# Where: https://www.quickprogrammingtips.com/python/how-to-create-canvas-animation-using-tkinter.html
# Why: reference for displaying a moving bar

import tkinter
 
class Game():
    # window size
    window_width=1500
    window_height=800

    # bar size and postion
    bar_width = 50
    bar_height = 150
    bar1_x = 1400
    
    bar1 = None

    exit = False

    # main window of the animation
    def create_animation_window(self):
        window = tkinter.Tk()
        window.title("IMU Visualization Demo")
        window.geometry(f'{self.window_width}x{self.window_height}')
        window.protocol("WM_DELETE_WINDOW", self.on_close)
        return window
    
    # create a canvas for animation and add it to main window
    def create_animation_canvas(self, window):
        canvas = tkinter.Canvas(window)
        canvas.configure(bg="black")
        canvas.pack(fill="both", expand=True)
        return canvas

    # get position
    def get_position(self):
        self.bar1.pos = 1

    # initialize window
    def initialize(self):
        self.window = self.create_animation_window()
        self.canvas = self.create_animation_canvas(self.window)
        
    # update bar position
    def update_frame(self, value):
        if self.bar1 is not None: 
            self.canvas.delete(self.bar1)
        self.bar1 = self.draw_bar(self.bar1_x, self.new_position(value))
        self.window.update()

    # calculate new position
    def new_position(self, value):
        new_pos =  int(value * self.window_height /2 + self.window_height /2 )
        if new_pos < self.bar_height/2:
            return self.bar_height/2
        elif new_pos > self.window_height - self.bar_height/2:
            return self.window_height - self.bar_height/2
        else:
            return new_pos

    # draw bar
    def draw_bar(self, x, y):
        return self.canvas.create_rectangle(x-(self.bar_width)/2, 
            y-(self.bar_height)/2, 
            x+(self.bar_width)/2, 
            y+(self.bar_height)/2, 
            fill="#fff")

    def on_close(self):
        print("exiting...")
        self.exit = True
        self.window.destroy()
