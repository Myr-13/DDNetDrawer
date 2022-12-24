import pygame
import random


pygame.init()


def rand_choice(arr):
	return random.choice(arr)


# Projectiles
PICKUPS = pygame.image.load("data/pickups.png")
LASER_1 = PICKUPS.subsurface((0, 0, 64, 64))
LASER_2 = PICKUPS.subsurface((64, 0, 64, 64))
LASER_3 = PICKUPS.subsurface((128, 0, 64, 64))
LASERS = [LASER_1, LASER_2, LASER_3]
# Pickups
HEART = PICKUPS.subsurface((0, 160, 64, 64))
ARMOR = PICKUPS.subsurface((64, 160, 64, 64))
# Weapons
GUN = PICKUPS.subsurface((128, 80, 128, 64))
HAMMER = PICKUPS.subsurface((128, 144, 128, 64))
LASER = PICKUPS.subsurface((0, 240, 256, 96))
GRENADE = PICKUPS.subsurface((0, 336, 256, 64))
SHOTGUN = PICKUPS.subsurface((0, 400, 256, 64))
CATANA = PICKUPS.subsurface((0, 464, 256, 64))

# Tools
TOOLS = pygame.image.load("data/tools.png")
LASER_TOOL = TOOLS.subsurface((0, 0, 48, 48))
PICKUP_TOOL = TOOLS.subsurface((48, 0, 48, 48))

FONT = pygame.font.Font("data/font.otf", 256)
