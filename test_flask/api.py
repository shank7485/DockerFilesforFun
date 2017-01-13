import socket
import fcntl
import struct
from flask import Flask


app = Flask(__name__)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
    return str(ip)

IP_ADDRESS = get_ip_address('eth0')


@app.route('/')
def hello_world():
    data = 'API endpoint hitting IP: ' + IP_ADDRESS
    return 'API is working.' + data + "  "


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
    return str(ip)
