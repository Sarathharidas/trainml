###
# Source: https://learnopencv.com/keras-tutorial-using-pre-trained-imagenet-models/
###

import os
import glob
import re
import json
import base64
import tempfile
import numpy as np
from fastapi.responses import FileResponse


data_dir = os.environ.get("TRAINML_DATA_PATH")
output_dir = os.environ.get("TRAINML_OUTPUT_PATH")

@app.post("/predict")
def predict_base64_voice(name, contents):
    wav_file = open("temp.wav", "wb")
    decode_string = base64.b64decode(contents)
    wav_file.write(decode_string)
    
    os.system('whisper "temp.wav" --task translate --model large')
    ## return Send back the srt file
    size_file = os.path.getsize("temp.wav")
    return {'size':size_file)
    #return FileResponse('subtitle.srt', media_type='application/octet-stream', filename='temp.srt')
        
   
