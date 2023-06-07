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
import aiofiles


data_dir = os.environ.get("TRAINML_DATA_PATH")
output_dir = os.environ.get("TRAINML_OUTPUT_PATH")
model_dir = os.environ.get("TRAINML_MODEL_PATH")


def predict_base64_voice(name, content):
    wav_file = open(f"{model_dir}/temp.wav", "wb")
    decode_string = base64.b64decode(content)
    wav_file.write(decode_string)
    os.system(f'whisper "{model_dir}/temp.wav" --task translate --model large --output_dir {model_dir}')
    #FileResponse('temp.srt')
    return FileResponse(f'temp.srt', media_type='text/plain', filename=f'{model_dir}/temp.srt')


            
if __name__ == "__main__":
    for filename in glob.glob(f"{data_dir}/*.wav"):
        predict_base64_voice(filename)
        #input_file = os.path.basename(filename)
        #FileResponse('subtitle.srt', media_type='application/octet-stream', filename='temp.srt')
        #output_file_name = re.sub(".JPEG", "_pred.json", input_file)

#         print(f"{output_file_name}: {classes}")

#         with open(f"{output_dir}/{output_file_name}", "w") as f:
#             json.dump(dict(file=input_file, classes=classes), f)
   
