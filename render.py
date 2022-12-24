import math
from typing import Tuple

import pygame
import config


class RenderRect:
	def __init__(self, x: int, y: int, w: int, h: int, color: Tuple[int, int, int]):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.color = color


class RenderTexture:
	def __init__(self, x: int, y: int, w: int, h: int, texture: pygame.Surface):
		self.x = x
		self.y = y
		texture = pygame.transform.scale(texture, (w, h))
		self.texture: pygame.Surface = texture


class RenderLine:
	def __init__(self, x1: int, y1: int, x2: int, y2: int, color: Tuple[int, int, int], width: int):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.color = color
		self.width = width


class Renderer:
	def __init__(self):
		self.win = pygame.display.set_mode((config.conf["SCREEN_WIDTH"], config.conf["SCREEN_HEIGHT"]))
		pygame.display.set_caption("DDNetDrawer " + config.conf["VERSION"])
		self.clock = pygame.time.Clock()
		self._render_query = []

	def add_rect(self, x: int, y: int, w: int, h: int, color: Tuple[int, int, int]):
		obj = RenderRect(x, y, w, h, color)
		self._render_query.append(obj)

	def add_texture(self, x: int, y: int, w: int, h: int, image: pygame.Surface):
		obj = RenderTexture(x, y, w, h, image)
		self._render_query.append(obj)

	def add_line(self, x1: int, y1: int, x2: int, y2: int, color: Tuple[int, int, int], width: int = 1):
		obj = RenderLine(x1, y1, x2, y2, color, width)
		self._render_query.append(obj)

	def add_text(self, x: int, y: int, text: str, color: Tuple[int, int, int], size: int, font: pygame.font.Font):
		image = font.render(text, False, color)
		w, h = image.get_size()
		obj = RenderTexture(x, y, int(w * size / 256), int(h * size / 256), image)
		self._render_query.append(obj)

	def render(self):
		self.clock.tick(60)

		self.win.fill((0, 0, 0))

		for i in range(len(self._render_query)):
			cur_obj = self._render_query[i]

			if isinstance(cur_obj, RenderRect):
				pygame.draw.rect(self.win, cur_obj.color, (cur_obj.x, cur_obj.y, cur_obj.w, cur_obj.h))

			if isinstance(cur_obj, RenderTexture):
				self.win.blit(cur_obj.texture, (cur_obj.x, cur_obj.y))

			if isinstance(cur_obj, RenderLine):
				color = cur_obj.color
				pfrom = (cur_obj.x1, cur_obj.y1)
				pto = (cur_obj.x2, cur_obj.y2)
				width = cur_obj.width

				pygame.draw.line(self.win, color, pfrom, pto, width)

		self._render_query.clear()

		pygame.display.update()
