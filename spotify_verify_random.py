import requests
import json

filename = "songs.csv"
# Get token from
#https://developer.spotify.com/console/get-user-player/?market=&additional_types=	

def get_current_song():
	url = "https://api.spotify.com/v1/me/player"
	headers = {'Accept':'application/json', 'Content-Type':'application/json', 'Authorization':'ADD YOUR TOKEN HERE'}
	r = requests.get(url,headers=headers)
	response = json.loads(r.text)
	return response

songs = {}

count = 0
while True:
  # Manually skip a song every time before pressing enter.
  # Not very convenient i know. 
	i = input("press ENTER to get current song")
	if i == "quit": break
	count += 1
	
	response = get_current_song()
	
	device = response['device']['type']
	shuffle_state = response['shuffle_state']
	song_name = response['item']['name']
	artist = response['item']['artists'][0]['name']
	key = artist + " - " + song_name
	
	if key not in songs.keys():
		songs[key] = {"device":device, "shuffle_state":shuffle_state, "artist":artist, "song_name":song_name, "counter":1}
	else:
		songs[key]["counter"] += 1
	print("Song number ", count)
	print("{}|{}|{}|{}|{}\n".format(device,shuffle_state,artist,song_name,songs[key]["counter"]))
    

f = open(filename, 'w+')
f.write("device|shuffle_state|artist|song_name|counter\n")
for k in songs.keys():
	f.write("{}|{}|{}|{}|{}\n".format(songs[k]["device"],songs[k]["shuffle_state"],songs[k]["artist"],songs[k]["song_name"],songs[k]["counter"]))
f.close()
