"""
    Defines methods for interacting with sound device
"""
import pyaudio
import math
import numpy as np
from datetime import datetime

# Settings to pass to pyaudio to establish connection
pa_settings = {
    "format": pyaudio.paInt16,
    "channels": 2,
    "rate": 44100,
    "input_device_index": 0,
    "input": True,
}

audio = pyaudio.PyAudio()
chunk = 1024  # common issues: if input overflow: increase the size of chunk
framerec = []
timerec = []
amprec = []
max_frame = 100
stream = False


def openstream():
    """
        Opens audio stream
    """
    global stream
    stream = audio.open(**pa_settings)
    print("Audio stream started")


def readstream():
    """
        Pushes data stream to other objects and trims if nessasary
    """
    framerec.append(np.frombuffer(stream.read(chunk), dtype=np.int16))
    timerec.append(datetime.now())
    amprec.append(20 * math.log10(np.amax(framerec[-1])))
    if len(framerec) > max_frame:  # remove items if above max buffer
        del timerec[0]
        del framerec[0]
        del amprec[0]


def endstream():
    """
        Closes stream objects, and turns off microphone input
    """
    stream.stop_stream()
    stream.close()
    audio.terminate()
    print("audio capture terminated")
