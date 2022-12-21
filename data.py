import pygame
import random


def rand_choice(arr):
	return random.choice(arr)


LASER_1 = pygame.image.load("data/laser_1.png")
LASER_2 = pygame.image.load("data/laser_2.png")
LASER_3 = pygame.image.load("data/laser_3.png")
LASERS = [LASER_1, LASER_2, LASER_3]
