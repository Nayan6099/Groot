#import pyaudio
import sounddevice as sd 
import numpy as np 

threshold = 3
Clap = False
def detect_clap(indata,frames,time,status):
    global Clap
    volume_norm = np.linalg.norm(indata)*10
    if volume_norm>threshold:
       print("clapped!!")
       Clap = True
    pass 
 
def Lishten_for_claps():
   with sd.InputStream(callback=detect_clap):
      return sd.sleep(1000)
def MainClapExe():

   while True:
      Lishten_for_claps()
      if Clap==True:
         break
      
      else:
         pass
   
      