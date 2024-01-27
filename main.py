from data import *

window = pygame.display.set_mode(setting["BG"])

app = QApplication([])
window_yes = QWidget()

name_crosse = QInputDialog().getText(QInputDialog(), "імя користувача", "введіть імя для гравця хрестиків")[0][:8]
name_nought = QInputDialog().getText(QInputDialog(), "імя користувача", "введіть імя для гравця нуликів")[0][:8]


def run():
    game = True
    #парне число - нулик, не парне число - хрестик
    move = 1
    winner_cord = False
    winner = False
    cross_point = 0
    nought_point = 0
    win_key = [(1,2,3,(13, 13 + 37, 210 + 74, 13 + 37)), 
               (4,5,6, (13, 110 + 37, 210 + 74, 110 + 37)), 
               (7,8,9, (13, 211 + 37, 210 + 74, 211 + 37)),
               (1,4,7, (13 + 37, 13, 13 + 37, 211 + 74)), 
               (2,5,8, (110 + 37, 13, 110 + 37, 211 + 74)), 
               (3,6,9, (210 + 37, 13, 210 + 37, 211 + 74)),
               (1,5,9, (13, 13, 210 + 74, 211 + 74)), 
               (3,5,7, (210 + 74, 13, 13, 211 + 74))]

    for i in range(1, 10):
        cords[i].append(pygame.Rect(cords[i][0], (74, 74)))
    
    font_name = pygame.font.SysFont("Comic Sans MC", 25)


    while game:
        window.fill((0,0,0))
        window.blit(bg_image, (0, 0))

        window.blit(font_name.render(name_crosse, True, (255, 255, 255)), (10, setting["BG"][0] + 5))
        window.blit(font_name.render(name_nought, True, (255, 255, 255)), (setting["BG"][0] - font_name.size(name_nought)[0] - 10, setting["BG"][0] + 5))
        window.blit(font_name.render(str(cross_point), True, (255, 255, 255)), (setting["BG"][0] // 2 - 20, setting["BG"][0] + 5))
        window.blit(font_name.render(str(nought_point), True, (255, 255, 255)), (setting["BG"][0] // 2 + 10, setting["BG"][0] + 5))
        

        for key in moves:
            if key[1] == "x":
                window.blit(cross_image, cords[key[0]][0])
            if key[1] == "o":
                window.blit(nought_image, cords[key[0]][0])
        
        if winner_cord:
            pygame.draw.line(window, (120,120,120), (winner_cord[0], winner_cord[1]), (winner_cord[2], winner_cord[3]), 10)
            if winner_cord[-1] == "x" and winner:
                cross_point += 1
            elif winner_cord[-1] == "o" and winner:
                nought_point += 1
            winner = False

        else:
            for key in win_key:
                if cords[key[0]][1] and cords[key[1]][1] and cords[key[2]][1]:
                    if cords[key[0]][3] == cords[key[1]][3] == cords[key[2]][3]:
                        if cords[key[0]][3] == "x":
                            print("XXXXXXXXXXX")
                        if cords[key[0]][3] == "o":
                            print("OOOOOOOOOOOOO")
                        winner_cord = (key[3][0], key[3][1], key[3][2], key[3][3], cords[key[0]][3])
                        winner = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                for key in cords:
                    if cords[key][2].collidepoint(x, y) and not cords[key][1]:
                        cords[key][1] = True
                        if move % 2 == 0:
                            moves.append((key, "o"))
                            cords[key].append("o")
                        if move % 2 != 0:
                            moves.append((key, "x"))
                            cords[key].append("x")
                        move += 1
                        print(moves)
        
        pygame.display.flip()

run()