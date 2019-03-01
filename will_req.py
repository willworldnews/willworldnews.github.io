from feedparser import parse
from requests import get
from pyquery import PyQuery as pyq

r = parse('http://wwwords.mscuttle.com/feed/')
e = r.entries
titles = []
contents = []
times = []

for en in e:
	time = en.published.split('+')[0].strip()
	times.append(time)
	link = en.link
	g = get(link)
	p = pyq(g.text)
	title = p('h2')
	titles.append(title.text())
	content = p('#left-div>.single-post-wrap>p')
	text = content.text()
	for _ in range(20):
		text = text.replace('  ', ' ')
	print(text)
	print()
	contents.append(text)

length = len(titles)
with open('index.html', 'w') as f:
	for i in range(length):
		f.write('<div style="border-radius:1vw;background-color:hsl(' + str(float(i / length * 360)) + ', 95%, 95%);font-size:20px;padding:2vh;margin:2vh;"><span style="font-size:16px;border-bottom:1px solid black;">' + times[i] + '</span><h2>' + titles[i] + '</h2>' + contents[i] + '</div>')
