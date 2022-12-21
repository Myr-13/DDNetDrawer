import render
import config
import pygame
import drawer


def main():
	config.default_config()
	renderer = render.Renderer()
	draw = drawer.Drawer()

	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			draw.on_event(event)

		draw.update()

		# Render query
		draw.render(renderer)

		renderer.render()


if __name__ == "__main__":
	main()
