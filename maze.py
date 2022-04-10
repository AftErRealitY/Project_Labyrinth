from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed ):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(100,100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <=500:
            self.direction = 'right'
        if self.rect.x >=600:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 700:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
font.init()
font = font.SysFont('Arial',36)
win = font.render("YOU WON!", True, (255,215,0))
lose = font.render("YOU LOSE!", True, (255,0,0))
win_height = 700
win_width = 500
window = display.set_mode((win_height,win_width))
display.set_caption("ERROR?")
background = transform.scale(image.load("background.jpg"),(700,500))
payer = Player('hero.png', 5, win_height - 390, 5)
oof = Enemy('cyborg.png', win_width - 80, 280, 1)
respect = GameSprite('treasure.png', win_width - 240, win_height - 700, 0)
w1 = Wall(153, 134, 253, 10,0, 100,50) 
w2 = Wall (153, 134, 253, 100,1, 100,300)
w3 = Wall (153, 134, 253, 150,100, 90,280)
w4 = Wall(153, 134, 253, 200,140, 80,220)
w5 = Wall(153, 134, 253, 280,112, 300,100)
w6 = Wall(153, 134, 253, 560,190, 20,200)
w7 = Wall(153, 134, 253, 380,320, 20,200)
w8 = Wall(153, 134, 253, 280,112, 200,111)
w9 = Wall(153, 134, 253, 280,112, 100,30)
game = True
finish = False
clock = time.Clock()
fps = 60
mixer.init()
mixer.music.load('jungles.ogg')
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
mixer.music.play()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        payer.update()
        oof.update()
        payer.reset()
        oof.reset()
        respect.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        if sprite.collide_rect(payer, respect):
            finish = True
            window.blit(win, (200, 200))
            money.play()
        if sprite.collide_rect(payer, oof) or sprite.collide_rect(payer, w1) or sprite.collide_rect(payer, w2) or sprite.collide_rect(payer, w3) or sprite.collide_rect(payer, w4):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
    clock.tick(fps)
    display.update()
    #end

