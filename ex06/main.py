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

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

def main():

    scr = Screen("刹那test", (1200, 800), "fig/pg_bg.jpg")
    fight = rdy_fight("fig/fight.png", 2.0, (600, 300))
    #kkt_w = rdy_fight("fig/9.png", 2.0, (600,300))
    #kkt_l = rdy_fight("fig/8.png", 2.0, (600,300))
    #kkt_u = rdy_fight("fig/7.png", 2.0, (600,300))
    cong_time = 0
    diley_frame = randint(2500,5000)# ms 2.5秒～5.0秒
    clock = pg.time.Clock()
    flag = 0
    scr.blit() # 背景表示
    while True:
        print (pg.time.get_ticks()) #デバッグ用
        if pg.time.get_ticks() >= diley_frame:
            if cong_time == 0:
                cong_time = pg.time.get_ticks()
            fight.blit(scr)
            CPU = cong_time + randint(270,300)
            flag = 1 #フラグ1にする
            if pg.time.get_ticks() >= CPU:
                push_time = pg.time.get_ticks()
                print(f"time:{push_time - cong_time}ms" )
                print("CPU WIN") # 敗北用
                #kkt_l.blit(scr)
                time.sleep(1)
                return
        key_states = pg.key.get_pressed()
        if key_states[pg.K_SPACE]:
            push_time = pg.time.get_ticks()
            if flag == 1:
                print(f"time:{push_time - cong_time}ms" ) # 推した瞬間の時間
                print("1P WIN") # 勝利用
                #kkt_w.blit(scr)
                time.sleep(1)
                return
            if flag == 0:
                print("1P おてつき!")
                #kkt_u.blit(scr)
                time.sleep(1)
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