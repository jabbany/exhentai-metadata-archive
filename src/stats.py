import json
from collections import Counter

if __name__ == '__main__':
    import sys, os, time
    if len(sys.argv) < 2:
        print('Usage: {} [file] [outdir]'.format(sys.argv[0]))
        print('    [file] - JSONL file to get the images from')
        exit(1)
    
    input = sys.argv[1]

    total_galleries, translated_galleries = 0, 0
    authors, languages = Counter(), Counter()
    fetish_female, fetish_male, fetish_misc = Counter(), Counter(), Counter()

    with open(input, 'r') as f:
        count = 0
        for line in f:
            if len(line.strip()) == 0:
                continue
            item = json.loads(line.strip())
            total_galleries += 1
            is_translated, is_tagged_lang = False, False
            for tag in item['tags']:
                if tag['namespace'] == 'language':
                    is_tagged_lang = True
                    if tag['tag'] == 'translated':
                        is_translated = True
                        translated_galleries += 1
                    else:
                        languages[tag['tag']] += 1
                if tag['namespace'] == 'artist':
                    authors[tag['tag']] += 1
                if tag['namespace'] == 'female':
                    fetish_female[tag['tag']] += 1
                if tag['namespace'] == 'male':
                    fetish_male[tag['tag']] += 1
                if tag['namespace'] == '':
                    fetish_misc[tag['tag']] += 1
            if not is_tagged_lang:
                languages['japanese'] += 1 # This is the default language
    
    print('Aggregate statistics')
    print('')
    print('  Total Galleries: {}'.format(total_galleries))
    print('  Total translated galleries: {}'.format(translated_galleries))
    print('')
    print('Most prolific authors:')
    print('')
    for author, books in authors.most_common(10):
        print(' {} | {}'.format(author, books))
    print('')
    print('Most used languages:')
    print('')
    for lang, books in languages.most_common(10):
        print(' {} | {}'.format(lang, books))
    print('')
    print('Most common tags in female namespace:')
    print('')
    for tag, books in fetish_female.most_common(10):
        print(' {} | {}'.format(tag, books))
    print('')
    print('Most common tags in male namespace:')
    print('')
    for tag, books in fetish_male.most_common(10):
        print(' {} | {}'.format(tag, books))
    print('')
    print('Most common tags in misc namespace:')
    print('')
    for tag, books in fetish_misc.most_common(10):
        print(' {} | {}'.format(tag, books))
    print('')