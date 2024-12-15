from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
try:
    data=pandas.read_csv("data/new_data.csv")

except (FileNotFoundError,AttributeError):
    original_val=pandas.read_csv("data/Tamil_words.csv")
    val=pandas.DataFrame(original_val)
    data=val

new_list=data.to_dict(orient="records") #Converts panda to list of dict

save_list=[]
window=Tk()
window.title="Flash Card"
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
time_left=6


flip_timer = None

def flip():

    canvas.itemconfig(bg_canvas, image=img2)
    canvas.itemconfig(top_txt,text="English")
    canvas.itemconfig(btm_txt,text=f"{save_list[0]}")
    save_list.clear()




def read_data():
       global flip_timer,current_card,time_left

       if flip_timer:
        window.after_cancel(flip_timer)
       canvas.itemconfig(bg_canvas,image=img)
       current_card = random.choice(new_list)
       word_ta = (current_card["Tamil"])
       save_list.clear()
       save_list.append(current_card["English"])
       canvas.itemconfig(top_txt,text=f"Tamil")
       canvas.itemconfig(btm_txt, text=f"{word_ta}")
       flip_timer = window.after(5000, flip)



def is_known():
    if current_card in new_list:
        new_list.remove(current_card)
        datum=pandas.DataFrame(new_list)
        datum.to_csv("data/new_data.csv")
        read_data()
    else:
        read_data()



canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR)
img=PhotoImage(file="images/card_front.png")
img2=PhotoImage(file="images/card_back.png")
bg_canvas=canvas.create_image(400, 262,image=img)
canvas.grid(row=0,column=0,columnspan=2)



top_txt=canvas.create_text(400,150,text="Title",font=("Ariel",20,"italic","bold"))
btm_txt=canvas.create_text(400,250,text="Word",font=("Ariel",40,"bold"))

right=PhotoImage(file="images/right.png")
right_un=Button(image=right,command=is_known)
right_un.grid(row=1,column=0)

wrong=PhotoImage(file="images/wrong.png")
wrong_un=Button(image=wrong,command=read_data)
wrong_un.grid(row=1,column=1)

read_data()

window.mainloop()
