import pygame
from typing import Tuple

import render
import data
from utils import *


class UI:
	def __init__(self, renderer: render.Renderer):
		self.mouse_x = 0
		self.mouse_y = 0

		self.mouse_b1 = False
		self.mouse_old_b1 = False
		self.mouse_click_b1 = False

		self.renderer = renderer

		self.ui_clicked = False

	def do_button(self, x: int, y: int, w: int, h: int, color: Tuple[int, int, int], text: str) -> bool:
		self.renderer.add_rect(x, y, w, h, color)
		self.renderer.add_text(x, y, text, (255, 255, 255), 36, data.FONT)

		if is_inside((self.mouse_x, self.mouse_y, 1, 1), (x, y, w, h)) and self.mouse_click_b1:
			self.ui_clicked = True
			return True
		return False

	def do_button_texture(self, x: int, y: int, w: int, h: int, texture: pygame.Surface, color: Tuple[int, int, int]):
		self.renderer.add_rect(x, y, w, h, color)
		self.renderer.add_texture(x, y, w, h, texture)

		if is_inside((self.mouse_x, self.mouse_y, 1, 1), (x, y, w, h)) and self.mouse_click_b1:
			self.ui_clicked = True
			return True
		return False

	def do_toggle(self, x: int, y: int, w: int, h: int, color: Tuple[int, int, int], text: str, toggled: bool):
		pass

	def render(self):
		self.ui_clicked = False
		self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
		self.mouse_old_b1 = self.mouse_b1
		self.mouse_b1 = pygame.mouse.get_pressed()[0]
		self.mouse_click_b1 = self.mouse_b1 and not self.mouse_old_b1
