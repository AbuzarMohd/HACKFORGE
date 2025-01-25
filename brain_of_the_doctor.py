# Step 1 :- Setup GROQ api key
import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Step 2 :- Convert the image to the required format
import base64

image_path = "acne.jpg"

def encode_image(image_path):
    image_file = open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')
    
# Step 3 :- Setup Multimodel LLM
from groq import Groq 
query = "I'm facing this rednees issue on my face. Is there something wrong with my face?"
model = "llama-3.2-90b-vision-preview"

def alyze_image_with_query(query, model, encode_image):
    client = Groq(api_key = GROQ_API_KEY)
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encode_image}",
                    },
                },
            ],
        }]
    chat_completion = client.chat.completions.create(
        messages = messages,
        model = model
    )
    return chat_completion.choices[0].message.content

#python Brain_of_the_doctor.py
print(alyze_image_with_query(query = query, model = model, encode_image = encode_image(image_path)))