## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound

################### Initialized window####################

root = Tk()
root.geometry('350x300')
root.resizable(0, 0)
root.config(bg='light green')
root.title('DataFlair - TEXT_TO_SPEECH')

##heading
Label(root, text='TEKST KÕNEKS', font='arial 20 bold', bg='light green').pack()

Label(root, text='Kriba siia midagi!', font='arial 22 bold', bg='light green').place(x=50, y=60)

##text variable
Msg = StringVar()

# Entry
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)


###################define function##############################

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')



def Exit():
    root.destroy()


def Reset():
    Msg.set("")


# Button
Button(root, text="räägi", font='arial 15 bold', command=Text_to_speech, width=4, bg='dark green').place(x=30, y=150)
Button(root, text='VÄLJU', font='arial 15 bold', command=Exit, bg='dark red').place(x=220, y=150)
Button(root, text='UUENDA', font='arial 15 bold', command=Reset).place(x=110, y=150)

# infinite loop to run program
root.mainloop()
