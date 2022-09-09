# Copies files from origin and rename to

import glob
import json
import os
from PIL import Image
from warnings import warn

dirs = glob.glob("origin/assets/*/")

filenamePrefix = "emoji_u"
pngSize = 128
destDir = "tools/png/128/"

os.makedirs(destDir, exist_ok=True)

for dir in dirs:
    raw = open(dir + "metadata.json")
    meta = json.load(raw)

    print(meta["cldr"])

    assets = [
        *glob.glob(dir + "3D/*_3d.png"),
        *glob.glob(dir + "Default/3D/*_3d_default.png"),
    ]

    if len(assets) == 0 :
        warn("no assets found in: {dir}")
    elif len(assets) > 1 :
        warn("multiple assets found: {assets}")
    
    filename = filenamePrefix + meta["unicode"].replace(" ", "_")  + ".png";
    dest = destDir + filename

    for asset in assets:
        image = Image.open(asset)
        output = image.resize((pngSize, pngSize), Image.Resampling.LANCZOS)
        output.save(dest, "PNG", quality = 100)

