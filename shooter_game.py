from pygame import *
from random import randint 
window = display.set_mode((700, 500))
background =transform.scale(image.load("galaxy.jpg"),(700, 500))
mixer.init() 
mixer.music.load('space.ogg')

mixer.music.play()

# monsters.add(monsters)
# monsters.update()
# monsters.draw(window)
monsters= sprite.Group()
# number = 0
# global number
# trir = GameSprite('treasure.png',500,400,600)
# phd = Enemy('cyborg.png',300,300,2)

bullets = sprite.Group()



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65, 65))
        self.speed=player_speed
        self.rect= self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))  
        

# trir = GameSprite('galaxy.jpg',500,400,600)


class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png",self.rect.centerx,self.rect.top,10)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y +=self.speed 
        if self.rect.y >700:
            self.rect.y = -50
            self.rect.x = randint(0,1000)
            self.speed = randint(2,5) 

class Bullet(GameSprite):
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y <0:
            self.kill()

for i in range(6):

    phd = Enemy('4.png',randint(0,1000),-30,randint(2,5))
    monsters.add(phd)


trip = Player('6.jpg',270,420,10) 
clock =time.Clock()
Finish= False
game= True
FPS =60
while game:
    if not Finish :
        window.blit(background,(0,0))
        trip.update()
        trip.reset()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)

        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        for g in sprites_list:
            phd = Enemy('4.png',randint(0,1000),-30,randint(2,5))
            monsters.add(phd)
    for e in event.get():
        if e.type== QUIT:
            game= False   
        if e.type==KEYDOWN:
            if e.key== K_SPACE:
                trip.fire()       

    clock.tick(FPS)
    display.update()
