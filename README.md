# exhentai-metadata-archive
Archival JSONL dump of the exhentai metadata from the community crawl.
In case you want to do some machine learning with it.

## Files
The dataset is compressed and can be found in `data/`. The current version 
contains the `no CG, no cosplay` pages.

An uncompressed `100`-record sample can be found in `data/sample-100.jsonl`.

## Schema
- `id`: Gallery id in the form of `g/*/*`
- `thumb`: URL of gallery thumbnail
- `title`: Title of gallery
- `category`: Gallery type
- `uploader`: Uploader display name
- `created`: Gallery post time `Y-m-d H:i`
- `pages`: Number of images in gallery
- `tags`: List of tags
    - `namespace`: Namespace of tag (for `misc:` this will be blank)
    - `tag`: Tag
    - `confident`: 1 if the tag passed the power threshold (solid border) otherwise 0
    
## Blacklist
Certain files from the community dump were blacklisted because they were the
wrong format (in "Minimal" view). These are ignored because the current script 
cannot handle the minimal page format and these pages do not have tag 
information for the galleries which arguably is the whole point of this export.
