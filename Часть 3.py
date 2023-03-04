import requests
import pygame


pygame.init()
coords = [56.045690, 54.787752]
# lon = '56.045690'
# lat = '54.787752'
# delta = '0.01'
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                if float(delta) > 0.0001:
                    delta = float(delta)
                    delta /= 1.5
                    delta = str(delta)
                    params = {
                        'll': ",".join([lon, lat]),
                        'spn': ",".join([delta, delta]),
                        'l': 'map'}
                    response = requests.get(api_server, params=params)
                    file = open('map.png', 'wb')
                    file.write(response.content)
                    file.close()
            if event.key == pygame.K_PAGEDOWN:
                if float(delta) < 43:
                    delta = float(delta)
                    delta *= 2
                    delta = str(delta)
                    params = {
                        'll': ",".join([lon, lat]),
                        'spn': ",".join([delta, delta]),
                        'l': 'map'}
                    response = requests.get(api_server, params=params)
                    file = open('map.png', 'wb')
                    file.write(response.content)
                    file.close()
            if event.key == pygame.K_UP:
                lat = float(lat)
                if lat < 84:
                    lat += 0.001
                lat = str(lat)
                params = {
                    'll': ",".join([lon, lat]),
                    'spn': ",".join([delta, delta]),
                    'l': 'map'}
                response = requests.get(api_server, params=params)
                file = open('map.png', 'wb')
                file.write(response.content)
                file.close()
            if event.key == pygame.K_DOWN:
                lat = float(lat)
                print(lat)
                if lat > -84:
                    lat -= 0.001
                lat = str(lat)
                params = {
                    'll': ",".join([lon, lat]),
                    'spn': ",".join([delta, delta]),
                    'l': 'map'}
                response = requests.get(api_server, params=params)
                file = open('map.png', 'wb')
                file.write(response.content)
                file.close()
            if event.key == pygame.K_LEFT:
                lon = float(lon)
                lon -= 0.001
                lon = str(lon)
                params = {
                    'll': ",".join([lon, lat]),
                    'spn': ",".join([delta, delta]),
                    'l': 'map'}
                response = requests.get(api_server, params=params)
                file = open('map.png', 'wb')
                file.write(response.content)
                file.close()
            if event.key == pygame.K_RIGHT:
                lon = float(lon)
                lon += 0.001
                lon = str(lon)
                params = {
                    'll': ",".join([lon, lat]),
                    'spn': ",".join([delta, delta]),
                    'l': 'map'}
                response = requests.get(api_server, params=params)
                file = open('map.png', 'wb')
                file.write(response.content)
                file.close()

    screen.blit(pygame.image.load('map.png'), (0, 0))
    pygame.display.flip()
pygame.quit()
