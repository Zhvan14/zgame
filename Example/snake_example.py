from zgame import zg
import random
import tkinter

CELL_SIZE = 50
WIDTH = 40
HEIGHT = 20

snake = [(10, 10)]
direction = "Right"
food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
game_over = False

# Draw game objects
def draw():
    zg.fill("black")
    for x, y in snake:
        zg.draw_shape("rectangle", f"snake_{x}_{y}", "green", x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE)
    fx, fy = food
    zg.draw_shape("rectangle", "food", "red", fx*CELL_SIZE, fy*CELL_SIZE, CELL_SIZE)
    draw_buttons()

# On-screen buttons coordinates
BUTTON_SIZE = 40
BUTTON_Y = HEIGHT*CELL_SIZE + 20
buttons = {
    "up":    (WIDTH*CELL_SIZE//2 - BUTTON_SIZE//2, BUTTON_Y),
    "down":  (WIDTH*CELL_SIZE//2 - BUTTON_SIZE//2, BUTTON_Y + 60),
    "left":  (WIDTH*CELL_SIZE//2 - 60, BUTTON_Y + 30),
    "right": (WIDTH*CELL_SIZE//2 + 60 - BUTTON_SIZE, BUTTON_Y + 30)
}

def draw_buttons():
    for name, (x, y) in buttons.items():
        zg.draw_shape("rectangle", f"btn_{name}", "gray", x, y, BUTTON_SIZE)
        zg.draw_text(name[0].upper(), x+BUTTON_SIZE//2, y+BUTTON_SIZE//2, f"text_{name}", size=16, color="white")

# Move snake
def move_snake():
    global snake, food, game_over
    if game_over:
        return
    head_x, head_y = snake[-1]
    if direction == "Up": head_y -= 1
    elif direction == "Down": head_y += 1
    elif direction == "Left": head_x -= 1
    elif direction == "Right": head_x += 1
    new_head = (head_x, head_y)

    if new_head in snake or not (0 <= head_x < WIDTH and 0 <= head_y < HEIGHT):
        game_over = True
        zg.draw_text("Game Over", WIDTH*CELL_SIZE//2, HEIGHT*CELL_SIZE//2, "game_over", size=20, color="white")
        return

    snake.append(new_head)
    if new_head == food:
        food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
    else:
        snake.pop(0)

    draw()
    zg.root.after(150, move_snake)

# Controls
def go_up():    global direction; direction = "Up"
def go_down():  global direction; direction = "Down"
def go_left():  global direction; direction = "Left"
def go_right(): global direction; direction = "Right"

zg.key_down("Up", go_up)
zg.key_down("Down", go_down)
zg.key_down("Left", go_left)
zg.key_down("Right", go_right)

# Mouse clicks for buttons
def click_handler():
    def handler():
        x, y = zg.root.winfo_pointerx() - zg.canvas.winfo_rootx(), zg.root.winfo_pointery() - zg.canvas.winfo_rooty()
        for name, (bx, by) in buttons.items():
            if bx <= x <= bx+BUTTON_SIZE and by <= y <= by+BUTTON_SIZE:
                if name == "up": go_up()
                elif name == "down": go_down()
                elif name == "left": go_left()
                elif name == "right": go_right()
    return handler

zg.mouse_down(1, click_handler())

draw()
move_snake()
zg.run()
