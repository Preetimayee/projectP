import pyttsx3
import os

pyttsx3("Hiee... how can i help you")


while True:
    print("chat with your requirement : " , end='')
    p = input()

    #print(p)
    #os.system(p)


    if (("run" in p) or ("open" in p) or ("upload" in p) or ("excute" in p)) and ("camera" in p): 
       pyttsx3.speak("lunching camera")    
       os.system("start microsoft.windows.camera:")

    elif ("run" in p) and ("chrome" in p):
          pyttsx3.speak("lunching chrome") 
          os.system('chrome')

    elif (("run" in p) or ("excute" in p) or ("open" in p) or ("upload" in p)) and (("notepad" in p) or ("editor" in p)):
             pyttsx3.speak("lunching notepade")
             os.system('notepad')

    elif (("run" in p) or ("excute" in p) or ("open" in p) or ("upload" in p)) and ("player" in p) and ("media" in p):
            pyttsx3.speak("lunching wmplayer")
            os.system('start wmplayer')

    elif (("run" in p) or ("excute" in p) or ("open" in p) or ("upload" in p)) and (("cmd" in p) or ("editor" in p)):
            pyttsx3.speak("lunching cmd")
            os.system('start cmd')

    elif (("run" in p) or ("excute" in p) or ("open" in p) or ("upload" in p)) and ("vlc" in p):
            pyttsx3.speak("lunching vlc")
            os.system('start vlc')

    elif (("run" in p) or ("excute" in p) or ("open" in p) or ("upload" in p)) and ("excel" in p) or ("this pc" in p):
            pyttsx3.speak("lunching excel")
            os.system('start excel')

    elif (("run" in p) or ("open" in p) or  ("execute" in p) or ("upload" in p)) and (("calc" in p) or ("calculator" in p)):
        pyttsx3.speak("lunching calculator")        
        os.system("start calc")

    elif (("run" in p) or ("open" in p) or  ("execute" in p) or ("upload" in p)) and (("store" in p) or ("windows store" in p) or ("app store" in p)):
        pyttsx3.speak("lunching ms store")      
        os.system("start ms-windows-store:")  

    elif (("run" in p) or ("open" in p) or  ("execute" in p) or ("upload" in p)) and (("news" in p) or ("microsoft news" in p)):
        pyttsx3.speak("lunching microsoft news")        
        os.system("start msnews:")  

    elif (("run" in p) or ("open" in p) or ("excute" in p) or ("upload" in p)) and (("clock" in p) or ("time" in p)):
          pyttsx3.speak("lunching alarm and clock")
          os.system("start ms-clock:")

    elif (("run" in p) or ("open" in p) or ("excute" in p) or ("upload" in p)) and (("control" in p) and ("panel" in p)):
         pyttsx3.speak("lunching control panel")
         os.system("start control")

    elif (("run" in p) or ("open" in p) or ("excute" in p) or ("upload" in p)) and  ("microsoft edge" in p):
          pyttsx3.speak("lunching microsoft edge broswer")
          os.system("start msedge")

    elif (("run" in p) or ("open" in p) or ("excute" in p) or ("upload" in p)) and ("aap store" in p):
          pyttsx3.speak("lunching ms store")
              

    elif (("run" in p) or ("open" in p) or  ("execute" in p ) or ("upload" in p)) and (("calender" in p) or ("planner" in p)):
        pyttsx3.speak("lunching calender")       
        os.system("start outlookcal:")

    elif (("run" in p) or ("open" in p) or  ("execute" in p ) or ("upload" in p)) and ("python" in p):
        pyttsx3.speak("lunching python interpretor")        
        os.system("start python")  
            
    elif (("run" in p) or ("open" in p) or ("execute" in p ) or ("upload" in p)) and (("google" in p) or ("ok google" in p)):
          pyttsx3.speak("lunching google")
          os.system("start chrome google.com") 

    elif (("run" in p) or ("open" in p) or ("execute" in p ) or ("upload" in p)) and (("facebook" in p) or ("fb" in p)): 
          pyttsx3.speak("lunching facebook")
          os.system("start chrome facebook.com")    

    elif (("run" in p) or ("open" in p) or ("execute" in p ) or ("upload" in p)) and (("youtube" in p) or ("you tube" in p)):
          pyttsx3.speak("lunching youtube")
          os.system("start chrome youtube.com") 

    elif (("run" in p) or ("open" in p) or ("execute" in p ) or ("upload" in p)) and (("linked" in p) or ("linkedin" in p)):
          pyttsx3.speak("lunching linkedin")
          os.system("start chrome linkedin.com") 

    elif (("run" in p) or ("open" in p) or ("execute" in p ) or ("upload" in p)) and ("instagram" in p):
          pyttsx3.speak("lunching instagram")
          os.system("start chrome instagram.com") 

 
    elif (("run" in p) or ("open" in p) or  ("execute" in p ) or ("upload" in p)) and (("amazon" in p) or ("amazon shopping" in p)): 
        pyttsx3.speak("opening amazon shoppin site")        
        os.system("start chrome amazon.com")
    
    elif (("run" in p) or ("open" in p) or  ("execute" in p ) or ("upload" in p)) and ("twitter" in p):
         pyttsx3.speak("lunching twitter")        
         os.system("start chrome twitter.com")
    
    elif (("run" in p) or ("open" in p) or  ("execute" in p ) or ("upload" in p)) and (("flipkart" in p) or ("flipkart shopping" in p)):
         pyttsx3.speak("lunching flipkart shopping site")        
         os.system("start chrome flipkart.com")
      
    elif (("run" in p) or ("open" in p) or ("execute" in p ) or ("upload" in p)) and (("myntra" in p) or ("mytra shopping" in p)):
        pyttsx3.speak("lunching myntra shopping site")        
        os.system("start chrome myntra.com")


    elif (("run" in p) or ("open" in p) or ("excute" in p) or ("upload" in p)) and ("gmail" in p):
        pyttsx3.speak("lunching gmail")
        os.system("start chrome gmail.com")


    elif  ("exit" in p)  or ("quit" in p) or ("close" in p)
	  pyttsx3.speak("thanks for using this se rvices")
          break    

    else: 
        pyttsx3.speak("please try again using correct command")   



