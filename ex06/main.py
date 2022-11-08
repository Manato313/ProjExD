from random import randint
import os
import sys
import time
import pygame as pg


class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class rdy_fight():
    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) 
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self):
        self.sfc.blit(self.sfc, self.rct)


#class Mode:
#    def __init__(self,level):
#        self.level = level
#
#    def title(): # level変更機能
#        pg.init() 
#        pg.display
#        screen.fill
#        level = 1
#        while(True):
#            key_states = pg.key.get_pressed()
#            if key_states[pg.K_UP]: level += 1
#            if level == 6: level = 5
#            if key_states[pg.K_DOWN]: level -= 1
#            if level == 0: level = 1
#            
#            if key_states[pg.K_SPACE]:
#                return level




def main():

    scr = Screen("刹那test", (1200, 800), "fig/pg_bg.jpg")
    #fight = rdy_fight("fig/6.png", 2.0, (600, 300))
    diley_frame = randint(2500,5000)# ms 2.5秒～5.0秒
    clock = pg.time.Clock()
    flag = 0
    while True:
        scr.blit() # 背景表示
        #print (pg.time.get_ticks()) #デバッグ用
        #if pg.time.get_ticks() >= diley_frame:
        #    fight.blit()
        #    flag = 1 #フラグ1にする
        #    img1 = pg.image.load("fig/5.png")
            #Screen.blit(img1)
        key_states = pg.key.get_pressed()
        #print(key_states[pg.K_SPACE])
        if key_states[pg.K_SPACE]:
            return
            if flag == 1:
                return
            if flag == 0:
                return
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return

        pg.display.update()
        clock.tick(1000)
        

        


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()