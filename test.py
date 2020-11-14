import requests, json

genresJson = requests.get("https://api.deezer.com/genre/")

for genre in genresJson.json()['data']:
  print (genre['id'], genre['name'])


artistJson = requests.get("https://api.deezer.com/genre/95/artists")

for artist in artistJson.json()['data']:
  print (artist['id'], artist['name'])
  



