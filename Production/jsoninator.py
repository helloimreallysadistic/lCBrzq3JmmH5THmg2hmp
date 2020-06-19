import os
from PIL import Image
import json

rootdir = os.path.dirname(os.path.realpath(__file__))
author = 'Lor and Company'
cr = 'Personal Use, Credits Required'
baselink = 'https://raw.githubusercontent.com/helloimreallysadistic/lCBrzq3JmmH5THmg2hmp/woah/Production'
downloadable = True

print(os.listdir())

js = []

for dir in os.listdir():
    if os.path.isdir(dir):
        for file in os.listdir(os.path.join(rootdir, dir)):
            if os.path.isfile(os.path.join(rootdir, dir, file)):
                print(file)
                im = Image.open(os.path.join(rootdir,dir,file))
                js.append({
                        "name": file.split('.')[0],
                        "author": author,
                        "url": '/'.join([baselink,dir,file]),
                        "thumbnail": '/'.join([baselink,dir,"thumb",file.split('.')[0]+'_thumb.jpg']),
                        "collections": dir,
                        "downloadable": downloadable,
                        "size": os.stat(os.path.join(rootdir,dir,file)).st_size,
                        "dimensions": str(im.size[0]) + 'x' + str(im.size[1]) + ' px',
                        "copyright": cr
                        })

with open('coordinator.json', "w") as f:
    f.write(json.dumps(js))
