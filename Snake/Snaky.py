import pygame
import time

win =  pygame.display.set_mode((500,480),pygame.HWSURFACE)


class Player :
    x =  0
    y = 0
    speed  = 20
    direction = 0

    def update(self):
        if self.direction == 0:
            self.x = self.x + self.speed
        if self.direction == 1:
            self.x = self.x - self.speed
        if self.direction == 2:
            self.y = self.y - self.speed
        if self.direction == 3:
            self.y = self.y + self.speed

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

class App:
    def __init__(self):
        self.windowWidth = 800
        self.windowHeight = 600
        self.player = 0
        self._running = True
        self.background = None
        self._image_surf = None
        self.player = Player()

    def on_init(self):
        pygame.init()

        self.background = pygame.display.set_mode((self.windowWidth,self.windowHeight),pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')

        self._running = True
        self.block = pygame.draw.rect(win,(255, 0, 0),(20,20,20,20))

    def on_event(self, event):
            if event.type == QUIT:
                self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        
        self.background.blit(win, (self.player.x, self.player.y))
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.get()
            keys = pygame.key.get_pressed()

            if (keys[pygame.K_RIGHT]):
                self.player.moveRight()

            if (keys[pygame.K_LEFT]):
                self.player.moveLeft()

            if (keys[pygame.K_UP]):
                self.player.moveUp()

            if (keys[pygame.K_DOWN]):
                self.player.moveDown()

            if (keys[pygame.K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()