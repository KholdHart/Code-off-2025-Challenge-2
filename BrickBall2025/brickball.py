import pygame, sys, random, os
pygame.init()
W,H=480,640; screen=pygame.display.set_mode((W,H))
clock=pygame.time.Clock(); font=pygame.font.SysFont("arial",24,bold=True)
WHITE,BLACK=(255,255,255),(0,0,0)

def save_score(score,high):
    open("high_score.txt","w").write(str(max(score,high)))

def game_screen(msg,score,high):
    save_score(score,high)
    while True:
        screen.fill(BLACK)
        title=font.render(msg,1,WHITE)
        stats=font.render(f"Score:{score} High:{max(score,high)}",1,WHITE)
        prompt=font.render("Press R to Restart or Q to Quit",1,WHITE)
        screen.blit(title,(W//2-title.get_width()//2,H//2-50))
        screen.blit(stats,(W//2-stats.get_width()//2,H//2))
        screen.blit(prompt,(W//2-prompt.get_width()//2,H//2+50))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); sys.exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_q: pygame.quit(); sys.exit()
                if e.key==pygame.K_r: main()

def main():
    lives,score,particles=9,0,[]
    powerups=[]; high=0
    if os.path.exists("high_score.txt"): high=int(open("high_score.txt").read())
    paddle=pygame.Rect(W//2-35,H-30,70,12); paddle_speed=7
    balls=[pygame.Rect(W//2-9,H//2,18,18)]; speeds=[[4,-4]]
    colors=[(200,200,200),(180,180,180),(150,150,150),(100,100,100)]
    bricks=[[pygame.Rect(c*58+20,r*26+60,54,22),colors[(r+c)%4],(r%3)+1]
            for r in range(6) for c in range(8) if random.random()>.2]
    stars=[[random.randint(0,W),random.randint(0,H),random.randint(1,3)] for _ in range(60)]
    def spawn_powerup(x,y): powerups.append([pygame.Rect(x,y,20,20),
        random.choice(["life","expand","shrink","multi","slow"])])
    while True:
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); sys.exit()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left>0: paddle.move_ip(-paddle_speed,0)
        if keys[pygame.K_RIGHT] and paddle.right<W: paddle.move_ip(paddle_speed,0)
        for s in stars: s[1]+=s[2]
        [stars.remove(s) or stars.append([random.randint(0,W),0,s[2]]) for s in stars if s[1]>H]
        for i,b in enumerate(balls[:]):
            b.move_ip(speeds[i])
            if b.left<=0 or b.right>=W: speeds[i][0]*=-1
            if b.top<=0: speeds[i][1]*=-1
            if b.colliderect(paddle):
                speeds[i][1]=-abs(speeds[i][1])
                speeds[i][0]+=((b.centerx-paddle.centerx)/(paddle.width//2))*2
            hit=b.collidelist([br[0] for br in bricks])
            if hit!=-1:
                rect,col,hp=bricks[hit]; speeds[i][1]*=-1; score+=10; bricks[hit][2]-=1
                if bricks[hit][2]<=0:
                    bricks.pop(hit); 
                    if random.random()<.08: spawn_powerup(rect.x,rect.y)
                else: bricks[hit][1]=(220,220,220)
                for _ in range(12): particles.append([rect.center,
                    [random.uniform(-2,2),random.uniform(-2,1)],WHITE,30])
                speeds[i][0]*=1.05; speeds[i][1]*=1.05
            if b.bottom>=H:
                lives-=1; balls.remove(b); speeds.pop(i)
                if not balls:
                    if lives<=0: game_screen("GAME OVER",score,high)
                    balls=[pygame.Rect(W//2-9,H//2,18,18)]; speeds=[[random.choice([-4,4]),-4]]
        for p in powerups[:]:
            p[0].move_ip(0,3)
            if p[0].colliderect(paddle):
                if p[1]=="life": lives+=1
                if p[1]=="expand": paddle.width=min(150,paddle.width+20)
                if p[1]=="shrink": paddle.width=max(40,paddle.width-20)
                if p[1]=="multi" and balls:
                    balls.append(pygame.Rect(balls[0])); speeds.append([-speeds[0][0],speeds[0][1]])
                if p[1]=="slow": speeds=[[v[0]*0.8,v[1]*0.8] for v in speeds]
                powerups.remove(p)
        for pa in particles[:]:
            pa[0]=(pa[0][0]+pa[1][0],pa[0][1]+pa[1][1]); pa[3]-=1
            if pa[3]<=0: particles.remove(pa)
        if not bricks: game_screen("YOU WIN!",score,high)
        screen.fill(BLACK)
        for s in stars: pygame.draw.circle(screen,WHITE,(s[0],s[1]),1)
        pygame.draw.rect(screen,WHITE,paddle,border_radius=3)
        for b in balls: pygame.draw.ellipse(screen,WHITE,b)
        for br,col,hp in bricks: pygame.draw.rect(screen,col,br,border_radius=3)
        for p in powerups: pygame.draw.rect(screen,WHITE,p[0],border_radius=3)
        for pa in particles: pygame.draw.circle(screen,pa[2],(int(pa[0][0]),int(pa[0][1])),2)
        hud=font.render(f"Score:{score} Lives:{lives} High:{max(score,high)}",1,WHITE)
        screen.blit(hud,(10,10)); pygame.display.flip(); clock.tick(60)

if __name__=="__main__": main()
