import speech_recognition as sr
import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk

recognizer = sr.Recognizer()
engine = pyttsx3.init()

window = tk.Tk()
window.title("Speech to Text and Text to Speech")

# Increase the size of the window
window.geometry("400x400")
window.configure(bg="white")

# Load the microphone image
mic_image = Image.open("C:/Users/acer/Downloads/microphone-icon-png.jpg")
mic_image = mic_image.resize((30, 30))  # Resize the image if needed
mic_photo = ImageTk.PhotoImage(mic_image)

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

def text_to_speech():
    input_text = input_box.get("1.0", tk.END).strip()
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, input_text)
    engine.say(input_text)
    engine.runAndWait()

# Create the header label
header_label = tk.Label(window, text="Speech to Text and Text to Speech", font=("Arial", 16, "bold"), bg="white")
header_label.pack(pady=10)

# Create a frame for the search bar
search_frame = tk.Frame(window, bg="white", bd=2, relief=tk.RAISED)
search_frame.pack(pady=10)

# Create the microphone button
mic_button = tk.Button(search_frame, image=mic_photo, command=speech_to_text, bd=0, highlightthickness=0)
mic_button.pack(side=tk.LEFT, padx=5, pady=5)

# Create a text box for input
input_box = tk.Text(search_frame, height=1, width=30, font=("Arial", 12), bd=0)
input_box.pack(side=tk.LEFT, padx=5)

# Create a frame for the output section
output_frame = tk.Frame(window, bg="white", bd=2, relief=tk.RAISED)
output_frame.pack(pady=10)

# Create a label for the output text
output_label = tk.Label(output_frame, text="Output:", font=("Arial", 14, "bold"), bg="white")
output_label.pack()

# Create a text box for displaying the output text
output_text = tk.Text(output_frame, height=5, width=30, font=("Arial", 12), bd=0)
output_text.pack()

# Create a button for text-to-speech
speak_button = tk.Button(window, text="Speak Text", command=text_to_speech, bg="#4CAF50", fg="white", relief=tk.RAISED)
speak_button.pack(pady=10)

window.mainloop()
