# import and initialize PyGame
import pygame
pygame.init()

# Set display to full screen and set the title
pygame.display.set_caption("PEC/Fortis Research")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Set the clock functionality
clock = pygame.time.Clock()

# Get the width and height of the program
width, height = pygame.display.get_surface().get_size()
screen_res = (width, height)

# Define the colour tuples
red = (255, 0, 0)
white = (255, 255, 255)

# Define the Ball Object
ballObject = pygame.draw.circle(surface = screen, color = red, center = [100, 100], radius = 40)

# define speed of ball (speed = [X direction speed, Y direction speed])
speed = [1, 20]

# define the number of bounces
bouncesSet = 34

# game loop
while True and bouncesSet > 0:
	
    # Insert the frames per second
    clock.tick(100)

    # event loop
    for event in pygame.event.get():
		# check if a user wants to exit the game or not
        if event.type == pygame.QUIT:
            exit()

	# fill white color on screen
    screen.fill(white)

	# move the ball
    ballObject = ballObject.move(speed)

	# if ball goes out of screen then change direction of movement
    if ballObject.left <= 0 or ballObject.right >= width:
        speed[0] = -speed[0]
        bouncesSet -= 1
    if ballObject.top <= 0 or ballObject.bottom >= height:
        speed[1] = -speed[1]
        bouncesSet -= 1

	# draw ball at new centers that are obtained after moving ballObject
    pygame.draw.circle(surface = screen, color = red, center = ballObject.center, radius = 40)

	# update screen
    pygame.display.flip()