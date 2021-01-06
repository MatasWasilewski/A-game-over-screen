import pygame

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

size = (800,800)

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game Over Message")

running = True

font = pygame.font.Font(None,55)

rect_y = 50
rect_x = 50
rect_change_x = 5
rect_change_y =5

clock = pygame.time.Clock()

game_over = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
           game_over = True

    if not game_over:
        rect_x += rect_change_x
        rect_y += rect_change_y

        if rect_y > 750 or rect_y <0:
            rect_change_y = rect_change_y * -1
        if rect_x > 750 or rect_x <0:
            rect_change_x = rect_change_x * -1


    screen.fill(black)
    pygame.draw.rect(screen,blue,[rect_x,rect_y,100,100])

    if game_over:
           text = font.render("GAME ENDED", True, green)
           text_rect = text.get_rect()
           text_x = screen.get_width()/2 - text_rect.width/2
           text_y = screen.get_width()/2 - text_rect.width/2
           screen.blit(text,[text_x,text_y])

    else:
           text = font.render("Click to end the game", True, red)
           text_rect = text.get_rect()
           text_x = screen.get_width()/2 - text_rect.width/2
           text_y = screen.get_width()/2 - text_rect.width/2
           screen.blit(text,[text_x,text_y])

    clock.tick(60)
    pygame.display.flip()
       

   
pygame.quit()
