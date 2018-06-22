from django.shortcuts import render
from .models import SpotifyToken
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import pprint
import spotipy
global access_token
def index(request):
    user = SpotifyToken()
    token = util.prompt_for_user_token(username=user.username, scope=user.scope,
                                   client_id=user.client_id, client_secret=user.client_secret,
                                   redirect_uri=user.redirect_uri)
    artist_url = 'spotify:artist:4vGrte8FDu062Ntj0RsPiZ?si=V6OE66e5T36DZBDtgDgrNQ'
    sp = spotipy.Spotify(auth=token)
    result = sp.artist(artist_url)
    pprint.pprint(result)
    return render(request,'start_spotipy/index.html',context=result)
# Create your views here.
