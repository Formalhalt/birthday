import pygame
import sys
import random

# Date of project start: july 21st
# Date of finish:   september 30th

# Hello saarah, let me start off by wishing you a happy happy birthday and many more to come.
# I wish for you to have a fruitful life ahead of you and I hope every day of yours is one to remember
# I hope you over come any challenge or adversary that presents itself to you, I know you are capable of doing so as you are
# strong, sweet and most of all very cool111111111

# Now, this is long overdue, I'm not sure how long but probably a few years now I've promised to make you a game.
# Perhaps in the future I'll be able to make you something even cooler11111111111111111111
# (Exclamation key doesn't work I don't know why)




pygame.init()
res = (1000, 600)
pygame.display.set_caption("Happy Birthday Saarah")
screen = pygame.display.set_mode(res)
worldbg = pygame.image.load("worldbg.png").convert_alpha()
clock = pygame.time.Clock()

programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)


rOl = 4
borderimg = pygame.image.load('border.png')

go = pygame.image.load("go.png")
go = pygame.transform.scale(go, (1000, 600))
startimg = pygame.image.load("startc.png")
startimg = pygame.transform.scale(startimg, (1000, 600))
gw = pygame.image.load("game won.png")
gppic = pygame.image.load("grouppic.png")
catsign = pygame.image.load("CATSIGN.png")
catsign = pygame.transform.scale(catsign, (250, 250))
glassesimg = pygame.image.load("glasses.png")
glassesimg = pygame.transform.scale(glassesimg, (50, 50))

s1 = pygame.image.load("s1.png")
s1 = pygame.transform.scale(s1, (80, 80))
s2 = pygame.image.load("s2.png")
s2 = pygame.transform.scale(s2, (80, 80))
s3 = pygame.image.load("s3.png")
s3 = pygame.transform.scale(s3, (80, 80))

# charges

c0 = pygame.image.load("nocharm.png")
c1 = pygame.image.load("1charm.png")
c2 = pygame.image.load("2charm.png")
c3 = pygame.image.load("3charm.png")
c4 = pygame.image.load("4charm.png")
c5 = pygame.image.load("5charm.png")

# hp bar

hp0 = pygame.image.load("0.png")
hp10 = pygame.image.load("10hp.png")
hp20 = pygame.image.load("20hp.png")
hp30 = pygame.image.load("30hp.png")
hp40 = pygame.image.load("40hp.png")
hp50 = pygame.image.load("50hp.png")
hp60 = pygame.image.load("60hp.png")
hp70 = pygame.image.load("70hp.png")
hp80 = pygame.image.load("80hp.png")
hp90 = pygame.image.load("90hp.png")
hp100 = pygame.image.load("100.png")
goldenhp = pygame.image.load("goldenhp.png")

class Cheetosr2(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 1000
        self.y = 400
        self.x_speed = -4
        self.y_speed = 2
        self.x_direction = -4
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("rch2.png"))
        self.sprites.append(pygame.image.load("rch2.png"))
        self.sprites.append(pygame.image.load("rch2.png"))
        self.sprites.append(pygame.image.load("rch2.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x > 1000:
            self.x_direction = -6
            self.x_direction = -2

        self.x_speed = random.randint(8, 12) * self.x_direction
        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y

class Cheetosr1(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 1000
        self.y = 200
        self.x_speed = -4
        self.y_speed = 2
        self.x_direction = -4
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("rch1.png"))
        self.sprites.append(pygame.image.load("rch1.png"))
        self.sprites.append(pygame.image.load("rch1.png"))
        self.sprites.append(pygame.image.load("rch1.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x > 1000:
            self.x_direction = -6
            self.x_direction = -2

        self.x_speed = random.randint(8, 12) * self.x_direction
        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y



class Cheetosl3(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 500
        self.x_speed = 4
        self.y_speed = 2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("lch3.png"))
        self.sprites.append(pygame.image.load("lch3.png"))
        self.sprites.append(pygame.image.load("lch3.png"))
        self.sprites.append(pygame.image.load("lch3.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x < 1000:
            self.x_direction = 6
            self.x_direction = 2

        self.x_speed = random.randint(8, 12) * self.x_direction
        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y

class Cheetosl2(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 300
        self.x_speed = 4
        self.y_speed = 2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("lch2.png"))
        self.sprites.append(pygame.image.load("lch2.png"))
        self.sprites.append(pygame.image.load("lch2.png"))
        self.sprites.append(pygame.image.load("lch2.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x < 1000:
            self.x_direction = 6
            self.x_direction = 2

        self.x_speed = random.randint(8, 12) * self.x_direction
        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y


class Cheetosl1(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 100
        self.x_speed = 4
        self.y_speed = 2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("lch1.png"))
        self.sprites.append(pygame.image.load("lch1.png"))
        self.sprites.append(pygame.image.load("lch1.png"))
        self.sprites.append(pygame.image.load("lch1.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x < 1000:
            self.x_direction = 6
            self.x_direction = 2

        self.x_speed = random.randint(8, 12) * self.x_direction
        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y



class Right4(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury4.rect.x
        self.y = Shury4.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("right.png"))
        self.sprites.append(pygame.image.load("right.png"))
        self.sprites.append(pygame.image.load("right.png"))
        self.sprites.append(pygame.image.load("right.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x < 1000:
            self.x_direction = 6
            self.x_direction = 2

        self.x_speed = random.randint(5, 8) * self.x_direction
        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y




class Left4(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury4.rect.x
        self.y = Shury4.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = -1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("left.png"))
        self.sprites.append(pygame.image.load("left.png"))
        self.sprites.append(pygame.image.load("left.png"))
        self.sprites.append(pygame.image.load("left.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x > 1000:
            self.x_direction = -6
            self.x_direction = -2

        self.x_speed = random.randint(5, 8) * self.x_direction
        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y


########## COPY LEFT3 AND UP3 THEY ARE CORRECT VERSION OF WHAT IS NEEDED #####################

class Down4(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury4.rect.x
        self.y = Shury4.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("down.png"))
        self.sprites.append(pygame.image.load("down.png"))
        self.sprites.append(pygame.image.load("down.png"))
        self.sprites.append(pygame.image.load("down.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


        if self.y > 600:
            self.y_direction = -6
            self.y_direction = -2


        self.y_speed = random.randint(5, 8)

        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y




class Up4(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury4.rect.x
        self.y = Shury4.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.y_direction = -1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("up.png"))
        self.sprites.append(pygame.image.load("up.png"))
        self.sprites.append(pygame.image.load("up.png"))
        self.sprites.append(pygame.image.load("up.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


        if self.y < 600:
            self.y_direction = -6
            self.y_direction = -2

        self.y_speed = random.randint(5, 8) * self.y_direction
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

class Right3(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury3.rect.x
        self.y = Shury3.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("right.png"))
        self.sprites.append(pygame.image.load("right.png"))
        self.sprites.append(pygame.image.load("right.png"))
        self.sprites.append(pygame.image.load("right.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x < 1000:
            self.x_direction = 6
            self.x_direction = 2

        self.x_speed = random.randint(5, 8) * self.x_direction
        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y




class Left3(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury3.rect.x
        self.y = Shury3.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = -1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("left.png"))
        self.sprites.append(pygame.image.load("left.png"))
        self.sprites.append(pygame.image.load("left.png"))
        self.sprites.append(pygame.image.load("left.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x > 1000:
            self.x_direction = -6
            self.x_direction = -2

        self.x_speed = random.randint(5, 8) * self.x_direction
        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y


########## COPY LEFT3 AND UP3 THEY ARE CORRECT VERSION OF WHAT IS NEEDED #####################

class Down3(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury3.rect.x
        self.y = Shury3.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("down.png"))
        self.sprites.append(pygame.image.load("down.png"))
        self.sprites.append(pygame.image.load("down.png"))
        self.sprites.append(pygame.image.load("down.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


        if self.y > 600:
            self.y_direction = -6
            self.y_direction = -2


        self.y_speed = random.randint(5, 8)

        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y




class Up3(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury3.rect.x
        self.y = Shury3.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.y_direction = -1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("up.png"))
        self.sprites.append(pygame.image.load("up.png"))
        self.sprites.append(pygame.image.load("up.png"))
        self.sprites.append(pygame.image.load("up.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


        if self.y < 600:
            self.y_direction = -6
            self.y_direction = -2

        self.y_speed = random.randint(5, 8) * self.y_direction
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y


class Right2(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury2.rect.x
        self.y = Shury2.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("right.png"))
        self.sprites.append(pygame.image.load("right.png"))
        self.sprites.append(pygame.image.load("right.png"))
        self.sprites.append(pygame.image.load("right.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x < 1000:
            self.x_direction = 6
            self.x_direction = 2

        self.x_speed = random.randint(5, 8)

        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y




class Left2(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury2.rect.x
        self.y = Shury2.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = -1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("left.png"))
        self.sprites.append(pygame.image.load("left.png"))
        self.sprites.append(pygame.image.load("left.png"))
        self.sprites.append(pygame.image.load("left.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x > 1000:
            self.x_direction = -6
            self.x_direction = -2

        self.x_speed = random.randint(5, 8) * self.x_direction
        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y



class Down2(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury2.rect.x
        self.y = Shury2.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("down.png"))
        self.sprites.append(pygame.image.load("down.png"))
        self.sprites.append(pygame.image.load("down.png"))
        self.sprites.append(pygame.image.load("down.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


        if self.y > 600:
            self.y_direction = -6
            self.y_direction = -2


        self.y_speed = random.randint(5, 8)

        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y




class Up2(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury2.rect.x
        self.y = Shury2.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("up.png"))
        self.sprites.append(pygame.image.load("up.png"))
        self.sprites.append(pygame.image.load("up.png"))
        self.sprites.append(pygame.image.load("up.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


        if self.y < 600:
            self.y_direction = -6
            self.y_direction = -2

        self.y_speed = random.randint(5, 8) * self.y_direction
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y


# WORK ON CBULLET USE THIS CLASS FOR ALL SHURIKENS
class Right1(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury1.rect.x
        self.y = Shury1.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("right.png"))
        self.sprites.append(pygame.image.load("right.png"))
        self.sprites.append(pygame.image.load("right.png"))
        self.sprites.append(pygame.image.load("right.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x < 1000:
            self.x_direction = 6
            self.x_direction = 2

        self.x_speed = random.randint(5, 8)

        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y




class Left1(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury1.rect.x
        self.y = Shury1.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = -1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("left.png"))
        self.sprites.append(pygame.image.load("left.png"))
        self.sprites.append(pygame.image.load("left.png"))
        self.sprites.append(pygame.image.load("left.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x > 1000:
            self.x_direction = -6
            self.x_direction = -2

        self.x_speed = random.randint(5, 8) * self.x_direction
        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y




class Down1(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury1.rect.x
        self.y = Shury1.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("down.png"))
        self.sprites.append(pygame.image.load("down.png"))
        self.sprites.append(pygame.image.load("down.png"))
        self.sprites.append(pygame.image.load("down.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


        if self.y > 600:
            self.y_direction = -6
            self.y_direction = -2


        self.y_speed = random.randint(5, 8)

        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

# MAKE IF THEY HIT BORDER TP BACK TO FLOWER CENTER


class Up1(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = Shury1.rect.x
        self.y = Shury1.rect.y
        self.x_speed = 2
        self.y_speed = 2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("up.png"))
        self.sprites.append(pygame.image.load("up.png"))
        self.sprites.append(pygame.image.load("up.png"))
        self.sprites.append(pygame.image.load("up.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


        if self.y < 600:
            self.y_direction = -6
            self.y_direction = -2

        self.y_speed = random.randint(5, 8) * self.y_direction
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y


class Shuriken4(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("cheetoshur1.png"))
        self.sprites.append(pygame.image.load("cheetoshur2.png"))
        self.sprites.append(pygame.image.load("cheetoshur3.png"))
        self.sprites.append(pygame.image.load("cheetoshur4.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.8
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())


class Shuriken3(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("cheetoshur1.png"))
        self.sprites.append(pygame.image.load("cheetoshur2.png"))
        self.sprites.append(pygame.image.load("cheetoshur3.png"))
        self.sprites.append(pygame.image.load("cheetoshur4.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.8
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())


class Shuriken2(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("cheetoshur1.png"))
        self.sprites.append(pygame.image.load("cheetoshur2.png"))
        self.sprites.append(pygame.image.load("cheetoshur3.png"))
        self.sprites.append(pygame.image.load("cheetoshur4.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.8
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())


class Shuriken1(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("cheetoshur1.png"))
        self.sprites.append(pygame.image.load("cheetoshur2.png"))
        self.sprites.append(pygame.image.load("cheetoshur3.png"))
        self.sprites.append(pygame.image.load("cheetoshur4.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.8
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())




class Boss9(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("f1.png"))
        self.sprites.append(pygame.image.load("f2.png"))
        self.sprites.append(pygame.image.load("f3.png"))
        self.sprites.append(pygame.image.load("f4.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.8
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]



class Boss8(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("l71.png"))
        self.sprites.append(pygame.image.load("l72.png"))
        self.sprites.append(pygame.image.load("l73.png"))
        self.sprites.append(pygame.image.load("l74.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.8
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]



class Boss7(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("l61.png"))
        self.sprites.append(pygame.image.load("l62.png"))
        self.sprites.append(pygame.image.load("l63.png"))
        self.sprites.append(pygame.image.load("l64.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.8
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


class Boss6(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("l51.png"))
        self.sprites.append(pygame.image.load("l52.png"))
        self.sprites.append(pygame.image.load("l53.png"))
        self.sprites.append(pygame.image.load("l54.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.8
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


class Boss5(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("l41.png"))
        self.sprites.append(pygame.image.load("l42.png"))
        self.sprites.append(pygame.image.load("l43.png"))
        self.sprites.append(pygame.image.load("l44.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.8
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


class Boss4(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("l31.png"))
        self.sprites.append(pygame.image.load("l32.png"))
        self.sprites.append(pygame.image.load("l33.png"))
        self.sprites.append(pygame.image.load("l34.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.8
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

class Boss3(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("l21.png"))
        self.sprites.append(pygame.image.load("l22.png"))
        self.sprites.append(pygame.image.load("l23.png"))
        self.sprites.append(pygame.image.load("l24.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.8
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

class Boss2(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("l11.png"))
        self.sprites.append(pygame.image.load("l12.png"))
        self.sprites.append(pygame.image.load("l13.png"))
        self.sprites.append(pygame.image.load("l14.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.8
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

class Boss1(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("stonecold1.png"))
        self.sprites.append(pygame.image.load("stonecold2.png"))
        self.sprites.append(pygame.image.load("stonecold3.png"))
        self.sprites.append(pygame.image.load("stonecold4.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.8
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

class Cage(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("cage.png"))
        self.sprites.append(pygame.image.load("cage.png"))
        self.sprites.append(pygame.image.load("cage.png"))
        self.sprites.append(pygame.image.load("cage.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]



class Hell(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("hellbg.png"))
        self.sprites.append(pygame.image.load("hellbg.png"))
        self.sprites.append(pygame.image.load("hellbg.png"))
        self.sprites.append(pygame.image.load("hellbg.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())


class Vegeb3(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("tb3.png"))

        self.sprites.append(pygame.image.load("exp1.png"))
        self.sprites.append(pygame.image.load("exp2.png"))
        self.sprites.append(pygame.image.load("exp3.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())


class Vegeb2(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("tb2.png"))

        self.sprites.append(pygame.image.load("exp1.png"))
        self.sprites.append(pygame.image.load("exp2.png"))
        self.sprites.append(pygame.image.load("exp3.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())


class Vegeb1(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("tb1.png"))

        self.sprites.append(pygame.image.load("exp1.png"))
        self.sprites.append(pygame.image.load("exp2.png"))
        self.sprites.append(pygame.image.load("exp3.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())


class Vegebombtrigger3(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("v3t.png"))

        self.sprites.append(pygame.image.load("vr1.png"))
        self.sprites.append(pygame.image.load("vr2.png"))
        self.sprites.append(pygame.image.load("vr3.png"))
        self.sprites.append(pygame.image.load("vr4.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())




class Vegebombtrigger1(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("v1t.png"))
        self.sprites.append(pygame.image.load("vr1.png"))
        self.sprites.append(pygame.image.load("vr2.png"))
        self.sprites.append(pygame.image.load("vr3.png"))
        self.sprites.append(pygame.image.load("vr4.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())


class Vegebombtrigger2(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("v2t.png"))

        self.sprites.append(pygame.image.load("vr1.png"))
        self.sprites.append(pygame.image.load("vr2.png"))
        self.sprites.append(pygame.image.load("vr3.png"))
        self.sprites.append(pygame.image.load("vr4.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        self.rect.clamp_ip(screen.get_rect())



class Egg(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = leaf.rect.x
        self.y = leaf.rect.y
        self.x_speed = 0.2
        self.y_speed = 0.2
        self.x_direction = 1
        self.y_direction = 1
        self.egg_list = []
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("egg.png"))
        self.sprites.append(pygame.image.load("egg.png"))
        self.sprites.append(pygame.image.load("egg.png"))
        self.sprites.append(pygame.image.load("egg.png"))



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x < player.rect.x + 40:
            self.x_direction = 6
            self.x_direction = 2
        elif self.x > player.rect.x + 40:
            self.x_direction = -6
            self.x_direction = -2

        if self.y > player.rect.y + 40:
            self.y_direction = -6
            self.y_direction = -2

        elif self.y < player.rect.y + 40:
            self.y_direction = 6
            self.y_direction = 2

        self.x_speed = random.randint(1, 2) * self.x_direction
        self.y_speed = random.randint(1, 2) * self.y_direction

        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y



        self.rect.clamp_ip(screen.get_rect())



class Ladybug(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(1, 1000)
        self.y = random.randint(1, 600)
        self.x_speed = 0.2
        self.y_speed = 0.2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("lb0.png"))
        self.sprites.append(pygame.image.load("lb1.png"))
        self.sprites.append(pygame.image.load("lb0.png"))
        self.sprites.append(pygame.image.load("lb1.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        if self.x < leaf.rect.x:
            self.x_direction = 2
            self.x_direction = 1
            self.image = pygame.transform.rotate(self.image, 360)
        elif self.x > leaf.rect.x:
            self.x_direction = -2
            self.x_direction = -1
            self.image = pygame.transform.rotate(self.image, 90)

        if self.y > leaf.rect.y:
            self.y_direction = -2
            self.y_direction = -1
            self.image = pygame.transform.rotate(self.image, 0)

        elif self.y < leaf.rect.y:
            self.image = pygame.transform.rotate(self.image, -180)
            self.y_direction = 2
            self.y_direction = 1





        self.x_speed = random.randint(0, 3) * self.x_direction
        self.y_speed = random.randint(0, 3) * self.y_direction

        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y


        self.rect.clamp_ip(screen.get_rect())


class Leaf(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("leaf1.png"))
        self.sprites.append(pygame.image.load("leaf2.png"))
        self.sprites.append(pygame.image.load("leaf3.png"))
        self.sprites.append(pygame.image.load("leaf4.png"))
        self.sprites.append(pygame.image.load("leaf5.png"))
        self.sprites.append(pygame.image.load("leaf5.png"))
        self.sprites.append(pygame.image.load("leaf4.png"))
        self.sprites.append(pygame.image.load("leaf3.png"))
        self.sprites.append(pygame.image.load("leaf2.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())


class Start(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(startimg)

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())


class Bingolady(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("bingo1.png"))
        self.sprites.append(pygame.image.load("bingo2.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())


class Gameover(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(go)

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())


class Border(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []

        self.sprites.append(borderimg)

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.clamp_ip(screen.get_rect())


class Truffles(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(1, 1000)
        self.y = random.randint(1, 600)
        self.x_speed = 0.2
        self.y_speed = 0.2
        self.x_direction = 1
        self.y_direction = 1
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("tru1.png"))
        self.sprites.append(pygame.image.load("tru2.png"))
        self.sprites.append(pygame.image.load("tru3.png"))
        self.sprites.append(pygame.image.load("tru4.png"))
        self.sprites.append(pygame.image.load("tru5.png"))
        self.sprites.append(pygame.image.load("tru4.png"))
        self.sprites.append(pygame.image.load("tru3.png"))
        self.sprites.append(pygame.image.load("tru2.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())

        if self.x <= 10:
            self.x_direction = 10
            self.x_direction = random.choice([-1, 1])
        elif self.x >= 980:
            self.x_direction = -10
            self.x_direction = random.choice([-1, 1])

        if self.y >= 600:
            self.y_direction = -10
            self.y_direction = random.choice([-1, 1])

        elif self.y <= 10:
            self.y_direction = 10
            self.y_direction = random.choice([-1, 1])

        self.x_speed = random.randint(0, 8) * self.x_direction
        self.y_speed = random.randint(0, 8) * self.y_direction
        if self.x_speed == 0 and self.y_speed == 0:
            self.x_speed = random.randint(0, 3) * self.x_direction
            self.y_speed = random.randint(0, 3) * self.y_direction

        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

        self.rect.clamp_ip(screen.get_rect())


class Glasses(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(glassesimg)

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.rect.clamp_ip(screen.get_rect())


class Meow(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("meow1.png"))
        self.sprites.append(pygame.image.load("meow2.png"))
        self.sprites.append(pygame.image.load("meow3.png"))
        self.sprites.append(pygame.image.load("meow4.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.20
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


class Vodka(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("vb1.png"))
        self.sprites.append(pygame.image.load("vb2.png"))
        self.sprites.append(pygame.image.load("vb3.png"))
        self.sprites.append(pygame.image.load("vb4.png"))
        self.sprites.append(pygame.image.load("vb5.png"))
        self.sprites.append(pygame.image.load("vb6.png"))
        self.sprites.append(pygame.image.load("vb7.png"))
        self.sprites.append(pygame.image.load("vb8.png"))
        self.sprites.append(pygame.image.load("vb9.png"))
        self.sprites.append(pygame.image.load("vb10.png"))
        self.sprites.append(pygame.image.load("vb11.png"))
        self.sprites.append(pygame.image.load("vb12.png"))
        self.sprites.append(pygame.image.load("vb13.png"))
        self.sprites.append(pygame.image.load("vb14.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.5
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        self.rect.clamp_ip(screen.get_rect())


class Soulmate(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("cat1.png"))
        self.sprites.append(pygame.image.load("cat2.png"))
        self.sprites.append(pygame.image.load("cat3.png"))
        self.sprites.append(pygame.image.load("cat2.png"))


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def animate(self):
        self.is_animating = True

    def control(self, x, y):
        self.x += x
        self.y += y

    def up(self, y):
        self.y += y

    def down(self, y):
        self.y -= y

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        self.rect.x = self.rect.x + self.x
        self.rect.y = self.rect.y + self.y

        if self.x < 0:
            self.frame += 1
            if self.frame > 3 * rOl:
                self.frame = 0
            self.image = self.sprites[self.frame // rOl]
            self.image = pygame.transform.flip(self.sprites[self.frame // rOl], True, False)

        if self.x > 0:
            self.frame += 1
            if self.frame > 3 * rOl:
                self.frame = 0
            self.image = self.sprites[self.frame // rOl]

        self.rect.clamp_ip(screen.get_rect())


class Grumpy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(pygame.image.load("sp1.png"))
        self.sprites.append(pygame.image.load("sp2.png"))
        self.sprites.append(pygame.image.load("sp3.png"))
        self.sprites.append(pygame.image.load("sp4.png"))
        self.sprites.append(pygame.image.load("sp5.png"))
        self.sprites.append(pygame.image.load("sp6.png"))
        self.sprites.append(pygame.image.load("sp7.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def animate(self):
        self.is_animating = True

    def control(self, x, y):
        self.x += x
        self.y += y



    def up(self, y):
        self.y += y

    def down(self, y):
        self.y -= y

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        self.rect.x = self.rect.x + self.x
        self.rect.y = self.rect.y + self.y

        if self.x < 0:
            self.frame += 1
            if self.frame > 3 * rOl:
                self.frame = 0
            self.image = self.sprites[self.frame // rOl]
            self.image = pygame.transform.flip(self.sprites[self.frame // rOl], True, False)

        if self.x > 0:
            self.frame += 1
            if self.frame > 3 * rOl:
                self.frame = 0
            self.image = self.sprites[self.frame // rOl]

        self.rect.clamp_ip(screen.get_rect())


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.frame = 0
        super().__init__()
        self.sprites = []
        self.is_animating = False

        self.sprites.append(s1)
        self.sprites.append(s2)
        self.sprites.append(s3)
        self.sprites.append(s1)

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def animate(self):
        self.is_animating = True

    def control(self, x, y):
        self.x += x
        self.y += y

    def up(self, y):
        self.y += y

    def down(self, y):
        self.y -= y

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]

        self.rect.x = self.rect.x + self.x
        self.rect.y = self.rect.y + self.y

        if self.x < 0:
            self.frame += 1
            if self.frame > 3 * rOl:
                self.frame = 0
            self.image = self.sprites[self.frame // rOl]
            self.image = pygame.transform.flip(self.sprites[self.frame // rOl], True, False)

        if self.x > 0:
            self.frame += 1
            if self.frame > 3 * rOl:
                self.frame = 0
            self.image = self.sprites[self.frame // rOl]

        self.rect.clamp_ip(screen.get_rect())


score = 0
score_font = pygame.font.Font('back-to-1982.regular.ttf', 25)
scx = 460
scy = 5
def s_score(x, y):
    scorer = score_font.render(str(score), True, (64, 64, 64))
    screen.blit(scorer, (x, y))


boss1hp = 0
boss = 0
lvl6sr = 0
lvl5sr = 0
lvl4sr = 0
lvl3sr = 0
lvl2sr = 0
rspt = 0
playerhp = 100
healcharge = 0
hcx = 820
hcy = 30
hpx = 845
hpy = 5
cshot = False
allshalldie = False
rsptc = False
lvl6 = False
lvl4 = False
lvl3 = False
lvl2 = False
lvl5 = False
ch1 = False
ch2 = False
ch3 = False
ch4 = False
ch5 = False
ch6 = False
reshoot1 = False
reshoot2 = False
reshoot3 = False
reshoot4 = False
reshoot5 = False
reshoot6 = False
reshoot7 = False
reshoot8 = False
reshoot9 = False
reshoot10 = False
reshoot11 = False
reshoot12 = False
reshoot13 = False
reshoot14 = False
reshoot15 = False
reshoot16 = False
winners = False
hpdisplay = True
bingor = False
eggmis = False
vbrs2 = False
vbrs3 = False
trs3 = False
trs2 = False
trs1 = False
vbrs1 = False
rg = False
btb = False
chh = False
sg = False
phgs = False
sb = False
ghps = False
gg = False
vodkadead = False
meowhit = False
boss1s = False
healself = False
charmdisplay = False
normalmusic = False

player = Player(0, 0)
player_sprites = pygame.sprite.Group()
player_sprites.add(player)
player.rect.x = random.randint(1, 1000)
player.rect.y = random.randint(1, 600)
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 8
jump = 7
dive = 7
up = 4

if boss1s is True:
    steps = 12
    dive = 10
    jump = 10

grumpy = Grumpy(0, 0)
grumpy_sprites = pygame.sprite.Group()
grumpy_sprites.add(grumpy)
grumpy.rect.x = -player.rect.x
grumpy.rect.y = -player.rect.y
grumpy_list = pygame.sprite.Group()
grumpy_list.add(grumpy)

soul = Soulmate(0, 0)
soul_sprites = pygame.sprite.Group()
soul_sprites.add(soul)
soul.rect.x = player.rect.x - 150
soul.rect.y = 300
soul_list = pygame.sprite.Group()
soul_list.add(soul)

vodka = Vodka(0, 0)
vodka_sprites = pygame.sprite.Group()
vodka_sprites.add(vodka)
vodka.rect.x = random.randint(0, 1000)
vodka.rect.y = random.randint(0, 600)
vodka_list = pygame.sprite.Group()
vodka_list.add(vodka)

meow = Meow(0, 0)
meow_sprites = pygame.sprite.Group()
meow_sprites.add(meow)
meow.rect.x = 1000
meow.rect.y = 700
meow_list = pygame.sprite.Group()
meow_list.add(meow)

glasses = Glasses(0, 0)
glasses_sprites = pygame.sprite.Group()
glasses_sprites.add(glasses)
glasses.rect.x = random.randint(1, 1000)
glasses.rect.y = random.randint(1, 600)
glasses.list = pygame.sprite.Group()
glasses.list.add(glasses)

truffles = Truffles(0, 0)
truffles_sprites = pygame.sprite.Group()
truffles_sprites.add(truffles)
truffles.rect.x = random.randint(1, 1000)
truffles.rect.y = random.randint(1, 600)
truffles.list = pygame.sprite.Group()
truffles.list.add(truffles)

border = Border(0, 0)
border_sprites = pygame.sprite.Group()
border_sprites.add(border)
border.rect.x = 0
border.rect.y = 0
border.list = pygame.sprite.Group()
border.list.add(border)

gameover = Gameover(0, 0)
gameover_sprites = pygame.sprite.Group()
gameover_sprites.add(gameover)
gameover.rect.x = 0
gameover.rect.y = 0
gameover.list = pygame.sprite.Group()
gameover.list.add(gameover)

startgame = Start(0, 0)
startgame_sprites = pygame.sprite.Group()
startgame_sprites.add(startgame)
startgame.rect.x = 0
startgame.rect.y = 0
startgame.list = pygame.sprite.Group()
startgame.list.add(startgame)

bingo = Bingolady(0, 0)
bingo_sprites = pygame.sprite.Group()
bingo_sprites.add(bingo)
bingo.rect.x = random.randint(1, 1000)
bingo.rect.y = random.randint(1, 600)
bingo.list = pygame.sprite.Group()
bingo.list.add(bingo)
bingomnumber = random.randint(1, 100)
bingonumber = random.randint(1, 100)
bingo_font = pygame.font.Font('back-to-1982.regular.ttf', 20)
BX = 5
BY = 8
B2X = 99
B2Y = 8

def bingo_nm2(x, y):
    bingonm2 = bingo_font.render(str(bingonumber), True, (255, 255, 255))
    screen.blit(bingonm2, (x, y))

def bingo_nm(x, y):
    bingonm = bingo_font.render(str(bingomnumber), True, (255, 255, 255))
    screen.blit(bingonm, (x, y))


leaf = Leaf(0, 0)
leaf_sprites = pygame.sprite.Group()
leaf_sprites.add(leaf)
leaf.rect.x = random.randint(0, 1000)
leaf.rect.y = random.randint(0, 600)
leaf.list = pygame.sprite.Group()
leaf.list.add(leaf)

ladybug = Ladybug(0, 0)
ladybug_sprites = pygame.sprite.Group()
ladybug_sprites.add(ladybug)
ladybug.rect.x = 0
ladybug.rect.y = 0
ladybug.list = pygame.sprite.Group()
ladybug.list.add(ladybug)

egg = Egg(0, 0)
egg_sprites = pygame.sprite.Group()
egg_sprites.add(egg)
egg.rect.x = leaf.rect.x
egg.rect.y = leaf.rect.y
egg.list = pygame.sprite.Group()
egg.list.add(egg)


vegebombtrigger1 = Vegebombtrigger1(0, 0)
vegebombtrigger1_sprites = pygame.sprite.Group()
vegebombtrigger1_sprites.add(vegebombtrigger1)
vegebombtrigger1.rect.x = random.randint(0, 1000)
vegebombtrigger1.rect.y = random.randint(0, 600)
vegebombtrigger1.list = pygame.sprite.Group()
vegebombtrigger1.list.add(vegebombtrigger1)

vegebombtrigger2 = Vegebombtrigger2(0, 0)
vegebombtrigger2_sprites = pygame.sprite.Group()
vegebombtrigger2_sprites.add(vegebombtrigger2)
vegebombtrigger2.rect.x = random.randint(0, 1000)
vegebombtrigger2.rect.y = random.randint(0, 600)
vegebombtrigger2.list = pygame.sprite.Group()
vegebombtrigger2.list.add(vegebombtrigger2)

vegebombtrigger3 = Vegebombtrigger3(0, 0)
vegebombtrigger3_sprites = pygame.sprite.Group()
vegebombtrigger3_sprites.add(vegebombtrigger3)
vegebombtrigger3.rect.x = random.randint(0, 1000)
vegebombtrigger3.rect.y = random.randint(0, 600)
vegebombtrigger3.list = pygame.sprite.Group()
vegebombtrigger3.list.add(vegebombtrigger3)

vegebomb1 = Vegeb1(0, 0)
vegebomb1_sprites = pygame.sprite.Group()
vegebomb1_sprites.add(vegebomb1)
vegebomb1.rect.x = vegebombtrigger1.rect.x
vegebomb1.rect.y = vegebombtrigger1.rect.y
vegebomb1.list = pygame.sprite.Group()
vegebomb1.list.add(vegebomb1)


vegebomb2 = Vegeb2(0, 0)
vegebomb2_sprites = pygame.sprite.Group()
vegebomb2_sprites.add(vegebomb2)
vegebomb2.rect.x = vegebombtrigger2.rect.x
vegebomb2.rect.y = vegebombtrigger2.rect.y
vegebomb2.list = pygame.sprite.Group()
vegebomb2.list.add(vegebomb1)


vegebomb3 = Vegeb3(0, 0)
vegebomb3_sprites = pygame.sprite.Group()
vegebomb3_sprites.add(vegebomb3)
vegebomb3.rect.x = vegebombtrigger3.rect.x
vegebomb3.rect.y = vegebombtrigger3.rect.y
vegebomb3.list = pygame.sprite.Group()
vegebomb3.list.add(vegebomb3)



hell = Hell(0, 0)
hell_sprites = pygame.sprite.Group()
hell_sprites.add(hell)
hell.rect.x = 0
hell.rect.y = 0
hell.list = pygame.sprite.Group()
hell.list.add(hell)


cage = Cage(0, 0)
cage_sprites = pygame.sprite.Group()
cage_sprites.add(cage)
cage.rect.x = 1200
cage.rect.y = 1200
cage.list = pygame.sprite.Group()
cage.list.add(cage)


boss1 = Boss1(0, 0)
boss1_sprites = pygame.sprite.Group()
boss1_sprites.add(boss1)
boss1.rect.x = 390
boss1.rect.y = 200
boss1.list = pygame.sprite.Group()
boss1.list.add(boss1)


boss2 = Boss2(0, 0)
boss2_sprites = pygame.sprite.Group()
boss2_sprites.add(boss2)
boss2.rect.x = 390
boss2.rect.y = 200
boss2.list = pygame.sprite.Group()
boss2.list.add(boss2)


boss3 = Boss3(0, 0)
boss3_sprites = pygame.sprite.Group()
boss3_sprites.add(boss3)
boss3.rect.x = 390
boss3.rect.y = 200
boss3.list = pygame.sprite.Group()
boss3.list.add(boss3)

boss4 = Boss4(0, 0)
boss4_sprites = pygame.sprite.Group()
boss4_sprites.add(boss4)
boss4.rect.x = 390
boss4.rect.y = 200
boss4.list = pygame.sprite.Group()
boss4.list.add(boss4)

boss5 = Boss5(0, 0)
boss5_sprites = pygame.sprite.Group()
boss5_sprites.add(boss5)
boss5.rect.x = 390
boss5.rect.y = 200
boss5.list = pygame.sprite.Group()
boss5.list.add(boss5)


boss6 = Boss6(0, 0)
boss6_sprites = pygame.sprite.Group()
boss6_sprites.add(boss6)
boss6.rect.x = 390
boss6.rect.y = 200
boss6.list = pygame.sprite.Group()
boss6.list.add(boss6)



boss7 = Boss7(0, 0)
boss7_sprites = pygame.sprite.Group()
boss7_sprites.add(boss7)
boss7.rect.x = 390
boss7.rect.y = 200
boss7.list = pygame.sprite.Group()
boss7.list.add(boss7)



boss8 = Boss8(0, 0)
boss8_sprites = pygame.sprite.Group()
boss8_sprites.add(boss8)
boss8.rect.x = 390
boss8.rect.y = 200
boss8.list = pygame.sprite.Group()
boss8.list.add(boss8)



boss9 = Boss9(0, 0)
boss9_sprites = pygame.sprite.Group()
boss9_sprites.add(boss9)
boss9.rect.x = 390
boss9.rect.y = 200
boss9.list = pygame.sprite.Group()
boss9.list.add(boss9)


Shury1 = Shuriken1(0, 0)
Shury1_sprites = pygame.sprite.Group()
Shury1_sprites.add(Shury1)
Shury1.rect.x = player.rect.x
Shury1.rect.y = random.randint(0, 600)
Shury1.list = pygame.sprite.Group()
Shury1.list.add(Shury1)

Shury2 = Shuriken2(0, 0)
Shury2_sprites = pygame.sprite.Group()
Shury2_sprites.add(Shury2)
Shury2.rect.x = random.randint(0, 1000)
Shury2.rect.y = player.rect.y
Shury2.list = pygame.sprite.Group()
Shury2.list.add(Shury2)

Shury3 = Shuriken3(0, 0)
Shury3_sprites = pygame.sprite.Group()
Shury3_sprites.add(Shury3)
Shury3.rect.x = random.randint(0, 1000)
Shury3.rect.y = random.randint(0, 600)
Shury3.list = pygame.sprite.Group()
Shury3.list.add(Shury3)


Shury4 = Shuriken4(0, 0)
Shury4_sprites = pygame.sprite.Group()
Shury4_sprites.add(Shury4)
Shury4.rect.x = random.randint(0, 1000)
Shury4.rect.y = random.randint(0, 600)
Shury4.list = pygame.sprite.Group()
Shury4.list.add(Shury4)

up1 = Up1(0, 0)
up1_sprites = pygame.sprite.Group()
up1_sprites.add(up1)
up1.rect.x = Shury1.rect.x
up1.rect.y = Shury1.rect.y
up1.list = pygame.sprite.Group()
up1.list.add(up1)

down1 = Down1(0, 0)
down1_sprites = pygame.sprite.Group()
down1_sprites.add(down1)
down1.rect.x = Shury1.rect.x
down1.rect.y = Shury1.rect.y
down1.list = pygame.sprite.Group()
down1.list.add(down1)

right1 = Right1(0, 0)
right1_sprites = pygame.sprite.Group()
right1_sprites.add(right1)
right1.rect.x = Shury1.rect.x
right1.rect.y = Shury1.rect.y
right1.list = pygame.sprite.Group()
right1.list.add(right1)


left1 = Left1(0, 0)
left1_sprites = pygame.sprite.Group()
left1_sprites.add(left1)
left1.rect.x = Shury1.rect.x
left1.rect.y = Shury1.rect.y
left1.list = pygame.sprite.Group()
left1.list.add(left1)


up2 = Up2(0, 0)
up2_sprites = pygame.sprite.Group()
up2_sprites.add(up2)
up2.rect.x = Shury2.rect.x
up2.rect.y = Shury2.rect.y
up2.list = pygame.sprite.Group()
up2.list.add(up2)

down2 = Down2(0, 0)
down2_sprites = pygame.sprite.Group()
down2_sprites.add(down2)
down2.rect.x = Shury2.rect.x
down2.rect.y = Shury2.rect.y
down2.list = pygame.sprite.Group()
down2.list.add(down2)

right2 = Right2(0, 0)
right2_sprites = pygame.sprite.Group()
right2_sprites.add(right2)
right2.rect.x = Shury2.rect.x
right2.rect.y = Shury2.rect.y
right2.list = pygame.sprite.Group()
right2.list.add(right2)


left2 = Left2(0, 0)
left2_sprites = pygame.sprite.Group()
left2_sprites.add(left2)
left2.rect.x = Shury2.rect.x
left2.rect.y = Shury2.rect.y
left2.list = pygame.sprite.Group()
left2.list.add(left2)

up3 = Up3(0, 0)
up3_sprites = pygame.sprite.Group()
up3_sprites.add(up3)
up3.rect.x = Shury3.rect.x
up3.rect.y = Shury3.rect.y
up3.list = pygame.sprite.Group()
up3.list.add(up3)

down3 = Down3(0, 0)
down3_sprites = pygame.sprite.Group()
down3_sprites.add(down3)
down3.rect.x = Shury3.rect.x
down3.rect.y = Shury3.rect.y
down3.list = pygame.sprite.Group()
down3.list.add(down3)

right3 = Right3(0, 0)
right3_sprites = pygame.sprite.Group()
right3_sprites.add(right3)
right3.rect.x = Shury3.rect.x
right3.rect.y = Shury3.rect.y
right3.list = pygame.sprite.Group()
right3.list.add(right3)


left3 = Left3(0, 0)
left3_sprites = pygame.sprite.Group()
left3_sprites.add(left3)
left3.rect.x = Shury3.rect.x
left3.rect.y = Shury3.rect.y
left3.list = pygame.sprite.Group()
left3.list.add(left3)


up4 = Up4(0, 0)
up4_sprites = pygame.sprite.Group()
up4_sprites.add(up4)
up4.rect.x = Shury4.rect.x
up4.rect.y = Shury4.rect.y
up4.list = pygame.sprite.Group()
up4.list.add(up4)

down4 = Down4(0, 0)
down4_sprites = pygame.sprite.Group()
down4_sprites.add(down4)
down4.rect.x = Shury4.rect.x
down4.rect.y = Shury4.rect.y
down4.list = pygame.sprite.Group()
down4.list.add(down4)

right4 = Right4(0, 0)
right4_sprites = pygame.sprite.Group()
right4_sprites.add(right4)
right4.rect.x = Shury4.rect.x
right4.rect.y = Shury4.rect.y
right4.list = pygame.sprite.Group()
right4.list.add(right4)


left4 = Left4(0, 0)
left4_sprites = pygame.sprite.Group()
left4_sprites.add(left4)
left4.rect.x = Shury4.rect.x
left4.rect.y = Shury4.rect.y
left4.list = pygame.sprite.Group()
left4.list.add(left4)

cheetosl1 = Cheetosl1(0, 0)
cheetosl1_sprites = pygame.sprite.Group()
cheetosl1_sprites.add(cheetosl1)
cheetosl1.rect.x = 0
cheetosl1.rect.y = 100
cheetosl1.list = pygame.sprite.Group()
cheetosl1.list.add(cheetosl1)


cheetosl2 = Cheetosl2(0, 0)
cheetosl2_sprites = pygame.sprite.Group()
cheetosl2_sprites.add(cheetosl2)
cheetosl2.rect.x = 0
cheetosl2.rect.y = 300
cheetosl2.list = pygame.sprite.Group()
cheetosl2.list.add(cheetosl2)


cheetosl3 = Cheetosl3(0, 0)
cheetosl3_sprites = pygame.sprite.Group()
cheetosl3_sprites.add(cheetosl3)
cheetosl3.rect.x = 0
cheetosl3.rect.y = 500
cheetosl3.list = pygame.sprite.Group()
cheetosl3.list.add(cheetosl3)


cheetosr1 = Cheetosr1(0, 0)
cheetosr1_sprites = pygame.sprite.Group()
cheetosr1_sprites.add(cheetosr1)
cheetosr1.rect.x = 1000
cheetosr1.rect.y = 200
cheetosr1.list = pygame.sprite.Group()
cheetosr1.list.add(cheetosr1)

cheetosr2 = Cheetosr2(0, 0)
cheetosr2_sprites = pygame.sprite.Group()
cheetosr2_sprites.add(cheetosr2)
cheetosr2.rect.x = 1000
cheetosr2.rect.y = 400
cheetosr2.list = pygame.sprite.Group()
cheetosr2.list.add(cheetosr2)






gamestart = True
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.animate()
            if event.key == event.key == ord('a'):
                player.control(-steps, 0)
                grumpy.control(steps, 0)
                soul.control(-steps, 0)

            if event.key == event.key == ord('d'):
                player.control(steps, 0)
                grumpy.control(-steps, 0)
                soul.control(steps, 0)

            if event.key == event.key == ord('w'):
                player.up(-jump)
                grumpy.up(-jump)
                soul.up(-jump)

            if event.key == event.key == ord('s'):
                player.down(-dive)
                grumpy.down(-dive)
                soul.up(dive)

            if event.key == pygame.K_UP:
                soul.up(-jump)
            if event.key == pygame.K_DOWN:
                soul.up(dive)
            if event.key == pygame.K_RIGHT:
                soul.control(steps, 0)
            if event.key == pygame.K_LEFT:
                soul.control(-steps, 0)

            if healself is True:

                if event.key == pygame.K_1:
                    playerhp += 30
                    healcharge -= 5
            if event.key == pygame.K_SPACE:
                gamestart = False

                soul.animate()
                player.animate()
                grumpy.animate()
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                soul.up(jump)
            if event.key == pygame.K_DOWN:
                soul.up(-dive)
            if event.key == pygame.K_RIGHT:
                soul.control(-steps, 0)
            if event.key == pygame.K_LEFT:
                soul.control(steps, 0)

            if event.key == event.key == ord('a'):
                player.control(steps, 0)
                grumpy.control(-steps, 0)
                soul.control(steps, 0)

            if event.key == event.key == ord('d'):
                player.control(-steps, 0)
                soul.control(-steps, 0)
                grumpy.control(steps, 0)

            if event.key == event.key == ord('w'):
                player.up(jump)
                grumpy.up(-jump)
                soul.up(jump)

            if event.key == event.key == ord('s'):
                player.down(dive)
                grumpy.down(-dive)
                soul.up(-dive)
                player.animate()
                soul.animate()
    vodka.animate()
    meow.animate()
    glasses.animate()
    truffles.animate()
    bingo.animate()
    ladybug.animate()
    leaf.animate()
    vegebombtrigger1.animate()
    vegebombtrigger2.animate()
    vegebombtrigger3.animate()
    vegebomb1.animate()
    vegebomb2.animate()
    vegebomb3.animate()
    boss1.animate()
    boss2.animate()
    boss3.animate()
    boss4.animate()
    boss5.animate()
    boss6.animate()
    boss7.animate()
    boss8.animate()
    boss9.animate()
    Shury1.animate()
    Shury2.animate()
    Shury3.animate()
    Shury4.animate()
    up1.animate()
    up2.animate()
    up3.animate()
    up4.animate()
    down1.animate()
    down2.animate()
    down3.animate()
    down4.animate()
    right1.animate()
    right2.animate()
    right3.animate()
    right4.animate()
    left1.animate()
    left2.animate()
    left3.animate()
    left4.animate()
    cheetosl1.animate()
    cheetosl2.animate()
    cheetosl3.animate()
    cheetosr1.animate()
    cheetosr2.animate()


    if soul.rect.x > player.rect.x + 180:
        soul.rect.x = player.rect.x + 150
    elif soul.rect.x < player.rect.x - 180:
        soul.rect.x = player.rect.x - 150

    if soul.rect.y > player.rect.y + 180:
        soul.rect.y = player.rect.y + 150
    elif soul.rect.y < player.rect.y - 180:
        soul.rect.y = player.rect.y - 150

    # collisions

    hits = pygame.sprite.spritecollide(vodka, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
    if hits:
        pygame.sprite.Sprite.kill(vodka)
        vodkadead = True
        playerhp = playerhp - 8

    if vodkadead is True:
        vodka = Vodka(0, 0)
        vodka_sprites = pygame.sprite.Group()
        vodka_sprites.add(vodka)
        vodka.rect.x = random.randint(0, 1000)
        vodka.rect.y = random.randint(0, 600)
        vodka_list = pygame.sprite.Group()
        vodka_list.add(vodka)

    if playerhp >= 0:
        vodkadead = False

    if playerhp <= 0:
        pygame.sprite.Sprite.kill(player)

    soul_hit = pygame.sprite.spritecollide(soul, vodka_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
    if soul_hit:
        pygame.sprite.Sprite.kill(vodka)
        vodkadead = True
        lvl2sr += 1
        score += 1
        boss += 1

    grumpy_hit = pygame.sprite.spritecollide(grumpy, vodka_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
    if grumpy_hit:
        pygame.sprite.Sprite.kill(vodka)
        vodkadead = True
        lvl2sr += 1
        score += 1
        boss += 1

    meowhit = pygame.sprite.spritecollide(grumpy, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.5))
    if meowhit:
        pygame.sprite.Sprite.kill(meow)
        meowhit = True

    if meowhit is True:
        meow = Meow(0, 0)
        meow_sprites = pygame.sprite.Group()
        meow_sprites.add(meow)
        meow.rect.x = soul.rect.x
        meow.rect.y = soul.rect.y + 30
        meow_list = pygame.sprite.Group()
        meow_list.add(meow)

    playermeow = pygame.sprite.spritecollide(player, meow_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
    if playermeow:
        playerhp += 1

    if lvl2sr >= 4:
        lvl2 = True

    if lvl2 is True:

        ghg = pygame.sprite.spritecollide(grumpy, truffles_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        if ghg:
            pygame.sprite.Sprite.kill(truffles)
            lvl3sr += 1
            score += 10
            sg = True
            boss += 1

        shg = pygame.sprite.spritecollide(soul, truffles_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        if shg:
            pygame.sprite.Sprite.kill(truffles)
            score += 10
            lvl3sr += 1
            sg = True
            boss += 1

        if sg is True:
            truffles = Truffles(0, 0)
            truffles_sprites = pygame.sprite.Group()
            truffles_sprites.add(truffles)
            truffles.rect.x = random.randint(1, 1000)
            truffles.rect.y = random.randint(1, 600)
            truffles.list = pygame.sprite.Group()
            truffles.list.add(truffles)

            sg = False

        gng = pygame.sprite.spritecollide(truffles, glasses_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        if gng:
            playerhp -= 50
            pygame.sprite.Sprite.kill(truffles)
            pygame.sprite.Sprite.kill(glasses)
            gg = True

        if gg is True:
            glasses = Glasses(0, 0)
            glasses_sprites = pygame.sprite.Group()
            glasses_sprites.add(glasses)
            glasses.rect.x = random.randint(1, 1000)
            glasses.rect.y = random.randint(1, 600)
            glasses.list = pygame.sprite.Group()
            glasses.list.add(glasses)

            truffles = Truffles(0, 0)
            truffles_sprites = pygame.sprite.Group()
            truffles_sprites.add(truffles)
            truffles.rect.x = random.randint(1, 1000)
            truffles.rect.y = random.randint(1, 600)
            truffles.list = pygame.sprite.Group()
            truffles.list.add(truffles)

            gg = False

        phg = pygame.sprite.spritecollide(player, glasses_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        if phg:
            pygame.sprite.Sprite.kill(glasses)
            playerhp += 0.2
            score += 1
            phgs = True
            lvl3sr += 1
            boss += 1

        if phgs is True:
            glasses = Glasses(0, 0)
            glasses_sprites = pygame.sprite.Group()
            glasses_sprites.add(glasses)
            glasses.rect.x = random.randint(1, 1000)
            glasses.rect.y = random.randint(1, 600)
            glasses.list = pygame.sprite.Group()
            glasses.list.add(glasses)

            vodka = Vodka(0, 0)
            vodka_sprites = pygame.sprite.Group()
            vodka_sprites.add(vodka)
            vodka.rect.x = random.randint(0, 1000)
            vodka.rect.y = random.randint(0, 600)
            vodka_list = pygame.sprite.Group()
            vodka_list.add(vodka)

            phgs = False

        ghp = pygame.sprite.spritecollide(player, truffles_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        if ghp:
            pygame.sprite.Sprite.kill(truffles)
            playerhp -= 20
            ghps = True

        if ghps is True:
            truffles = Truffles(0, 0)
            truffles_sprites = pygame.sprite.Group()
            truffles_sprites.add(truffles)
            truffles.rect.x = random.randint(1, 1000)
            truffles.rect.y = random.randint(1, 600)
            truffles.list = pygame.sprite.Group()
            truffles.list.add(truffles)

            ghps = False

        truffles_sprites.draw(screen)
        truffles_sprites.update()
        glasses_sprites.draw(screen)
        glasses_sprites.update()

    if lvl3sr >= 6:
        lvl3 = True


    if lvl3 is True:

        charmdisplay = True

        if bingonumber == bingomnumber:
            playerhp -= 10
            print(playerhp)

        shb = pygame.sprite.spritecollide(soul, bingo_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        if shb:
            healcharge += 1
            lvl4sr += 1
            score += 50
            boss += random.randint(1, 10)
            pygame.sprite.Sprite.kill(bingo)
            bingor = True

        ghb = pygame.sprite.spritecollide(grumpy, bingo_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        if ghb:
            healcharge += 1
            lvl4sr += 1
            score += 50
            boss += random.randint(1, 10)
            pygame.sprite.Sprite.kill(bingo)
            bingor = True

        if healcharge <= 4:
            healself = False

        if healcharge >= 5:
            healself = True

        if healcharge >= 6:
            healcharge -= 1

        if bingor is True:
            bingo = Bingolady(0, 0)
            bingo_sprites = pygame.sprite.Group()
            bingo_sprites.add(bingo)
            bingo.rect.x = random.randint(1, 1000)
            bingo.rect.y = random.randint(1, 600)
            bingo.list = pygame.sprite.Group()
            bingo.list.add(bingo)
            bingomnumber = random.randint(1, 100)
            bingonumber = random.randint(1, 100)
            bingor = False

        bingo_sprites.draw(screen)
        bingo_sprites.update()



    if lvl4sr >= 12:
        lvl4 = True

    if lvl4 is True:


        chl = pygame.sprite.spritecollide(ladybug, leaf_sprites, False, pygame.sprite.collide_circle_ratio(0.3))
        if chl:
            eggmis = True
            pygame.sprite.Sprite.kill(ladybug)
            pygame.sprite.Sprite.kill(leaf)
            egg.egg_list.append(Egg(ladybug.x, ladybug.y))
            chh = True


        phc = pygame.sprite.spritecollide(player, ladybug_sprites, False, pygame.sprite.collide_circle_ratio(0.3))
        if phc:
            pygame.sprite.Sprite.kill(ladybug)
            score += 10
            boss += random.randint(1, 10)
            chh = True
            lvl5sr += 1


        shc = pygame.sprite.spritecollide(soul, ladybug_sprites, False, pygame.sprite.collide_circle_ratio(0.3))
        if shc:
            pygame.sprite.Sprite.kill(ladybug)
            score += 10
            boss += random.randint(1, 10)
            chh = True
            lvl5sr += 1


        ghc = pygame.sprite.spritecollide(grumpy, ladybug_sprites, False, pygame.sprite.collide_circle_ratio(0.3))
        if ghc:
            pygame.sprite.Sprite.kill(ladybug)
            score += 10
            boss += random.randint(10, 20)

            chh = True
            lvl5sr += 1

        if chh is True:

            ladybug = Ladybug(0, 0)
            ladybug_sprites = pygame.sprite.Group()
            ladybug_sprites.add(ladybug)
            ladybug.rect.x = 0
            ladybug.rect.y = 0
            ladybug.list = pygame.sprite.Group()
            ladybug.list.add(ladybug)

            leaf = Leaf(0, 0)
            leaf_sprites = pygame.sprite.Group()
            leaf_sprites.add(leaf)
            leaf.rect.x = random.randint(0, 1000)
            leaf.rect.y = random.randint(0, 600)
            leaf.list = pygame.sprite.Group()
            leaf.list.add(leaf)

            chh = False

        leaf_sprites.draw(screen)
        leaf_sprites.update()
        ladybug_sprites.draw(screen)
        ladybug_sprites.update()

    if eggmis is True:

        for egg in egg.list:
            egg.update()

        for egg in egg.list:

            ehs = pygame.sprite.spritecollide(egg, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.77))
            if ehs:
                pygame.sprite.Sprite.kill(egg)
                rg = True
                score += 20
                boss += random.randint(1, 10)

            ehg = pygame.sprite.spritecollide(egg, grumpy_sprites, False, pygame.sprite.collide_circle_ratio(0.77))
            if ehs:
                pygame.sprite.Sprite.kill(egg)
                rg = True
                score += 20
                boss += random.randint(1, 10)

            eh = pygame.sprite.spritecollide(egg, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            if eh:
                pygame.sprite.Sprite.kill(egg)
                playerhp -= 25
                rg = True

        if rg is True:
            egg = Egg(0, 0)
            egg_sprites = pygame.sprite.Group()
            egg_sprites.add(egg)
            egg.rect.x = leaf.rect.x
            egg.rect.y = leaf.rect.y
            egg.list = pygame.sprite.Group()
            egg.list.add(egg)

            rg = False
            eggmis = False

        for egg in egg.list:
            egg_sprites.draw(screen)
            egg_sprites.update()

    if lvl5sr >= 12:
        lvl5 = True

    if lvl5 is True:


        vegebombtrigger1_sprites.draw(screen)
        vegebombtrigger1_sprites.update()
        vegebombtrigger2_sprites.draw(screen)
        vegebombtrigger2_sprites.update()
        vegebombtrigger3_sprites.draw(screen)
        vegebombtrigger3_sprites.update()


        pht1 = pygame.sprite.spritecollide(vegebombtrigger1, player_sprites, False, pygame.sprite.collide_circle_ratio(0.7))
        if pht1:

            pygame.sprite.Sprite.kill(vegebombtrigger1)

            vegebomb1_sprites.draw(screen)
            vegebomb1_sprites.update()

            trs1 = True

        phvb1 = pygame.sprite.spritecollide(vegebomb1, player_sprites, False, pygame.sprite.collide_circle_ratio(0.7))
        if phvb1:

            pygame.sprite.Sprite.kill(vegebomb1)
            playerhp -= 30
            vbrs1 = True


        if trs1 is True:

            vegebombtrigger1 = Vegebombtrigger1(0, 0)
            vegebombtrigger1_sprites = pygame.sprite.Group()
            vegebombtrigger1_sprites.add(vegebombtrigger1)
            vegebombtrigger1.rect.x = random.randint(0, 1000)
            vegebombtrigger1.rect.y = random.randint(0, 600)
            vegebombtrigger1.list = pygame.sprite.Group()
            vegebombtrigger1.list.add(vegebombtrigger1)

            trs1 = False

        if vbrs1 is True:

            vegebomb1 = Vegeb1(0, 0)
            vegebomb1_sprites = pygame.sprite.Group()
            vegebomb1_sprites.add(vegebomb1)
            vegebomb1.rect.x = vegebombtrigger1.rect.x
            vegebomb1.rect.y = vegebombtrigger1.rect.y
            vegebomb1.list = pygame.sprite.Group()
            vegebomb1.list.add(vegebomb1)

            vbrs1 = False


        pht2 = pygame.sprite.spritecollide(vegebombtrigger2, player_sprites, False, pygame.sprite.collide_circle_ratio(0.7))
        if pht2:

            pygame.sprite.Sprite.kill(vegebombtrigger2)

            vegebomb2_sprites.draw(screen)
            vegebomb2_sprites.update()

            trs2 = True

        phvb2 = pygame.sprite.spritecollide(vegebomb2, player_sprites, False, pygame.sprite.collide_circle_ratio(0.7))
        if phvb2:

            pygame.sprite.Sprite.kill(vegebomb2)
            playerhp -= 30
            vbrs2 = True

        if trs2 is True:
            vegebombtrigger2 = Vegebombtrigger2(0, 0)
            vegebombtrigger2_sprites = pygame.sprite.Group()
            vegebombtrigger2_sprites.add(vegebombtrigger2)
            vegebombtrigger2.rect.x = random.randint(0, 1000)
            vegebombtrigger2.rect.y = random.randint(0, 600)
            vegebombtrigger2.list = pygame.sprite.Group()
            vegebombtrigger2.list.add(vegebombtrigger2)

            trs2 = False

        if vbrs2 is True:
            vegebomb2 = Vegeb2(0, 0)
            vegebomb2_sprites = pygame.sprite.Group()
            vegebomb2_sprites.add(vegebomb2)
            vegebomb2.rect.x = vegebombtrigger2.rect.x
            vegebomb2.rect.y = vegebombtrigger2.rect.y
            vegebomb2.list = pygame.sprite.Group()
            vegebomb2.list.add(vegebomb2)

            vbrs2 = False


        pht3 = pygame.sprite.spritecollide(vegebombtrigger3, player_sprites, False, pygame.sprite.collide_circle_ratio(0.7))
        if pht3:

            pygame.sprite.Sprite.kill(vegebombtrigger3)

            vegebomb2_sprites.draw(screen)
            vegebomb2_sprites.update()

            trs3 = True

        phvb3 = pygame.sprite.spritecollide(vegebomb3, player_sprites, False, pygame.sprite.collide_circle_ratio(0.7))
        if phvb3:

            pygame.sprite.Sprite.kill(vegebomb3)
            playerhp -= 30
            vbrs3 = True

        if trs3 is True:
            vegebombtrigger3 = Vegebombtrigger3(0, 0)
            vegebombtrigger3_sprites = pygame.sprite.Group()
            vegebombtrigger3_sprites.add(vegebombtrigger3)
            vegebombtrigger3.rect.x = random.randint(0, 1000)
            vegebombtrigger3.rect.y = random.randint(0, 600)
            vegebombtrigger3.list = pygame.sprite.Group()
            vegebombtrigger3.list.add(vegebombtrigger3)

            trs3 = False

        if vbrs3 is True:
            vegebomb3 = Vegeb3(0, 0)
            vegebomb3_sprites = pygame.sprite.Group()
            vegebomb3_sprites.add(vegebomb3)
            vegebomb3.rect.x = vegebombtrigger2.rect.x
            vegebomb3.rect.y = vegebombtrigger2.rect.y
            vegebomb3.list = pygame.sprite.Group()
            vegebomb3.list.add(vegebomb3)

            vbrs3 = False

    if boss >= 300:
        allshalldie = True
        boss1s = True

    if allshalldie is True:
        # soul and player will damage boss by raming it and player will only take damage from seperate attacks
        pygame.sprite.Sprite.kill(glasses)
        pygame.sprite.Sprite.kill(truffles)
        pygame.sprite.Sprite.kill(meow)
        pygame.sprite.Sprite.kill(vegebomb3)
        pygame.sprite.Sprite.kill(vegebombtrigger3)
        pygame.sprite.Sprite.kill(vegebombtrigger2)
        pygame.sprite.Sprite.kill(vegebombtrigger1)
        pygame.sprite.Sprite.kill(vegebomb2)
        pygame.sprite.Sprite.kill(vegebomb1)
        pygame.sprite.Sprite.kill(egg)
        pygame.sprite.Sprite.kill(bingo)
        pygame.sprite.Sprite.kill(vodka)


        hell_sprites.draw(screen)
        hell_sprites.update()


        phcage = pygame.sprite.spritecollide(cage, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        shcage = pygame.sprite.spritecollide(cage, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))

        if phcage:
            player.rect.x = 500
            player.rect.y = 300
            playerhp -= 50
        if shcage:
            soul.rect.x = player.rect.x
            soul.rect.y = player.rect.y
            pygame.sprite.Sprite.kill(meow)

        grumpy.rect.x = 450
        grumpy.rect.y = 1
        cage.rect.x = 450
        cage.rect.y = 1

        if grumpy.rect.x > 450:
            grumpy.rect.x = 450
        elif grumpy.rect.x < 450:
            grumpy.rect.x = 450

        if grumpy.rect.y > 1:
            grumpy.rect.y = 1
        elif grumpy.rect.y < 1:
            grumpy.rect.y = 1


        scx = 70
        scy = 1

        BX = 1200
        BY = 1200
        B2X = 1200
        B2Y = 1200


    if boss1s is True:

        pygame.sprite.Sprite.kill(vodka)

        boss1_sprites.draw(screen)
        boss1_sprites.update()
        Shury1_sprites.draw(screen)
        Shury1_sprites.update()
        Shury2_sprites.draw(screen)
        Shury2_sprites.update()
        Shury3_sprites.draw(screen)
        Shury3_sprites.update()
        Shury4_sprites.draw(screen)
        Shury4_sprites.update()

        rhp1 = pygame.sprite.spritecollide(right1, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        rhp2 = pygame.sprite.spritecollide(right2, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        rhp3 = pygame.sprite.spritecollide(right3, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        rhp4 = pygame.sprite.spritecollide(right4, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        lhp1 = pygame.sprite.spritecollide(left1, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        lhp2 = pygame.sprite.spritecollide(left2, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        lhp3 = pygame.sprite.spritecollide(left3, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        lhp4 = pygame.sprite.spritecollide(left4, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))

        if rhp1:
            pygame.sprite.Sprite.kill(right1)
            playerhp -= 1
            reshoot9 = True

        if reshoot9 is True:
            right1 = Right1(0, 0)
            right1_sprites = pygame.sprite.Group()
            right1_sprites.add(right1)
            right1.rect.x = Shury1.rect.x
            right1.rect.y = Shury1.rect.y
            right1.list = pygame.sprite.Group()
            right1.list.add(right1)
            reshoot9 = False

        if rhp2:
            pygame.sprite.Sprite.kill(right2)
            playerhp -= 1
            reshoot10 = True

        if reshoot10 is True:
            right2 = Right2(0, 0)
            right2_sprites = pygame.sprite.Group()
            right2_sprites.add(right2)
            right2.rect.x = Shury2.rect.x
            right2.rect.y = Shury2.rect.y
            right2.list = pygame.sprite.Group()
            right2.list.add(right2)
            reshoot10 = False

        if rhp3:
            pygame.sprite.Sprite.kill(right3)
            playerhp -= 1
            reshoot11 = True

        if reshoot11 is True:
            right3 = Right3(0, 0)
            right3_sprites = pygame.sprite.Group()
            right3_sprites.add(right3)
            right3.rect.x = Shury3.rect.x
            right3.rect.y = Shury3.rect.y
            right3.list = pygame.sprite.Group()
            right3.list.add(right3)
            reshoot12 = False

        if rhp4:
            pygame.sprite.Sprite.kill(right4)
            playerhp -= 1
            reshoot12 = True

        if reshoot12 is True:
            right4 = Right4(0, 0)
            right4_sprites = pygame.sprite.Group()
            right4_sprites.add(right4)
            right4.rect.x = Shury4.rect.x
            right4.rect.y = Shury4.rect.y
            right4.list = pygame.sprite.Group()
            right4.list.add(right4)
            reshoot12 = False

        if lhp1:
            pygame.sprite.Sprite.kill(left1)
            playerhp -= 1
            reshoot13 = True

        if reshoot13 is True:

            left1 = Left1(0, 0)
            left1_sprites = pygame.sprite.Group()
            left1_sprites.add(left1)
            left1.rect.x = Shury1.rect.x
            left1.rect.y = Shury1.rect.y
            left1.list = pygame.sprite.Group()
            left1.list.add(left1)

            reshoot13 = False

        if lhp2:
            pygame.sprite.Sprite.kill(left2)
            playerhp -= 1
            reshoot14 = True

        if reshoot14 is True:
            left2 = Left2(0, 0)
            left2_sprites = pygame.sprite.Group()
            left2_sprites.add(left2)
            left2.rect.x = Shury2.rect.x
            left2.rect.y = Shury2.rect.y
            left2.list = pygame.sprite.Group()
            left2.list.add(left2)

            reshoot14 = False

        if lhp3:
            pygame.sprite.Sprite.kill(left3)
            playerhp -= 1
            reshoot15 = True

        if reshoot15 is True:
            left3 = Left3(0, 0)
            left3_sprites = pygame.sprite.Group()
            left3_sprites.add(left3)
            left3.rect.x = Shury3.rect.x
            left3.rect.y = Shury3.rect.y
            left3.list = pygame.sprite.Group()
            left3.list.add(left3)

            reshoot15 = False


        if lhp4:
            pygame.sprite.Sprite.kill(left4)
            playerhp -= 1
            reshoot16 = True

        if reshoot16 is True:
            left4 = Left4(0, 0)
            left4_sprites = pygame.sprite.Group()
            left4_sprites.add(left4)
            left4.rect.x = Shury4.rect.x
            left4.rect.y = Shury4.rect.y
            left4.list = pygame.sprite.Group()
            left4.list.add(left4)

            reshoot16 = False


        uhp1 = pygame.sprite.spritecollide(up1, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        uhp2 = pygame.sprite.spritecollide(up2, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        uhp3 = pygame.sprite.spritecollide(up3, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        uhp4 = pygame.sprite.spritecollide(up4, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        dhp1 = pygame.sprite.spritecollide(down1, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        dhp2 = pygame.sprite.spritecollide(down2, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        dhp3 = pygame.sprite.spritecollide(down3, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        dhp4 = pygame.sprite.spritecollide(down4, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))


        if dhp1:
            pygame.sprite.Sprite.kill(down1)
            playerhp -= 1
            reshoot5 = True

        if reshoot5 is True:

            down1 = Down1(0, 0)
            down1_sprites = pygame.sprite.Group()
            down1_sprites.add(down1)
            down1.rect.x = Shury1.rect.x
            down1.rect.y = Shury1.rect.y
            down1.list = pygame.sprite.Group()
            down1.list.add(down1)

            reshoot5 = False

        if dhp2:
            pygame.sprite.Sprite.kill(down2)
            playerhp -= 1
            reshoot6 = True

        if reshoot6 is True:

            down2 = Down2(0, 0)
            down2_sprites = pygame.sprite.Group()
            down2_sprites.add(down2)
            down2.rect.x = Shury2.rect.x
            down2.rect.y = Shury2.rect.y
            down2.list = pygame.sprite.Group()
            down2.list.add(down2)

            reshoot6 = False

        if dhp3:
            pygame.sprite.Sprite.kill(down3)
            playerhp -= 1
            reshoot7 = True

        if reshoot7 is True:

            down3 = Down3(0, 0)
            down3_sprites = pygame.sprite.Group()
            down3_sprites.add(down3)
            down3.rect.x = Shury3.rect.x
            down3.rect.y = Shury3.rect.y
            down3.list = pygame.sprite.Group()
            down3.list.add(down3)
            reshoot7 = False

        if dhp4:
            pygame.sprite.Sprite.kill(down4)
            playerhp -= 1
            reshoot8 = True

        if reshoot8 is True:

            down4 = Down4(0, 0)
            down4_sprites = pygame.sprite.Group()
            down4_sprites.add(down4)
            down4.rect.x = Shury4.rect.x
            down4.rect.y = Shury4.rect.y
            down4.list = pygame.sprite.Group()
            down4.list.add(down4)

            reshoot8 = False

        if uhp1:

            pygame.sprite.Sprite.kill(up1)
            playerhp -= 1
            reshoot1 = True

        if reshoot1 is True:

            up1 = Up1(0, 0)
            up1_sprites = pygame.sprite.Group()
            up1_sprites.add(up1)
            up1.rect.x = Shury1.rect.x
            up1.rect.y = Shury1.rect.y
            up1.list = pygame.sprite.Group()
            up1.list.add(up1)

            reshoot1 = False

        if uhp2:
            pygame.sprite.Sprite.kill(up2)
            playerhp -= 1
            reshoot2 = True

        if reshoot2 is True:
            up2 = Up2(0, 0)
            up2_sprites = pygame.sprite.Group()
            up2_sprites.add(up2)
            up2.rect.x = Shury2.rect.x
            up2.rect.y = Shury2.rect.y
            up2.list = pygame.sprite.Group()
            up2.list.add(up2)

            reshoot2 = False

        if uhp3:
            pygame.sprite.Sprite.kill(up3)
            playerhp -= 1
            reshoot3 = True

        if reshoot3 is True:
            up3 = Up3(0, 0)
            up3_sprites = pygame.sprite.Group()
            up3_sprites.add(up3)
            up3.rect.x = Shury3.rect.x
            up3.rect.y = Shury3.rect.y
            up3.list = pygame.sprite.Group()
            up3.list.add(up3)

            reshoot3 = False

        if uhp4:
            pygame.sprite.Sprite.kill(up4)
            playerhp -= 1
            reshoot4 = True

        if reshoot4 is True:
            up4 = Up4(0, 0)
            up4_sprites = pygame.sprite.Group()
            up4_sprites.add(up4)
            up4.rect.x = Shury4.rect.x
            up4.rect.y = Shury4.rect.y
            up4.list = pygame.sprite.Group()
            up4.list.add(up4)

            reshoot4 = False

        shs1 = pygame.sprite.spritecollide(Shury1, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        shs2 = pygame.sprite.spritecollide(Shury2, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        shs3 = pygame.sprite.spritecollide(Shury3, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        shs4 = pygame.sprite.spritecollide(Shury4, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))

        if shs1:

            playerhp += 35
            soul.rect.x = player.rect.x
            soul.rect.y = player.rect.y
            Shury1.rect.x = random.randint(-100, 700)
            Shury1.rect.x = random.randint(-100, 700)

        if shs2:
            playerhp += 25
            soul.rect.x = player.rect.x
            soul.rect.y = player.rect.y
            Shury2.rect.x = random.randint(-100, 700)
            Shury2.rect.x = random.randint(-100, 700)

        if shs3:
            playerhp += 35
            soul.rect.x = player.rect.x
            soul.rect.y = player.rect.y
            Shury3.rect.x = random.randint(-100, 700)
            Shury3.rect.x = random.randint(-100, 700)

        if shs4:
            playerhp += 25
            soul.rect.x = player.rect.x
            soul.rect.y = player.rect.y
            Shury4.rect.x = random.randint(-100, 700)
            Shury4.rect.x = random.randint(-100, 700)

        shp1 = pygame.sprite.spritecollide(Shury1, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        shp3 = pygame.sprite.spritecollide(Shury3, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))

        if shp1:

            playerhp -= 1
            player.rect.x = random.randint(-100, 700)
            player.rect.y = random.randint(-100, 700)


        if shp3:
            playerhp -= 1
            player.rect.x = random.randint(-100, 700)
            player.rect.y = random.randint(-100, 700)


        phb1 = pygame.sprite.spritecollide(boss1, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
        shb1 = pygame.sprite.spritecollide(boss1, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))

        if phb1:

            boss1hp += 1
            player.rect.x = random.randint(-100, 700)
            player.rect.y = random.randint(-100, 700)
            score += 25
            rspt += 1

        if shb1:
            boss1hp += 1
            soul.rect.x = player.rect.x
            soul.rect.y = player.rect.y
            player.rect.x = random.randint(-100, 700)
            player.rect.y = random.randint(-100, 700)
            score += 25
            rspt += 1
        if rspt >= 6.5:

            Shury1 = Shuriken1(0, 0)
            Shury1_sprites = pygame.sprite.Group()
            Shury1_sprites.add(Shury1)
            Shury1.rect.x = player.rect.x
            Shury1.rect.y = random.randint(0, 600)
            Shury1.list = pygame.sprite.Group()
            Shury1.list.add(Shury1)

            Shury2 = Shuriken2(0, 0)
            Shury2_sprites = pygame.sprite.Group()
            Shury2_sprites.add(Shury2)
            Shury2.rect.x = random.randint(0, 1000)
            Shury2.rect.y = player.rect.y
            Shury2.list = pygame.sprite.Group()
            Shury2.list.add(Shury2)

            Shury3 = Shuriken3(0, 0)
            Shury3_sprites = pygame.sprite.Group()
            Shury3_sprites.add(Shury3)
            Shury3.rect.x = random.randint(0, 1000)
            Shury3.rect.y = random.randint(0, 600)
            Shury3.list = pygame.sprite.Group()
            Shury3.list.add(Shury3)

            Shury4 = Shuriken4(0, 0)
            Shury4_sprites = pygame.sprite.Group()
            Shury4_sprites.add(Shury4)
            Shury4.rect.x = random.randint(0, 1000)
            Shury4.rect.y = random.randint(0, 600)
            Shury4.list = pygame.sprite.Group()
            Shury4.list.add(Shury4)

            up1 = Up1(0, 0)
            up1_sprites = pygame.sprite.Group()
            up1_sprites.add(up1)
            up1.rect.x = Shury1.rect.x
            up1.rect.y = Shury1.rect.y
            up1.list = pygame.sprite.Group()
            up1.list.add(up1)

            down1 = Down1(0, 0)
            down1_sprites = pygame.sprite.Group()
            down1_sprites.add(down1)
            down1.rect.x = Shury1.rect.x
            down1.rect.y = Shury1.rect.y
            down1.list = pygame.sprite.Group()
            down1.list.add(down1)

            right1 = Right1(0, 0)
            right1_sprites = pygame.sprite.Group()
            right1_sprites.add(right1)
            right1.rect.x = Shury1.rect.x
            right1.rect.y = Shury1.rect.y
            right1.list = pygame.sprite.Group()
            right1.list.add(right1)

            left1 = Left1(0, 0)
            left1_sprites = pygame.sprite.Group()
            left1_sprites.add(left1)
            left1.rect.x = Shury1.rect.x
            left1.rect.y = Shury1.rect.y
            left1.list = pygame.sprite.Group()
            left1.list.add(left1)

            up2 = Up2(0, 0)
            up2_sprites = pygame.sprite.Group()
            up2_sprites.add(up2)
            up2.rect.x = Shury2.rect.x
            up2.rect.y = Shury2.rect.y
            up2.list = pygame.sprite.Group()
            up2.list.add(up2)

            down2 = Down2(0, 0)
            down2_sprites = pygame.sprite.Group()
            down2_sprites.add(down2)
            down2.rect.x = Shury2.rect.x
            down2.rect.y = Shury2.rect.y
            down2.list = pygame.sprite.Group()
            down2.list.add(down2)

            right2 = Right2(0, 0)
            right2_sprites = pygame.sprite.Group()
            right2_sprites.add(right2)
            right2.rect.x = Shury2.rect.x
            right2.rect.y = Shury2.rect.y
            right2.list = pygame.sprite.Group()
            right2.list.add(right2)

            left2 = Left2(0, 0)
            left2_sprites = pygame.sprite.Group()
            left2_sprites.add(left2)
            left2.rect.x = Shury2.rect.x
            left2.rect.y = Shury2.rect.y
            left2.list = pygame.sprite.Group()
            left2.list.add(left2)

            up3 = Up3(0, 0)
            up3_sprites = pygame.sprite.Group()
            up3_sprites.add(up3)
            up3.rect.x = Shury3.rect.x
            up3.rect.y = Shury3.rect.y
            up3.list = pygame.sprite.Group()
            up3.list.add(up3)

            down3 = Down3(0, 0)
            down3_sprites = pygame.sprite.Group()
            down3_sprites.add(down3)
            down3.rect.x = Shury3.rect.x
            down3.rect.y = Shury3.rect.y
            down3.list = pygame.sprite.Group()
            down3.list.add(down3)

            right3 = Right3(0, 0)
            right3_sprites = pygame.sprite.Group()
            right3_sprites.add(right3)
            right3.rect.x = Shury3.rect.x
            right3.rect.y = Shury3.rect.y
            right3.list = pygame.sprite.Group()
            right3.list.add(right3)

            left3 = Left3(0, 0)
            left3_sprites = pygame.sprite.Group()
            left3_sprites.add(left3)
            left3.rect.x = Shury3.rect.x
            left3.rect.y = Shury3.rect.y
            left3.list = pygame.sprite.Group()
            left3.list.add(left3)

            up4 = Up4(0, 0)
            up4_sprites = pygame.sprite.Group()
            up4_sprites.add(up4)
            up4.rect.x = Shury4.rect.x
            up4.rect.y = Shury4.rect.y
            up4.list = pygame.sprite.Group()
            up4.list.add(up4)

            down4 = Down4(0, 0)
            down4_sprites = pygame.sprite.Group()
            down4_sprites.add(down4)
            down4.rect.x = Shury4.rect.x
            down4.rect.y = Shury4.rect.y
            down4.list = pygame.sprite.Group()
            down4.list.add(down4)

            right4 = Right4(0, 0)
            right4_sprites = pygame.sprite.Group()
            right4_sprites.add(right4)
            right4.rect.x = Shury4.rect.x
            right4.rect.y = Shury4.rect.y
            right4.list = pygame.sprite.Group()
            right4.list.add(right4)

            left4 = Left4(0, 0)
            left4_sprites = pygame.sprite.Group()
            left4_sprites.add(left4)
            left4.rect.x = Shury4.rect.x
            left4.rect.y = Shury4.rect.y
            left4.list = pygame.sprite.Group()
            left4.list.add(left4)

            cshot = True
            rsptc = True
        if rspt >= 6.5:

            Shury1 = Shuriken1(0, 0)
            Shury1_sprites = pygame.sprite.Group()
            Shury1_sprites.add(Shury1)
            Shury1.rect.x = player.rect.x
            Shury1.rect.y = random.randint(0, 600)
            Shury1.list = pygame.sprite.Group()
            Shury1.list.add(Shury1)

            Shury2 = Shuriken2(0, 0)
            Shury2_sprites = pygame.sprite.Group()
            Shury2_sprites.add(Shury2)
            Shury2.rect.x = random.randint(0, 1000)
            Shury2.rect.y = player.rect.y
            Shury2.list = pygame.sprite.Group()
            Shury2.list.add(Shury2)

            Shury3 = Shuriken3(0, 0)
            Shury3_sprites = pygame.sprite.Group()
            Shury3_sprites.add(Shury3)
            Shury3.rect.x = random.randint(0, 1000)
            Shury3.rect.y = random.randint(0, 600)
            Shury3.list = pygame.sprite.Group()
            Shury3.list.add(Shury3)

            Shury4 = Shuriken4(0, 0)
            Shury4_sprites = pygame.sprite.Group()
            Shury4_sprites.add(Shury4)
            Shury4.rect.x = random.randint(0, 1000)
            Shury4.rect.y = random.randint(0, 600)
            Shury4.list = pygame.sprite.Group()
            Shury4.list.add(Shury4)

            up1 = Up1(0, 0)
            up1_sprites = pygame.sprite.Group()
            up1_sprites.add(up1)
            up1.rect.x = Shury1.rect.x
            up1.rect.y = Shury1.rect.y
            up1.list = pygame.sprite.Group()
            up1.list.add(up1)

            down1 = Down1(0, 0)
            down1_sprites = pygame.sprite.Group()
            down1_sprites.add(down1)
            down1.rect.x = Shury1.rect.x
            down1.rect.y = Shury1.rect.y
            down1.list = pygame.sprite.Group()
            down1.list.add(down1)

            right1 = Right1(0, 0)
            right1_sprites = pygame.sprite.Group()
            right1_sprites.add(right1)
            right1.rect.x = Shury1.rect.x
            right1.rect.y = Shury1.rect.y
            right1.list = pygame.sprite.Group()
            right1.list.add(right1)

            left1 = Left1(0, 0)
            left1_sprites = pygame.sprite.Group()
            left1_sprites.add(left1)
            left1.rect.x = Shury1.rect.x
            left1.rect.y = Shury1.rect.y
            left1.list = pygame.sprite.Group()
            left1.list.add(left1)

            up2 = Up2(0, 0)
            up2_sprites = pygame.sprite.Group()
            up2_sprites.add(up2)
            up2.rect.x = Shury2.rect.x
            up2.rect.y = Shury2.rect.y
            up2.list = pygame.sprite.Group()
            up2.list.add(up2)

            down2 = Down2(0, 0)
            down2_sprites = pygame.sprite.Group()
            down2_sprites.add(down2)
            down2.rect.x = Shury2.rect.x
            down2.rect.y = Shury2.rect.y
            down2.list = pygame.sprite.Group()
            down2.list.add(down2)

            right2 = Right2(0, 0)
            right2_sprites = pygame.sprite.Group()
            right2_sprites.add(right2)
            right2.rect.x = Shury2.rect.x
            right2.rect.y = Shury2.rect.y
            right2.list = pygame.sprite.Group()
            right2.list.add(right2)

            left2 = Left2(0, 0)
            left2_sprites = pygame.sprite.Group()
            left2_sprites.add(left2)
            left2.rect.x = Shury2.rect.x
            left2.rect.y = Shury2.rect.y
            left2.list = pygame.sprite.Group()
            left2.list.add(left2)

            up3 = Up3(0, 0)
            up3_sprites = pygame.sprite.Group()
            up3_sprites.add(up3)
            up3.rect.x = Shury3.rect.x
            up3.rect.y = Shury3.rect.y
            up3.list = pygame.sprite.Group()
            up3.list.add(up3)

            down3 = Down3(0, 0)
            down3_sprites = pygame.sprite.Group()
            down3_sprites.add(down3)
            down3.rect.x = Shury3.rect.x
            down3.rect.y = Shury3.rect.y
            down3.list = pygame.sprite.Group()
            down3.list.add(down3)

            right3 = Right3(0, 0)
            right3_sprites = pygame.sprite.Group()
            right3_sprites.add(right3)
            right3.rect.x = Shury3.rect.x
            right3.rect.y = Shury3.rect.y
            right3.list = pygame.sprite.Group()
            right3.list.add(right3)

            left3 = Left3(0, 0)
            left3_sprites = pygame.sprite.Group()
            left3_sprites.add(left3)
            left3.rect.x = Shury3.rect.x
            left3.rect.y = Shury3.rect.y
            left3.list = pygame.sprite.Group()
            left3.list.add(left3)

            up4 = Up4(0, 0)
            up4_sprites = pygame.sprite.Group()
            up4_sprites.add(up4)
            up4.rect.x = Shury4.rect.x
            up4.rect.y = Shury4.rect.y
            up4.list = pygame.sprite.Group()
            up4.list.add(up4)

            down4 = Down4(0, 0)
            down4_sprites = pygame.sprite.Group()
            down4_sprites.add(down4)
            down4.rect.x = Shury4.rect.x
            down4.rect.y = Shury4.rect.y
            down4.list = pygame.sprite.Group()
            down4.list.add(down4)

            right4 = Right4(0, 0)
            right4_sprites = pygame.sprite.Group()
            right4_sprites.add(right4)
            right4.rect.x = Shury4.rect.x
            right4.rect.y = Shury4.rect.y
            right4.list = pygame.sprite.Group()
            right4.list.add(right4)

            left4 = Left4(0, 0)
            left4_sprites = pygame.sprite.Group()
            left4_sprites.add(left4)
            left4.rect.x = Shury4.rect.x
            left4.rect.y = Shury4.rect.y
            left4.list = pygame.sprite.Group()
            left4.list.add(left4)

        if rsptc is True:
            rspt = 0
            rsptc = False

        if cshot is True:
            up1_sprites.draw(screen)
            up2_sprites.draw(screen)
            up3_sprites.draw(screen)
            up4_sprites.draw(screen)
            up1_sprites.update()
            up2_sprites.update()
            up3_sprites.update()
            up4_sprites.update()
            down1_sprites.draw(screen)
            down2_sprites.draw(screen)
            down3_sprites.draw(screen)
            down4_sprites.draw(screen)
            down1_sprites.update()
            down2_sprites.update()
            down3_sprites.update()
            down4_sprites.update()
            right1_sprites.draw(screen)
            right2_sprites.draw(screen)
            right3_sprites.draw(screen)
            right4_sprites.draw(screen)
            right1_sprites.update()
            right2_sprites.update()
            right3_sprites.update()
            right4_sprites.update()
            left1_sprites.draw(screen)
            left2_sprites.draw(screen)
            left3_sprites.draw(screen)
            left4_sprites.draw(screen)
            left1_sprites.update()
            left2_sprites.update()
            left3_sprites.update()
            left4_sprites.update()
        if boss1hp >= 12.5:

            boss2_sprites.draw(screen)
            boss2_sprites.update()

            pygame.sprite.Sprite.kill(boss1)


            phb2 = pygame.sprite.spritecollide(boss2, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            shb2 = pygame.sprite.spritecollide(boss2, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))

            if phb2:
                boss1hp += 2.5
                player.rect.x = random.randint(-100, 100)
                player.rect.y = random.randint(-100, 100)
                score += 25

            if shb2:
                boss1hp += 2.5
                soul.rect.x = player.rect.x
                soul.rect.y = player.rect.y
                score += 25


        if boss1hp >= 25:

            boss3_sprites.draw(screen)
            boss3_sprites.update()

            pygame.sprite.Sprite.kill(boss2)


            phb3 = pygame.sprite.spritecollide(boss3, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            shb3 = pygame.sprite.spritecollide(boss3, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))

            if phb3:
                boss1hp += 2.5
                player.rect.x = random.randint(-100, 100)
                player.rect.y = random.randint(-100, 100)
                score += 25

            if shb3:
                boss1hp += 2.5
                soul.rect.x = player.rect.x
                soul.rect.y = player.rect.y
                score += 25


        if boss1hp >= 37.5:

            boss4_sprites.draw(screen)
            boss4_sprites.update()

            pygame.sprite.Sprite.kill(boss3)

            phb4 = pygame.sprite.spritecollide(boss4, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            shb4 = pygame.sprite.spritecollide(boss4, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))

            if phb4:
                boss1hp += 2.5
                player.rect.x = random.randint(-100, 100)
                player.rect.y = random.randint(-100, 100)
                score += 25

            if shb4:
                boss1hp += 2.5
                soul.rect.x = player.rect.x
                soul.rect.y = player.rect.y
                score += 25




        if boss1hp >= 50:

            cheetosl1_sprites.draw(screen)
            cheetosl1_sprites.update()
            cheetosl2_sprites.draw(screen)
            cheetosl2_sprites.update()
            cheetosl3_sprites.draw(screen)
            cheetosl3_sprites.update()
            boss5_sprites.draw(screen)
            boss5_sprites.update()

            pygame.sprite.Sprite.kill(boss4)

            if cheetosl1.rect.x >= 1100:
                ch1 = True

            if cheetosl2.rect.x >= 1100:
                ch2 = True


            if cheetosl3.rect.x >= 1100:
                ch3 = True

            phb5 = pygame.sprite.spritecollide(boss5, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            shb5 = pygame.sprite.spritecollide(boss5, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            phc1 = pygame.sprite.spritecollide(cheetosl1, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            phc2 = pygame.sprite.spritecollide(cheetosl2, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            phc3 = pygame.sprite.spritecollide(cheetosl3, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            shc1 = pygame.sprite.spritecollide(cheetosl1, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            shc2 = pygame.sprite.spritecollide(cheetosl2, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            shc3 = pygame.sprite.spritecollide(cheetosl3, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))

            if shc1:

                playerhp += 20
                pygame.sprite.Sprite.kill(cheetosl1)
                ch1 = True

            if shc2:
                playerhp += 20
                pygame.sprite.Sprite.kill(cheetosl2)
                ch2 = True

            if shc2:
                playerhp += 20
                pygame.sprite.Sprite.kill(cheetosl3)
                ch3 = True


            if phc1:

                playerhp -= 1
                pygame.sprite.Sprite.kill(cheetosl1)
                ch1 = True

            if ch1 is True:
                cheetosl1 = Cheetosl1(0, 0)
                cheetosl1_sprites = pygame.sprite.Group()
                cheetosl1_sprites.add(cheetosl1)
                cheetosl1.rect.x = 0
                cheetosl1.rect.y = 100
                cheetosl1.list = pygame.sprite.Group()
                cheetosl1.list.add(cheetosl1)
                ch1 = False

            if phc2:
                playerhp -= 1
                pygame.sprite.Sprite.kill(cheetosl2)
                ch2 = True

            if ch2 is True:

                cheetosl2 = Cheetosl2(0, 0)
                cheetosl2_sprites = pygame.sprite.Group()
                cheetosl2_sprites.add(cheetosl2)
                cheetosl2.rect.x = 0
                cheetosl2.rect.y = 100
                cheetosl2.list = pygame.sprite.Group()
                cheetosl2.list.add(cheetosl2)
                ch2 = False

            if phc3:
                playerhp -= 1
                pygame.sprite.Sprite.kill(cheetosl3)
                ch3 = True

            if ch3 is True:
                cheetosl3 = Cheetosl3(0, 0)
                cheetosl3_sprites = pygame.sprite.Group()
                cheetosl3_sprites.add(cheetosl3)
                cheetosl3.rect.x = 0
                cheetosl3.rect.y = 100
                cheetosl3.list = pygame.sprite.Group()
                cheetosl3.list.add(cheetosl3)
                ch3 = False


            if phb5:
                boss1hp += 1
                player.rect.x = random.randint(-100, 100)
                player.rect.y = random.randint(-100, 100)
                score += 25

            if shb5:
                boss1hp += 1
                soul.rect.x = player.rect.x
                soul.rect.y = player.rect.y
                score += 25




        if boss1hp >= 62.5:

            boss6_sprites.draw(screen)
            boss6_sprites.update()
            cheetosr1_sprites.draw(screen)
            cheetosr1_sprites.update()
            cheetosr2_sprites.draw(screen)
            cheetosr2_sprites.update()


            if cheetosr1.rect.x <= -100:
                ch4 = True

            if cheetosr2.rect.x <= -100:
                ch5 = True



            pygame.sprite.Sprite.kill(boss5)
            phc4 = pygame.sprite.spritecollide(cheetosr1, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            phc5 = pygame.sprite.spritecollide(cheetosr2, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            phb6 = pygame.sprite.spritecollide(boss6, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            shb6 = pygame.sprite.spritecollide(boss6, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))


            if phc4:

                playerhp -= 1
                pygame.sprite.Sprite.kill(cheetosr1)
                ch4 = True

            if ch4 is True:
                cheetosr1 = Cheetosr1(0, 0)
                cheetosr1_sprites = pygame.sprite.Group()
                cheetosr1_sprites.add(cheetosr1)
                cheetosr1.rect.x = 1000
                cheetosr1.rect.y = 200
                cheetosr1.list = pygame.sprite.Group()
                cheetosr1.list.add(cheetosr1)
                ch4 = False

            if phc5:
                playerhp -= 1
                pygame.sprite.Sprite.kill(cheetosr2)
                ch5 = True

            if ch5 is True:

                cheetosr2 = Cheetosr2(0, 0)
                cheetosr2_sprites = pygame.sprite.Group()
                cheetosr2_sprites.add(cheetosr2)
                cheetosr2.rect.x = 1000
                cheetosr2.rect.y = 400
                cheetosr2.list = pygame.sprite.Group()
                cheetosr2.list.add(cheetosr2)
                ch5 = False



            if phb6:
                boss1hp += 2.5
                player.rect.x = random.randint(-100, 100)
                player.rect.y = random.randint(-100, 100)
                score += 25

            if shb6:
                boss1hp += 2.5
                soul.rect.x = player.rect.x
                soul.rect.y = player.rect.y
                score += 25


        if boss1hp >= 75:


            boss7_sprites.draw(screen)
            boss7_sprites.update()

            pygame.sprite.Sprite.kill(boss6)

            phb7 = pygame.sprite.spritecollide(boss7, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            shb7 = pygame.sprite.spritecollide(boss7, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))

            if phb7:
                boss1hp += 2.5
                player.rect.x = random.randint(-100, 100)
                player.rect.y = random.randint(-100, 100)
                score += 25

            if shb7:
                boss1hp += 2.5
                soul.rect.x = player.rect.x
                soul.rect.y = player.rect.y
                score += 25


        if boss1hp >= 87.5:

            boss8_sprites.draw(screen)
            boss8_sprites.update()

            pygame.sprite.Sprite.kill(boss7)

            phb8 = pygame.sprite.spritecollide(boss8, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            shb8 = pygame.sprite.spritecollide(boss8, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))

            if phb8:
                boss1hp += 2.5
                player.rect.x = random.randint(-100, 100)
                player.rect.y = random.randint(-100, 100)
                score += 25

            if shb8:
                boss1hp += 2.5
                soul.rect.x = player.rect.x
                soul.rect.y = player.rect.y
                score += 25



        if boss1hp >= 100:

            boss9_sprites.draw(screen)
            boss9_sprites.update()

            pygame.sprite.Sprite.kill(boss8)

            phb9 = pygame.sprite.spritecollide(boss9, player_sprites, False, pygame.sprite.collide_circle_ratio(0.2))
            shb9 = pygame.sprite.spritecollide(boss9, soul_sprites, False, pygame.sprite.collide_circle_ratio(0.2))

            if phb9:
                boss1hp += 2.5
                player.rect.x = random.randint(-100, 100)
                player.rect.y = random.randint(-100, 100)
                score += 25

            if shb9:
                boss1hp += 2.5
                soul.rect.x = player.rect.x
                soul.rect.y = player.rect.y
                score += 25

            winners = True

    if winners is True:
        charmdisplay = False
        hpdisplay = False
        vodka.rect.x = 2000
        grumpy.rect.x = -2000
        soul.rect.x = 2000
        player.rect.x = 2000
        cage.rect.x = 2000
        meow.rect.x = 2000
        hpx = 2000
        hpy = 2000
        hcx = 2000
        hcy = 2000
        scy = 220
        scx = 390
        B2X = 2000
        BY = 2000
        screen.blit(gw, (0, 0))
        screen.blit(gppic, (450, 100))
        screen.blit(catsign, (110, 300))


    if charmdisplay is True:

        if healcharge >= 5:
            screen.blit(c5, (hcx, hcy))

        if healcharge == 4:
            screen.blit(c4, (hcx, hcy))

        if healcharge == 3:
            screen.blit(c3, (hcx, hcy))

        if healcharge == 2:
            screen.blit(c2, (hcx, hcy))

        if healcharge == 1:
            screen.blit(c1, (hcx, hcy))

        if healcharge <= 0:
            screen.blit(c0, (hcx, hcy))

    if gamestart is True:
        pygame.sprite.Sprite.kill(player)
        pygame.sprite.Sprite.kill(glasses)
        pygame.sprite.Sprite.kill(truffles)
        pygame.sprite.Sprite.kill(vodka)
        pygame.sprite.Sprite.kill(meow)
        pygame.sprite.Sprite.kill(grumpy)
        pygame.sprite.Sprite.kill(soul)

        hpdisplay = False

        startgame_sprites.draw(screen)
        startgame_sprites.update()

    if gamestart is False:
        hpdisplay = True
        normalmusic = True
        player_sprites = pygame.sprite.Group()
        player_sprites.add(player)
        player_list = pygame.sprite.Group()
        player_list.add(player)


        grumpy_sprites = pygame.sprite.Group()
        grumpy_sprites.add(grumpy)
        grumpy_list = pygame.sprite.Group()
        grumpy_list.add(grumpy)

        soul_sprites = pygame.sprite.Group()
        soul_sprites.add(soul)
        soul_list = pygame.sprite.Group()
        soul_list.add(soul)

        vodka_sprites = pygame.sprite.Group()
        vodka_sprites.add(vodka)
        vodka_list = pygame.sprite.Group()
        vodka_list.add(vodka)

        meow_sprites = pygame.sprite.Group()
        meow_sprites.add(meow)
        meow_list = pygame.sprite.Group()
        meow_list.add(meow)

        glasses_sprites = pygame.sprite.Group()
        glasses_sprites.add(glasses)
        glasses.list = pygame.sprite.Group()
        glasses.list.add(glasses)

        truffles_sprites = pygame.sprite.Group()
        truffles_sprites.add(truffles)
        truffles.list = pygame.sprite.Group()
        truffles.list.add(truffles)

        border_sprites = pygame.sprite.Group()
        border_sprites.add(border)
        border.list = pygame.sprite.Group()
        border.list.add(border)

        gameover_sprites = pygame.sprite.Group()
        gameover_sprites.add(gameover)
        gameover.list = pygame.sprite.Group()
        gameover.list.add(gameover)

        bingo_sprites = pygame.sprite.Group()
        bingo_sprites.add(bingo)
        bingo.list = pygame.sprite.Group()
        bingo.list.add(bingo)




    if playerhp <= 0:
        pygame.sprite.Sprite.kill(player)
        pygame.sprite.Sprite.kill(glasses)
        pygame.sprite.Sprite.kill(truffles)
        pygame.sprite.Sprite.kill(vodka)
        pygame.sprite.Sprite.kill(soul)
        pygame.sprite.Sprite.kill(grumpy)
        gameover.animate()

        gameover_sprites.draw(screen)
        gameover_sprites.update()
        hpdisplay = False




    if hpdisplay is True:

        if playerhp <= 100:
            screen.blit(hp100, (hpx, hpy))

        if playerhp <= 90:
            screen.blit(hp90, (hpx, hpy))

        if playerhp <= 80:
            screen.blit(hp80, (hpx, hpy))

        if playerhp <= 70:
            screen.blit(hp70, (hpx, hpy))

        if playerhp <= 60:
            screen.blit(hp60, (hpx, hpy))

        if playerhp <= 50:
            screen.blit(hp50, (hpx, hpy))

        if playerhp <= 40:
            screen.blit(hp40, (hpx, hpy))

        if playerhp <= 30:
            screen.blit(hp30, (hpx, hpy))

        if playerhp <= 20:
            screen.blit(hp20, (hpx, hpy))

        if playerhp <= 10:
            screen.blit(hp10, (hpx, hpy))

        if playerhp <= 0:
            screen.blit(hp0, (hpx, hpy))

        if playerhp > 100:
            screen.blit(goldenhp, (hpx, hpy))



    bingo_nm(BX, BY)
    bingo_nm2(B2X, B2Y)
    s_score(scx, scy)
    border_sprites.draw(screen)
    border_sprites.update()
    meow_sprites.draw(screen)
    meow_sprites.update()
    vodka_sprites.draw(screen)
    vodka_sprites.update()
    soul_sprites.draw(screen)
    soul_sprites.update()
    grumpy_sprites.draw(screen)
    grumpy_sprites.update()
    player_sprites.draw(screen)
    player_sprites.update()
    cage_sprites.draw(screen)
    cage_sprites.update()
    pygame.display.update()
    screen.blit(worldbg, (0, 0))
    clock.tick(60)

