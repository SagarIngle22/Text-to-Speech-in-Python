import pyttsx3  # type: ignore # Import pyttsx3 for text-to-speech

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the speech rate
engine.setProperty('rate', 70)

# Get the available voices
voices = engine.getProperty('voices')

# Function to print the current voice being used
def new_func(voice):
    print("Using voice:", repr(voice))

# Loop through available voices, set each voice, and speak
for voice in voices:
    new_func(voice)
    engine.setProperty('voice', voice.id)
    engine.say("PHN Technology Private Limited")

# Run the text-to-speech engine
engine.runAndWait()
