from urllib.request import urlretrieve



def downloader(url, path, file_name):
    path = path + file_name
    
    try:
        print('Wait a few moment...')
        urlretrieve(url, path)
        
        print('Download successful!!')
        print(f'{file_name} save in {path}')
    
    except:
        print('ERROR! SOME PROBLEM IN DOWNLOAD')


def downloader_yt(link_video, path, file_name):
    pass
    

def downloader_insta(link_video, path, file_name):
    pass
    
    

while True:
    print('*'*46)
    print('{:^46}'.format('pyDownloader'))
    print('*'*46)

    url = str(input('Type or paste url link: '))
    path = str(input('Type a address that you would like file: '))
    file_name = str(input('Type a file name with extension "file name.type_file": '))

    downloader(url, path, file_name)



