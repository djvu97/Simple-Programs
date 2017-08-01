import copy
import pygame
import random
import time
cells = [[i for i in range(50)] for i in range(50)]
def generate():
        for x in xrange(50):
                for y in xrange(50):
                        cells[x][y] = random.randint(0, 1)
def update():
        cells2=copy.deepcopy(cells)
        neighbours = [[-1,-1],[-1,0],[-1,+1],[0,-1],[0,+1],[+1,-1],[+1,0],[+1,+1]]
        for x in xrange(50):
                for y in xrange(50):
                        ngb=0
                        for i in neighbours:
                                dy=i[0]+y
                                dx=i[1]+x
                                dx=dx%50;
                                dy=dy%50;
                                if cells2[dx][dy]==1:
                                        ngb+=1
                        if cells2[x][y]==1 and 2<=ngb<=3:
                                cells[x][y]=1
                        else:
                                cells[x][y]=0
                        if cells2[x][y]==0 and ngb==3:
                                cells[x][y]=1                                
pygame.init()
color1=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
color2=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
pygame. display.set_caption("Conway's Game of life")
print("Conway's Game of life")
print("Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.")
print("RULES:-")
print("1)Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.")
print("2)Any live cell with two or three live neighbours lives on to the next generation.")
print("3)Any live cell with more than three live neighbours dies, as if by overpopulation.")
print("4)Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.")
scrn = pygame.display.set_mode((500, 500))
mainsrf = pygame.Surface((500, 500))
mainsrf.fill((255, 255, 255))
clock = pygame.time.Clock()
generate()
while 1:
        clock.tick(20)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
        for y in xrange(50):
                for x in xrange(50):
                        if cells[x][y]==1:
                                pygame.draw.rect(mainsrf, color1, (x*10, y*10, 10, 10))
                        else:
                                pygame.draw.rect(mainsrf,color2, (x*10, y*10, 10, 10))
        update()
        scrn.blit(mainsrf, (0, 0))
        pygame.display.update()
