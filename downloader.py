import yt_dlp
import colorama
colorama.init()
from colorama import Fore, Style
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os

def get_spotify_playlist(playlist_url):
    global results
    with open('info.json', 'r') as file:
        data = json.load(file)
    client_id = data['spotify_client_id']
    client_secret = data['spotify_client_secret']
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    results = sp.playlist_tracks(playlist_id)

def download_music():
        download_folder = os.path.join(os.getcwd(), 'downloads')
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        ydl_opts = {
            'format' : 'bestaudio/best',
            'extractaudio' : True,
            'audioformat' : 'mp3',
            'quiet': True,
            'no_warnings': True,
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                for track in results['items']:
                    try:
                        song_name = track['track']['name'] + " " + track['track']['artists'][0]['name']
                        search_url = f"ytsearch:{song_name}"
                        ydl.download([search_url])
                        print(f'{Fore.LIGHTMAGENTA_EX}Audio {song_name} audio downloaded successfully.{Style.RESET_ALL}')
                    except Exception as e:
                        print(f"{Fore.RED}A sound was not found !{Style.RESET_ALL}")
                        pass

def main():
    print(f'{Fore.CYAN}Program developed by masc3, spotify playlist downloader. github: masc3{Style.RESET_ALL}\n')
    print(f'{Fore.CYAN}Before you start, make sure you have filled in the info.json correctly.{Style.RESET_ALL}')
    playlist_url = input('Enter your playlist link (spotify url) -')
    print(f'{Fore.CYAN}\nThe download will start..\n{Style.RESET_ALL}')
    get_spotify_playlist(playlist_url)
    download_music()
    end = input(f'{Fore.CYAN}Finished ! press any key to exit..{Style.RESET_ALL}')

if __name__ == '__main__':
    main()
