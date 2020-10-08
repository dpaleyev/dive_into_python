import os
import tempfile
import json
import argparse

parser = argparse.ArgumentParser(description='Storage')

parser.add_argument('--key', action="store", dest="key")
parser.add_argument('--val', action="store", dest="value")

args = parser.parse_args()

storage_path = 'storage.data'
records = None

if not os.path.isfile(storage_path):
    records = dict()
else:
    with open(storage_path) as f:
        records = json.loads(f.read())

if args.value is None:
    if args.key not in records:
        records[args.key] = []
    print(', '.join(str(i) for i in records[args.key]))

else:
    if args.key not in records:
        records[args.key] = []
    records[args.key].append(args.value)

with open(storage_path, 'w') as f:
    f.write(json.dumps(records))
