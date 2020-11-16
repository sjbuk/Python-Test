import requests, json,pickle


GenreList = {}
GenreArtists = {}
ArtistSongs = {}

def LoadDeezerGenreList():
    genresJson = requests.get("https://api.deezer.com/genre/")

    for genre in genresJson.json()['data']:
        #print (genre['id'], genre['name'])
        id = genre['id']
        genreName = genre['name']
        GenreList[id] = genreName

def LoadDeezerGenreArtists(GenreId):
    apiUrl = "https://api.deezer.com/genre/" + str(GenreId) + "/artists"
    artistJson = requests.get(apiUrl)

    for artist in artistJson.json()['data']:
        #print (genre['id'], genre['name'])
        id = artist['id']
        artistName = artist['name']
        GenreArtists[id] = artistName

def LoadDeezerArtistSongs(ArtistId):
    apiUrl = "https://api.deezer.com/artist/" + str(ArtistId) + "/top?limit=30"
    songsJson = requests.get(apiUrl)

    for song in songsJson.json()['data']:
        #print (song['id'], song['name'])
        id = song['id']
        songName = song['title']
        ArtistSongs[id] = songName



def SaveGenreList():
    with open('genre.json','w') as filehandle:
        json.dump(GenreList,filehandle)


def LoadGenreList():
    global GenreList
    with open('genre.json','r') as filehandler:
        GenreList = json.load(filehandler)



if __name__ == "__main__":
    #LoadDeezerGenreList()
    #LoadGenreList()
    #print (GenreList)
    #SaveGenreList()
    #LoadDeezerGenreArtists(0)
    #print(GenreArtists)
    LoadDeezerArtistSongs(384236)
    print(ArtistSongs)


