import pygame
import sys
from game_window_class import *
from button_class import *
from text_class import *

WIDTH, HEIGHT = 800, 1000
BACKGROUND = (100, 200, 150)
FPS = 60
newFPS = FPS


#-Setting--------------------------#
def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def update():
    global FPS
    global newFPS
    game_window.update()
    if FPS != 60:
        FPS = 60
        newFPS = FPS
        buttons.pop
        buttons.append(Button(window, WIDTH/4 - 50, 50, 50, 30, text=str(FPS), color=(20,50,20), hover_color=(20,50,20), state='', function=0))
    for button in buttons:
        button.update(mouse_pos, game_state=state)

def draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    for text in texts:
        text.draw()
    game_window.draw()
#-Running--------------------------#
def running_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def running_update():
    global FPS
    global newFPS
    game_window.update()
    if FPS != newFPS:
        FPS = newFPS
        newFPS = FPS
        buttons.pop
        buttons.append(Button(window, WIDTH/4 - 50, 50, 50, 30, text=str(FPS), color=(20,50,20), hover_color=(20,50,20), state='', function=0))
    for button in buttons:
        button.update(mouse_pos, game_state=state)
    game_window.evaluate()

def running_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    for text in texts:
        text.draw()
    game_window.draw()

#-Paused--------------------------#

def paused_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def paused_update():
    global FPS
    global newFPS
    game_window.update()
    if FPS != newFPS:
        FPS = newFPS
        newFPS = FPS
        buttons.pop
        buttons.append(Button(window, WIDTH/4 - 50, 50, 50, 30, text=str(FPS), color=(20,50,20), hover_color=(20,50,20), state='', function=0))
    for button in buttons:
        button.update(mouse_pos, game_state=state)

def paused_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    for text in texts:
        text.draw()
    game_window.draw()
#---------------------------#

def mouse_on_grid(pos):
    if pos[0] > 100 and pos[0] < WIDTH-100:
        if pos[1] > 180 and pos[1] < HEIGHT-20:
            return True
    return False

def click_cell(pos):
    grid_pos = [pos[0]-100, pos[1]-180]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True

def make_buttons():
    buttons = []
    buttons.append(Button(window, WIDTH/3 - 50, 50, 100, 30, text='Start', color=(20,50,20), hover_color=(100,155,125), function=run_game, state='setting'))
    buttons.append(Button(window, WIDTH/2 - 50, 50, 100, 30, text='Pause', color=(20,20,50), hover_color=(100,125,155), function=pause_game, state='running'))
    buttons.append(Button(window, WIDTH/1.5 - 50, 50, 100, 30, text='Clear', color=(50,20,20), hover_color=(155,100,125), function=reset_game, state='paused'))
    buttons.append(Button(window, WIDTH/3 - 50, 50, 100, 30, text='Resume', color=(20,50,20), hover_color=(100,155,125), function=run_game, state='paused'))
    buttons.append(Button(window, WIDTH/1.5 - 50, 50, 100, 30, text='Random', color=(225,150,150), hover_color=(150,50,50), function=game_window.randomize, state='setting'))
    buttons.append(Button(window, WIDTH/4 - 50, 10, 50, 30, text='↑', color=(150,200,200), hover_color=((150,200,150)), function=increase_speed, state=''))
    buttons.append(Button(window, WIDTH/4 - 50, 90, 50, 30, text='↓', color=(200,200,150), hover_color=((150,200,150)), function=decrease_speed, state=''))
    buttons.append(Button(window, WIDTH/4 - 50, 50, 50, 30, text=str(FPS), color=(20,50,20), hover_color=(20,50,20), state='', function=0))
    return buttons

def make_texts():
    texts = []
    rulesText = ['Any live cell with fewer than two live neighbours dies, as if by underpopulation.', 'Any live cell with two or three live neighbours lives on to the next generation.', 'Any live cell with more than three live neighbours dies, as if by overpopulation.','Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.']
    count = 0
    for t in range(len(rulesText)):
        texts.append(Text(window, WIDTH/4 - 100, 800 + count, 600, 25, text_size=15, color=(80, 120, 80), content=rulesText[t]))
        count += 25
    return texts

def run_game():
    global state
    state = 'running'
    print(state)

def pause_game():
    global state
    state = 'paused'
    print(state)

def reset_game():
    global state
    state = 'setting'
    game_window.reset_grid()


def increase_speed():
    global newFPS
    newFPS += 10

    
def decrease_speed():
    global newFPS
    if FPS > 10:
        newFPS -= 10



pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Conways Game of Life')
clock = pygame.time.Clock()
game_window = Game_window(window, 100, 180)
buttons = make_buttons()
texts = make_texts()
state = 'setting'


running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    if state == 'setting':
        get_events()
        update()
        draw()
    if state == 'running':
        running_get_events()
        running_update()
        running_draw()
    if state == 'paused':
        paused_get_events()
        paused_update()
        paused_draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()