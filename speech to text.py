import speech_recognition as sr
import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speech_to_text():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            recognized_text = recognizer.recognize_google(audio)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, recognized_text)
        except sr.UnknownValueError:
            print("Unable to recognize speech")
