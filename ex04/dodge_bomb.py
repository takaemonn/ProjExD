from turtle import right, width
import pygame as pg
import sys
from random import randint

bnd = 10    

def check_bound(obj_rct, scr_rct):
    """
cbj_rct:こうかとんrct or 爆弾rct
scr_rct:スクリーンrct
領域内:+1/領域外:-1
    """
    yoko, tate = 1, 1

    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def bomb_bound(bomb_rct, scr_rct):
    global bnd
    if bomb_rct.left < scr_rct.left or scr_rct.right < bomb_rct.right:
        bnd += 1
    if bomb_rct.top < scr_rct.top or scr_rct.bottom < bomb_rct.bottom:
        bnd += 1
    return bnd


def main():
    global bnd
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()

    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    clock = pg.time.Clock()


    tori_sfc = pg.image.load("fig/5.png") #surface
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect() #rect
    tori_rct.center = 900, 400
    
    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)

    #tmr = pg.time.get_ticks()
    #fonto = pg.font.Font(None, 100)
    #txt = fonto.render(str(tmr), True,"WHITE")

    vx, vy = 1.5, 1.5
    
    

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
    
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:
            tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_states[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx += 1


        if tori_rct.right > scrn_rct.width:
            tori_rct.right=scrn_rct.width
        if tori_rct.left < 0:
            tori_rct.left = 0
        if tori_rct.top < 0:
            tori_rct.top = 0
        if tori_rct.bottom > scrn_rct.bottom:
            tori_rct.bottom = scrn_rct.bottom

        scrn_sfc.blit(tori_sfc, tori_rct)

        yoko, tate = check_bound(bomb_rct, scrn_rct)
        bnd = bomb_bound(bomb_rct, scrn_rct)
        if bnd%10 == 0 and bnd<=50:
            vx = vx*yoko*1.0005
            vy = vy*tate*1.0005
        else:
            vx *= yoko
            vy *= tate

        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)

        #scrn_sfc.blit(txt, (300, 200))
        
        if tori_rct.colliderect(bomb_rct):
           return

        pg.display.update()
        clock.tick(1000)



if __name__=="__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit #初期化の解除
    sys.exit() #プログラムの終了