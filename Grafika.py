from tkinter import *
k=0
def klikker(event):
    global k
    k+=1
    btn.configure(text=k)

def klikkermaha(event):
    global k
    k-=1
    btn.configure(text=k)

def tekst_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0,END) #2,7



aken=Tk()
aken.geometry('400x500')
aken.title('Minu esimene aken')

lbl=Label(aken,text='Elemendid',bg='gold',fg='#AA4A44',font='Arial 20',height=5,width=15)
btn=Button(aken,text='Vajuta siia',font='Arial 24',relief=RAISED)
ent=Entry(aken,fg='blue',bg='Lightblue',width=15,font='Arial 20',justify=CENTER)


btn.bind('<Button-1>',klikker) #lkm
btn.bind('<Button-3>',klikkermaha) #pkm
ent.bind('<Return>',tekst_to_lbl) #Enter
lbl.pack() 
btn.pack(side=BOTTOM)
ent.pack(side=BOTTOM)

aken.mainloop()
