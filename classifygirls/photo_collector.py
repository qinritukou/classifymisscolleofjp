import os
import bs4
import urllib2
from itertools import chain
from urllib import urlretrieve

base_url = 'http://misscolle.com'

def fetch_page_urls():
	html = urllib2.urlopen('{}/versions'.format(base_url))
	soup = bs4.BeautifulSoup(html, 'html.parser')

	columns = soup.find_all('ul', class_='columns')
	atags = map(lambda column: column.find_all('a'), columns)

	with open('page_urls.txt', 'w') as f:
		for _ in chain.from_iterable(atags):
			path = _.get('href')
			if not path.startswith('http'):	# relative path
				path = '{}{}'.format(base_url, path)
			if path[-1] == '/':
				path = path[:-1]
			f.write('{}\n'.format(path))

def fetch_photos():
	with open('page_urls.txt') as f:
		for url in f:
			# make directories for savina images
			dirpath = 'photos/{}'.format(url.strip().split('/')[-1])
			# if os.listdir(dirpath) == []: 
			# 	print(dirpath)
			# 	os.rmdir(dirpath)
			if not os.path.exists(dirpath):
				os.makedirs(dirpath)
			
			if os.listdir(dirpath) == []: 
				try:
					html = urllib2.urlopen('{}/photo'.format(url.strip()))
					soup = bs4.BeautifulSoup(html, 'html.parser')
					
					photos = soup.find_all('li', class_='photo')
					paths = map(lambda path: path.find('a').get('href'), photos)
				
					for path in paths:
						filename = '_'.join(path.split('?')[0].split('/')[-2:])
						print(path + " download file" + filename)
						filepath = '{}/{}'.format(dirpath, filename)
						# download image file
						urlretrieve('{}{}'.format(base_url, path), filepath)
						# add random waiting time
						# time.sleep(4 + random.randint(0, 2))
				except:
					print(url)

if __name__ == '__main__':
	fetch_page_urls()
	fetch_photos()
		
