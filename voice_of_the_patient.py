# Step 1 :- Setup audio recoder (ffmpeg and portaudio)
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

# os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            #Record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            #Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            logging.info(f"Audio saved to {file_path}")
    except Exception as e:
        logging.error(f"An error occured: {e}")
       

audio_filepath = "patient_voice_test.mp3"       
print(record_audio(file_path = audio_filepath))

# python Voice_of_the_patient.py
# Step 2 :- Setup Speech to txt-STT-model for transcription
import os
from groq import Groq # type: ignore
groq_api_key = os.environ.get("GROQ_API_KEY")
stt_model = "whisper-large-v3"

def transcribe_with_groq(stt_model, audio_filepath, groq_api_key):
    client = Groq(api_key=groq_api_key)
    
    audio_file = open(audio_filepath, "rb")
    transcription = client.audio.transcriptions.create(
    model = stt_model,
    file = audio_file,
    language = "en"
    )
    return transcription.text
print(transcribe_with_groq(stt_model = stt_model, audio_filepath = audio_filepath, groq_api_key = groq_api_key))
