import datetime #for reading present date
import time 
import requests #for retreiving coronavirus data from web
from plyer import notification #for getting notification on your PC

#let there is no data initially
covidData = None
try:
    covidData = requests.get(("https://corona-rest-api.herokuapp.com/Api/")+input("World/ Enter Country Name: \n"))
    
except:
    #if the data is not fetched due to lack of internet
    print("Please! Check your internet connection")

    #if we fetched data
if (covidData != None):
    
    #converting data into JSON format
    data = covidData.json()['Success']
    
    
    #repeating the loop for multiple times
    t = float(input("Next Notification in (hour): "))
    while(True):
        notification.notify(
            #title of the notification,
            title = "COVID19 Stats on {}".format(datetime.datetime.now()),
            
        
            #the body of the notification
            message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data["active"]),  
            #creating icon for the notification
            #we need to download a icon of ico file format
            app_icon = r"C:\Users\yashk\Downloads\Icons8-Ios7-Healthcare-Virus.ico",
            # the notification stays for 50sec
            timeout  = 50
        )
        #sleep for t hrs => 60*60*t sec
        #notification repeats after every 4hrs
        
        time.sleep(t*60*60)
        if t==0:
            break