import pygame as pg
from settings import W, H, colors, draw_background, CreateButton, big_font, small_font

pg.mixer.init()

button_click = pg.mixer.Sound('assets/sounds/button-click.mp3')

SKINS = [
    {
        'name': 'Базовий',
        "colors": {"main": (0, 0, 255), "accent": (0, 100, 255)}
    },
    {
        'name': 'Багач',
        "colors": {"main": (255, 215, 0), "accent": (255, 255, 0)}
    },
    {
        'name': 'Гора',
        "colors": {"main": (224, 255, 255), "accent": (0, 255, 255)}
    }
]

FRUITS = [
    {
        'name': 'Яблоко',
        "color": (200, 0, 0)
    },
    {
        'name': 'Апельсин',
        "color": (255, 165, 0)
    },
    {
        'name': 'Лайм',
        "color": (173, 255, 47)
    }
]

current_skin_index = 0

current_fruit_index = 0

SKIN1 = SKINS[current_skin_index]["colors"]["main"]
SKIN2 = SKINS[current_skin_index]["colors"]["accent"]

FRUIT_SKIN = FRUITS[current_fruit_index]["color"]

def shop_cycle(display):
    global current_skin_index, SKIN1, SKIN2, FRUIT_SKIN, current_fruit_index

    text = big_font.render('Skins shakes', True, colors["WHITE"])

    back_button = CreateButton((W // 2 - 100), (H - 75), 200, 75, 'BACK', 'assets/images/Button.png',
                               'assets/images/Button_Hover.png')

    running = True

    while running:
        current_skin_name = SKINS[current_skin_index]['name']

        current_fruit_name = FRUITS[current_fruit_index]['name']

        change_skin_button = CreateButton((W // 2 - 300), (H // 2 - 75), 300, 125, current_skin_name,'assets/images/Button.png',
                                          'assets/images/Button_Hover.png')

        change_fruit_button = CreateButton((W // 2), (H // 2 - 75), 300, 125, current_fruit_name,'assets/images/Button.png',
                                          'assets/images/Button_Hover.png')

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                quit()

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if change_skin_button.btn_rect.collidepoint(event.pos):
                    button_click.play()
                    current_skin_index = (current_skin_index + 1) % len(SKINS)

                    SKIN1 = SKINS[current_skin_index]["colors"]["main"]
                    SKIN2 = SKINS[current_skin_index]["colors"]["accent"]

                if change_fruit_button.btn_rect.collidepoint(event.pos):
                    button_click.play()
                    current_fruit_index = (current_fruit_index + 1) % len(FRUITS)

                    FRUIT_SKIN = FRUITS[current_fruit_index]["color"]

                if back_button.btn_rect.collidepoint(event.pos):
                    button_click.play()
                    return "menu"

        draw_background(display)
        change_skin_button.draw(display)
        change_fruit_button.draw(display)
        back_button.draw(display)

        display.blit(text, (W // 2 - text.get_width() // 2, H // 2 - 200))

        pg.display.flip()

    pg.quit()
    quit()