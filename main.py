import machine
import network
import socket
import os

ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid="ESP8266", authmode=network.AUTH_WPA_WPA2_PSK, password="xcubae00")
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

pin = machine.Pin(2, machine.Pin.OUT)

with open("index.html") as f:
    html = f.read()
    systemData = os.uname()
    systemInfo = """
    {}
    <ul>
        <li>System: {}</li>
        <li>Release: {}</li>
        <li>MicroPython: {}</li>
    </ul>
    """.format(systemData[4], systemData[0], systemData[2], systemData[3])
    html = html.replace("$SYSTEM_INFO", systemInfo, 1)
    f.close()

def handleAsset(what, client):
    try:
        with open(what) as f:
            while True:
                chunk = f.read(256)
                if chunk:
                    client.write(chunk)
                else:
                    break
            f.close()
    except Exception as e:
        print(e)

def handleGET(what, rest, client):
    while True:
        line = rest.readline()
        if not line or line == b'\r\n':
            break
    what = what[1:].decode("utf-8")
    if what.startswith("TOOGLE_LED"):
        pin.value(not pin.value())
    elif what.startswith("TOOGLE_BLINK"):
        pin.value(not pin.value())
    elif what.endswith("css") or what.endswith("ico"):
        return handleAsset(what, client)
    res = html.replace("$LED_STATUS", "OFF" if pin.value() else "ON", 1)
    res = res.replace("$BLINK_STATUS", "OFF" if pin.value() else "ON", 1)
    client.write(res)

while True:
    cl, addr = s.accept()
    data = cl.makefile('rwb', 0)
    line = data.readline()
    tokens = line.split()
    if len(tokens) < 2:
        continue
    response = None
    if tokens[0] == b'GET':
        handleGET(tokens[1], data, cl)
    cl.close()
