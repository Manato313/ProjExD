import pygame as pg
import sys
from random import randint

from sympy import public

def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():

    i = 0

    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400


    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_sfc2 = pg.Surface((50, 50))
    bomb_sfc2.set_colorkey((0, 255, 0))
    pg.draw.circle(bomb_sfc2, (0, 255, 0), (20, 20), 20)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct2 = bomb_sfc2.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)
    bomb_rct2 = bomb_sfc.get_rect()
    bomb_rct2.centerx = randint(0, scrn_rct.width)
    bomb_rct2.centery = randint(0, scrn_rct.height)

    vx, vy = +3, +3
    vx2, vy2 = +2, +2


    clock = pg.time.Clock()
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
        scrn_sfc.blit(bg_sfc, bg_rct)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:    tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:  tori_rct.centery += 1
        if key_states[pg.K_LEFT]:  tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 1
        #Space押されたら加速
        if key_states[pg.K_UP] and key_states [pg.K_SPACE]:    tori_rct.centery -= 5
        if key_states[pg.K_DOWN] and key_states [pg.K_SPACE]:  tori_rct.centery += 5
        if key_states[pg.K_LEFT] and key_states [pg.K_SPACE]:  tori_rct.centerx -= 5
        if key_states[pg.K_RIGHT] and key_states [pg.K_SPACE]: tori_rct.centerx += 5
        
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]: 
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
            if key_states[pg.K_LEFT] and key_states [pg.K_SPACE]: 
                tori_rct.centerx += 5
            if key_states[pg.K_RIGHT] and key_states [pg.K_SPACE]:
                tori_rct.centerx -= 5
        if tate == -1:
            if key_states[pg.K_UP]: 
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_states[pg.K_UP] and key_states [pg.K_SPACE]: 
                tori_rct.centery += 5
            if key_states[pg.K_DOWN] and key_states [pg.K_SPACE]:
                tori_rct.centery -= 5         
        scrn_sfc.blit(tori_sfc, tori_rct)
        scrn_sfc.blit(tori_sfc, tori_rct)

        yoko, tate = check_bound(bomb_rct, scrn_rct)
        yoko2, tate2 = check_bound(bomb_rct2, scrn_rct)
        vx *= yoko
        vy *= tate
        vx2 *= yoko2
        vy2 *= tate2
        bomb_rct.move_ip(vx, vy)
        bomb_rct2.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        scrn_sfc.blit(bomb_sfc, bomb_rct2)

        if tori_rct.colliderect(bomb_rct) or tori_rct.colliderect(bomb_rct2):
            return

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()