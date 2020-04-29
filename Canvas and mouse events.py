import tkinter
from tkinter import ttk

class PenData(object):
    def __init__(self):
        self.color = 'blue'
        self.mouse_position_x = None
        self.mouse_position_y = None
        self.is_dragging = False

def mainclass():
        pen_data = PenData()

        root = tkinter.Tk()

        main_frame = ttk.Frame(root, padding=5).grid()

        instruct = 'Click the left mouse button to make circles,/n'
        instruct = instruct + 'drag left mouse button to draw'
        label = ttk.Label(main_frame, text=instruct).grid()

        #Draw canvas
        canvas = tkinter.Canvas(main_frame, background='lightgray').grid()

        #Make callback
        canvas.bind('<Button-1>', lambda event: left_mouse_click(event))
        canvas.bind('<B1-Motion>', lambda event: left_mouse_drag(event, pen_data))
        canvas.bind('<B1-ButtonRelease>', lambda event: left_mouse_release(pen_data))

        #button to change color
        button = ttk.Button(main_frame, text='Flip pen color').grid()
               button['command'] = lambda: flip_pen_color(pen_data)

        root.mainloop()


def left_mouse_click(event):
        canvas = event.widget
        canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y +10, fill='green', width=3)

def left_mouse_drag(event, data):
        canvas = event.widget
        if data.is_dragging:
            canvas.create_line(data.mouse_position_x, data.mouse_position_y, event.x, event.y, fill=data.color, width=5)
        else:
            data.is_dragging = True
            data.mouse_position_x = event.x
            data.mouse_position_y = event.y

def left_mouse_release(data):
        data.is_dragging = False

def flip_pen_color(data):
        if data.color == 'blue':
           data.color = 'red'
        else:
            data.color = 'blue'


mainclass()
    

        
