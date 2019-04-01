# Prettify JSON

Script for JSON output in pretty form.

# Quickstart

The script requires an installed Python interpreter version 3.5, no additional packages required.

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py test.json
[
    {
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1,
        "Cells": {
            "global_id": 14371450,
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "geoData": {
                "type": "Point",
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ]
            }
        }
    }
]

```

Use in Windows similarly.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
