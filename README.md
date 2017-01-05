# Phone Notifications using **Macrodroid**
This is a small project for my own use that will allow me to get the notifications from my phone on my computer.

# How to use:
* Install **Macrodroid** on android
* Configure a macro in **Macrodroid** with these settings:
  * Triggers - Notification Received
  * Action 1 - Set variable with name notif to **[not_title]-[notification]**
  * Action 2 - UDP Command to your computer ip and port and choose the **Macrodroid** variable "notif" as the message
* Run app.py and you're done :D
