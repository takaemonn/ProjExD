import pygame as pg
import sys
from random import randint


class screen():
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #"test"
        self.sfc = pg.display.set_mode(wh) #(600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) 
        self.bgi_rct = self.bgi_sfc.get_rect()

    def  blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

    

class chara():
    key_delta = {
        pg.K_q:[-1, 0],
        pg.K_w :[+1, 0],
        pg.K_SPACE:[0, -2]
    }

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct= self.sfc.get_rect()
        self.rct.center = xy #300, 900

    def blit(self, scr:screen):
        scr.sfc.blit(self.sfc,self.rct )

    def update(self, scr:screen):
        chara_g = 0
        chara_g += 1
        self.rct.move_ip(0, chara_g)
        key_states = pg.key.get_pressed()
        for key, delta in chara.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr)


class floor():
    def __init__(self, color, side, vx, scr:screen):
        self.sfc = pg.Surface((500, 10)) 
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.rect(self.sfc, (255, 0, 0),(0,880,500, 10), 5) # 足場用の長方形を描く
        self.rct = self.sfc.get_rect()
        self.vx= vx

    def blit(self, scr:screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr:screen):
        self.rct.move_ip(self.vx, self.vy) 
        yoko= check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.blit(scr)


class enemy():
    def __init__(self, color, radius, vxy, scr:screen):
        self.sfc = pg.Surface((radius*2, radius*2)) 
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (radius, radius), radius)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy 

    def blit(self, scr:screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr:screen):
        self.rct.move_ip(self.vx, self.vy) 
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1 
    return yoko, tate


def main():
    scr = screen("test", (600, 900), "fig/pg_bg.jpg")
    cha = chara("fig/chara.png", 0.15, (300, 50))
    enm = enemy((255, 0, 0), 10, (+1, +1), scr)

    clock = pg.time.Clock()
    while True:
        scr.blit()
        
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return

        cha.update(scr)
        enm.update(scr)
        
        if cha.rct.colliderect(enm .rct): 
           return

        pg.display.update() 
        clock.tick(1000)

if __name__=="__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit #初期化の解除
    sys.exit() #プログラムの終了