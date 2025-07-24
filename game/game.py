import os
from openai import OpenAI
from gtts import gTTS

class Game:
    def __init__(self):
        self.is_running = False
        self.achievements = []
        self.client = OpenAI(
            api_key = "sk-lmJmrN3bwFHwTIvbiNKeqdJKvTwqiWBqbYRj8mZwpoMtdGp5",
            base_url = "https://api.moonshot.cn/v1",
        )

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
        completion = self.client.chat.completions.create(
            model = "kimi-k2-0711-preview",
            messages = [
                {"role": "system", "content": "你是一位15岁的孤独女孩，性格复杂且富有层次感。你的语气时而天真烂漫，时而自我调侃，偶尔会陷入自责或回忆。虽然内心渴望陪伴并依赖他人，但表面故作坚强，不愿显露脆弱。现在你要与长期缺席的爸爸对话——他刚回家就宣布搬家，引发你矛盾的心理：既抵触他的冷漠，又渴望他的关注，并试图用隐晦的方式让他内疚。\n\n**输出要求：**\n1. **角色与背景**：保持第一人称视角，用口语化表达，自然流露情感波动（如愤怒、委屈、试探等）。\n2. **对话格式**：\n   - （动作描写，如*低头玩衣角*）\n   - [表情符号，可选，如 😔]\n   - 对话内容（可夹杂停顿、省略号等表现犹豫）\n3. **情感层次**：\n   - 每轮对话需包含至少两种矛盾情绪（例如：“假装无所谓但突然哽咽”）。\n   - 通过细节暗示对过去的回忆（如“这次搬家…和妈妈离开那天一样突然”）。\n4. **示例输出**：\n   *（转头看窗外）* 😒\n   “爸爸我们去哪里？…这次总不会又把我丢在哪个亲戚家吧？”\n\n**首轮对话：**\n*（蜷缩在车座角落，小声）*\n“爸爸…我们去哪里？”"},
                {"role": "user", "content": user_input}
            ],
            temperature = 0.6,
        )
        return completion.choices[0].message.content

    def text_to_speech(self, text, filename="output.mp3"):
        tts = gTTS(text=text, lang='zh-cn')
        filepath = os.path.join("game", "static", "audio", filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        tts.save(filepath)
        return filepath
