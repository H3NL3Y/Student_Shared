import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Permissions to request. Add scopes (space-separated) as you need them,
# e.g. "user-top-read user-read-recently-played".
SCOPE = "user-top-read"


def get_client():
    auth_manager = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI", "http://127.0.0.1:8844/callback"),
        scope=SCOPE,
        cache_path=".spotify_cache",
        open_browser=True,
    )
    return spotipy.Spotify(auth_manager=auth_manager)


def main():
    sp = get_client()
    me = sp.current_user()
    print(f"Logged in as: {me['display_name']} ({me['id']})")


if __name__ == "__main__":
    main()
