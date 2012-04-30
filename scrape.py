from lxml import html, etree
import urllib2

for i in range(1, 521):
    print i
    url = 'http://www.mitchclem.com/nothingnice/'+str(i)
    doc = html.parse(url)
    img = doc.getroot().cssselect('img.centeredImage')
    if (len(img) == 0):
        print "\tcouldn't find"
        continue
    u = urllib2.urlopen('http://www.mitchclem.com'+img[0].get('src'))
    localFile = open('/Users/relwell/Desktop/nothingnice/'+str(i)+'.jpg', 'w')
    localFile.write(u.read())
    localFile.close()
