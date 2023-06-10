import pygame

# Initialize Pygame
pygame.init()

# Load the MP3 file
pygame.mixer.music.load('ex021.mp3')

# Play the music
pygame.mixer.music.play()

# Wait for the music to finish
pygame.event.wait()
