echo "Copying source files"

sudo ampy --port /dev/ttyUSB0 put main.py
sudo ampy --port /dev/ttyUSB0 put index.html

exit

# update bootstrap dependencies - this may take few minutes

echo "Copying javascript"
sudo ampy --port /dev/ttyUSB0 put js

echo "Copying CSS"
sudo ampy --port /dev/ttyUSB0 put css

echo "Copying icon"
sudo ampy --port /dev/ttyUSB0 put favicon.ico
