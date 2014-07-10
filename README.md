PiBot

Repository for Raspberry Pi 

PiBot is a Linux executable that takes full control of the Raspberry Pi. Use your Pi as a robot and run rampad in the streets 

Necessary Hardware

PiBot needs four servo motors in order to run properly, a Wiimote for contorl and a bluetooth usb dongle

Installation
- Extract contents to any location
- Run the command (sudo hciconfig hci0 piscan) in terminal to make your Pi discoverable
- Run (hciconfig | grep "BD Address") in terminal to print your bluetooth address
- Navigate to PiBot folder via the terminal and type (./ PiBot) to run PiBot
- Enter your bluetooth address

Special Thank To:
- The CodeAcademy Team
- cl.cam.ac.uk
- The PyBluez Team
