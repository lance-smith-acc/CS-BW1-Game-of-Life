import pygame
vec = pygame.math.Vector2

class Text:
    def __init__(self, surface, x, y, width, height, color=(0,0,0), content='', font_name="arial", text_size=20, text_color=(255,255,255)):
        self.type = 'button'
        self.x = x
        self.y = y
        self.pos = vec(x,y)
        self.width = width
        self.height = height
        self.surface = surface
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.color = color
        self.content = content
        self.text_color = text_color
        self.font_name = font_name
        self.text_size = text_size

    def draw(self):
        self.image.fill(self.color)
        font = pygame.font.SysFont(self.font_name, self.text_size)
        text = font.render(self.content, False, self.text_color)
        size = text.get_size()
        x, y = self.width//2-(size[0]//2), self.height//2-(size[1]//2)
        pos = vec(x,y)
        self.image.blit(text, pos)
        self.surface.blit(self.image, self.pos)
