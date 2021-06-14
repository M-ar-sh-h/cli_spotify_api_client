import requests

ACCESS_TOKEN = 'BQAcOiBnu43fjuLByjO5skYqLD71rDzptm_VpA3OydKqidBmgB1f0uPRBWdx7GHnZ_4vv3fEmbYEdbB1yg49eY5qkLfuuNWfYwFfFeAW3lcugJPslYxih27J25kfvxo03g7haNhSf2R1jZAXC_tMav8H5kfdaxbV0k3H4GK71lM6h0Y_3ifdsR5remc9yOWe9CJ-55764S1PfSDGdvGCc93i53BkzkvmMXSRnFqV'

def create_playlist_onSpotify(name, public):
    SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/tuigwtwn64zr2w68wsd1p96hy/playlists'
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json = {
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()
    return json_resp


def add_track_to_playlist(public):
    init_var = search_spotify()
    init_var_choice = int(input("Which track do you want to add? "))
    var = init_var[init_var_choice - 1]
    var = var.replace(":","%3A")
    var = var.replace(",","%2C")
    init_playlist = get_playlists()
    init_playlist_choice = int(input("Which playlist do you want to add the track to? "))
    playlist_id = init_playlist[init_playlist_choice - 1]
    ADD_TRACK_URL = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={var}'
    response = requests.post(
        ADD_TRACK_URL,
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json = {
            "public": public
        }
    )
    json_resp = response.json()
    return json_resp


def search_spotify():
    keyword = input("Search for the track: ")
    SEARCH_URL = f'https://api.spotify.com/v1/search?q={keyword}&type=track&limit=3&offset=0'
    response = requests.get(
        SEARCH_URL,
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    )
    response_json = response.json()
    tracks = [track for track in response_json['tracks']['items']]
    track_ids = [track['id'] for track in tracks]
    tracks_uri = []
    count = 1
    for track in tracks:
        print(f"{count}. {track['name']}")
        tracks_uri.append(track['uri'])
        count += 1
    return tracks_uri    
    

def get_playlists():
    GET_PLAYLIST_URL = "https://api.spotify.com/v1/me/playlists?offset=0"
    response = requests.get(
        GET_PLAYLIST_URL,
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    )
    response_json = response.json()
    playlists = [playlist for playlist in response_json['items']]
    playlist_ids = [playlist['id'] for playlist in playlists]
    playlists_id = []
    count = 1
    for playlist in playlists:
        print(f"{count}. {playlist['name']}")
        playlists_id.append(playlist['id'])
        count+=1    
    return playlists_id

def main(n):
    if n == 1:
        playlist = create_playlist_onSpotify(
            name = f"{input('Playlist name: ')}",
            public = False
        )
        print(f"Playlist: {playlist}")

    if n == 2:    
        add_track = add_track_to_playlist(
            public = False
        )

    if n == 3:
        search_track = search_spotify()

    if n == 4:
        display_playlists = get_playlists()    


if __name__ == '__main__':
    print("Operations:-\n1. Create Playlist\n2. Add song(s) to a playlist\n3. Search for a track\n4. View your playlists")
    main(int(input()))
