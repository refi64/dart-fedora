#!/usr/bin/env python3

import shutil


with open('dart-uber.spec', 'w') as uber:
    with open('dart.spec') as source:
        for line in source:
            if line.startswith('%include'):
                spec = line.split()[1].strip()
                with open(spec) as included:
                    shutil.copyfileobj(included, uber)
            else:
                uber.write(line)
