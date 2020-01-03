import urllib.request


def download_image(url):
    name = "deb"+".jpg"
    urllib.request.urlretrieve(url, name)


download_image('https://www.insidehook.com/wp-content/uploads/2019/11/Best-Thanksgiving-Hikes-Bay-Area.png?fit=1500%2C1000')