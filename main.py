import os
import random
import speech_recognition

# Инициализация распознавателя речи
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

# Словарь команд
commands_dict = {
    'commands': {
        'greeting': ['привет', 'приветствую'],
        'create_task': ['добавить задачу', 'создать задачу', 'заметка'],
        'play_music': ['включить музыку', 'дискотека']
    }
}


def listen_command():
    """Функция для прослушивания команды и распознавания речи"""
    
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            
        return query
    except speech_recognition.UnknownValueError:
        return 'Damn... Не понял что ты сказал :/'


def greeting():
    """Функция для приветствия"""
    
    return 'Привет! Я робот Shefi. Чем могу помочь?'


def create_task():
    """Функция для создания задачи"""
    
    print('Что добавим в список дел?')
    
    query = listen_command()
        
    with open('todo-list.txt', 'a') as file:
        file.write(f'❗️ {query}\n')
        
    return f'Задача {query} добавлена в todo-list!'


def play_music():
    """Функция для воспроизведения случайной музыки"""
    
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'xdg-open {random_file}')
    
    return f'Танцуем под {random_file.split("/")[-1]} 🔊🔊🔊'


def main():
    query = listen_command()
    
    for k, v in commands_dict['commands'].items():
        if query in v:
            print(globals()[k]())
        

if __name__ == '__main__':
    main()