# Gamified Experience

This project is a gamified Python application with a web interface. The application features a 15-year-old girl character who interacts with the user through an AI-powered chat interface. The AI's responses are converted to speech and played back to the user. The application also includes a simple achievement system and animations.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python game/app.py
   ```
2. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

- `game/app.py`: The main Flask application file.
- `game/game.py`: The core game logic.
- `game/templates/index.html`: The main HTML file for the frontend.
- `game/static/`: The directory for static files (CSS, images, etc.).
- `requirements.txt`: The list of Python dependencies.
