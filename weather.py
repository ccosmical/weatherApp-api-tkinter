import tkinter as tk
import requests

api_key="your key"
url="https://api.openweathermap.org/data/2.5/weather"


def getWeather(city):
    parameters = {"appid":api_key, "q":city}
    data = requests.get(url,params=parameters).json()
    print(data)
    if data:
        location= data["name"]
        temperature=int((data["main"]["temp"])-273.15)
        condition=data["weather"][0]["description"]
        return (location, temperature, condition)     
                                                                                                
def main():                                                      
    city = entry.get()           ## get function = return     
    weather=getWeather(city)                                   
    if weather:                                                           
        locationLabel["text"]="{}".format(weather[0])           # returned location 1st in getWeather func
        temperatureLabel["text"]="{}°C".format(weather[1])       # returned location 2nd in getWeather func
        conditionLabel["text"]="{}".format(weather[2])          # returned location 3rd in getWeather func

window = tk.Tk()
window.title("Weather")
window.geometry("300x400")

msg=tk.Label(window, text="Enter the city below")
msg.pack()


entry= tk.Entry(window,justify="center")
entry.focus()
entry.pack()


searchButton=tk.Button(window,text="Search",font=("Arial",10),command= main)
searchButton.pack(ipadx=10, ipady=10)


locationLabel= tk.Label(window)
locationLabel.pack()

temperatureLabel= tk.Label(window)
temperatureLabel.pack()

conditionLabel= tk.Label(window)
conditionLabel.pack()


window.mainloop()

