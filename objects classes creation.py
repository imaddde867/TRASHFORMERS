import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Trash Picker Game")

# Set up clock
clock = pygame.time.Clock()

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - 50)

# NPC class
class NPC(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, width), random.randint(0, height))

# Trash class
class Trash(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Replace with your trash image
        self.image = pygame.Surface((20, 20))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, width), 0)

# Create player, NPCs, and trash groups
player = Player()
npcs = [NPC() for _ in range(2)]
trash_group = pygame.sprite.Group([Trash() for _ in range(5)])

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update game logic
    player_rect = player.rect

    # Move NPCs
    for npc in npcs:
        npc.rect.x += random.choice([-1, 1])  # Random movement left or right
        npc.rect.y += random.choice([-1, 1])  # Random movement up or down

    # Move trash
    for trash in trash_group:
        trash.rect.y += 5  # Adjust the speed of falling trash

        # Check collision with player
        if pygame.sprite.collide_rect(player, trash):
            trash_group.remove(trash)  # Remove trash when picked up

    # Draw background
    screen.fill(white)

    # Draw player, NPCs, and trash
    screen.blit(player.image, player_rect)
    for npc in npcs:
        screen.blit(npc.image, npc.rect)
    trash_group.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
