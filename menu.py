import pygame as pg
from settings import W, H, colors, draw_background, CreateButton, small_font, big_font

pg.mixer.init()

button_click = pg.mixer.Sound('assets/sounds/button-click.mp3')

def menu_cycle(display):

    text = small_font.render('credits: Abhijith14 & Kiooqq', True, colors["WHITE"])
    text_rect = text.get_rect(center=(W - 50, H - 20))
    text1 = big_font.render('Classic Shake', True, colors["WHITE"])
    text_rect1 = text.get_rect(center=(W - 50, H - 20))


    play_button = CreateButton((W // 2 - 100), (H // 2 - 75), 200, 75, 'PLAY', 'assets/images/Button.png',
                               'assets/images/Button_Hover.png')
    shop_button = CreateButton((W // 2 - 100), (H // 2), 200, 75, 'SHOP', 'assets/images/Button.png',
                               'assets/images/Button_Hover.png')
    exit_button = CreateButton((W // 2 - 100), (H // 2 + 75), 200, 75, 'EXIT', 'assets/images/Button.png',
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
                if shop_button.btn_rect.collidepoint(event.pos):
                    button_click.play()
                    return "shop"
                if exit_button.btn_rect.collidepoint(event.pos):
                    button_click.play()
                    return "exit"


        draw_background(display)
        play_button.draw(display)
        shop_button.draw(display)
        exit_button.draw(display)

        display.blit(text, (W - 270, H - 20))
        display.blit(text1, (W // 2 - 200, H // 2 - 175))

        pg.display.flip()

    quit()