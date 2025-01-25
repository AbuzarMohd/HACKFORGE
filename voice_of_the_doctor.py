# Step1a :- Setup Text to Speech_TTS_model gTTS
from pydub import AudioSegment
from playsound import playsound
# Function to convert MP3 to WAV
def convert_mp3_to_wav(mp3_filepath, wav_filepath):
    audio = AudioSegment.from_mp3(mp3_filepath)
    audio.export(wav_filepath, format="wav")
    
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, outpt_filepath):
    language = "en"
    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )
    audioobj.save(outpt_filepath)
    
input_text = "Hi this is AI doctor! Do you need any help? Please descripe your problem"
#text_to_speech_with_gtts_old(input_text = input_text, outpt_filepath = "gtts_testing.mp3")

# Step1b :- Setup Text to Speech_TTS_model ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

def text_to_speec_with_elevenlabs_old(input_text, output_filepath):
    client = ElevenLabs(api_key = ELEVENLABS_API_KEY)
    audio = client.generate(
        text = input_text,
        voice = "Aria",
        output_format = "mp3_22050_32", 
        model = "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    
#text_to_speec_with_elevenlabs_old(input_text, output_filepath = "elevenlabs_testing.mp3")   

# Step 2 :- Use model for Text output to voice 
import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        playsound(output_filepath)  # Directly play the MP3 file
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

    
input_text = "Hi this is AI doctor new! Do you need any help? Please descripe your problem and the autoplay audio"
#text_to_speech_with_gtts(input_text = input_text, output_filepath = "gtts_testing_autoplay.mp3")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key = ELEVENLABS_API_KEY)
    audio = client.generate(
        text = input_text,
        voice = "Aria",
        output_format = "mp3_22050_32",
        model = "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    
    try:
        playsound(output_filepath)  # Directly play the MP3 file
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
text_to_speech_with_elevenlabs(input_text = input_text, output_filepath ="elevenlabs_testing_autoplay.mp3")
 
#python voice_of_the_doctor.py
