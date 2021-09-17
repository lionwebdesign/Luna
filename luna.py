# Chatterbot libraries
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import spacy
# text to speech libraries
import speech_recognition as sr
from gtts import gTTS
# Sound libraries
from pydub import AudioSegment 
from pydub.playback import play
# jokes?
import pyjokes
# Others
import datetime
# Weather
from weather_request.weather import CLIMA
# Position
from geolocation.current_position import CURRENT_GEOLOCATION

class LUNA:
    def __init__(self):
        self.speech = [ "hola", "hola!",
                        "¿cómo estás?", "estoy bien ¿y tú?",
                        "¿cómo te llamas?", "mi nombre es luna",
                        "¿a qué te dedicas?", "¡soy una inteligencia artificial en desarrollo!",
                        "¿cómo fuiste creada?", "ruben, mi creador, quiere desarrollar una inteligencia capaz de conversar con su esposa y sus hijos sin tener que molestarse, así que básicamente soy producto de la pereza de un hombre, irónico ¿no?",
                        "¿cuáles son tus aspiraciones?", "me gustaría poder ayudar a la humanidad de alguna forma, ser esa confiable amiga a la que puedes contarle todo, pero que si la traicionas, comparte tus secretos con el mundo"]
        self.bot = ChatBot("Luna")
        self.trainer = ListTrainer(self.bot)
        self.trainer.train(self.speech)
        self.microphone = sr.Recognizer()
        self.clima = CLIMA()
        self.geo = CURRENT_GEOLOCATION()
        
    def UserMicrophoneIn(self):
        with sr.Microphone() as source:
            self.microphone.adjust_for_ambient_noise(source)
            print("...")
            self.microphone.pause_threshold = 1
            self.audio = self.microphone.listen(source)
        try:
            self.sentence = self.microphone.recognize_google(self.audio, language='es-MX')
            print(f"User: {self.sentence}")
        except Exception as e:
            print("Lo siento, no entendi")
            return "None"
        return self.sentence

    def LunaVoice(self, lunaAnswerText):
        tts = gTTS(lunaAnswerText, lang='es', tld='com.mx')
        tts.save('./assets/voice_files/voicesLuna.mp3')
        self.voicesLuna = AudioSegment.from_mp3('./assets/voice_files/voicesLuna.mp3')
        print(f"Luna: {lunaAnswerText}")
        play(self.voicesLuna)

    def Joke(self):
        joke = pyjokes.get_joke(language="es", category="all")
        self.LunaVoice(joke)

    def Time(self):
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        self.LunaVoice(strTime)
        
    def Clima(self):
        self.current_lat = self.geo.get_location()[0]
        self.current_lng = self.geo.get_location()[1]
        self.clima_de_hoy = self.clima.get_clima(self.current_lat, self.current_lng)
        self.LunaVoice(self.clima_de_hoy)

    def Interaction(self):
        while True:
            self.sentence = input("User: ")#self.UserMicrophoneIn().low()
            if('cuentame algo gracioso' in self.sentence or 'dime una broma' in self.sentence or 'cuentame un chiste' in self.sentence):
                self.Joke()
            elif('me puedes dar la hora' in self.sentence or 'qué hora es' in self.sentence):
                self.Time()
            elif ('como esta el clima' in self.sentence or 'como esta el tiempo' in self.sentence):
                self.Clima()
            elif('hastá luego luna' in self.sentence or 'adios luna' in self.sentence or 'nos vemos luna' in self.sentence or 'buenas noches luna' in self.sentence):
                self.LunaVoice("De acuerdo, nos vemos más tarde")
                break     
            else:
                self.userIn = self.sentence
                self.userInStr = str(self.userIn)
                self.lunaAnswer = self.bot.get_response(self.userInStr)
                self.lunaAnswerStr = str(self.lunaAnswer)
                self.LunaVoice(self.lunaAnswerStr)
                
if (__name__ == "__main__"):
    luna = LUNA()
    luna.Interaction()