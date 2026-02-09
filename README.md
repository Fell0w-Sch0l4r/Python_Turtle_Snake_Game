# Turtle Snake Game

A simple Snake game implemented with Python's built-in `turtle` module.

Overview
--------
Move the snake to eat food, grow longer, and try to beat the high score.

Requirements
------------
- Python 3.x (3.8+ recommended)
- `turtle` (included with standard Python on most platforms)

Run
---
From the project directory run:

```bash
python main.py
```

Controls
--------
- Arrow keys: move the snake (Up, Down, Left, Right).

Files
-----
- `main.py`: Game runner that creates the window, instantiates game objects and runs the main loop.
- `snake.py`: Implements the `Snake` class (segments, movement, growth, collision detection).
- `food.py`: Implements the `Food` class (a small turtle that relocates to random positions).
- `scoreboard.py`: Implements the `ScoreBoard` class (displaying score and persisting high score to `HighScore.txt`).
- `HighScore.txt`: Simple text file storing the high score (single integer).

Notes
-----
- `HighScore.txt` must be present and contain a valid integer (the repository includes a default `0`).
- The game uses a 600x600 window and checks collisions near a +/-280 pixel boundary.

License
-------
This project is provided as-is for learning and demonstration purposes.
