import msvcrt
from urllib import error

from pytube import YouTube
from pytube import exceptions

download_dir = 'download'

print('This is YouTube video downloader~~')
print('You can download video or audio from YouTube')
print('Prohibited for commercial!!!\n')
print('Default storage location for files is "download" folder near this exe file')
print('Press enter to continue, other keys to change the storage location...')

if ord(msvcrt.getch()) != 13:
    while True:
        download_dir = input('\nEnter the storage location you want\n>> ')
        if len(download_dir) != 0:
            break

while True:
    URL = input('\nEnter the URL of the video\n>> ')
    if len(URL) == 0:
        print('This item is required!')
        continue

    try:
        yt = YouTube(URL)
    except exceptions.RegexMatchError:
        print('URL is fault, please check it')
        continue

    download_kind = input('\nVideo or Audio? (v/a)\n>> ')
    while len(download_kind) != 1 or ['a', 'A', 'v', 'V'].count(download_kind) == 0:
        download_kind = input('\nVideo or Audio? (v/a)\n>> ')

    print('\nStart download, please wait for a short time~~\n')

    try:
        if download_kind == 'a' or download_kind == 'A':
            yt.streams.get_audio_only().download(download_dir)
        if download_kind == 'v' or download_kind == 'V':
            yt.streams.get_highest_resolution().download(download_dir)
    except error.URLError:
        print('\nUnable to connect to the internet\n')
    except exceptions.AgeRestrictedError:
        print('\nUnable to download age-restricted videos\n')
    except exceptions.LiveStreamError:
        print('\nUnable to download the video in the live\n')
    except exceptions.MembersOnly:
        print('\nUnable to download ' + yt.author + '\'s member-only videos\n')
    except exceptions:
        print('\nUnknown exception\n')
    else:
        print('--------------------------------------------------')
        print('Video name：' + yt.title)
        print('Uploader：' + yt.author)
        if download_kind == 'a' or download_kind == 'A':
            print('Audio downloaded successfully~')
        if download_kind == 'v' or download_kind == 'V':
            print('Video download successfully~')
        print('--------------------------------------------------')

    print('\nPress Enter to download other videos, other keys to close...')
    if ord(msvcrt.getch()) != 13:
        break
