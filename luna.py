# Chatterbot libraries
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import spacy
import pyjokes
import datetime
from weather_request.weather import CLIMA
from geolocation.position import CURRENT_GEOLOCATION
from linguistic_functions.linguistic_functions import LUNA_VOICE, SPEECH_RECOGNITION

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
        self.clima = CLIMA()
        self.geo = CURRENT_GEOLOCATION()
        self.voice = LUNA_VOICE()
        self.listening = SPEECH_RECOGNITION()

    def Joke(self):
        joke = pyjokes.get_joke(language="es", category="all")
        self.voice.LunaVoice(joke)

    def Time(self):
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        self.voice.LunaVoice(strTime)
        
    def Clima(self):
        current_lat = self.geo.get_location()[0]
        current_lng = self.geo.get_location()[1]
        clima_de_hoy = self.clima.get_clima(self.current_lat, self.current_lng)
        self.voice.LunaVoice(clima_de_hoy)

    def Interaction(self):
        while True:
            #sentence = input("User: ") 
            pure_sentence = self.listening.User_voice_in() 
            sentence = pure_sentence
            if('cuentame algo gracioso' in sentence or 'dime una broma' in sentence or 'cuentame un chiste' in sentence):
                self.Joke()
            elif('me puedes dar la hora' in sentence or 'qué hora es' in sentence):
                self.Time()
            elif ('como esta el clima' in sentence or 'como esta el tiempo' in sentence):
                self.Clima()
            elif('hastá luego luna' in sentence or 'adios luna' in sentence or 'nos vemos luna' in sentence or 'buenas noches luna' in sentence):
                self.voice.LunaVoice("De acuerdo, nos vemos más tarde")
                break     
            else:
                userIn = sentence
                userInStr = str(userIn)
                lunaAnswer = self.bot.get_response(userInStr)
                lunaAnswerStr = str(lunaAnswer)
                self.voice.LunaVoice(lunaAnswerStr)
                
if (__name__ == "__main__"):
    luna = LUNA()
    luna.Interaction()