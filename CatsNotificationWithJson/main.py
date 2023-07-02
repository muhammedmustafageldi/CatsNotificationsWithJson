from plyer import notification
import time
import requests

while True:
    catsTip = None

    try:
        catsTip = requests.get("https://catfact.ninja/fact")
    except:
        print("Please check your internet connection")

    if catsTip is not None:
        jsonData = catsTip.json()
        fact = jsonData['fact']

        print("Fact:", fact)

        notificationTitle = "About The Cats"
        notificationMessage = fact
        iconPath = 'cat.ico'

        notification.notify(title=notificationTitle, message=notificationMessage, app_icon=iconPath)

    time.sleep(60*60*12)
