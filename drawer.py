import pygame
import items
import data
import ui


class Drawer:
	def __init__(self):
		self.items = []

		# Input
		self.button_holding1 = False
		self.button_holding2 = False
		self.old_button_holding1 = False
		self.old_button_holding2 = False

		# Select
		self.selected_item = items.LaserLine
		self.selected_type = 0

		# Working
		self.working_item = None

		self.tick = 0
		self.ui = ui.UI()

	def _render_item(self, renderer, item):
		if isinstance(item, items.LaserLine):
			renderer.add_line(item.x1, item.y1, item.x2, item.y2, (255, 255, 255), 7)
			renderer.add_texture(item.x1 - 12, item.y1 - 12, 24, 24, data.LASERS[int(self.tick % 9 / 3)])
			renderer.add_texture(item.x2 - 12, item.y2 - 12, 24, 24, data.LASERS[int(self.tick % 9 / 3)])

	def render(self, renderer):
		# Items on screen
		for item in self.items:
			self._render_item(renderer, item)

		if self.working_item is not None:
			self._render_item(renderer, self.working_item)

		# UI
		if self.ui.do_button(0, 100, 20, 20, ""):
			self.selected_item = items.LaserLine
		if self.ui.do_button(0, 140, 20, 20, ""):
			self.selected_item = items.Pickup

	def update(self):
		self.old_button_holding1 = self.button_holding1
		self.old_button_holding2 = self.button_holding2
		self.button_holding1 = pygame.mouse.get_pressed()[0]
		self.button_holding2 = pygame.mouse.get_pressed()[2]
		button_click1 = (self.button_holding1 and not self.old_button_holding1)
		button_click2 = (self.button_holding2 and not self.old_button_holding2)
		mouse_pos = pygame.mouse.get_pos()

		self.tick = min(self.tick + 1, 1000)

		# Add working item
		# Yapi, shit code
		if self.selected_item is not None and self.working_item is None:
			if button_click1:
				if self.selected_item == items.LaserLine:
					self.working_item = items.LaserLine(mouse_pos[0], mouse_pos[1], mouse_pos[0], mouse_pos[1])

		# Add working item to self.items array when we release lmb
		if self.working_item is not None:
			if not self.button_holding1:
				self.items.append(self.working_item)
				self.working_item = None

		# Line item
		if self.button_holding1 and isinstance(self.working_item, items.LaserLine):
			self.working_item.x2 = mouse_pos[0]
			self.working_item.y2 = mouse_pos[1]

	def on_event(self, event: pygame.event.Event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			rmb = pygame.mouse.get_pressed()[0]
			mmb = pygame.mouse.get_pressed()[1]
			lmb = pygame.mouse.get_pressed()[2]
