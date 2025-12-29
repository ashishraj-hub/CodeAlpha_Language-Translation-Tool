from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator
import pyttsx3

engine = pyttsx3.init()

# Window Setup
root = Tk()
root.title("Language Translator")
root.geometry("600x400")

# Languagee List
languages = GoogleTranslator().get_supported_languages(as_dict=True)

def translate_text():
    text = input_text.get("1.0", END).strip()
    if text == "":
        output_text.delete("1.0",END)
        output_text.insert(END,"Please enter some text to translate.")
        return
    
    source = src_lang.get()
    target = tar_lang.get()

    translated = GoogleTranslator(source=source, target=target).translate(text)

    output_text.delete("1.0",END)
    output_text.insert(END,translated)

def clear_all():
    input_text.delete("1.0", END)
    output_text.delete("1.0",END)
    src_lang.set("english")
    tar_lang.set("hindi")

def speak_text():
    text = output_text.get("1.0",END).strip()
    if text=="":
        output_text.insert(END, "\n(No text to speak.)")
        return
    engine.say(text)
    engine.runAndWait()

# UI Design
Label(root, text="Language Translation Tool", font=("Arial",18,"bold")).pack(pady=10)
frame = Frame(root)
frame.pack(pady=10)

#Source Language
Label(frame, text="From:").grid(row=0, column=0)
src_lang = ttk.Combobox(frame, values=list(languages.keys()),width=20)
src_lang.grid(row=0, column=1)
src_lang.set("english")

#Target Language
Label(frame, text="To:").grid(row=0, column=2)
tar_lang = ttk.Combobox(frame, values=list(languages.keys()),width=20)
tar_lang.grid(row=0, column=3)
tar_lang.set("hindi")

# Input Text
input_text = Text(root, height=6, width=70)
input_text.pack(pady=10)

#Translate Button
Button(root, text="Translate", command=translate_text, bg="blue", fg="white").pack()

#Clean Button
Button(frame, text="Clean", command=clear_all, bg="red", fg="white", width=20).grid(row=2, column=0, padx=10)

#Speak Button
Button(frame, text="Speak", command=speak_text, width=20, bg="green", fg="white").grid(row=2, column=1, padx=10)

#Output Text
output_text = Text(root, height=6, width=70)
output_text.pack(pady=10)


root.mainloop()