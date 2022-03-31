import pyaudio
import array
import requests

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print("recording...")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    print(len(data))
    frames.append(data)
print("finished recording")

pcm = array.array('h')
pcm.frombytes( b''.join(frames))

print(len(pcm))

stream.stop_stream()
stream.close()
audio.terminate()

obj = {
    'audio': pcm
}

requests.post("localhost:11111", obj)
