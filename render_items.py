from typing import Tuple
import pygame


class RenderRect:
	def __init__(self, x: int, y: int, w: int, h: int, color: Tuple[int, int, int], ui: bool):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.color = color
		self.ui = ui


class RenderTexture:
	def __init__(self, x: int, y: int, w: int, h: int, texture: pygame.Surface, ui: bool):
		self.x = x
		self.y = y
		texture = pygame.transform.scale(texture, (w, h))
		self.texture: pygame.Surface = texture
		self.ui = ui


class RenderLine:
	def __init__(self, x1: int, y1: int, x2: int, y2: int, color: Tuple[int, int, int], width: int, ui: bool):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.color = color
		self.width = width
		self.ui = ui
