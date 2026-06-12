import pygame as pg
from settings import W, H, colors, draw_background, CreateButton, big_font

pg.mixer.init()

button_click = pg.mixer.Sound('assets/sounds/button-click.mp3')

def game_over_cycle(display):

    text = big_font.render('GAME OVER', True, colors["RED"])
    text_rect = text.get_rect(center=(W - 50, H - 20))

    play_button = CreateButton((W // 2 - 100), (H // 2), 200, 75, 'RESTART', 'assets/images/Button.png',
                               'assets/images/Button_Hover.png')
    menu_button = CreateButton((W // 2 - 100), (H // 2 + 75), 200, 75, 'MENU', 'assets/images/Button.png',
                               'assets/images/Button_Hover.png')
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.btn_rect.collidepoint(event.pos):
                    button_click.play()
                    return "game"
                if menu_button.btn_rect.collidepoint(event.pos):
                    button_click.play()
                    return "menu"


        draw_background(display)
        play_button.draw(display)
        menu_button.draw(display)

        display.blit(text, (W // 2 - 150, H // 2 - 100))

        pg.display.flip()

    quit()