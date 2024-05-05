# Import thư viện
import speech_recognition
import pyttsx3
from datetime import date, datetime
import pygame

# Khởi tạo 
robot_ear = speech_recognition.Recognizer()          
robot_mouth = pyttsx3.init()
robot_brain = ""
app = pygame.init()
screen = pygame.display.set_mode((500,600))
# Màu:
LightBlack = (0,4,26)
White = (230,230,255)
# Font chữ
font = pygame.font.SysFont('sans', 50)
text_1 = font.render('Nói', True, LightBlack)

running = True
# Hệ thống
while running:
    screen.fill(LightBlack)
    Screen = pygame.draw.rect(screen, LightBlack, (255,255,300,200))
    Button = pygame.draw.circle(screen, White, (242,547),100)
     
    screen.blit(text_1, (202,504))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
           if event.button == 1 in Button:
             with speech_recognition.Microphone() as mic:
              audio = robot_ear.listen(mic)
             try:
              you = robot_ear.recognize_google(audio, language = 'vi-VN')
             except:
              you = ""
             with speech_recognition.Microphone() as mic:  
              print("GoX2: Tôi đang nghe bạn nói đây.")
              robot_brain = "Tôi đang nghe bạn nói đây."
              audio = robot_ear.listen(mic)
              voices = robot_mouth.getProperty("voices")
              robot_mouth.setProperty("voice", voices[1].id)
              robot_mouth.say(robot_brain)
              robot_mouth.runAndWait()
              print("GoX2: ...")                          
              you = robot_ear.recognize_google(audio, language = 'vi-VN')
              print("You:" + you)            
              if you == "":
                robot_brain = "Tôi không thể nghe bạn đang nói gì, hãy thử lại hoặc kiểm tra micro của bạn."
              elif "chào" in you:
                robot_brain = "Chào. Bạn cảm thấy như thế nào?" 
                      
              else:
                robot_brain = "Tôi không hiểu bạn đang nói gì."
                print("GoX2: " + robot_brain)
           

              voices = robot_mouth.getProperty("voices")
              robot_mouth.setProperty("voice", voices[1].id)
              robot_mouth.say(robot_brain)
              robot_mouth.runAndWait()           
            
    pygame.display.flip() 

pygame.quit() 
