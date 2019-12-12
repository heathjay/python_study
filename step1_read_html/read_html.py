#coding=utf-8
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
html = getHtml("https://www.cnblogs.com/fnng/p/3576154.html")

print(html)
