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


# def predict_base64_voice(name):
#     download_blob('quicktranslates', filename, filename)
#     decode_string = base64.b64decode(content)
#     wav_file.write(decode_string)
#     os.system(f'whisper "{model_dir}/temp.wav" --task translate --model large --output_dir {model_dir}')
#     #FileResponse('temp.srt')
#     return FileResponse(f'temp.srt', media_type='text/plain', filename=f'{model_dir}/temp.srt')

def login(youtube_link: str = Form(...), language: str = Form(...)):
    
    video_file_only_name = str(youtube_link)[-5:]
    video_folder_path = os.path.join(os.getcwd(), video_file_only_name)

    if not os.path.exists(video_folder_path):
        os.makedirs(video_folder_path)
    
    os.chdir(video_folder_path)

    file_name = 'my_audio_file'
    
    ytdl_opts = {
    'outtmpl': file_name,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    }
    ytdl = yt_dlp.YoutubeDL(ytdl_opts)
    
    ytdl.download([youtube_link])
    
    audio_file_path = 'my_audio_file.wav'

    #srtFilename = whisper_api(audio_file_path, language)
    os.system(f'whisper "{model_dir}/temp.wav" --task translate --model large --output_dir {model_dir}')
    os.remove(audio_file_path)
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
