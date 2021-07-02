import pyshorteners
link = input("Enter The URL: ")
shortener=pyshorteners.Shortener()
X = shortener.tinyurl.short(link)
print(X)