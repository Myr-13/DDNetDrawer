from typing import Tuple

import pygame


def is_inside(rect1: Tuple[int, int, int, int], rect2: Tuple[int, int, int, int]) -> bool:
	return pygame.Rect(rect1).colliderect(rect2)
