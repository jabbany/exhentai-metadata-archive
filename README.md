# exhentai-metadata-archive
Archival JSONL dump of the exhentai metadata from the community crawl.
In case you want to do some machine learning with it.

## Files
The dataset is compressed and can be found in `data/`. The current version 
contains the `no CG, no cosplay` pages.

An uncompressed `100`-record sample can be found in `data/sample-100.jsonl`.

## Stats
Total galleries included: `576056`
Total translated: `209095`

### Prolific Artists
| Artist        | Galleries  |
| ------------- | ---------- |
|mizuryu kei    | 837        |
| nakajima yuka | 836        |
| crimson       | 768        |
| saigado       | 757        |
| cle masahiro  | 734        |
| itaba hiroshi | 641        |
| sanbun kyoden | 621        |
| shiwasu no okina | 601     |
| yuzuki n dash | 592        |
| inochi wazuka | 572        |

### Languages
| Language     | Galleries  |
| ------------ | ---------- |
| japanese     | 309041     |
| english      | 97687      |
| chinese      | 51711      |
| korean       | 36013      |
| spanish      | 26756      |
| russian      | 14119      |
| portuguese   | 8904       |
| french       | 8248       |
| speechless   | 6500       |
| thai         | 4714       |

### Most common tags by namespace
**Female**: 
big breasts (162918), lolicon (114988), sole female (101170), stockings (84915),
schoolgirl uniform (73813)

**Male**:
sole male (89600), shotacon (61892, yaoi (43680), males only (32906), 
anal (30191)

**Misc**:
group (89827), full color (70355), incest (40864), mosaic censorship (30386),
tankoubon (28461)


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
