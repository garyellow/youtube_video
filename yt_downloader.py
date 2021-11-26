import msvcrt
from urllib import error

from pytube import YouTube
from pytube import exceptions

download_dir = 'download'

print('This is YouTube video downloader~~')
print('You can download video or audio from YouTube')
print('Prohibited for commercial use\n')
print('Default storage location for files is "download" folder')
print('Press enter to continue, other keys to change the storage location...')

if ord(msvcrt.getch()) != 13:
    while True:
        download_dir = input('\nEnter the storage location you want\n>> ')
        if len(download_dir) != 0:
            break

while True:
    URL = input('\nEnter the URL of the video\n>> ')
    if len(URL) == 0:
        print('This is required!')
        continue

    try:
        yt: YouTube = YouTube(URL)
    except exceptions.RegexMatchError:
        print('URL is fault, please check it')
        continue

    while True:
        download_kind = input('\nOnly audio? (y/n)\n>> ')
        print('\nStart download, please wait for a short time~~')

        if download_kind == 'y' or download_kind == 'Y':
            try:
                yt.streams.get_audio_only().download(download_dir)
            except error.URLError:
                print('\nUnable to connect to the internet\n')
                break
            except exceptions.AgeRestrictedError:
                print('\nUnable to download age-restricted videos\n')
                break
            except exceptions.LiveStreamError:
                print('\nUnable to download the video in the live\n')
                break
            except exceptions.MembersOnly:
                print('\nUnable to download ' + yt.author + '\'s member-only videos\n')
                break
            except exceptions:
                print('\nUnknown exception\n')
                break
            else:
                print('\n\nVideo name：' + yt.title)
                print('Uploader：' + yt.author)
                print('\nAudio file downloaded successfully~\n\n')
                break

        if download_kind == 'n' or download_kind == 'N':
            try:
                yt.streams.get_highest_resolution().download(download_dir)
            except error.URLError:
                print('\nUnable to connect to the internet\n')
                break
            except exceptions.AgeRestrictedError:
                print('\nUnable to download age-restricted videos\n')
                break
            except exceptions.LiveStreamError:
                print('\nUnable to download the video in the live\n')
                break
            except exceptions.MembersOnly:
                print('\nUnable to download ' + yt.author + '\'s member-only videos\n')
                break
            except exceptions:
                print('\nUnknown exception\n')
                break
            else:
                print('\nVideo name：' + yt.title)
                print('Uploader：' + yt.author)
                print('\nVideo download successfully~\n')
                break

    print('Press Enter to download other videos, other keys to close...')
    if ord(msvcrt.getch()) != 13:
        break
