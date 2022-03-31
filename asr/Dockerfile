FROM tf-devel-cpu-arm64v8-jupyter
MAINTAINER Federico Rossetto

RUN pip3 install --upgrade pip

COPY asr/ /source
RUN pip3 install -r /source/requirements.txt

RUN pip3 install tensorflow-aarch64 -f https://tf.kmtea.eu/whl/stable.html
RUN pip3 install tensorflow -f https://tf.kmtea.eu/whl/stable.html

RUN pip3 install automatic_speech_recognition

WORKDIR /source

CMD python3 main.py