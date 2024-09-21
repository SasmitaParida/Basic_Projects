import pygame
import time
import random

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display configurations
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15  # Initial speed

font_style = pygame.font.SysFont(None, 50)
bold_font = pygame.font.Font(None, 50)
message_font = pygame.font.Font(None, 36)


def our_snake(snake_block, snake_list, score):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
    # Draw snake head as a red circle
    pygame.draw.circle(dis, red, (snake_list[-1][0] + snake_block // 2, snake_list[-1][1] + snake_block // 2),
                       snake_block // 2)
    score_font = font_style.render("Score: " + str(score), True, black)
    dis.blit(score_font, [0, 0])


def message(msg_lines, color, size, pos):
    y_pos = pos[1]
    for line in msg_lines:
        mesg = bold_font.render(line, True, color)
        dis.blit(mesg, [pos[0], y_pos])
        y_pos += size * 1.2  # Add some space between lines


def gameLoop():
    global snake_speed  # Define snake_speed as global
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    score = 0
    high_score = 0

    while not game_over:

        while game_close:
            dis.fill(blue)
            if score > high_score:
                high_score = score
            message(["You lost😔", f"Score: {score} High Score: {high_score}", "Press Q-Quit or C-Play Again"], red, 50, (dis_width / 2 - 150, dis_height / 2 - 50))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        score = 0
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list, score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 5  # Increase score by 5 when food is eaten
            snake_speed += 1  # Increase speed as the snake grows

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
