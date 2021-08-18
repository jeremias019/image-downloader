import urllib.request

def dl_png(url, file_path, file_name):
    full_path = file_path + file_name + '.png'
    urllib.request.urlretrieve(url, full_path)

url = input('Enter img url to download:')
file_name = input('Enter file name to save as')

img_dl(url, 'images/', file_name)