import math

import pygame
import items
import data
import ui


class Drawer:
	def __init__(self, renderer):
		self.items = []

		# Input
		self.button_holding1 = False
		self.button_holding2 = False
		self.button_holding3 = False
		self.old_button_holding1 = False
		self.old_button_holding2 = False
		self.mouse_pos = [0, 0]
		self.old_mouse_pos = [0, 0]

		# Select
		self.selected_item = items.LaserLine
		self.selected_type = 0

		# Working
		self.working_item = None

		self.tick = 0
		self.renderer = renderer
		self.ui = ui.UI(self.renderer)

	def _render_item(self, item):
		if isinstance(item, items.LaserLine):
			self.renderer.add_line(item.x1, item.y1, item.x2, item.y2, (255, 255, 255), 7)
			self.renderer.add_texture(item.x1 - 12, item.y1 - 12, 24, 24, data.LASERS[int(self.tick % 9 / 3)])
			self.renderer.add_texture(item.x2 - 12, item.y2 - 12, 24, 24, data.LASERS[int(self.tick % 9 / 3)])
		if isinstance(item, items.Pickup):
			x = item.x + int(math.cos(self.tick / 24) * 4)
			y = item.y + int(math.sin(self.tick / 24) * 4)

			if item.type == items.PICKUP_ARMOR:
				self.renderer.add_texture(x, y, 48, 48, data.ARMOR)
			if item.type == items.PICKUP_HEART:
				self.renderer.add_texture(x, y, 48, 48, data.HEART)
			if item.type == items.WEAPON_GUN:
				self.renderer.add_texture(x, y, 128, 64, data.GUN)
			if item.type == items.WEAPON_HAMMER:
				self.renderer.add_texture(x, y, 128, 64, data.HAMMER)
			if item.type == items.WEAPON_LASER:
				self.renderer.add_texture(x, y, 256, 96, data.LASER)
			if item.type == items.WEAPON_GRENADE:
				self.renderer.add_texture(x, y, 256, 64, data.GRENADE)
			if item.type == items.WEAPON_SHOTGUN:
				self.renderer.add_texture(x, y, 256, 64, data.SHOTGUN)
			if item.type == items.WEAPON_NINJA:
				self.renderer.add_texture(x, y, 256, 64, data.CATANA)

	def render(self):
		# Items on screen
		for item in self.items:
			self._render_item(item)

		if self.working_item is not None:
			self._render_item(self.working_item)

		# UI
		self.ui.render()

		if self.ui.do_button_texture(0, 24, 48, 48, data.LASER_TOOL, (30, 30, 30)):
			self.selected_item = items.LaserLine
		if self.ui.do_button_texture(0, 72, 48, 48, data.PICKUP_TOOL, (30, 30, 30)):
			self.selected_item = items.Pickup

	def update(self):
		self.old_button_holding1 = self.button_holding1
		self.old_button_holding2 = self.button_holding2
		self.button_holding1 = pygame.mouse.get_pressed()[0]
		self.button_holding3 = pygame.mouse.get_pressed()[1]
		self.button_holding2 = pygame.mouse.get_pressed()[2]
		button_click1 = (self.button_holding1 and not self.old_button_holding1)
		button_click2 = (self.button_holding2 and not self.old_button_holding2)
		self.old_mouse_pos = self.mouse_pos
		self.mouse_pos = [x for x in pygame.mouse.get_pos()]
		camera_x = self.renderer.camera.x
		camera_y = self.renderer.camera.y
		camera_z = self.renderer.camera.zoom

		delta_mouse = [
			self.mouse_pos[0] - self.old_mouse_pos[0],
			self.mouse_pos[1] - self.old_mouse_pos[1]
		]

		self.tick = (self.tick + 1) % 1000

		if self.button_holding3:
			self.renderer.camera.x -= delta_mouse[0]
			self.renderer.camera.y -= delta_mouse[1]

		#                UI
		if self.ui.ui_clicked:
			return

		# Add working item
		# Yapi, shit code
		if self.selected_item is not None and self.working_item is None:
			if button_click1:
				if self.selected_item == items.LaserLine:
					self.working_item = items.LaserLine(
						(self.mouse_pos[0] + camera_x) * camera_z, (self.mouse_pos[1] + camera_y) * camera_z,
						(self.mouse_pos[0] + camera_x) * camera_z, (self.mouse_pos[1] + camera_y) * camera_z
					)
				if self.selected_item == items.Pickup:
					self.working_item = items.Pickup(self.mouse_pos[0] + camera_x, self.mouse_pos[1] + camera_y, items.PICKUP_ARMOR)

		# Add working item to self.items array when we release lmb
		if self.working_item is not None:
			if not self.button_holding1:
				self.items.append(self.working_item)
				self.working_item = None

		if self.button_holding1 and self.working_item is not None:
			# Line item
			if isinstance(self.working_item, items.LaserLine):
				self.working_item.x2 = (self.mouse_pos[0] + camera_x) * camera_z
				self.working_item.y2 = (self.mouse_pos[1] + camera_y) * camera_z
			else:  # All others items
				x_offset = 24
				y_offset = 24

				self.working_item.x = (self.mouse_pos[0] + camera_x - x_offset) * camera_z
				self.working_item.y = (self.mouse_pos[1] + camera_y - y_offset) * camera_z

	def on_event(self, event: pygame.event.Event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4:
				self.renderer.camera.zoom += 0.05
			if event.button == 5:
				self.renderer.camera.zoom -= 0.05
