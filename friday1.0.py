from distutils.log import error
from msilib.schema import Error
from pickle import TRUE
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import cv2
from time import sleep

#voice in and output
import speech_recognition as sr
import pyttsx3
listener = sr.Recognizer()
engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

import win32com.client
import datetime as dt 
from os import path

from win32com.client import Dispatch

import win32com.client as win32

import tkinter as tk
from tkinter import simpledialog
import numpy as np
import tflearn
import tensorflow
import random

import webbrowser as wb
import subprocess as sp
import winsound
from datetime import datetime
  


import os
root_dir = os.path.realpath(os.path.join(os.path.dirname(__file__),))
ac = (os.path.join(root_dir,'AC-DC - Highway to Hell.wav'))
jon = (os.path.join(root_dir,'intens.json'))
bad = (os.path.join(root_dir,'girl in red bad idea.wav'))
steam_dir = os.path.realpath(os.path.join(os.path.dirname(__file__),'..','..','..','..','..'))
steam = (os.path.join(steam_dir,'C:\Program Files (x86)\Steam\steam.exe'))
opencv_cascade = (os.path.join(root_dir,'cascade'))
opencv_faces = (os.path.join(opencv_cascade,'haarcascade_frontalface_default.xml'))
visual_dir = (os.path.join(root_dir,'visual'))
visual = (os.path.join(visual_dir,'My project.exe'))


musik_dir = os.path.realpath(os.path.join(os.path.dirname(__file__),'musik'))

depri_dir = (os.path.join(musik_dir,'depri'))

addict = (os.path.join(depri_dir,'ADDICT Music Video HAZBIN HOTEL.wav'))
how_does_it_feel = (os.path.join(depri_dir,'Citizen - How Does It Feel (Official Music Video).wav'))
the_night_i_drove_alone = (os.path.join(depri_dir,'Citizen - The Night I Drove Alone.wav'))
the_summer = (os.path.join(depri_dir,'Citizen - The Summer (Official Music Video).wav'))
girls = (os.path.join(depri_dir,'girl in red girls.wav'))
we_fell_in_love_in_october = (os.path.join(depri_dir,'girl in red we fell in love in october.wav'))
fuck_it = (os.path.join(depri_dir,'Days N Daze ~ Fuck it!.wav'))
alive = (os.path.join(depri_dir,'jaiden stylez - alive (lyric video).wav'))
luftballongs = (os.path.join(depri_dir,'NENA 99 Luftballons [1983] [Offizielles HD Musikvideo].wav'))
make_a_move = (os.path.join(depri_dir,'Icon For Hire - Make A Move.wav'))
serotonin = (os.path.join(depri_dir,'girl in red - Serotonin (official video).wav'))
girls_in_bikinis = (os.path.join(depri_dir,'Girls In Bikinis.wav'))
irgendwann = (os.path.join(depri_dir,'NENA Irgendwie · Irgendwo · Irgendwann [1984] [Offizielles HD Musikvideo].wav'))
soilders_eyes = (os.path.join(depri_dir,'Jack Savoretti - Soldiers Eyes (Sons of Anarchy).wav'))
skin_boots = (os.path.join(depri_dir,'Alligator Skin Boots.wav'))
Salish = (os.path.join(depri_dir,'Salish.wav'))
haning_tree = (os.path.join(depri_dir,'The Hanging Tree.wav'))
novermber_was_white = (os.path.join(depri_dir,'Say Hi - November Was White, December Was Grey .wav'))

galaxy_dir = (os.path.join(musik_dir,'galaxy'))

mr_blue_sky = (os.path.join(galaxy_dir,'01 Mr. Blue Sky.wav'))
fox_on_the_run = (os.path.join(galaxy_dir,'02 Fox On The Run.wav'))
lake_shore_drive = (os.path.join(galaxy_dir,'03 Lake Shore Drive.wav'))
the_chain = (os.path.join(galaxy_dir,'04 The Chain.wav'))
bring__it_home_to_me = (os.path.join(galaxy_dir,'05 Bring It On Home To Me.wav'))
southern_nights = (os.path.join(galaxy_dir,'06 Southern Nights.wav'))
my_sweet_lord = (os.path.join(galaxy_dir,'07 My Sweet Lord.wav'))
brandy = (os.path.join(galaxy_dir,'08 Brandy (Youre A Fine Girl).wav'))
come_a_little_bit_closer = (os.path.join(galaxy_dir,'09 Come A Little Bit Closer.wav'))
wham_bam_shang_a_lang = (os.path.join(galaxy_dir,'10 Wham Bam Shang-A-Lang.wav'))
surrender = (os.path.join(galaxy_dir,'11 Surrender.wav'))
father_and_son = (os.path.join(galaxy_dir,'12 Father And Son.wav'))
flash_light = (os.path.join(galaxy_dir,'13 Flash Light.wav'))
guardians_inferno = (os.path.join(galaxy_dir,'14 Guardians Inferno.wav'))

cpp = (os.path.join(root_dir,'c++_programming'))
hello_world = (os.path.join(cpp,'test.cpp'))




laut_dir = (os.path.join(musik_dir,'laut'))

back_in_black = (os.path.join(laut_dir,'back in black.wav'))
sk8er_boi = (os.path.join(laut_dir,'Avril Lavigne Sk8er Boi Official Music Video.wav'))
covet = (os.path.join(laut_dir,'Basement - Covet (Official Audio).wav'))
spoiled = (os.path.join(laut_dir,'Basement - Spoiled (Official Audio).wav'))
whole = (os.path.join(laut_dir,'Basement - Whole (Official Audio).wav'))
capri_pants =(os.path.join(laut_dir,'Bikini Kill - Capri Pants.wav'))
antipleasure = (os.path.join(laut_dir,'bikini kill antipleasure dissertation (lyrics) Letra en Español.wav'))
rebels = (os.path.join(laut_dir,'Call Me Karizma Rebels.wav'))
carnival = (os.path.join(laut_dir,'Carnival.wav'))
demirep = (os.path.join(laut_dir,'Demirep.wav'))
i_wish_i_was_a_riot_grrrrl = (os.path.join(laut_dir,'Destructo Disk - I wish I was a Riot Grrrl.wav'))
junge = (os.path.join(laut_dir,'Die Ärzte Junge.wav'))
lasse_reden = (os.path.join(laut_dir,'Die Ärzte Lasse Redn.wav'))
männer_und_frauen = (os.path.join(laut_dir,'die ärzte MF Performance.wav'))
wannsee = (os.path.join(laut_dir,'Die Toten Hosen Wannsee Offizielles Musikvideo.wav'))
distinct = (os.path.join(laut_dir,'Distinct Complicity.wav'))
dividing_by_zero = (os.path.join(laut_dir,'Dividing By ZeroSlim Pickens Does The Right Thing And Rides The Bomb To Hell Official Video.wav'))
doom = (os.path.join(laut_dir,'Doom Eternal OST The Only Thing they Fear is You Mick Gordon.wav'))
double_dare_ya = (os.path.join(laut_dir,'Double Dare Ya.wav'))
centuries = (os.path.join(laut_dir,'Fall Out Boy Centuries Official Music Video.wav'))
feels_blinde = (os.path.join(laut_dir,'Feels Blind.wav'))
drinking_with_the_living_dead = (os.path.join(laut_dir,'Ghoultown Drink With The Living Dead OFFICIAL VIDEO.wav'))
i_hope_you_die_in_a_fire = (os.path.join(laut_dir,'Grand Commander I Hope You Die in a Fire.wav'))
oh_no = (os.path.join(laut_dir,'grandson oh no Official Audio.wav'))
american_idiot = (os.path.join(laut_dir,'Green Day American Idiot Official Music Video.wav'))
i_cant_handle_change = (os.path.join(laut_dir,'I Cant Handle Change.wav'))
i_threw_glass_at_my_finds_eye_and_now_im_on_porbation = (os.path.join(laut_dir,'I Threw Glass at My Friends Eyes and Now Im on Probation.wav'))
doom_2 = (os.path.join(laut_dir,'II Demigod Doom OST.wav'))
prinzesschen = (os.path.join(laut_dir,'LaFee Prinzesschen.wav'))
magnet = (os.path.join(laut_dir,'Magnet.wav'))
beggin = (os.path.join(laut_dir,'Måneskin Beggin Lyrics.wav'))
i_wanna_be_your_slaver = (os.path.join(laut_dir,'Måneskin I WANNA BE YOUR SLAVE LyricsTesto Eurovision 2021.wav'))
atomic_blonde = (os.path.join(laut_dir,'Marilyn Manson Tyler Bates Stigmata Atomic Blonde Soundtrack.wav'))
doom_3 = (os.path.join(laut_dir,'Mick Gordon 02 Rip Tear.wav'))
doom_4 = (os.path.join(laut_dir,'Mick Gordon 04 Rust Dust Guts.wav'))
new_radio = (os.path.join(laut_dir,'New Radio.wav'))
angel_with_a_shotgun = (os.path.join(laut_dir,'Nightcore Angel With A Shotgun.wav'))
labyrint = (os.path.join(laut_dir,'Oomph Labyrinth German Version with German Lyrics.wav'))
i_write_sins_not_tragaties = (os.path.join(laut_dir,'Panic At The Disco I Write Sins Not Tragedies OFFICIAL VIDEO.wav'))
rebel_girl = (os.path.join(laut_dir,'Rebel Girl.wav'))
reject_all_american = (os.path.join(laut_dir,'Reject All American.wav'))
partners_in_crime = (os.path.join(laut_dir,'Set It Off Partners In Crime Official Video.wav'))
teenagers = (os.path.join(laut_dir,'Teenagers.wav'))
seven_nation_army = (os.path.join(laut_dir,'The White Stripes Seven Nation Army Official Music Video.wav'))
anarchist = (os.path.join(laut_dir,'YUNGBLUD - Anarchist (Official Audio).wav'))
original_me = (os.path.join(laut_dir,'YUNGBLUD - original me ft. dan reynolds of imagine dragons (Official Music Video).wav'))
perents = (os.path.join(laut_dir,'YUNGBLUD - Parents (Official Music Video).wav'))
psychotic_kids = (os.path.join(laut_dir,'YUNGBLUD - Psychotic Kids.wav'))
gladiator = (os.path.join(laut_dir,'ZAYDE WOLF GLADIATOR Official Audio.wav'))
fortunet_son = ((os.path.join(laut_dir,'Creedence Clearwater Revival - vietnam war song.wav')))

six_the_musical = (os.path.join(musik_dir,'six the musical'))

ex_wives =  (os.path.join(six_the_musical,'SIX the Musical - Ex Wives (from the Studio Cast Recording).wav'))
dont_lose_your_head = (os.path.join(six_the_musical,'SIX the Musical - Don&#x27;t Lose Ur Head (from the Studio Cast Recording).wav'))
get_down = (os.path.join(six_the_musical,'SIX the Musical - Get Down (from the Studio Cast Recording).wav'))
haus_of_holbein = (os.path.join(six_the_musical,'SIX the Musical - Haus of Holbein (from the Studio Cast Recording).wav'))
all_you_wanna_do = (os.path.join(six_the_musical,'SIX the Musical (featuring Aimie Atkinson) - All You Wanna Do (from the Studio Cast Recording).wav'))


import json
with open(jon) as file:
    data = json.load(file)


words = []
labels = []
docs_x = []
docs_y = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])
        
    if intent['tag'] not in labels:
        labels.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)


training = np.array(training)
output = np.array(output)


net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save("model.tflearn")
#begin coding 
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return np.array(bag)

def speak(audio):
    speaking = Dispatch('Sapi.Spvoice')
    speaking.speak(audio)


def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = sp.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


#begin functions for talking with the bot
def listening():
    def face():
        cap = cv2.VideoCapture(0)
        cap.set(3,640)
        cap.set(4,480)
        cap.set(10,100)

        while True:
            success, img = cap.read()
            
            print(img)

            facecascade = cv2.CascadeClassifier(opencv_faces)

            gry = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


            faces = facecascade.detectMultiScale(gry,1.1,4)

            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


            print(faces)
            break
        face.has_been_called = True
        pass

    

    face()

#Actual Code:

    if face.has_been_called:

        def chat():
            while True:
                    
                    
                    
                 with sr.Microphone() as source:
                    listener.adjust_for_ambient_noise(source)
                    speak('ich höre zu')
                    print('listening...')
                    voice = listener.listen(source)
                    vc = listener.recognize_google(voice, language= "de-DE").lower()
                        
                        
                        #voice comands
                    if  ('such') in vc:
                        vc = vc.replace('such','')
                        try:
                            if ('youtube') in vc:
                                url = ('https://www.youtube.com/results?search_query=')
                                try:
                                    vs = vc.replace('youtube','')
                                    search = vs
                                    wb.open_new(url+search)        
                                except error:
                                    print('not able to search debug pls')
                                    #google searche
        
        
                            if ('google') in vc:
                                try:
                                    url =('https://www.google.com/search?q=')
                                    vs = vc.replace('google','')
                                    search = vs
                                    wb.open_new(url+search)
                                except error:
                                    print('not able to search debug pls')
        #rafisa start seite
        
        
                            if ('rafisa start') in vc:
                                try:
                                    speak('du wirst weitergeleitet')
                                    wb.open_new('https://wiki.rafisa.net/doku.php')
                                except error:
                                    print('error')
        #maki tages jurnal
        
                            if ('doku') in vc:
                                try:
                                    speak('du wirst weitergeleitet')                                        
                                    wb.open_new('https://wiki.rafisa.net/doku.php?id=team:max-ivens:tagesjournal:journal')
                                except error :
                                    print('error')
        #wekan öffnen
        
        
                            if ('wekan') in vc:
                                try:
                                    speak('du wirst weitergeleitet')
                                    wb.open_new('https://wekan.rafisa.net/b/N6RCwXTLiXuTw63JZ/rafisa-lernende')
                                except error:
                                    print('error')
        #rafisa einstempfel seite login
        
        
                            if ('rafisa login') in vc:
                                try:
                                    speak('du wirst weitergeleitet')
                                    wb.open_new('https://intern.stiftung-ifa.ch/betrieb/mitarbeiter/leute_over.php')
                                    winsound.PlaySound(ac,winsound.SND_ASYNC)
                                except error :
                                    print('error')
                #musik spielen
                            if ('musik') in vc:
                                try:
                                    wb.open_new('https://www.youtube.com/watch?v=lK_mT-XKe48&list=PL8IRz3Ud3qI6HD_p1X_gQuKALIUD_jSTM&index=1')
                                except error:
                                    speak('musik konnte nicht gespielt werden')
                
                #maki begrüsen und nach dem befinden fragen
                            if ('maki') in vc:
                                try:
                                    speak('Hallo Maki wilkommen wie geht es dir')
                                    with sr.Microphone() as source:
                                        print('listening...')
                                        voice = listener.listen(source)
                                        vc = listener.recognize_google(voice, language= "de-DE").lower()
                                    if vc ==('gut'):
                                        try:
                                            speak('schön das zu hören hier etwas musik für dich')
                                            winsound.PlaySound(bad,winsound.SND_ASYNC)
                                        except error:
                                            speak('maki ich brauche hilfe')
                                    else:
                                        speak('ich bin zwar nur virtuell aber ich kann musik spielen lassen')
                                        wb.open_new('https://www.youtube.com/watch?v=jOOw5Q_O6oY')
                                except error:
                                    speak('maki ich brauche hilfe')

                #ein gutes lied abspielen
                            if ('girl in red') in vc:
                                try:
                                    speak('gute wahl es spielt gleich ab')
                                    winsound.PlaySound(bad,winsound.SND_FILENAME)
                                except error:
                                    speak('kann nicht abspielen')
                            if ('gay') in vc:
                                try:
                                    wb.open_new('https://www.youtube.com/watch?v=QQK24wYyQZY')
                                except error:
                                    print('konnte nicht abspielen')
                            if ('spiele') in vc:
                                try:
                                    sp.Popen(steam)
                                except IOError:
                                    print('error')
                            if ('news') in vc:
                                try:
                                    wb.open_new('https://edition.cnn.com/')
                                except error:
                                    speak('ich konnte die news nicht öffnen')

                        except error:
                            speak('etwas stimt nicht')

                    elif ('programmieren') in vc:
                        if ('hello world') in vc:
                            if not path.exists('programm.cs'):
                                f = open('programm.cs','w')
                                f.write('using System.Collections; using System.Collections.Generic; void main(){print(hello world;)}')
                                f.close()
                            else:
                                speak('dieses programm gibt es schon siehe unter programm.cs in diesem ordner')

                    elif ('visualisierung') in vc:
                        sp.Popen(visual)
                    elif ('mail') in vc:



                        if ('lesen') in vc:
                            if not path.exists('lol.txt'):
                                f = open('lol.txt','w')
                                f.write('08/05/2019 00:00:00')
                                f.close()
                                
                                date_time = dt.datetime.now() 

                                f = open('lol.txt', 'r')
                                a = f.read()
                                a = dt.datetime.strptime(a,'%m/%d/%Y  %H:%M:%S')

                                lastdaydatetime = dt.datetime.now() - a

                                lastdaydatetime = date_time - lastdaydatetime

                                outlook = win32com.client.Dispatch('Outlook.Application').GetNameSpace('MAPI')
                                inbox = outlook.GetDefaultFolder(6)

                                messages = inbox.Items
                                messages.Sort("[ReceivedTime]", True)


                                lastdaymessages = messages.Restrict("[ReceivedTime] >= '"+ lastdaydatetime.strftime("%m/%d/%y %H:%M %p")+"'")
                                f = open('lol.txt', 'r')
                                a = f.read()
                                b = str(lastdaymessages[0].ReceivedTime)
                                if (b!=a):
                                    for message in lastdaymessages:
                                        speak(message.Receivedtime)
                                        speak(message.SenderName)
                                        speak(message.Subject)
                                        test_string = message.Body
                                        spl_word = 'https'
                                        res = test_string.partition(spl_word)[0]
                                        speak(res)
                                    f.close()
                                os.remove('lol.txt')
                        else:
                            try:
                                with sr.Microphone() as source:
                                    listener.adjust_for_ambient_noise(source)
                                    speak('ich höre zu')
                                    print('listeningl...')
                                    voice = listener.listen(source)
                                    vm = listener.recognize_google(voice, language= "de-DE").lower()
                                    outlook = win32.Dispatch('outlook.application')
                                    mail = outlook.CreateItem(0)
                                    mail.To = 'your mail' # add here your own mail
                                    mail.Subject = 'friday'
                                    mail.Body = vm
                                    mail.Send()
                            except error:
                                speak('mail kontte nicht gesendet werden')
                    elif ('kaffe') in vc:
                        speak('tut mir leid aber ich kann dir aktuell noch keinen kaffee machen')
                    elif ('reden') in vc:
                        try:
                            speak('wie geht es dir?')
                            with sr.Microphone() as source:
                                listener.adjust_for_ambient_noise(source)
                                speak('ich höre dir zu')
                                print('listening...')
                                voice = listener.listen(source)
                                vf = listener.recognize_google(voice, language= "de-DE").lower()
                            if ('gut') in vf:
                                try:
                                    speak('schön das zu hören hier etwas musik')
                                    winsound.PlaySound(ac, winsound.SND_ASYNC)
                                except error:
                                    speak('ich kann nicht mehr reden')
                            else:
                                try:
                                    speak('ich hoffe dir geht es bald besser')
                                    winsound.PlaySound(bad, winsound.SND_FILENAME)
                                except error:
                                    speak('ich kann nicht mehr reden')
                        except error:
                            speak('ich kann dich momentan nicht fragen wie es dir geht')
                                
                    #break while loop
                    elif ('musik') in vc:
                        if ('song') in vc:
                        #laut
                            if ('skater boy') in vc:
                                winsound.PlaySound(sk8er_boi,winsound.SND_FILENAME)
                            elif ('back in black') in vc:
                                winsound.PlaySound(back_in_black,winsound.SND_FILENAME)
                            elif ('covet') in vc:
                                winsound.PlaySound(covet,winsound.SND_FILENAME)
                            elif ('spoiled') in vc:
                                winsound.PlaySound(spoiled,winsound.SND_FILENAME)
                            elif ('whole') in vc:
                                winsound.PlaySound(whole,winsound.SND_FILENAME)
                            elif ('capri pants') in vc:
                                winsound.PlaySound(capri_pants,winsound.SND_FILENAME)
                            elif ('antiplesure') in vc:
                                winsound.PlaySound(antipleasure,winsound.SND_FILENAME)
                            elif ('rbels') in vc:
                                winsound.PlaySound(rebels,winsound.SND_FILENAME)
                            elif ('carnival') in vc:
                                winsound.PlaySound(carnival,winsound.SND_FILENAME)
                            elif ('demirep') in vc:
                                winsound.PlaySound(demirep,winsound.SND_FILENAME)
                            elif ('i wish i was a riot girl') in vc:
                                winsound.PlaySound(i_wish_i_was_a_riot_grrrrl,winsound.SND_FILENAME)
                            elif ('junge') in vc:
                                winsound.PlaySound(junge,winsound.SND_FILENAME)
                            elif ('lass reden') in vc:
                                winsound.PlaySound(lasse_reden,winsound.SND_FILENAME)
                            elif ('männer und frauen') in vc:
                                winsound.PlaySound(männer_und_frauen,winsound.SND_FILENAME)
                            elif ('wannsee') in vc:
                                winsound.PlaySound(wannsee,winsound.SND_FILENAME)
                            elif ('distinct') in vc:
                                winsound.PlaySound(distinct,winsound.SND_FILENAME)
                            elif ('dividing by zero') in vc:
                                winsound.PlaySound(dividing_by_zero,winsound.SND_FILENAME)
                            elif ('doom') in vc:
                                winsound.PlaySound(doom,winsound.SND_FILENAME)
                            elif ('duble dare') in vc:
                                winsound.PlaySound(double_dare_ya,winsound.SND_FILENAME)
                            elif ('centuries') in vc:
                                winsound.PlaySound(centuries,winsound.SND_FILENAME)
                            elif ('feels blind') in vc:
                                winsound.PlaySound(feels_blinde,winsound.SND_FILENAME)
                            elif ('drinking with the living dead') in vc:
                                winsound.PlaySound(drinking_with_the_living_dead,winsound.SND_FILENAME)
                            elif ('i hope you die in a fire') in vc:
                                winsound.PlaySound(i_hope_you_die_in_a_fire,winsound.SND_FILENAME)
                            elif ('oh no') in vc:
                                winsound.PlaySound(oh_no,winsound.SND_FILENAME)
                            elif ('american idiot') in vc:
                                winsound.PlaySound(american_idiot,winsound.SND_FILENAME)
                            elif ('i cant handl a change') in vc:
                                winsound.PlaySound(i_cant_handle_change,winsound.SND_FILENAME)
                            elif ('i threw glass') in vc:
                                winsound.PlaySound(i_threw_glass_at_my_finds_eye_and_now_im_on_porbation,winsound.SND_FILENAME)
                            elif ('doom 2') in vc:
                                winsound.PlaySound(doom_2,winsound.SND_FILENAME)
                            elif ('prinzesschen') in vc:
                                winsound.PlaySound(prinzesschen,winsound.SND_FILENAME)
                            elif ('magnet') in vc:
                                winsound.PlaySound(magnet,winsound.SND_FILENAME)
                            elif ('bagging') in vc:
                                winsound.PlaySound(beggin,winsound.SND_FILENAME)
                            elif ('i wanna') in vc:
                                winsound.PlaySound(i_wanna_be_your_slaver,winsound.SND_FILENAME)
                            elif ('atomic blond') in vc:
                                winsound.PlaySound(atomic_blonde,winsound.SND_FILENAME)
                            elif ('doom 3') in vc:
                                winsound.PlaySound(doom_3,winsound.SND_FILENAME)
                            elif ('doom 4') in vc:
                                winsound.PlaySound(doom_4,winsound.SND_FILENAME)
                            elif ('new radio') in vc:
                                winsound.PlaySound(new_radio,winsound.SND_FILENAME)
                            elif ('angle') in vc:
                                winsound.PlaySound(angel_with_a_shotgun,winsound.SND_FILENAME)
                            elif ('labyrint') in vc:
                                winsound.PlaySound(labyrint,winsound.SND_FILENAME)
                            elif ('i write sins') in vc:
                                winsound.PlaySound(i_write_sins_not_tragaties,winsound.SND_FILENAME)
                            elif ('rebel girl') in vc:
                                winsound.PlaySound(rebel_girl,winsound.SND_FILENAME)
                            elif ('reject') in vc:
                                winsound.PlaySound(reject_all_american,winsound.SND_FILENAME)
                            elif ('partners') in vc:
                                winsound.PlaySound(partners_in_crime,winsound.SND_FILENAME)
                            elif ('teenagers') in vc:
                                winsound.PlaySound(teenagers,winsound.SND_FILENAME)
                            elif ('seven nation army') in vc:
                                winsound.PlaySound(seven_nation_army,winsound.SND_FILENAME)
                            elif ('anarchist') in vc:
                                winsound.PlaySound(anarchist,winsound.SND_FILENAME)
                            elif ('orginale me') in vc:
                                winsound.PlaySound(original_me,winsound.SND_FILENAME)
                            elif ('perents') in vc:
                                winsound.PlaySound(perents,winsound.SND_FILENAME)
                            elif ('kids') in vc:
                                winsound.PlaySound(psychotic_kids,winsound.SND_FILENAME)
                            elif ('gladiator') in vc:
                                winsound.PlaySound(gladiator,winsound.SND_FILENAME)
                            elif ('fortunet son') in vc:
                                winsound.PlaySound(fortunet_son,winsound.SND_FILENAME)
                            #depri
                            elif ('haning tree') in vc:
                                winsound.PlaySound(haning_tree,winsound.SND_FILENAME)
                            elif ('addict') in vc:
                                winsound.PlaySound(addict,winsound.SND_FILENAME)
                            elif ('how dose it feel') in vc:
                                winsound.PlaySound(how_does_it_feel,winsound.SND_FILENAME)
                            elif ('the night i drove alone') in vc:
                                winsound.PlaySound(the_night_i_drove_alone,winsound.SND_FILENAME)
                            elif ('the summer') in vc:
                                winsound.PlaySound(the_summer,winsound.SND_FILENAME)
                            elif ('bad idea') in vc:
                                winsound.PlaySound(bad,winsound.SND_FILENAME)
                            elif ('girls') in vc:
                                winsound.PlaySound(girls,winsound.SND_FILENAME)
                            elif ('we fell in love in october') in vc:
                                winsound.PlaySound(we_fell_in_love_in_october,winsound.SND_FILENAME)
                            elif ('fuck it') in vc:
                                winsound.PlaySound(fuck_it,winsound.SND_FILENAME)
                            elif ('alive') in vc:
                                winsound.PlaySound(alive,winsound.SND_FILENAME)
                            elif ('99 luftballongs') in vc:
                                winsound.PlaySound(luftballongs,winsound.SND_FILENAME)
                            elif ('make a move') in vc:
                                winsound.PlaySound(make_a_move,winsound.SND_FILENAME)
                            elif ('serotonin') in vc:
                                winsound.PlaySound(serotonin,winsound.SND_FILENAME)
                            elif ('girls in bikinis') in vc:
                                winsound.PlaySound(girls_in_bikinis,winsound.SND_FILENAME)
                            elif ('irgendwann') in vc:
                                winsound.PlaySound(irgendwann,winsound.SND_FILENAME)
                            elif ('soldiers eyes') in vc:
                                winsound.PlaySound(soilders_eyes,winsound.SND_FILENAME)
                            elif ('skin boots') in vc:
                                winsound.PlaySound(skin_boots,winsound.SND_FILENAME)
                            elif ('salish') in vc:
                                winsound.PlaySound(Salish,winsound.SND_FILENAME)
                            elif ('november') in vc:
                                winsound.PlaySound(novermber_was_white,winsound.SND_FILENAME)
                        #galaxy
                            elif ('mr blue sky') in vc:
                                winsound.PlaySound(mr_blue_sky,winsound.SND_FILENAME)
                            elif ('fox on the run') in vc:
                                winsound.PlaySound(fox_on_the_run,winsound.SND_FILENAME)
                            elif ('lake shore drive') in vc:
                                winsound.PlaySound(lake_shore_drive,winsound.SND_FILENAME)
                            elif ('the chain') in vc:
                                winsound.PlaySound(the_chain,winsound.SND_FILENAME)
                            elif ('bring it home to me') in vc:
                                winsound.PlaySound(bring__it_home_to_me,winsound.SND_FILENAME)
                            elif ('southern nights') in vc:
                                winsound.PlaySound(southern_nights,winsound.SND_FILENAME)
                            elif ('my sweet lord') in vc:
                                winsound.PlaySound(my_sweet_lord,winsound.SND_FILENAME)
                            elif ('brandy') in vc:
                                winsound.PlaySound(brandy,winsound.SND_FILENAME)
                            elif ('come a little bit closer') in vc:
                                winsound.PlaySound(come_a_little_bit_closer,winsound.SND_FILENAME)
                            elif ('komisch') in vc:
                                winsound.PlaySound(wham_bam_shang_a_lang,winsound.SND_FILENAME)
                            elif ('surrender') in vc:
                                winsound.PlaySound(surrender,winsound.SND_FILENAME)
                            elif ('father and son') in vc:
                                winsound.PlaySound(father_and_son,winsound.SND_FILENAME)
                            elif ('flash light') in vc:
                                winsound.PlaySound(flash_light,winsound.SND_FILENAME)
                            elif ('inferno') in vc:
                                winsound.PlaySound(guardians_inferno,winsound.SND_FILENAME)
                            #six the musical
                            elif ('ex wives') in vc:
                                winsound.PlaySound(ex_wives,winsound.SND_FILENAME)
                            elif ('dont lose your head') in vc:
                                winsound.PlaySound(dont_lose_your_head,winsound.SND_FILENAME)
                            elif ('haus of holbein') in vc:
                                winsound.PlaySound(haus_of_holbein,winsound.SND_FILENAME)
                            elif ('get down') in vc:
                                winsound.PlaySound(get_down,winsound.SND_FILENAME)
                            elif ('all you wanna do') in vc:
                                winsound.PlaySound(all_you_wanna_do,winsound.SND_FILENAME)
                                                
                                


                        elif ('zufällig') in vc:
                            random_song_list = (back_in_black
,we_fell_in_love_in_october
,fuck_it
,alive
,luftballongs
,make_a_move
,serotonin
,girls_in_bikinis
,irgendwann
,bad
,girls
,sk8er_boi
,covet
,spoiled
,whole
,capri_pants
,antipleasure
,rebels
,carnival
,demirep
,i_wish_i_was_a_riot_grrrrl
,junge
,lasse_reden
,männer_und_frauen
,wannsee
,distinct
,dividing_by_zero
,doom 
,double_dare_ya 
,centuries 
,feels_blinde
,drinking_with_the_living_dead 
,i_hope_you_die_in_a_fire 
,oh_no 
,american_idiot 
,i_cant_handle_change 
,i_threw_glass_at_my_finds_eye_and_now_im_on_porbation 
,doom_2 
,prinzesschen 
,magnet 
,beggin 
,i_wanna_be_your_slaver 
,atomic_blonde
,doom_3
,doom_4
,new_radio 
,angel_with_a_shotgun 
,labyrint 
,i_write_sins_not_tragaties 
,rebel_girl 
,reject_all_american 
,partners_in_crime
,teenagers 
,seven_nation_army 
,anarchist 
,original_me 
,perents 
,psychotic_kids 
,gladiator)
                            random_song = random.choice(random_song_list)
                            winsound.PlaySound(random_song,winsound.SND_FILENAME)

 
                    elif vc == ("aus"):
                        speak('auf wiedersehen')                        
                        break
                    else:
                        #awnser printing from the intens.json file
                        results = model.predict([bag_of_words(vc, words)])
                        results_index = np.argmax(results)
                        tag = labels[results_index]
                        for tg in data["intents"]:
                            if tg['tag'] == tag:
                                responses = tg['responses']
                                speak(random.choice(responses))
                    
            
    
        
        chat()
    else:
        print("no face")
listening()
input('press ENTER to exit')