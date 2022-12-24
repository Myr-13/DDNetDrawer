from typing import Tuple
import pygame

import config
from render_items import *


class Camera:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.zoom = 1


class Renderer:
	def __init__(self):
		self.win = pygame.display.set_mode((config.conf["SCREEN_WIDTH"], config.conf["SCREEN_HEIGHT"]))
		pygame.display.set_caption("DDNetDrawer " + config.conf["VERSION"])
		self.clock = pygame.time.Clock()
		self._render_query = []
		self.camera = Camera()

	def add_rect(self, x: int, y: int, w: int, h: int, color: Tuple[int, int, int], is_ui: bool = False):
		obj = RenderRect(x, y, w, h, color, is_ui)
		self._render_query.append(obj)

	def add_texture(self, x: int, y: int, w: int, h: int, image: pygame.Surface, is_ui: bool = False):
		obj = RenderTexture(x, y, w, h, image, is_ui)
		self._render_query.append(obj)

	def add_line(self, x1: int, y1: int, x2: int, y2: int, color: Tuple[int, int, int], width: int = 1, is_ui=False):
		obj = RenderLine(x1, y1, x2, y2, color, width, is_ui)
		self._render_query.append(obj)

	def add_text(self, x: int, y: int, text: str, color: Tuple[int, int, int], size, font: pygame.font.Font, is_ui=False):
		image = font.render(text, False, color)
		w, h = image.get_size()
		obj = RenderTexture(x, y, int(w * size / 256), int(h * size / 256), image, is_ui)
		self._render_query.append(obj)

	def render(self):
		self.clock.tick(60)

		self.win.fill((0, 0, 0))

		for i in range(len(self._render_query)):
			cur_obj = self._render_query[i]

			if isinstance(cur_obj, RenderRect):
				cx = self.camera.x
				cy = self.camera.y
				cz = self.camera.zoom
				if cur_obj.ui:
					cx = 0
					cy = 0
					cz = 1
				x = (cur_obj.x - cx) * cz
				y = (cur_obj.y - cy) * cz
				w = cur_obj.w * cz
				h = cur_obj.h * cz
				pygame.draw.rect(self.win, cur_obj.color, (x, y, w, h))

			if isinstance(cur_obj, RenderTexture):
				cx = self.camera.x
				cy = self.camera.y
				cz = self.camera.zoom
				if cur_obj.ui:
					cx = 0
					cy = 0
					cz = 1
				x = (cur_obj.x - cx) * cz
				y = (cur_obj.y - cy) * cz
				w = cur_obj.w * cz
				h = cur_obj.h * cz
				texture = pygame.transform.scale(cur_obj.texture, (w, h))
				self.win.blit(texture, (x, y))

			if isinstance(cur_obj, RenderLine):
				color = cur_obj.color
				pfrom = (
					(cur_obj.x1 - self.camera.x) * self.camera.zoom,
					(cur_obj.y1 - self.camera.y) * self.camera.zoom
				)
				pto = (
					(cur_obj.x2 - self.camera.x) * self.camera.zoom,
					(cur_obj.y2 - self.camera.y) * self.camera.zoom
				)
				width = int(cur_obj.width * self.camera.zoom)

				pygame.draw.line(self.win, color, pfrom, pto, width)

		self._render_query.clear()

		pygame.display.update()
