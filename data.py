import csv
import os
from tkinter import *


os.chdir("C:\\Users\\maroc\\Desktop\\ECOLE\\Vues")
def Colonne(Numero_Colonne):
    Numero_Colonne-=1
    L=[]
    file = open("1_informations_generales.csv" , "r",encoding='utf8')
    reader = csv.reader(file , delimiter = ";")
    for elt in reader:
        if elt[Numero_Colonne]!='':
            L.append(elt[Numero_Colonne])
    L.pop(0)
    return L


def Tri(Colonne):
    Tri=[]
    Dico={}
    for elt in Colonne:
        if elt not in Tri:
            Tri.append(elt)
    for i in Tri:
        a=Colonne.count(i)
        Dico[i]=a
    return Dico


a=Tri(Colonne(20))
print(a)

app = Tk()
app.title("DATA")
screen_x=int(app.winfo_screenwidth())
screen_y=int(app.winfo_screenheight())
window_x=1920
window_y=1080
posX= ( screen_x // 2) - (window_x // 2)
posY= ( screen_y // 2) - (window_y // 2)
geo="{}x{}+{}+{}".format(window_x,window_y,posX,posY)
app.geometry(geo)
app.configure(bg="#0652DD")
viiide=Label(bg="#0652DD")
viiide.pack()
for i in a:
    lab=Label()
    lab['text']=i +" : "+ str(a[i])
    lab.pack()
    vide=Label(bg="#0652DD")
    vide.pack()
app.mainloop()