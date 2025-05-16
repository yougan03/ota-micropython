# import ugit
# from machine import Pin
# import time

# pin = Pin(0,Pin.IN,Pin.PULL_UP)
# if pin.value() is 0:
#     ugit.pull_all()
    
# #main code here
# TIME_MS=100
# LED = Pin("LED", Pin.OUT)
# while True:
#     LED.off()
#     time.sleep_ms(TIME_MS)
#     LED.on()
#     time.sleep_ms(TIME_MS)

# uart tx and rx
from machine import UART, Pin
import time

uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))

uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

txdat= 'hello\n\r'

uart1.write(txdat)
time.sleep(1)
rxdat=bytes()

while uart0.any() > 0:
    rxdat += uart0.read(1)
    
    print(rxdat.decode('utf-8'))

