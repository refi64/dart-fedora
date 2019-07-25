#!/usr/bin/env python3

import os
import shutil


os.chdir(os.path.dirname(__file__))

try:
    os.mkdir('scratch')
except FileExistsError:
    pass

with open('dart-uber.spec', 'w') as uber:
    with open('dart.spec') as source:
        for line in source:
            if line.startswith('%include'):
                spec = line.split()[1].strip()
                with open(spec) as included:
                    shutil.copyfileobj(included, uber)
            else:
                uber.write(line)

shutil.copy2('dart-uber.spec', 'scratch/dart-uber.spec')
