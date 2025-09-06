# Annoying Fake YouTube Volume Slider

This project is a playful web demo that simulates an annoying volume slider (like the one on YouTube) that jumps around and resets your volume randomly. It's built using HTML, CSS, and JavaScript.

## Features

- The volume slider moves to a random location when you try to interact with it.
- Occasionally, the slider resets your volume and displays a playful alert.
- Uses a screenshot as a background for a more realistic effect.

## Running the Project

1. **Clone the Repository**
   
   ```bash
   git clone https://github.com/KholdHart/Code-Off-2025-Challenge-1.git
   ```

2. **Navigate to the Project Directory**
   
   ```bash
   cd Code-Off-2025-Challenge-1/Annoying\ Slider
   ```

3. **Open the Demo in Your Browser**
   
   Open the `index.html` file in your web browser (double-click or use a live server extension if using VSCode).

   Alternatively, on the command line:
   ```bash
   open index.html          # macOS
   xdg-open index.html      # Linux
   start index.html         # Windows
   ```

## Project Structure

```
Annoying Slider/
├── index.html      # Main HTML file
├── main.js         # JavaScript for slider logic
├── styles.css      # CSS styling
├── Screenshot 2025-08-24 194221.png # Background image
```

## Requirements

- Modern web browser (Chrome, Firefox, Edge, etc.)
- No additional dependencies required.

## How It Works

- The slider (`input[type=range]`) listens for mouse enter and input events.
- On mouse enter, it jumps to a random location inside the container.
- On input, there’s a 30% chance it resets your volume and shows an alert.

## Notes

- Make sure `Screenshot 2025-08-24 194221.png` is present in the same folder as `styles.css` for the background to display properly.
- This is intended as a fun demo; it does not save or interact with real audio.

## License

MIT (or specify your license here)