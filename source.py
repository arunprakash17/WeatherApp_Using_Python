from geopy.geocoders import Nominatim
from tkinter import *
import tkinter as tk
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
root=Tk()
root.title("Wether App")
root.geometry("900x500+200+100")
root.resizable(False,False)

def getWeather():

    
    city=textfield.get()
        
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
            
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
        
     
        #weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9a1e349e3883d619bde78d0a6883feb8"
        
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
        
    t.config(text=(temp,'°'))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)
    #except Exception as e:
     #   messagebox.showerror("Weather App","Invalid Entry!")
    

#search box

Search_image=PhotoImage(file="images/search.png")
myimage=Label(root,image=Search_image)
myimage.place(x=20,y=20)

textfield=Entry(root,justify="center",width=17,font=("Consolas",25,"bold"),bg="#404040",fg="white",border=0)
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="images/Search_icon.png")
myimage_icon=Button(root,image=Search_icon,cursor="hand2",bg="#404040",command=getWeather,fg="green",borderwidth=0)
myimage_icon.place(x=400,y=34)

#logo
Logo_image=PhotoImage(file="images/logo.png")
logo=Label(root,image=Logo_image,text="")
logo.place(x=150,y=100)

#Bottom box
Frame_image=PhotoImage(file="images/box.png")
frame_myimage=Label(root,image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("Consolas",17,"bold"),fg="green")
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20,"bold"),fg="#111")
clock.place(x=30,y=130)

#label

label1=Label(root,text="WIND",font=("Consolas",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Consolas",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=225,y=400)

label3=Label(root,text="DESCRIPTION",font=("Consolas",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Consolas",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(root,font=("arial",70,"bold"),fg="#ee666d")
t.place(x=430,y=150)
c=Label(root,font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(root,text="....",font=("arial",19,"bold"),bg="#1ab5ef")
w.place(x=130,y=430)

h=Label(root,text="....",font=("arial",19,"bold"),bg="#1ab5ef")
h.place(x=250,y=430)

d=Label(root,text="....",font=("arial",19,"bold"),bg="#1ab5ef")
d.place(x=440,y=430)

p=Label(root,text="....",font=("arial",19,"bold"),bg="#1ab5ef")
p.place(x=670 ,y=430)



root.mainloop()


