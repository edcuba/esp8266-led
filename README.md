# ESP8266 LED controller

## Author

Eduard Čuba

## Course

Microprocessors and Embedded Systems, Brno University of Technology, Faculty of Information Technology 2017.

## Description

The application provides a simple browser interface for controlling LEDs attached to the ESP8266 board.
Server is runnning directly on the ESP8266 board.
User can connect to the device using WiFi access point.
- SSID: ESP8266
- WPA2 password: xcubae00
- Server address: _192.168.4.1_
- Port: default (_80_)

## Commands

The interface contains a control button for each of the three LEDs, a blink sequence button, a rotation sequence button, and basic system information.

- https://photos.app.goo.gl/stGbcUhomzzYHTZ83
- https://photos.app.goo.gl/FtehtEO1xjZRt9a42

## Scheme

The controller uses two built-in LEDs (GPIO2 and GPIO16) and one external connected to GPIO4.
You may need to use a 220 Ohm resistor to connect the LED to GPIO4. See following pictures:
- https://photos.app.goo.gl/AGtaYONGmuB03Nj02
- https://photos.app.goo.gl/xhrKweaEnehSuP472

NodeMCU Development kit provides access to these GPIOs of ESP8266. The only thing to take care is that NodeMCU Dev kit pins are numbered differently than internal GPIO notations of ESP8266 as shown in below figure and table. For example, the D0 pin on the NodeMCU Dev kit is mapped to the internal GPIO pin 16 of ESP8266. See this scheme: http://www.electronicwings.com/nodemcu/nodemcu-gpio-with-arduino-ide


## Implementation

Project is implemented in MicroPython as simple iterative HTTP server using following predefined HTTP GET methods.

- **GET /TOOGLE_LED2** - toogles LED connected to GPIO2
- **GET /TOOGLE_LED4** - toogles LED connected to GPIO4
- **GET /TOOGLE_LED16** - toogles LED connected to GPIO16
- **GET /BLINK** - toogles blink sequence
- **GET /ROTATE** - toogles rotate sequence

Otherwise, **GET /$FILE** will return the required file (e.g. index.html) as usual.
Commands can be issued using web interface or directly (i.e. using _telnet_).

Web dashboard is using https://purecss.io framework.

HTML template is based on (changes 80% - reduced and simplified)
- https://purecss.io/layouts/pricing/

Stylesheet is based on (changes 5% - wrapped them together and changed the color scheme)
- https://purecss.io/layouts/pricing/
- https://unpkg.com/purecss@1.0.0/build/pure-min.css
- https://unpkg.com/purecss@1.0.0/build/grids-responsive-min.css

## Deployment

First you need to get MicroPython running on your board.
See this guide: http://docs.micropython.org/en/v1.9.3/esp8266/esp8266/tutorial/intro.html

Then you need to copy in source files. You may use script _deploy.sh_ (requires _ampy_ to be installed).

## Summary

The application provides a simple interface for LED control.
Solution can be possibly used for building a "smart" home.

### Problems
- handling multiple devices at the time (iterative server due to limited RAM)
- dangers of using GET method for LED control (page reload executes command)
