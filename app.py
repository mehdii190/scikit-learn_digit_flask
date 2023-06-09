# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 14:46:43 2023

@author: persian computer
"""

import io
import base64

from flask import Flask, render_template, request, jsonify

from model import ImageDeskewApplier # XXX unpickling
from recognition import recognize


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload/', methods=['POST'])
def file_upload():
    # convert request body to valid base64 string
    encoded_image = request\
        .data\
        .decode()\
        .replace('data:image/png;base64,', '')\
        .replace(' ', '+')

    # decode image content
    content = base64.b64decode(encoded_image)

    # create file buffer
    tmp_file = io.BytesIO(content)

    # send image to recognition
    recognition_results = recognize(tmp_file)

    # return JSON response
    return jsonify(recognition_results)

if __name__ == '__main__':
    app.config.from_pyfile('config.py')
    app.run()