import json
import os
from collections import OrderedDict

js_obj = {}

files = os.listdir("poems")

for file in files:
	with open(f"poems/{file}") as fh:
		js_obj[file.split(".")[0]] = fh.read()

print(json.dumps(dict(sorted(js_obj.items())), indent=2))