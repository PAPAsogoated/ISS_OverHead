import requests
from datetime import datetime
import smtplib as smt
my_email = "parsagp77@gamil.com"
my_pass = "odtc bwse zvbf xxqi"

MY_LAT = 47.535365 #your latitude
MY_LONG = 19.002849 #your longitude

def is_iss_close():
    """this function gets the ISS coordinates data and checks if the iss is close to your coordinates."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5 :
        return True

def is_night():
    """this function checks if it is night in your location so the the ISS is visible."""



    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now>= sunset or time_now<= sunrise:
        return True

#if the ISS is close to your location
# and it is currently night
# send an email to inform 


while True:
    if is_night() and is_iss_close():
        connection = smt.SMTP("smtp.gmail.com", port=587) #your SMTP address
        connection.starttls()
        connection.login(my_email, my_pass)
        connection.send_message(from_addr=my_email,
                                to_addrs="your email",
                                msg="the informing message" 
                                    )