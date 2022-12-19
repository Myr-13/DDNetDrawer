import pygame
import config


class RenderRect:
	def __init__(self, x, y, w, h, color):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.color = color


class RenderTexture:
	def __init__(self, x, y, texture):
		self.x = x
		self.y = y
		self.texture: pygame.Surface = texture


class Renderer:
	def __init__(self):
		self.win = pygame.display.set_mode((config.conf["SCREEN_WIDTH"], config.conf["SCREEN_HEIGHT"]))
		self.clock = pygame.time.Clock()
		self.render_query = []

	def add_rect(self, x, y, w, h, color):
		obj = RenderRect(x, y, w, h, color)
		self.render_query.append(obj)

	def add_texture(self, x, y, texture):
		img = pygame.image.load(texture)
		obj = RenderTexture(x, y, img)
		self.render_query.append(obj)

	def render(self):
		self.win.fill((0, 0, 0))

		for i in range(len(self.render_query)):
			cur_obj = self.render_query[i]

			if isinstance(cur_obj, RenderRect):
				pygame.draw.rect(self.win, cur_obj.color, (cur_obj.x, cur_obj.y, cur_obj.w, cur_obj.h))

			if isinstance(cur_obj, RenderTexture):
				cur_obj.texture.blit(self.win, (cur_obj.x, cur_obj.y))

		self.render_query.clear()

		pygame.display.update()
