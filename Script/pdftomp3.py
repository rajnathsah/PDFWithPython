from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pdftotext
from gtts import gTTS

root = Tk()
filelocation = askopenfilename()
#print(filelocation)

with open(filelocation, 'rb') as f:
    try:        
        pdf = pdftotext.PDF(f)
    except Exception as ex:
        print(ex)
        
string_of_text = ''
#print(pdf[0])
for text in pdf:
    #print(text)
    string_of_text += text
    
final_file = gTTS(text=string_of_text, lang='en')  # store file in variable
final_file.save("Generated Speech.mp3")  # save file to computer    
#print(string_of_text)
    