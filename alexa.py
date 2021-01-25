#!/bin/python

import os
import sys
from datetime import datetime
import time

import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import pyjokes
import play_on_yt


class Alexa:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.get_input()

    def get_input(self):
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice, language='de-DE').lower()
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                    print(command)
                    self.run_alexa(command)
        except:
            pass

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def run_alexa(self, command):
        if 'time' in command or 'what time is it' in command:
            current_time = str(self.return_current_time())
            self.talk(current_time)
        elif 'date' in command:
            date = self.return_date()
            self.talk(date)
        elif ' play ' in command:
            video = command.replace('play', '')
            self.talk('Playing ' + video)
            self.play_on_yt(video)
        elif 'what is' in command or 'wikipedia' in command:
            search = command.replace('what is ', '')
            search = search.replace(' wikipedia ', '')
            self.talk(self.return_wikipedia_info(search))
        elif 'joke' in command:
            joke = pyjokes.get_joke(category='all')
            print(joke)
            self.talk(joke)
        elif 'translate' in command or 'into english' in command:
            words = command.replace('translate ', '')
            self.translate_into_english(words)
        elif 'translate' in command or 'into german' in command:
            words = command.replace('translate ', '')
            self.translate_into_german(words)
        else:
            self.talk("Sorry I didn't understand. Please repeat!")

    def return_wikipedia_info(self, search_string):
        search_string = search_string.replace(' ', '_')
        url = f'https://en.wikipedia.org/wiki/{search_string}'
        webbrowser.open(url)
        info = wikipedia.summary(search_string, 5)
        return info

    def return_date(self):
        date = datetime.today().strftime('%d-%B')
        return date

    def return_current_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        return current_time

    def play_on_yt(self, video):
        if 'second entry' in video:
            video = video.replace('second entry', '')
            play_on_yt.PlayOnYt(video)
        if 'third entry' in video:
            video = video.replace('second entry', '')
            play_on_yt.PlayOnYt(video)
        elif 'second entry' not in video and 'third entry' not in video:
            play_on_yt.PlayOnYt(video)

    def translate_into_german(self, words):
        print(words)
        url = f'https://www.deepl.com/de/translator#en/de/{words}'
        webbrowser.open(url)

    def translate_into_english(self, words):
        print(words)
        url = f'https://www.deepl.com/en/translator#de/en/{words}'
        webbrowser.open(url)


if __name__ == '__main__':
    alexa = Alexa()
