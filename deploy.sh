echo "Copying source files"

sudo ampy --port /dev/ttyUSB0 put main.py
sudo ampy --port /dev/ttyUSB0 put index.html

echo "Copying CSS"

sudo ampy --port /dev/ttyUSB0 put styles.css

echo "Copying icon"
sudo ampy --port /dev/ttyUSB0 put favicon.ico
