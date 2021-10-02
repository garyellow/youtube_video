import msvcrt
from urllib import error

from pytube import YouTube
from pytube import exceptions

download_dir = 'download'

print('歡迎使用YouTube影片下載器～～\n')
print('檔案的預設儲存位置為與此程式同資料夾的「download」資料夾')
print('按enter鍵繼續，其他鍵變更儲存位置......')

if ord(msvcrt.getch()) != 13:
    while True:
        download_dir = input('\n請輸入儲存位置\n>> ')
        if len(download_dir) != 0:
            break

while True:
    URL = input('\n請輸入影片網址\n>> ')
    if len(URL) == 0:
        print('此項必填')
        continue

    try:
        yt: YouTube = YouTube(URL)
    except exceptions.RegexMatchError:
        print('網址錯誤')
        continue

    while True:
        download_kind = input('\n是否僅需下載音檔(y/n)\n>> ')
        print('\n開始下載～～')

        if download_kind == 'y' or download_kind == 'Y':
            try:
                yt.streams.get_audio_only().download(download_dir)
            except error.URLError:
                print('\n無法連線至網際網路\n')
                break
            except exceptions.AgeRestrictedError:
                print('\n無法下載設有年齡限制的影片\n')
                break
            except exceptions.LiveStreamError:
                print('\n無法下載直播中的影片\n')
                break
            except exceptions.MembersOnly:
                print('\n無法下載' + yt.author + '的會員專屬影片\n')
                break
            except exceptions:
                print('\n未知異常\n')
                break
            else:
                print('\n\n影片名稱：' + yt.title)
                print('上傳者：' + yt.author)
                print('\n音檔下載成功～\n\n')
                break

        if download_kind == 'n' or download_kind == 'N':
            try:
                yt.streams.get_highest_resolution().download(download_dir)
            except error.URLError:
                print('\n無法連線至網際網路\n')
                break
            except exceptions.AgeRestrictedError:
                print('\n無法下載設有年齡限制的影片\n')
                break
            except exceptions.LiveStreamError:
                print('\n無法下載直播中的影片\n')
                break
            except exceptions.MembersOnly:
                print('\n無法下載' + yt.author + '的會員專屬影片\n')
                break
            except exceptions:
                print('\n未知異常\n')
                break
            else:
                print('\n\n影片名稱：' + yt.title)
                print('上傳者：' + yt.author)
                print('\n影片下載成功～\n\n')
                break

    print('按Enter鍵下載其他影片，其他鍵關閉......')
    if ord(msvcrt.getch()) != 13:
        break
