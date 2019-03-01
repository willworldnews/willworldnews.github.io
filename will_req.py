from feedparser import parse
from requests import get
from pyquery import PyQuery as pyq

r = parse('http://wwwords.mscuttle.com/feed/')
e = r.entries
titles = []
contents = []

for en in e:
    link = en.links[0].href
    g = get(link)
    p = pyq(g.text)
    title = p('h2')
    titles.append(title.text())
    content = p('#left-div>.single-post-wrap>p')
    contents.append(content.text())


length = len(titles)
with open('index.html', 'w') as f:
    for i in range(length):
        f.write('<h2>%s</h2>' % titles[i])
        f.write('<p style="background-color:hsl(' + str(float(i / length * 360)) + ', 90%, 90%);font-size:20px;padding:1%;">' + contents[i] + '</p><hr/>')
