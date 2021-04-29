#Harden, Scott.(July 19,2016) Realtime Audio Visualization in Python [python file] https://swharden.com/blog/2016-07-19-realtime-audio-visualization-in-python/
#Librosa. (n.d.) Beat Tracking Example [webpage] https://librosa.org/doc/latest/tutorial.html
#Ordnung, David.(n.d.) Fading [python file] http://dordnung.de/raspberrypi-ledstrip/
#Sloria.(June 2, 2013)recorder [python file] https://gist.github.com/sloria/5693955


# Beat tracking example

import librosa
import pyaudio
import wave
import os
import sys
import termios
import tty
import pigpio
import time
import threading


# The Pins. Use Broadcom numbers.
RED_PIN   = 17
GREEN_PIN = 22
BLUE_PIN  = 24

bright = 255
r = 255.0
g = 0.0
b = 0.0

brightChanged = False
abort = False
state = True

pi = pigpio.pi()

def updateColor(color, step):
    color += step

    if color > 255:
        return 255
    if color < 0:
        return 0
    return color

def setLights(pin, brightness):
    realBrightness = int(int(brightness) * (float(bright) / 255.0))
    pi.set_PWM_dutycycle(pin, realBrightness)

def getCh():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def checkKey():
    global bright
    global brightChanged
    global state
    global abort
    
def runLights():
    global bright
    global brightChanged
    global state
    global abort    
    global STEPS
    global r
    global g
    global b
    setLights(RED_PIN, r)
    setLights(GREEN_PIN, g)
    setLights(BLUE_PIN, b)

    while abort == False:
        if state and not brightChanged:
            if r == 255 and b == 0 and g < 255:
                g = updateColor(g, STEPS)
                setLights(GREEN_PIN, g)
            
            elif g == 255 and b == 0 and r > 0:
                r = updateColor(r, -STEPS)
                setLights(RED_PIN, r)

            elif r == 0 and g == 255 and b < 255:
                b = updateColor(b, STEPS)
                setLights(BLUE_PIN, b)

            elif r == 0 and b == 255 and g > 0:
                g = updateColor(g, -STEPS)
                setLights(GREEN_PIN, g)

            elif g == 0 and b == 255 and r < 255:
                r = updateColor(r, STEPS)
                setLights(RED_PIN, r)

            elif r == 255 and g == 0 and b > 0:
                b = updateColor(b, -STEPS)
                setLights(BLUE_PIN, b)
                
chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 5
filename = "output.wav"
p = pyaudio.PyAudio()  # Create an interface to PortAudio

STEPS = 0.05
x = threading.Thread(target=runLights,args=())
x.start()

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

while (1==1):
    print('Recording')


    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds

    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print(f"frames size: {len(frames)}")

    print('Finished recording')

    # Save the recorded data as a WAV file

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    # 1. Get the file path to an included audio example
    # filename = 'outputSD.wav'
    # 2. Load the audio as a waveform `y`
    #    Store the sampling rate as `sr`

    y, sr = librosa.load(filename)

    # 3. Run the default beat tracker

    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    # Number of color changes per step (more is faster, less is slower).
    # You also can use 0.X floats.
    STEPS     = tempo/1000

    print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
    
# Stop and close the stream

stream.stop_stream()
stream.close()

# Terminate the PortAudio interface    
p.terminate()

time.sleep(5)

print ("Aborting...")

setLights(RED_PIN, 0)
setLights(GREEN_PIN, 0)
setLights(BLUE_PIN, 0)

time.sleep(5)

pi.stop()
