import requests
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' + \
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.80 ' + \
        'Safari/537.36'
}

def get_image(item, filename, headers={}, cookies={}):
    r = requests.get(item['thumb'], headers=headers, cookies=cookies)
    if r.status_code == requests.codes.ok:
        with open(filename, 'wb') as f:
            f.write(r.content)
    else:
        print(r.content)
        print(r.status_code)

if __name__ == '__main__':
    import sys, os, time
    if len(sys.argv) < 3:
        print('Usage: {} [file] [outdir]'.format(sys.argv[0]))
        print('    [file] - JSONL file to get the images from')
        print('    [outdir] - Directory to save the images to')
        exit(1)
    
    input = sys.argv[1]
    outdir = sys.argv[2]

    # Try to read in the cookies file
    cookies = {}
    try:
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)
    except Exception as e:
        print('Read cookies failed with exception:')
        print(e)
        exit(1)

    with open(input, 'r') as f:
        count = 0
        for line in f:
            if len(line.strip()) == 0:
                continue
            item = json.loads(line.strip())
            print('Downloading thumbnail for {}'.format(item['id']))
            outfile = os.path.join(outdir, 
                'th-{}.jpg'.format(item['id'].replace('/', '-')))
            if os.path.isfile(outfile):
                print(' Skipping existing file.')
                continue
            count += 1
            get_image(item, outfile, headers=HEADERS, cookies=cookies)
            if count % 10 == 0:
                print('--Short Break--')
                time.sleep(1)