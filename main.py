import pygame as pg

from models.constantes import (
    ALTO_VENTANA, ANCHO_VENTANA, FPS
)
from models.player.main_player import Jugador

from models.enemigo.main_enemigo import Enemigo

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.init()
clock = pg.time.Clock()

back_img = pg.image.load('./assets/img/background/the_simpson_background.png')
back_img = pg.transform.scale(back_img, (ANCHO_VENTANA, ALTO_VENTANA))


juego_ejecutandose = True

vegeta = Jugador(0, 1, frame_rate=70, speed_walk=20, speed_run=40, gravity=10, jump=32)
enemigo_1 = Enemigo(0, 0.1, frame_rate=70, speed_walk=20, speed_run=40, gravity=0, jump=32)

while juego_ejecutandose:
    
    #print(delta_ms)
    lista_eventos = pg.event.get()
    for event in lista_eventos:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                vegeta.jump(True)

        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                vegeta.jump(False)        
            
        if event.type == pg.KEYDOWN:    
            if event.key == pg.K_ESCAPE:
                juego_ejecutandose = False
                break
    
    tecla_presionada = pg.key.get_pressed()
    if tecla_presionada[pg.K_RIGHT] and not tecla_presionada[pg.K_LEFT]:
        vegeta.walk('Right')
    if tecla_presionada[pg.K_LEFT] and not tecla_presionada[pg.K_RIGHT]:
        vegeta.walk('Left')

    if not tecla_presionada[pg.K_RIGHT] and not tecla_presionada[pg.K_LEFT] and not tecla_presionada[pg.K_SPACE]:
        vegeta.stay()
    
    if tecla_presionada[pg.K_RIGHT] and tecla_presionada[pg.K_LSHIFT] and not tecla_presionada[pg.K_LEFT]:
        vegeta.run('Right')
    if tecla_presionada[pg.K_LEFT] and tecla_presionada[pg.K_LSHIFT] and not tecla_presionada[pg.K_RIGHT]:
        vegeta.run('Left')
    
        
    
    screen.blit(back_img, back_img.get_rect())
    delta_ms = clock.tick(FPS)
    vegeta.update(delta_ms)
    vegeta.draw(screen)
    
    enemigo_1.update(delta_ms)
    enemigo_1.draw(screen)
    pg.display.update()

pg.quit()