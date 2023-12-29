import sounddevice as sd
import numpy as np

# Constants
CHUNK = 2048
RATE = 22050
CHANNELS = 1

# Callback function to stream audio
def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata

# Open a stream
with sd.Stream(
    samplerate=RATE,
    blocksize=CHUNK,
    channels=CHANNELS,
    dtype=np.int16,
    callback=callback
) as stream:
    print("Recording and playing back. Press Ctrl+C to stop.")
    try:
        # Keep the stream active
        while True:
            sd.sleep(1000)  # Sleep for 1000 milliseconds (1 second) at a time
    except KeyboardInterrupt:
        print("\nStopping...")

    # The stream is automatically closed when exiting the 'with' block
