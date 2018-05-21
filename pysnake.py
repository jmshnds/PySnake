
import pygame
from colors import color # color dictionary
from snake import Snake
from direction import direction
from keys import keycode
from food import Food
from random import randint
from enum import Enum

# screen size
WIDTH = 400
HEIGHT = 300

# size of blocks
BLOCK_S = 10
BLOCK_W = WIDTH / BLOCK_S
BLOCK_H = HEIGHT / BLOCK_S

class Game(Enum):
    MENU = 0
    START = 1
    PAUSE = 2
    END = 3

def process_snake_keys(snake, event):
    # Check if a key has been pressed
    if event.scancode is keycode['up']:
        snake.changeDirection(direction['NORTH'])
    elif event.scancode is keycode['down']:
        snake.changeDirection(direction['SOUTH'])
    elif event.scancode is keycode['left']:
        snake.changeDirection(direction['WEST'])
    elif event.scancode is keycode['right']:
        snake.changeDirection(direction['EAST'])

def process_state_keys(game_state, event):
    if event.scancode is keycode['P']:
        print(game_state)
        return Game.PAUSE if game_state != Game.PAUSE else Game.START
    else:
        return game_state

if __name__ == '__main__':

    pygame.init()
    draw = pygame.draw
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()
    game_state = Game.PAUSE # game starts paused

    # create snake
    snake = Snake(int(BLOCK_W/2), int(BLOCK_H/2))
    snake.grow(5) # start snake at size 6

    # place initial piece of food
    food = Food(randint(0, BLOCK_W-1), randint(0, BLOCK_H-1))

    while game_state is not Game.END:
        for event in pygame.event.get():

            # Check if the window has been closed
            if event.type == pygame.QUIT:
                game_state = Game.END
            elif event.type == pygame.KEYDOWN:
                game_state = process_state_keys(game_state, event) # Process game state keys
                
                if game_state == Game.START:
                    process_snake_keys(snake, event) # Process arrow keys
                    break


            #print(event) # debug print events

        # Draw game objects
        screen.fill(color['white'])
        snake.draw(draw, screen, color['red'], (BLOCK_S, BLOCK_S, BLOCK_S, BLOCK_S))
        food.draw(draw, screen, color['blue'], (BLOCK_S, BLOCK_S, BLOCK_S, BLOCK_S))

        # Move snake and check snake conditions
        if game_state == Game.START:
            snake.move()

            # Check if the snake has moved off screen
            if snake.x < 0:
                snake.x = BLOCK_W
            elif snake.x >= BLOCK_W:
                snake.x = 0
            if snake.y < 0:
                snake.y = BLOCK_H
            elif snake.y >= BLOCK_H:
                snake.y = 0

            # Check if the snake ran into its tail
            for i in range(1, len(snake.tail)):
                if snake.x == snake.tail[i].x and snake.y == snake.tail[i].y:
                    print("Game over: tail")
                    game_state = Game.END

            # Check if the snake has eaten a piece of food
            if snake.x == food.x and snake.y == food.y:
                if not food.isPoison:
                    snake.grow(2)
                    # change position
                    food.x = randint(0, BLOCK_W-1)
                    food.y = randint(0, BLOCK_H-1)
                else:
                    print("Game Over: poison food")
                    game_state = Game.END

        pygame.display.update() # Update game display
        clock.tick(12) # FPS

    pygame.quit() # Quit pygame instance

