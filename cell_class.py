import pygame
import random

white = (255,255,255)
black = (0,0,0)

class Cell:
    def __init__(self, surface, grid_x, grid_y):
        self.alive = False
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect()
        self.neighbors = []
        self.alive_neighbors = 0
    
    def update(self):
        self.rect.topleft = (self.grid_x*20, self.grid_y*20)


    def draw(self):
        if self.alive:
            self.image.fill(black)
        else:
            self.image.fill(black)
            pygame.draw.rect(self.image, white, (1,1,18,18))
        self.surface.blit(self.image, (self.grid_x*20, self.grid_y*20))

    def get_neighbors(self, grid):
        neighbor_count = [[0, 1], [ 1, 0], [1, 1], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1]]
        for neighbor in neighbor_count:
            neighbor[0] += self.grid_x
            neighbor[1] += self.grid_y
        for neighbor in neighbor_count:
            if neighbor[0] < 0:
                neighbor[0] += 30
            if neighbor[1] < 0:
                neighbor[1] += 30
            if neighbor[1] > 29:
                neighbor[1] -= 30
            if neighbor[0] > 29:
                neighbor[0] -= 30
        for neighbor in neighbor_count:
            try:
                self.neighbors.append(grid[neighbor[1]][neighbor[0]])
            except:
                print(neighbor)
    
    def live_neighbors(self):
        count = 0
        for neighbor in self.neighbors:
            if neighbor.alive:
                count +=1
        
        self.alive_neighbors = count