from django.db import models

# Create your models here.

class SpotifyToken(object):
    def __init__(self):
        self.username = '21oqajoreaqsljzhjcv2zvbqq?si=eE2ZtNgvTdadOm2wpQ4f5Q' #your-spotify-client-id
        self.client_id = '8b474160369048188c6cf5df4f9be5f5' #your-spotify-client-secret
        self.client_secret = 'eea9b775bccc4c87a7501dd660695b74' #your-app-redirect-url
        self.redirect_uri = 'http://127.0.0.1:8000/'
        self.scope = 'playlist-modify-public'
