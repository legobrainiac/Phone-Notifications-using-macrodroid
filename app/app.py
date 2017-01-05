from PyQt5 import Qt
import sys
import socket

IPPORT = ("",5000)

Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Socket.bind(IPPORT)

def DisplayNot(text):
    app = Qt.QApplication(sys.argv)
    bubble = Qt.QSystemTrayIcon(app)
    bubble.show()
    bubble.showMessage('Phone Notification', text)
    pass

while True:
    data = Socket.recv(1024)
    DisplayNot(data.decode("utf-8"))
    pass
