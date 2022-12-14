import pygame as pg
import sys
from random import randint
import os
import time

class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0]
    }

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) 
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                if key_states[pg.K_SPACE]:
                    self.rct.centerx += delta[0] * 3
                    self.rct.centery += delta[1] * 3
                else:
                    self.rct.centerx += delta[0]
                    self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Bomb:
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


main_dir = os.path.split(os.path.abspath(__file__))[0]


class Sound:
    def load_sound(file):
        if not pg.mixer:
            return None
        file = os.path.join(main_dir, "data", file)
        try:
            sound = pg.mixer.Sound(file)
            return sound
        except pg.error:
            print("Warning, unable to load, %s" % file)
        return None

def main():

    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    kkt = Bird("fig/6.png", 2.0, (900, 400))

    bkd1 = Bomb((255, 0, 0), 10, (+1, +1), scr)
    bkd2 = Bomb((0, 255, 0), 30, (+3, +3), scr)

    bgm = Sound.load_sound("bgm1.mp3")
    dath_sound = Sound.load_sound("miss!.mp3")

    clock = pg.time.Clock() 
    bgm.play()
    while True:
        scr.blit() 
        
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return

        kkt.update(scr)

        bkd1.update(scr)
        bkd2.update(scr)

        if kkt.rct.colliderect(bkd1.rct):
            pg.mixer.music.stop
            dath_sound.play()
            time.sleep(3)
            return

        if kkt.rct.colliderect(bkd2.rct):
            pg.mixer.music.stop
            dath_sound.play()
            time.sleep(3)
            return

        pg.display.update() 
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()