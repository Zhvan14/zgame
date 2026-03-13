import tkinter as tk
class Sprite:
    def __init__(self, canvas, x, y, color, width=30, height=30):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x + width, y + height, fill=color)
        self.x_speed = 0
        self.y_speed = 0
    def move(self, x_speed, y_speed):
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.canvas.move(self.id, self.x_speed, self.y_speed)
class Window(tk.Tk):
    def __init__(self, title, geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)     
        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)    
        self.sprites = []
        self._engine_loop()
    def sprite(self, x, y, color):
        new_sprite = Sprite(self.canvas, x, y, color)
        self.sprites.append(new_sprite)
        return new_sprite
    def button(self, text, command, **kwargs):
        btn = tk.Button(self, text=text, command=command, **kwargs)
        self.canvas.create_window(10, 10, window=btn, anchor="nw")
    def _engine_loop(self):
        for sprite in self.sprites:
            sprite.update()
        self.after(16, self._engine_loop)
    def run(self):
        self.mainloop()