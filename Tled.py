# Bibliotheken laden
from gpiozero import LED, Button
from datetime import datetime as DateTime
import sqlite3, os, time


verbindung = sqlite3.connect('LED.db')
zeiger = verbindung.cursor()


db_creat = """
CREATE TABLE IF NOT EXISTS TLED(
id INTEGER PRIMARY KEY,
timeLED TIMESTAMP,
is_on BOOL
)
"""
zeiger.execute(db_creat)
verbindung.commit()

class LED(LED):
    def __init__(self,pin):
        super().__init__(pin)
        self.is_checked = None
        
    def on(self):
        super().on()
        self.is_checked = False
        #print(self.is_checked)
    
    def off(self):
        super().off()
        self.is_checked = False
        #print(self.is_checked)


# Initialisierung von GPIO27 als Button (Eingang)
button = Button(23)

# Initialisierung von GPIO17 als LED (Ausgang)
led = LED(24)


# Wenn der Button gedrückt wird
button.when_pressed = led.toggle

while True:
    if led.is_checked == False:
        zeit = DateTime.now()
        time = zeit.strftime('%H:%M:%S')
        is_on = led.is_active 
        zeiger.execute("""INSERT INTO TLED (timeLED,is_on) VALUES(?,?)""",[time,is_on])
        verbindung.commit()
        led.is_checked = True
        
verbindung.commit()
verbindung.close()

