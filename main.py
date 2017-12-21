import network

ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid="ESP8266", authmode=network.AUTH_WPA_WPA2_PSK, password="xcubae00")
    
import machine
pin = machine.Pin(2, machine.Pin.OUT)

index = open('index.html')
html = index.read()
index.close()

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

import os

def generateHTTPok(length):
    response = "HTTP/1.0 200 OK\r\n"
    response += "Content-Length: " + str(length) + "\r\n"
    response += "Content-Type: text/plain\r\n\r\n"
    return response

def handleGET(what, rest, client):
    while True:
        line = rest.readline()
        if not line or line == b'\r\n':
            break

    what = what[1:].decode("utf-8")
    print("Handling GET request on '{}'".format(what))
    
    # handle assets
    if what.startswith("css") or what == "favicon.ico":
        try:
            with open(what) as f:
                response = generateHTTPok(os.stat(what)[6])
                client.write(response)
                while True:
                    chunk = f.read(256)
                    if chunk:
                        client.write(chunk)
                    else:
                        break
                f.close()
        except Exception as e:
            print(e)
        return
    
    # generate index
    row = '<tr><td>{}</td><td>{}</td></tr>'.format(pin, pin.value())
    response = html.replace("$TABLE", row)
    client.write(response)


# main server loop
while True:
    # accept connection
    cl, addr = s.accept()
    print('client connected from', addr)
    # read the request
    data = cl.makefile('rwb', 0)
    # read the request header
    line = data.readline()
    tokens = line.split()
    if len(tokens) < 2:
        continue
    # generate response
    response = None
    print(tokens)
    if tokens[0] == b'GET':
        handleGET(tokens[1], data, cl)
    cl.close()
