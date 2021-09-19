import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment 
from pydub.playback import play

class LUNA_VOICE():
    def LunaVoice(self, lunaAnswerText):
        tts = gTTS(lunaAnswerText, lang='es', tld='com.mx')
        tts.save('assets/voice_files/voicesLuna.mp3')
        self.voicesLuna = AudioSegment.from_mp3('assets/voice_files/voicesLuna.mp3')
        print(f"Luna: {lunaAnswerText}")
        play(self.voicesLuna)

class SPEECH_RECOGNITION(): 
    def __init__(self):
        self.microphone = sr.Recognizer()
    
    def User_voice_in(self):
        with sr.Microphone() as source:
            self.microphone.adjust_for_ambient_noise(source)
            print("...")
            self.microphone.pause_threshold = 1
            self.audio = self.microphone.listen(source)
        try:
            sentence = self.microphone.recognize_google(self.audio, language='es-MX').lower()
            print(f"User: {sentence}")
        except Exception as e:
            print("Lo siento, no entendi")
            return "None"
        return sentence