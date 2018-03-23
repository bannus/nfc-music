import sys
import spotipy
import spotipy.util as util

scope = 'user-modify-playback-state user-read-playback-state'
ROOM_ON_FIRE = 'spotify:album:3HFbH1loOUbqCyPsLuHLLh'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    result = sp.current_playback()
    if (result['is_playing']):
        sp.pause_playback()
    else:
        sp.start_playback(context_uri=ROOM_ON_FIRE)
else:
    print "Can't get token for", username

