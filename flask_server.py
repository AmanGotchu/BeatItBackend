import os
from flask import Flask
import numpy as np
import requests
import base64
import rap
import json
import scipy
import scikits.audiolab


from flask import (
    Blueprint, redirect, request, jsonify, abort
)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    # Detected audio text
    # Tones
    # QPM
    # Wav file (Base 64) #I'll have to decode
    #a, fs, enc = audiolab.wavread('file1.wav')
    # b, fs, enc = audiolab.wavread('file2.wav')
    # c = scipy.vstack((a,b))
    # audiolab.wavwrite(c, 'file3.wav', fs, enc)

    @app.route('/hello', methods=['GET', 'POST'])
    def hello():
        #rap.get_mah_goods()
        encoded_f1 = ""
        with open("generated_output.wav", "rb") as f1,open("b64.txt", "w") as f2:
            encoded_f1 = base64.b64encode(f1.read())
        return encoded_f1
    return app
