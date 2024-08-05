import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.246', 50007))  # Replace with the IP address of the Raspberry Pi

try:
    while True:
        data = stream.read(CHUNK)
        s.sendall(data)
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
p.terminate()
s.close()
