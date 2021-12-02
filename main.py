from tkinter import *
import PyPDF2
from tkinter import filedialog, messagebox
import pyttsx3
from gtts import gTTS


root = Tk()
root.title('PDF Converter')
root.geometry('600x700')
root.config(padx=100, pady=50, bg="#F7EADD")

pdf_text = " "


def open_pdf():
    open_file = filedialog.askopenfilename(
        initialdir="/", title="open pdf file",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
    )
    return open_file


def upload_pdf():
    global pdf_text
    try:
        file_path = open_pdf()
        with open(file_path, "rb") as file:
            pdf = PyPDF2.PdfFileReader(file)

            for page in range(pdf.numPages):
                data = pdf.getPage(page)
                pdf_data = data.extractText()
                pdf_text = pdf_text + pdf_data
                my_text.insert(1.0, pdf_data)
    except FileNotFoundError:
        messagebox.showwarning(title="UPLOAD", message="Please upload file")


def read_pdf():
        engine = pyttsx3.init()
        engine.setProperty('rate', 200)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(my_text.get(1.0, END+"-1c"))
        engine.runAndWait()


def save_audio():
    global pdf_text
    try:
        audio_path = filedialog.asksaveasfilename(defaultextension=".mp3")
        audio_file = gTTS(text=pdf_text, lang="en", tld='co.uk')
        audio_file.save(audio_path)
    except FileNotFoundError:
        messagebox.showwarning("warning", "Save file to play")


my_button = Button(root, text='Upload Pdf', command=upload_pdf, highlightthickness=0, height=2, width=10)
my_button.pack(pady=15)

my_button = Button(root, text='Read Pdf', command=read_pdf, highlightthickness=0, height=2, width=10)
my_button.pack(pady=15)

my_button = Button(root, text='Save Audio', command=save_audio, highlightthickness=0, height=2, width=10)
my_button.pack(pady=15)

my_button = Button(root, text='Exit', command=root.quit, highlightthickness=0, height=2, width=10)
my_button.pack(pady=15)

my_text = Text(root, height=100, width=100, wrap='word', bg='#FEFAF7')
my_text.pack(pady=10)

root.mainloop()
