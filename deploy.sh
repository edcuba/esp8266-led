# Author: Eduard Cuba
# Email: xcubae00@stud.fit.vutbr.cz
# original
# Last modified: 26.12.2017
# Desc: deploy project to ESP8266 board

echo "Copying source files"

sudo ampy --port /dev/ttyUSB0 put main.py
sudo ampy --port /dev/ttyUSB0 put index.html

echo "Copying CSS"

sudo ampy --port /dev/ttyUSB0 put styles.css

echo "Copying icon"
sudo ampy --port /dev/ttyUSB0 put favicon.ico
