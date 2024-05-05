import pygame

pygame.init()

screen = pygame.display.set_mode((500,600))

LightBlack = (0,4,26)
White = (230,230,255)

font = pygame.font.SysFont('sans', 50)
text_1 = font.render('Say anything', True, LightBlack)

running = True

while running:
    screen.fill(LightBlack)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x, mouse_y)
    Screen = pygame.draw.rect(screen, LightBlack, (255,255,300,200))
    Button = pygame.draw.circle(screen, White, (242,547), 150)
     
    screen.blit(text_1, (111,505))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
             print("xxx")    

    pygame.display.flip() 

pygame.quit()       