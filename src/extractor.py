from bs4 import BeautifulSoup
import json

def extract_record(item):
	title_div = item.find_all('td', class_='gl1e')[0]
	title_link = title_div.find_all('a')[0]
	title_img = title_div.find_all('img')[0]
	
	meta_td = item.find_all('td', class_='gl2e')[0]
	meta_div = meta_td.find_all('div', class_='gl3e')[0]
	# Find the category
	cat_div = meta_div.find_all('div', class_='cn')[0]

	# Find the uploader name
	uploader = [a.get_text() for a in meta_div.find_all('a') if a['href'].startswith('https://exhentai.org/uploader/')][0]
	
	# Find the internal divs:
	int_divs = meta_div.find_all('div', recursive=False)
	# Find the upload time
	created = [d.get_text() for d in int_divs if 'id' in d.attrs and d['id'].startswith('posted_')][0]
	
	# Find the page count
	pages = [int(d.get_text().split()[0]) for d in int_divs if d.get_text().endswith(' pages') or d.get_text().endswith(' page')][0]

	# Find the tags
	tags_tables = meta_td.find_all('table')
	tags = []
	if len(tags_tables) > 0:
		tags_table = tags_tables[0]
		tags_solid = [t['title'] for t in tags_table.find_all('div', class_='gt')]
		tags_maybe = [t['title'] for t in tags_table.find_all('div', class_='gtl')]
		for t in tags_solid:
			namespace, tag = t.split(':')
			tags.append({
				'namespace': namespace,
				'tag': tag,
				'confident': 1
			})
		for t in tags_maybe:
			namespace, tag = t.split(':')
			tags.append({
				'namespace': namespace,
				'tag': tag,
				'confident': 0
			})
	return {
		'id': '/'.join(title_link['href'].split('/')[-4:-1]),
		'thumb': title_img['src'],
		'title': title_img['alt'],
		'category': cat_div.get_text(),
		'uploader': uploader,
		'created': created,
		'pages': pages,
		'tags': tags
	}

if __name__ == '__main__':
	import sys
	if len(sys.argv) < 3:
		print('Usage: {} [path] [count]'.format(sys.argv[0]))
		print('    [path] - Path containing the page dumps')
		print('    [count] - Number of pages dumped (page # of last page)')
		exit(1)
	
	records = {}
	extracted = 0
	for i in range(1, int(sys.argv[2]) + 1):
		with open('{}/exhentai_page_{}.html'.format(sys.argv[1], i), 'r') as f:
			soup = BeautifulSoup(f.read(), 'html.parser')
			print('Page {}:'.format(i))
			# Get the gallery table
			table = soup.find_all('table', class_='itg glte')[0]
			for item in table.find_all('tr', recursive=False):
				record = extract_record(item)
				records[record['id']] = record
				extracted += 1
				print(' Extracted record {}'.format(extracted))

	print('Total of {} unique records'.format(len(records)))

	with open('all_exhentai_metadata.jsonl', 'w') as f:
		for record in records:
			f.write('{}\n'.format(json.dumps(records[record])))