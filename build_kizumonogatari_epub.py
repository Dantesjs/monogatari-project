import os
import zipfile
import uuid
import datetime

BASE_DIR = "/data/data/com.termux/files/home/monogatari-project/kizumonogatari_epub"
EPUB_OUT = "/data/data/com.termux/files/home/monogatari-project/04_Kizumonogatari_TR.epub"

os.makedirs(f"{BASE_DIR}/META-INF", exist_ok=True)
os.makedirs(f"{BASE_DIR}/EPUB/styles", exist_ok=True)
os.makedirs(f"{BASE_DIR}/EPUB/text", exist_ok=True)

# 1. mimetype
with open(f"{BASE_DIR}/mimetype", "w", encoding="utf-8") as f:
    f.write("application/epub+zip")

# 2. container.xml
with open(f"{BASE_DIR}/META-INF/container.xml", "w", encoding="utf-8") as f:
    f.write("""<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>""")

print("Container and mimetype written.")
