import pygame,sys
from pygame.locals import*
import math
def draw_centered(surface1, surface2, position):
    rect = surface1.get_rect()
    rect = rect.move(position[0]-rect.width//2, position[1]-rect.height//2)
    surface2.blit(surface1, rect)


def pivot_centre(image, rect, angle):
        rotate_image = pygame.transform.rotate(image, angle)
        rotate_rect = rotate_image.get_rect(center=rect.center)
        return rotate_image,rotate_rect


def distance(p, q):
    return math.sqrt(p**2+q**2)

pygame.init()

longueur = 900
hauteur = 900

monImage = pygame.image.load("dragon.png")

fenetre = pygame.display.set_mode((longueur,hauteur))
pygame.display.set_caption("Mon jeu !")

class Spaceship(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = monImage
        self.rect = self.image.get_rect(center=(x,y))
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.moteur_off = False
        self.position = list(position[:])
        self.direction = [0,-1]
    def draw(self,ecran):
        if self.moteur_off:
            new_image, rect = pivot_centre(self.image, monImage.get_rect(),self.angle)
        else:
            new_image, rect = pivot_centre(self.image,self.image.get_rect(), self.angle)
        draw_centered(new_image, ecran, self.position)
    def move(self):
        self.direction[0] = math.sin(-math.radians(self.angle))
        self.direction[1] = -math.cos(math.radians(self.angle))
        self.position[0] += self.direction[0] * self.speed
        self.position[1] += self.direction[1] * self.speed
    def update(self):
        touches = pygame.key.get_pressed()
        if touches[pygame.K_UP]:
            self.moteur_off = True
            if  self.speed<20:
                self.speed += 1
        else:
            if  self.speed>0:
                self.speed -= 1
            self.moteur_off = False

fps = 30
boucle = True
x=10
y=10
vaisseau = Spaceship ((longueur // 2, hauteur // 2))

while boucle:
    pygame.time.delay(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boucle = False
    fenetre.fill((159,159,159))
    touches = pygame.key.get_pressed()
    if touches[K_RIGHT]:
        vaisseau.angle -= 10
        vaisseau.angle %= 360
    if touches[K_LEFT]:
        vaisseau.angle += 10
        vaisseau.angle %= 360
    vaisseau.draw(fenetre)
    vaisseau.move()
    vaisseau.update()
    pygame.display.update()
pygame.quit()
