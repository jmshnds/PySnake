
import pygame
from random import randint

from button import Button
from colors import Color
from direction import Direction
from food import Food
from keys import keycode
from snake import Snake

# screen size
WIDTH = 400
HEIGHT = 300

# size of blocks
BLOCK_S = 10
BLOCK_W = WIDTH / BLOCK_S
BLOCK_H = HEIGHT / BLOCK_S

class Game:
    MENU = 0
    START = 1
    PAUSE = 2
    END = 3

def process_snake_keys(snake, event):
    # Check if a key has been pressed
    if event.scancode is keycode['up']:
        snake.changeDirection(Direction.NORTH)
    elif event.scancode is keycode['down']:
        snake.changeDirection(Direction.SOUTH)
    elif event.scancode is keycode['left']:
        snake.changeDirection(Direction.WEST)
    elif event.scancode is keycode['right']:
        snake.changeDirection(Direction.EAST)

def process_state_keys(game_state, event):
    if event.scancode is keycode['P']:
        return Game.PAUSE if game_state != Game.PAUSE else Game.START
    else:
        return game_state

if __name__ == '__main__':
    pygame.init()
    draw = pygame.draw
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()
    game_state = Game.MENU # game starts at main menu

    # create snake
    snake = Snake(int(BLOCK_W/2), int(BLOCK_H/2))
    snake.grow(5) # start snake at size 6

    # Place initial piece of food
    food = Food(randint(0, BLOCK_W-1), randint(0, BLOCK_H-1))
   
    # Initialize buttons
    start_button = Button(BLOCK_S*BLOCK_W/2, BLOCK_S*BLOCK_H/2, BLOCK_S*6, BLOCK_S*2, "start")

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.isClicked(event.pos):
                    game_state = Game.START
                    break


            #print(event) # debug print events

        if game_state == Game.MENU:
            screen.fill(Color.WHITE)
            start_button.draw(draw, screen, Color.GREEN)
        elif game_state == Game.START:
            # Draw game objects
            screen.fill(Color.WHITE)
            snake.draw(draw, screen, Color.RED, (BLOCK_S, BLOCK_S, BLOCK_S, BLOCK_S))
            food.draw(draw, screen, Color.BLUE, (BLOCK_S, BLOCK_S, BLOCK_S, BLOCK_S))

            # Move snake and check snake conditions
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

