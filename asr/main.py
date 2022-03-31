import automatic_speech_recognition as asr
from flask import Flask, request

app = Flask(__name__)
pipeline = asr.load('deepspeech2', lang='en')

@app.route('/')
def app_interface():

    obj = request.json()
    sample = obj['audio']
    sentences = pipeline.predict([sample])
    print(sentences)
    return []


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
