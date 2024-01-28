import pygame
import random
import os
import math

class FallingImage:
    def __init__(self, image_path, position, scale_factor=1):
        original_image = pygame.image.load(image_path)
        original_width, original_height = original_image.get_size()

        # Scale the image
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        self.image = pygame.transform.scale(original_image, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.fall_speed = random.uniform(1, 3)

    def update(self, target_position, ground_rect):
        # Calculate direction towards the target point
        direction = pygame.math.Vector2(target_position[0] - self.rect.x, target_position[1] - self.rect.y)
        direction.normalize_ip()

        # Update position based on the direction and a slower fall speed
        self.rect.x += direction.x * (self.fall_speed * 0.5)
        self.rect.y += direction.y * (self.fall_speed * 0.5)

        # Check if the image is within the ground rectangle
        if self.rect.colliderect(ground_rect):
            # Stop falling only if the image is almost inside the rectangle
            if (
                self.rect.x >= ground_rect.x
                and self.rect.x + self.rect.width <= ground_rect.x + ground_rect.width
                and self.rect.y >= ground_rect.y
                and self.rect.y + self.rect.height <= ground_rect.y + ground_rect.height
            ):
                self.fall_speed = 0

class FallingImagesGame:
    def __init__(self, screen_width, screen_height, trash):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Falling Images Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.falling_images = []
        self.trash = trash
        self.spawn_positions = [
            (399, 134), (1192, 122), (1105, 64), (1361, 71), (1354, 295),
            (1449, 147), (1445, 347), (1385, 482), (1447, 550), (1358, 594),
            (1357, 773), (1201, 716), (1097, 726), (935, 779), (756, 780),
            (826, 731), (698, 691), (500, 783), (437, 725), (293, 718),
            (326, 778), (211, 654), (156, 641), (152, 509), (247, 555),
            (247, 316), (207, 209), (154, 290), (159, 360), (291, 129), (408, 74)
        ]
        self.spawn_timer = 0
        self.spawn_delay = 60  # Set a longer delay for spawning

    def get_random_image_path(self):
        image_files = [f for f in os.listdir(self.trash) if f.endswith(('.png', '.jpg', '.jpeg'))]
        if not image_files:
            return None
        return os.path.join(self.trash, random.choice(image_files))

    def spawn_falling_image(self):
        image_path = self.get_random_image_path()
        if image_path:
            position = random.choice(self.spawn_positions)
            falling_image = FallingImage(image_path, position, scale_factor=1)
            self.falling_images.append(falling_image)

    def run(self):
        target_position = (800, 450)  # Set the target position
        ground_rect = pygame.Rect(255, 212, 1090, 478)  # Define the ground rectangle

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.spawn_timer += 1
            if self.spawn_timer >= self.spawn_delay:
                self.spawn_falling_image()
                self.spawn_timer = 0

            for falling_image in self.falling_images:
                falling_image.update(target_position, ground_rect)

            self.screen.fill((255, 255, 255))  # White background

            for falling_image in self.falling_images:
                self.screen.blit(falling_image.image, falling_image.rect)

            pygame.display.flip()
            self.clock.tick(60)  # Adjust the frame rate as needed

        pygame.quit()

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.realpath(__file__))
    trash = os.path.join(script_directory, 'trash')
    game = FallingImagesGame(1600, 900, trash)
    game.run()
