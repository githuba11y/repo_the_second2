import os

def read_file(filename):          # user-controlled input
    path = os.path.join("/var/data", filename)  # ← source
    with open(path) as f:                       # ← sink
        return f.read()
