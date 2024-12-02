import pyttsx3
import speech_recognition as sr
import pyaudio

print("PyAudio успешно установлен!")
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:"
from datetime import datetime

with open('song.txt', 'r', encoding='UTF-8') as song:
    song_read = song.read()



class ChatBot:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # скорость речи
        self.engine.setProperty('volume', 5.0)  # Громкость
        self.response = {
            'как тебя зовут': 'Меня зовут ККС Бот молиывлмоиывьмжыфвьдадлывожфипвлжофиамлдифлдомвиылдфивлдмо',
            'на каком курсе ты учишься': "В данный момент я не могу учиться так как я Бот",
            'твое любимое блюдо': 'Шаурма',
            'песня': song_read,
        }
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def get_response(self, user_input):
        if 'время' in user_input:
            now = datetime.now().strftime('%H:%M')
            return f'Сейчас {now}'
        return self.response.get(user_input, 'Сорян я не знаю что ответить!')

    def listen(self):
        with sr.Microphone() as source:
            print('Слушаю тебя мой дорогой!')
            self.speak('Слюшаю тибя мой дорогой чаловэк!')
            try:
                audio = self.recognizer.listen(source, timeout=7, phrase_time_limit=5)
                text = self.recognizer.recognize_google(audio, language='ru-RU')  # Используем публичный Google API
                print(f'Ай дорогой ти сказяль {text}')
                return text.lower()
            except sr.UnknownValueError:
                print('Ай дорогой я тибиуа ни поняль')
                self.speak('Ай дорогой я тибиуа ни поняль')
            except sr.RequestError:
                print('Ошбика подключения к серверу')
                self.speak('Ошибка подключения к серверу')
            except sr.WaitTimeoutError:
                print('Не молчи ну плииииз!')
                self.speak('Не молчи ну плииииз!')
            return None

    def start(self):
        print('Иоу есть пару вопросов Чувак!')
        self.speak('Задай вопрос ну плиииииз!')

        while True:
            user_input = self.listen()
            if user_input is None:
                continue
            if 'выход' in user_input:
                print('Адиос Амигос')
                self.speak('Адиос Амигос Амикардос')
                break
            response = self.get_response(user_input)
            print(f'Бот сказал: {response}')
            self.speak(response)


if __name__ == '__main__':
    bot = ChatBot()
    bot.start()
