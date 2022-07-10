import os
from PIL import Image
import json
from stat import S_ISREG, ST_CTIME, ST_MODE
from pathlib import Path

rootdir = os.path.dirname(os.path.realpath(__file__))
author = 'Lor and Company'
cr = 'Personal Use, Credits Required'
baselink = 'https://raw.githubusercontent.com/helloimreallysadistic/lCBrzq3JmmH5THmg2hmp/woah/Production'
downloadable = True

print(os.listdir())

js = []

paths = sorted(Path(rootdir).iterdir(), key=os.path.getmtime)
paths.reverse()
print(paths)
for dir in paths:
    actualdir = dir
    dir = dir.__str__()
    if os.path.isdir(dir):
        print(dir)
        if dir == "C:\\Users\\Metallic Semicolon\\Documents\\GitHub\\lCBrzq3JmmH5THmg2hmp\\Production\\blur":
            print("FUCKKKKK")
            continue
        items = os.listdir(dir)
        sortie = [(os.stat(os.path.join(dir , item)), os.path.join(dir , item), item) for item in items]
        entries = [(stat[ST_CTIME], path, name) for stat, path, name in sortie if S_ISREG(stat[ST_MODE])]
        a = sorted(entries, key=lambda entry: entry[0])
        a.reverse()
        dir = dir.split("\\")[-1]
        for file in a:
            if os.path.isfile(file[1]):
                print(file)
                im = Image.open(file[1])
                js.append({
                        "creationtime" : file[0],
                        "name": file[2].split('.')[0],
                        "author": author,
                        "url": '/'.join([baselink,dir,file[2]]),
                        "thumbnail": '/'.join([baselink,dir,"thumb",file[2].split('.')[0]+'_thumb.jpg']),
                        "collections": dir,
                        "downloadable": downloadable,
                        "size": os.stat(file[1]).st_size,
                        "dimensions": str(im.size[0]) + 'x' + str(im.size[1]) + ' px',
                        "copyright": cr
                        })

final = sorted(js, key=lambda l: l['creationtime'])
final.reverse()

with open('coordinator.json', "w") as f:
    f.write(json.dumps(final, indent=4, sort_keys=True))
