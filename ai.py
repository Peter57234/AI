# Import thư viện
import speech_recognition
import pyttsx3
from datetime import date, datetime
import pygame

# Khởi tạo 
robot_ear = speech_recognition.Recognizer()          
robot_mouth = pyttsx3.init()
robot_brain = ""
pygame.init()
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
    clock = pygame.time.Clock() 
    Text = screen.blit(text_1, (202,504))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
          if Button.collidepoint(event.pos):
            while True:
                 with speech_recognition.Microphone() as mic:  
                  print("GoX2: Tôi đang nghe bạn nói đây.")
                  robot_brain = "Tôi đang nghe bạn nói đây."
                  audio = robot_ear.listen(mic)
                  voices = robot_mouth.getProperty("voices")                 
                  robot_mouth.setProperty("voice", voices[1].id)
                  robot_mouth.say(robot_brain)               
                  robot_mouth.runAndWait() 
                  print("GoX2: ...")                         
                 try:                 
                  you = robot_ear.recognize_google(audio, language = 'vi-VN')
                 except:
                  you = ""
                 print("You: " + you)              
                                                           
                 if you == "":
                    robot_brain = "Tôi không thể nghe bạn đang nói gì, hãy thử lại hoặc kiểm tra micro của bạn."
                 elif "chào" in you:
                   robot_brain = "Chào. Bạn cảm thấy như thế nào?" 
                 elif "bạn là ai" in you:
                   robot_brain = "Tôi là GoX2, 1 trợ lý ảo được xây dựng trên ngôn ngữ lập trình Python."
                 elif "Hôm nay là ngày mấy" in you:
                   today = date.today()
                   robot_brain = today.strftime("%B %d, %Y")
                 elif "Bây giờ là mấy giờ" in you:
                   now = datetime.now()
                   robot_brain = now.strftime("%H hours %M minutes %S seconds")
                 elif "Ai là tổng thống Mỹ" in you:
                   robot_brain = "Tính đến thời điểm ngày 21/4/2024, Joe Biden là tổng thống của Hợp chủng quốc Hoa Kỳ."
                 elif "Việt Nam là gì" in you:
                   robot_brain = "Việt Nam, tên chính thức là Cộng hòa xã hội chủ nghĩa Việt Nam, là một quốc gia xã hội chủ nghĩa nằm ở cực Đông của bán đảo Đông Dương thuộc khu vực Đông Nam Á, giáp với Lào, Campuchia, Trung Quốc, biển Đông và vịnh Thái Lan (Nguồn: Wikiwand)."
                 elif "Bạn cảm thấy như thế nào" in you:
                   robot_brain = "Tôi là 1 trí thông minh nhân tạo nên tôi không có cảm xúc, nhưng tôi luôn sẵn sàng và hào hứng khi được giúp đỡ bạn! Bạn đang quan tâm đến vấn đề gì hôm nay?"
                 elif "Hoa Kỳ là gì" in you:
                   robot_brain = "Hợp chúng quốc Hoa Kỳ (tiếng Anh: The United States of America, United States of America, USA), gọi tắt là Hoa Kỳ (tiếng Anh: United States, US hoặc U.S., nguyên văn 'Hợp chúng quốc') hoặc cũng thường được gọi là Mỹ, là một quốc gia cộng hòa lập hiến liên bang ở châu Mỹ, nằm tại Tây Bán cầu, lãnh thổ bao gồm 50 tiểu bang và một đặc khu liên bang (trong đó có 48 tiểu bang lục địa), thủ đô là Washington, D.C., thành phố lớn nhất là New York. Hoa Kỳ nằm ở giữa Bắc Mỹ, giáp biển Thái Bình Dương ở phía tây, Đại Tây Dương ở phía đông, Canada ở phía bắc và Mexico ở phía nam (Nguồn: Wikipedia)."
                 elif "WHO là gì" in you:
                   robot_brain = "Tổ chức Y tế Thế giới (viết tắt TCYTTG; tiếng Anh: World Health Organization - WHO; tiếng Pháp: Organisation mondiale de la santé - OMS) là một cơ quan chuyên môn của Liên Hợp Quốc, WHO đóng vai trò thẩm quyền điều phối các vấn đề sức khỏe và y tế cộng đồng trên bình diện quốc tế, WHO tham gia giúp đỡ các quốc gia thành viên, WHO cung cấp những thông tin chính xác, những địa chỉ đáng tin cậy trên lĩnh vực sức khỏe con người, WHO sẽ đứng ra để giải quyết những vấn đề cấp bách về sức khỏe cộng đồng và dịch bệnh của con người (Nguồn: Wikipedia)."
                 elif "Bạn làm sai rồi" in you:
                   robot_brain = "Xin lỗi vì đã làm sai. Bạn có thể cho tôi biết thêm chi tiết không để tôi có thể giúp đỡ bạn tốt hơn?"
                 elif "Bạn có khỏe không" in you:
                   robot_brain = "Tôi không có cảm xúc như con người, nhưng cảm ơn bạn đã hỏi! Tôi sẵn sàng giúp đỡ bạn. Bạn cần gì hôm nay?"
                 elif "Giải bóng đá thế giới là gì" in you:
                   robot_brain = "FIFA World Cup, hay đơn giản là World Cup, còn gọi là Giải vô địch bóng đá thế giới hoặc Cúp bóng đá thế giới trong tiếng Việt[1][2], là giải đấu bóng đá do Liên đoàn Bóng đá Quốc tế (FIFA) tổ chức với chu kỳ 4 năm 1 lần cho tất cả các đội tuyển bóng đá nam quốc gia của những nước thành viên FIFA. Giải lần đầu tiên được tổ chức vào năm 1930, và bị gián đoạn 2 lần vào các năm 1942 và 1946 do Chiến tranh thế giới thứ hai (Nguồn: Wikipedia)."
                 elif "Minecraft là gì" in you:
                   robot_brain = "Minecraft, một trò chơi điện tử phổ biến. Minecraft cho phép người chơi xây dựng và khám phá một thế giới được tạo nên từ các khối vuông. Người chơi có thể tạo ra các công trình, thu thập tài nguyên, và chiến đấu với những sinh vật, hoặc tham gia các chế độ chơi khác nhau như chế độ sinh tồn, chế độ sáng tạo, và chế độ phiêu lưu."
                 elif "roblox là gì" in you:
                   robot_brain = "Roblox là một nền tảng trò chơi trực tuyến và một hệ thống để tạo trò chơi, cho phép người dùng thiết kế và chia sẻ các trò chơi của riêng họ cũng như chơi trò chơi do người khác tạo ra. Nền tảng này được phát triển và quản lý bởi công ty Roblox Corporation và đã được ra mắt vào năm 2006."
                 elif "liên minh huyền thoại là gì" in you:
                   robot_brain = "Liên Minh Huyền Thoại(League of Legends), thường được gọi là LoL, là một trò chơi điện tử thể loại MOBA (Multiplayer Online Battle Arena) phổ biến, được phát triển và phát hành bởi Riot Games vào năm 2009. Trò chơi này đã trở thành một trong những trò chơi esport hàng đầu trên thế giới, thu hút hàng triệu người chơi và người xem."                      
                 elif "tạm biệt" in you:
                   robot_brain = "Hẹn gặp lại"
                   voices = robot_mouth.getProperty("voices")
                   robot_mouth.setProperty("voice", voices[1].id)
                   robot_mouth.say(robot_brain)
                   print("GoX2: " + robot_brain)
                   robot_mouth.runAndWait()               
                   break                 
                 else:
                   robot_brain = "Tôi không hiểu bạn đang nói gì."
                 voices = robot_mouth.getProperty("voices")
                 robot_mouth.setProperty("voice", voices[1].id)
                 robot_mouth.say(robot_brain)
                 print("GoX2: " + robot_brain)
                 robot_mouth.runAndWait()                                             
    clock.tick(60) 
    pygame.display.flip() 

pygame.quit() 
