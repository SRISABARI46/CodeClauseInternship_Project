import pyshorteners

url = input('Enter the url: ')
def shortenurl(url):
    s = pyshorteners.Shortener()
    print("Shortend URL : ",s.tinyurl.short(url))


shortenurl(url)