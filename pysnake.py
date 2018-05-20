
import pygame
from colors import color # color dictionary
from snake import Snake
from direction import direction
from keys import keycode
from food import Food
from random import randint

# screen size
WIDTH = 400
HEIGHT = 300

# size of blocks
BLOCK_S = 10
BLOCK_W = WIDTH / BLOCK_S
BLOCK_H = HEIGHT / BLOCK_S

if __name__ == '__main__':

    pygame.init()
    draw = pygame.draw
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()
    exit_game = False

    # create snake
    snake = Snake(int(BLOCK_W/2), int(BLOCK_H/2))
    snake.grow(5) # start snake at size 6

    # place initial piece of food
    food = Food(randint(0, BLOCK_W-1), randint(0, BLOCK_H-1))

    while not exit_game:
        for event in pygame.event.get():

            # Check if the window has been closed
            if event.type == pygame.QUIT:
                exit_game = True

            # Check if a key has been pressed
            elif event.type == pygame.KEYDOWN:
                if event.scancode is keycode['up']:
                    snake.changeDirection(direction['NORTH'])
                elif event.scancode is keycode['down']:
                    snake.changeDirection(direction['SOUTH'])
                elif event.scancode is keycode['left']:
                    snake.changeDirection(direction['WEST'])
                elif event.scancode is keycode['right']:
                    snake.changeDirection(direction['EAST'])

            #print(event) # debug print events

        # draw background
        screen.fill(color['white'])

        # draw snake
        for tail_piece in snake.tail:
            #print(tail_piece.toString()) # print tailpiece information
            draw.rect(screen, color['red'], (tail_piece.x*BLOCK_S, tail_piece.y*BLOCK_S, BLOCK_S, BLOCK_S))

        # draw food
        draw.rect(screen, color['blue'], (food.x*BLOCK_S, food.y*BLOCK_S, BLOCK_S, BLOCK_S))

        snake.move()
        # check if snake has moved off screen
        if snake.x < 0:
            snake.x = BLOCK_W
        elif snake.x >= BLOCK_W:
            snake.x = 0
        if snake.y < 0:
            snake.y = BLOCK_H
        elif snake.y >= BLOCK_H:
            snake.y = 0

        # check if snake ran into tail
        for i in range(1, len(snake.tail)):
            if snake.x == snake.tail[i].x and snake.y == snake.tail[i].y:
                print("Game over")
                exit_game = True

        # check if the food has been eaten
        if snake.x == food.x and snake.y == food.y:
            snake.grow(2)
            # change position
            food.x = randint(0, BLOCK_W-1)
            food.y = randint(0, BLOCK_H-1)

        pygame.display.update()
        clock.tick(12) # FPS

    pygame.quit() # quit pygame instance
