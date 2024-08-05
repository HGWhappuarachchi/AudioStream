import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 50007))
s.listen(1)

conn, addr = s.accept()
print("Connected by", addr)

try:
    while True:
        data = conn.recv(CHUNK)
        stream.write(data)
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
p.terminate()
conn.close()
