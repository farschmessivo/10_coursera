import bs4 as bs
import urllib.request
import pandas

source = urllib.request.urlopen('https://www.coursera.org/learn/modern-art-ideas').read()
soup = bs.BeautifulSoup(source, 'lxml')
#print(soup.find_all('p'))
#название, язык, ближайшую дату начала, количество недель и среднюю оценку
#title
for p in soup.find_all('h1', class_='title'):
    print(p.text)

for d in soup.find_all('div', class_='ratings-text bt3-visible-xs'):
    print(p.text)




for p in soup.find_all('p', class_='course-description'):
# for paragraph in soup.find_all('p'):
#     print(paragraph.text)



# for url in soup.find_all('loc')[:10]:
#     print(url.text)


# source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/')
# soup = bs.BeautifulSoup(source, 'lxml')
#
# #print(soup.title.text)
#
# #print(soup.get_text())
#
# #table = soup.table
# table = soup.find('table')
#
# table_row = table.find_all('tr')
#
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     print(row)


# dfs = pandas.read_html('https://pythonprogramming.net/parsememcparseface/', header=0)
# for df in dfs:
# print(df)