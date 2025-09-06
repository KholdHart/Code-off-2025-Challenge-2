# BrickBall 2025

A classic arcade-style brick breaker game built with Python and Pygame. Smash bricks, collect powerups, and aim for a high score!

## How to Run

### Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/) library

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/KholdHart/Code-off-2025-Challenge-2.git
   ```

2. **Install Pygame**

   You can install pygame using pip:

   ```bash
   pip install pygame
   ```

3. **Navigate to the Game Directory**

   ```bash
   cd Code-off-2025-Challenge-2/BrickBall2025
   ```

### Running the Game

Launch the game from the command line:

```bash
python brickball.py
```

A window will open with the game. Use the left and right arrow keys to control the paddle at the bottom of the screen.

## Gameplay

- **Objective:** Destroy all bricks by bouncing balls off your paddle.
- **Lives:** You start with 9 lives. Lose a life when the ball falls below the paddle.
- **Powerups:** Occasionally, breaking bricks spawns powerups:
  - `life` — Gain an extra life
  - `expand` — Make your paddle longer
  - `shrink` — Make your paddle shorter
  - `multi` — Adds an extra ball
  - `slow` — Slows down ball speed
- **High Score:** Your best score is saved between sessions in `high_score.txt`.

## Controls

- **Left Arrow:** Move paddle left
- **Right Arrow:** Move paddle right
- **R:** Restart after game over or win
- **Q:** Quit after game over or win

## Using VS Code

To edit and run the game in [Visual Studio Code](https://code.visualstudio.com/):

1. **Open the Project Folder in VS Code**
2. **Install the Python Extension:**
   - Click on the Extensions icon (side bar) or press `Ctrl+Shift+X`
   - Search for **"Python"** (by Microsoft)
   - Click **Install**
   - This enables Python syntax highlighting, linting, debugging, and running files directly.
3. **Select Your Python Interpreter:**
   - Press `Ctrl+Shift+P` and type `Python: Select Interpreter`
   - Choose your installed Python version

Now you can run and debug `brickball.py` directly from VS Code!

## Files

- `BrickBall2025/brickball.py` — Main game script
- `high_score.txt` — Stores high scores (created automatically)

## License

MIT (or specify your license here)

---

Enjoy the game and aim for the high score!
