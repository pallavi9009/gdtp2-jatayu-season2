import speech_recognition as sr
import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def text_to_speech():
    input_text = input_box.get("1.0", tk.END).strip()
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, input_text)
    engine.say(input_text)
    engine.runAndWait()
