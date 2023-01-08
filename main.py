import sys
from random import random

import pygame

#create a level class with a backround, a list of obstacles, and a player, and a name
class Level:
    def __init__(self, name, background, obstacles, player):
        self.name = name
        self.background = background
        self.obstacles = obstacles
        self.player = player

# Create an obstacle
#create an obstacle class
class Obstacle:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.x -=3

    def off_screen(self):
        return self.x < -50

    def collision(self, other):
        # check collision detection based on img size
        collided = pygame.Rect((self.x, self.y), (self.img.get_width(), self.img.get_height())).colliderect(pygame.Rect((other.x, other.y), (other.img.get_width(), other.img.get_height())))
        if collided:
            print('collision detected')
        return collided

#create a player class
class Player:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.dy = 0

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def jump(self):
        self.dy = -10

    def move(self):
        self.y += self.dy
        self.dy += 1

    def off_screen(self):
        return self.y > 300

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((512, 512))

# Set the title of the window
pygame.display.set_caption('Poseidon''s Odyssey')

# Create a clock to control the game's frame rate
clock = pygame.time.Clock()

player_dy = 0

#create a pet character
pet_img = pygame.image.load('doggie.png')

#create the shark obstacle
shark_img = pygame.image.load('shark.png')
shark = Obstacle(550 + random() * 200, random() * 200 + 100, shark_img)

#create the stingray obstacle
stingray_img = pygame.image.load('stingray.png')
stingray = Obstacle(550 + random() * 200, random() * 200 + 100, stingray_img)

#create the pufferfish obstacle
pufferfish_img = pygame.image.load('pufferfish.png')
pufferfish = Obstacle(550 + random() * 200, random() * 200 + 100, pufferfish_img)

#create the bird obstacle
bird_img = pygame.image.load('bird.png')
bird = Obstacle(550 + random() * 200, random() * 200 + 100, bird_img)

#create the rock obstacle
rock_img = pygame.image.load('rock.png')
rock = Obstacle(550 + random() * 200, random() * 200 + 100, rock_img)

#create a level list
level_list = []

#create level 1 with the ocean background, the shark, stingray, and pufferfish obstacles, and the poseidon player
level_list.append(Level("Under The Ocean", pygame.image.load('ocean.png'), [shark, stingray, pufferfish], Player(50, 300, pygame.image.load('poseidon.png'))))

#create level 2 with the sky background, the bird and rock obstacles, and the chariot player
level_list.append(Level("In The Sky", pygame.image.load('sky.png'), [bird], Player(50, 300, pygame.image.load('chariot.png'))))

#start the game on level 1
level = level_list[0]

# Set up the pet's starting position and speed
pet_x = 0
pet_y = 0
pet_speed = 5

jump_strength = 10

# Set up the game clock
clock = pygame.time.Clock()

# Create a flag to indicate if the game is over
game_over = False

#create a flag to indicate if the game is won
game_won = False

#show a dark screen with the title of the game "Poseidon's Odyssey"
screen.fill((0, 0, 0))
font = pygame.font.SysFont('Arial', 30)
text = font.render('Poseidon\'s Odyssey', True, (255, 255, 255))
screen.blit(text, (150, 200))
pygame.display.flip()

# Wait for the user to press a key
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            break
    else:
        continue
    break

#set the time_limit to 10 seconds
time_limit = 10000

#repeat the gameloop in the next level if the player wins
while not game_over:
    #use the obstacles in the current level
    obstacles = level.obstacles
    #use the player in the current level
    player = level.player
    #use the background in the current level
    background = level.background
    game_won = False

    # reset the game clock
    start_time = pygame.time.get_ticks()
    background_x = 0
    background_y = 0

    #when the current level starts show the caption of the current level
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(level.name, True, (255, 255, 255))
    screen.blit(text, (150, 200))
    pygame.display.flip()

    # Wait for the user to press a key
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                break
        else:
            continue
        break

    # Run the game loop until the game is lost or won
    while not game_over and not game_won:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player_dy = -5
        # Update the player position
        player.y += player_dy
        player_dy += 0.5
        if player.y > 350:
            player.y = 350
            player_dy = 0
        # Update the obstacle position
        for obstacle in obstacles:
            obstacle.move()
            if obstacle.off_screen():
                #once the obstacle is off the screen, move it to a new random position
                obstacle.x = 550 + random() * 200
                obstacle.y = random() * 200 + 100

        #Update the pet's position to follow the player
        pet_x = player.x - 20
        pet_y = player.y

        # Check if the player and obstacle have collided
        for obstacle in obstacles:
            if obstacle.collision(player):
                game_over = True
                #add a message to the screen that says "Game Over"
                font = pygame.font.SysFont('Arial', 30)
                text = font.render('Game Over', True, (255, 0, 0))
                screen.blit(text, (200, 200))

        # Draw the background
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        #scroll the background
        screen.blit(background, (background_x, background_y))
        background_x -= 1
        if background_x < -512:
            background_x = 0
        #use pygame transform to flip the background
        screen.blit(pygame.transform.flip(background, True, False), (background_x + 512, background_y))

        # Draw the game objects
        player.draw()
        screen.blit(pet_img, (pet_x,pet_y))
        # Draw the obstacles
        for obstacle in obstacles:
            obstacle.draw()

        #draw the remaining time on the screen
        elapsed_time = pygame.time.get_ticks() - start_time
        remaining_time = time_limit - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
        font = pygame.font.SysFont('Arial', 30)
        text = font.render('Time: ' + str(remaining_time // 1000), True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(60)

        #if the player has not collided with an obstacle for 2 minutes, the player wins
        if pygame.time.get_ticks() - start_time > time_limit:
            game_won = True

            #if the player wins, move to the next level from the current level
            level = level_list[level_list.index(level) + 1]

            #once the game is over, display a message to the player
            font = pygame.font.SysFont('Arial', 30)
            text = font.render('You Win!', True, (255, 255, 255))
            screen.blit(text, (200, 200))

            # wait for 2 seconds before closing the game
            pygame.time.wait(2000)


#wait for 2 seconds before closing the game
pygame.time.wait(2000)


# Quit the game
pygame.quit()