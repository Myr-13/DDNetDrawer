import render
import config
import pygame


def main():
	config.default_config()
	renderer = render.Renderer()

	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# Add render query here

		renderer.render()


if __name__ == "__main__":
	main()
