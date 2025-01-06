import tkinter as tk 
from tkinter import colorchooser


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        
        self.brush_color = "black"
        self.brush_size = 5
        self.current_tool = "brush"

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.toolbar = tk.Frame(self.root, bg="lightgray")
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_tool_buttons()

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonPress-1>", self.start_paint)
        self.canvas.bind("<ButtonRelease-1>", self.stop_paint)

        self.start_x = None
        self.start_y = None
        self.shape_id = None

    def add_tool_buttons(self):
        size_slider = tk.Scale(self.toolbar, from_=1, to=50, orient=tk.HORIZONTAL, label="Размер")
        size_slider.set(self.brush_size)
        size_slider.pack(side=tk.LEFT, padx=5, pady=5)
        size_slider.bind("<Motion>", self.change_brush_size)

        self.color_button = tk.Button(self.toolbar, width=4, command=self.choose_color, bg=self.brush_color)
        self.color_button.pack(side=tk.LEFT, padx=5, pady=5)

        brush_button = tk.Button(self.toolbar, text="Brush", command=lambda: self.set_tool("brush"))
        brush_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        line_button = tk.Button(self.toolbar, text="Line", command=lambda: self.set_tool("line"))
        line_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        rect_button = tk.Button(self.toolbar, text="Rectangle", command=lambda: self.set_tool("rectangle"))
        rect_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        oval_button = tk.Button(self.toolbar, text="Oval", command=lambda: self.set_tool("oval"))
        oval_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        clear_button = tk.Button(self.toolbar, text="Clear", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=5, pady=5)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color
            self.color_button.config(bg=color)

    def change_brush_size(self, event):
        self.brush_size = event.widget.get()

    def set_tool(self, tools):
        self.current_tool = tools

    def start_paint(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.current_tool in ["line", "rectangle", "oval"]:
            self.shape_id = None


    def paint(self, event):
        if self.current_tool == "brush":
            x1 , y1 = event.x - self.brush_size, event.y - self.brush_size
            x2 , y2 = event.x + self.brush_size, event.y + self.brush_size
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline="")

        elif self.current_tool  in  ["line",  "rectangle",  "oval"]  and  self.start_x  and  self.start_y:
             if  self.shape_id:
                 self.canvas.delete(self.shape_id)
             if  self.current_tool  ==  "line":
                 self.shape_id  =  self.canvas.create_line(self.start_x,  self.start_y,  event.x,  event.y,  width=self.brush_size,  fill=self.brush_color)
             elif  self.current_tool  ==  "rectangle":
                 self.shape_id  =  self.canvas.create_rectangle(self.start_x,  self.start_y,  event.x,  event.y,  outline=self.brush_color,  width=self.brush_size)
             elif  self.current_tool  ==  "oval":
                 self.shape_id  =  self.canvas.create_oval(self.start_x,  self.start_y,  event.x,  event.y,  outline=self.brush_color,  width=self.brush_size) 
    
    def stop_paint(self, event):
        self.start_x = None
        self.start_y = None
        self.start_id = None


    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()