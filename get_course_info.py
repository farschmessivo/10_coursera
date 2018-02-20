import bs4 as bs
import urllib.request


urls = []
for url in soup.find_all('loc')[:10]:
     append(url.text).urls

source = requests.get.urlopen('https://www.coursera.org/learn/modern-art-ideas').read()
soup = bs.BeautifulSoup(source, 'lxml')
# title
for p in soup.find_all('h1', class_='title'):
    print(p.text)
# rating
for d in soup.find_all('div', class_='ratings-text bt3-visible-xs'):
    print(d.text)
# start date
for s in soup.find_all('div', class_='startdate'):
    print(s.text)

for l in soup.find_all('div', class_='rc-Language'):
    print(l.text)

for c in soup.find_all(class_='td-data', data-reactid='183'):
    print(c.text)


# , data-reactid='183'