#!/usr/bin/env python3

import sys
import string

inFileArg = sys.argv[1]
stats = {}

with open(inFileArg) as inFile:
	for line in open(inFileArg, encoding="ISO-8859-1"):
		try:
			line.encode('ascii')
		except UnicodeEncodeError:
			pass
		else:
			pass
			mask = ""
			if line[-1] == "\n":
				line = line[:-1]
			for c in line:
				if c.isnumeric():
					mask += "?d"
				elif c.isupper():
					mask += "?u"
				elif c.islower():
					mask += "?l"
				else:
					mask += "?s"
			if mask in stats:
				stats[mask] += 1
			else:
				stats[mask] = 1

stats = {k: v for k, v in sorted(stats.items(), reverse=True, key=lambda item: item[1])}
for k in stats:
	print(str(stats[k]) + "\t" + k)
