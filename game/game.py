import os
from gtts import gTTS
from game.ai import AI

class Game:
    def __init__(self):
        self.is_running = False
        self.achievements = []
        self.ai = AI()

    def start_game(self):
        self.is_running = True
        return "Game started!"

    def end_game(self):
        self.is_running = False
        return "Game over!"

    def trigger_achievement(self, achievement):
        self.achievements.append(achievement)
        return f"Achievement unlocked: {achievement}"

    def ask_ai(self, user_input):
        return self.ai.ask(user_input)

    def text_to_speech(self, text, filename="output.mp3"):
        tts = gTTS(text=text, lang='zh-cn')
        filepath = os.path.join("game", "static", "audio", filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        tts.save(filepath)
        return filepath
