from gtts import gTTS 
  
import os 

fh = open("sample1.txt", "r")
myText = fh.read().replace("\n", " ")

language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")
fh.close()

# Play the converted file 
from playsound import playsound
playsound('output.mp3')
#os.system("output.mp3")
