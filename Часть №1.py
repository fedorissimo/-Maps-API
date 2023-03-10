import requests
import pygame

pygame.init()
coords = [56.045690, 54.787752]
lon = input('Введите первую координату')
lat = input('Введите вторую координату')
delta = input('Введите масштаб')

api_server = 'http://static-maps.yandex.ru/1.x/'
params = {
    'll': ",".join([lon, lat]),
    'spn': ",".join([delta, delta]),
    'l': 'map'}
response = requests.get(api_server, params=params)
file = open('map.png', 'wb')
file.write(response.content)
file.close()
size = width, height = 600, 450
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(pygame.image.load('map.png'), (0, 0))
    pygame.display.flip()
pygame.quit()
