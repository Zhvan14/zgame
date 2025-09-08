# ZGame

ZGame is a simple, intuitive game engine for Python. 

## Installation

```bash
pip install zgame

# zgame Commands

## Fill Background
```python
zg.fill(color="white")
# color: optional, default "white"
```

## Draw Shape
```python
zg.draw_shape(shape_type="rectangle", name=None, color="black", x=0, y=0, size=50)
# shape_type: optional, default "rectangle" (options: "rectangle", "oval")
# name: optional, string identifier
# color: optional, default "black"
# x: optional, default 0
# y: optional, default 0
# size: optional, default 50
```

## Draw Text
```python
zg.draw_text(text, x=0, y=0, name=None, size=20, color="black")
# text: required
# x: optional, default 0
# y: optional, default 0
# name: optional
# size: optional, default 20
# color: optional, default "black"
```

## Draw Sprite
```python
zg.draw_sprite(path, name=None, x=0, y=0)
# path: required (file path)
# name: optional
# x: optional, default 0
# y: optional, default 0
```

## Move
```python
zg.move(name, dx=0, dy=0)
# name: required
# dx: optional, default 0
# dy: optional, default 0
```

## Go To Position
```python
zg.goto(name, x=0, y=0)
# name: required
# x: optional, default 0
# y: optional, default 0
```

## Delete
```python
zg.delete(name)
# name: required
```

## Key Press
```python
zg.key_down(key, function)
# key: required (e.g., "Up", "Down", "space")
# function: required, callable to execute on key press
```

## Mouse Click
```python
zg.mouse_down(button=1, function=None)
# button: optional, default 1
#   1 = Left click (default)
#   2 = Middle click
#   3 = Right click
# function: required, callable to execute on click
```

## Sprite Click
```python
zg.sprite_down(name, function)
# name: required
# function: required, callable to execute on click
```

## Collision
```python
zg.collides(name1, name2, function)
# name1: required
# name2: required
# function: required, callable to execute on collision
```

## Update Canvas
```python
zg.update()
# no arguments, optional to call manually
```

## Run Game
```python
zg.run(fps=60)
# fps: optional, default 60
```

## Stop Game
```python
zg.stop()
# no arguments
```

