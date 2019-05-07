import os

for root, _, files in os.walk(os.path.join('/tmp')):
    for name in files:
        if name.endswith('.EXTENSION'):
            pass
