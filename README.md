# HACKFORGE
# AI Doctor

This repository contains the code for an AI Doctor system that leverages advanced machine learning techniques to analyze medical images, process voice data, and provide medical advice. The system integrates various AI models and APIs to simulate a virtual healthcare experience.

## Overview

The core logic behind the AI Doctor's medical analysis resides in the `brain_of_the_doctor.py` file. This file is responsible for:

- **Analyzing Medical Images**: The AI model processes uploaded images (such as medical scans or photos) and provides a diagnosis based on visual clues.
- **Processing Voice Data**: The file also helps in analyzing voice inputs (e.g., patient symptoms or queries) by converting them to text and combining that data with visual input for a more accurate diagnosis.
- **Providing Medical Responses**: Once the analysis is done, `brain_of_the_doctor.py` generates concise, human-like medical responses to assist users. It mimics the behavior of a professional doctor based on the system's understanding.

## How It Works

1. **Image Analysis**: The system receives an image upload (e.g., medical scans) and processes it through a pre-trained model to detect any anomalies. The result is an actionable diagnosis or recommendation.
2. **Voice-to-Text**: Using speech recognition, the system transcribes any patient-provided voice notes into text. This text is combined with the image analysis to make a more informed decision.
3. **Medical Response**: Based on the information provided (both visual and verbal), the AI Doctor generates a medical response. This response is then converted back into speech (voice output) for the user to listen to.

### Features

- **AI-Powered Diagnosis**: Advanced machine learning models (like Llama-3.2-11b-vision-preview) are used to analyze medical images and provide diagnoses.
- **Voice Interaction**: Users can interact with the AI Doctor through voice, which is transcribed and processed to provide more personalized feedback.
- **Voice Feedback**: The system generates voice output based on the AI's response, ensuring a complete hands-free interaction.
