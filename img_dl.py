#importing required libraries
import urllib.request

#adding user agent information
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

#calling urlretrieve function to get resource
def dl_png(url, file_path, file_name):
    full_path = file_path + file_name + '.png'
    urllib.request.urlretrieve(url, full_path)

url = input('Enter img url to download:')
file_name = input('Enter file name to save as:')

dl_png(url, 'images/', file_name)