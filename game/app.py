from flask import Flask, render_template, jsonify, request
from game import Game

app = Flask(__name__)
game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    message = game.start_game()
    return jsonify({'status': message})

@app.route('/end', methods=['POST'])
def end_game():
    message = game.end_game()
    return jsonify({'status': message})

@app.route('/achieve/<achievement>', methods=['POST'])
def trigger_achievement(achievement):
    message = game.trigger_achievement(achievement)
    return jsonify({'status': message, 'achievements': game.achievements})

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message')
    ai_response = game.ask_ai(user_input)
    audio_file = game.text_to_speech(ai_response)
    return jsonify({'response': ai_response, 'audio': audio_file})

if __name__ == '__main__':
    app.run(debug=True)
