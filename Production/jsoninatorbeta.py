import os
from PIL import Image
import json
from stat import S_ISREG, ST_CTIME, ST_MODE

rootdir = os.path.dirname(os.path.realpath(__file__))
author = 'Lor and Company'
cr = 'Personal Use, Credits Required'
baselink = 'https://raw.githubusercontent.com/helloimreallysadistic/lCBrzq3JmmH5THmg2hmp/woah/Production'
downloadable = True

print(os.listdir())

js = []

for dir in os.listdir():
    if os.path.isdir(dir):
        items = os.listdir(os.path.join(rootdir, dir))
        sortie = [(os.stat(os.path.join(rootdir, dir , item)), os.path.join(rootdir, dir , item), item) for item in items]
        entries = [(stat[ST_CTIME], path, name) for stat, path, name in sortie if S_ISREG(stat[ST_MODE])]
        a = sorted(entries, key=lambda entry: entry[0])
        a.reverse()
        for file in a:
            if os.path.isfile(file[1]):
                im = Image.open(file[1])
                js.append({
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

with open('coordinator.json', "w") as f:
    f.write(json.dumps(js, indent=4, sort_keys=True))
