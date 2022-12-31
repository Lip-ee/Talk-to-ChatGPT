# import modules
import openai
from gtts import gTTS
import speech_recognition as sr

# api key
openai.api_key = "paste your api key here"

# configuring GPT-3
model_engine = "text-davinci-002"
output_format = "text"

# configuring speech_recognition
r = sr.Recognizer()

# user input using the microphone
with sr.Microphone() as source:
    print("Listening:")
    audio = r.listen(source)

# speech-to-text
text = r.recognize_google(audio)

# calling the GPT-3 COMPLETION function
completion = openai.Completion.create(
    engine = model_engine,
    prompt = text,
    temperature = 0.5,
    max_tokens = 1024,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0,
)

# post completion text on output var
output = completion.choices[0].text

# text-to-speech
tts = gTTS(output)

# saving the audio on a file
tts.save("output.mp3")

# playing the audio using playsound
from playsound import playsound
playsound("output.mp3")