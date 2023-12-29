import pyaudio
import sys

# Constants
CHUNK = 1024
FORMAT = pyaudio.paInt16 
CHANNELS = 1
RATE = 44100

# Initialize PyAudio
py_Audio = pyaudio.PyAudio()

# Open Stream
stream = py_Audio.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       input=True,
                       output=True,
                       frames_per_buffer=CHUNK)

print("Recording and playing back. Press Ctrl+C to stop.")

try:
    while True:
        data = stream.read(CHUNK)
        stream.write(data, CHUNK)
except KeyboardInterrupt:
    # Handle Ctrl+C
    print("\nStopping . . . ")
    stream.stop_stream
    stream.close()
    py_Audio.terminate()
    sys.exit()
