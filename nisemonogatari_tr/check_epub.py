# -*- coding: utf-8 -*-
"""EPUB yapısal doğrulama."""
import zipfile, re, sys
from xml.etree import ElementTree as ET

EPUB = '/data/data/com.termux/files/home/monogatari-project/05-06_Nisemonogatari_TR.epub'
z = zipfile.ZipFile(EPUB)
names = z.namelist()
errs = []

# mimetype
if names[0] != 'mimetype' or z.getinfo('mimetype').compress_type != zipfile.ZIP_STORED:
    errs.append('mimetype ilk/uncompressed değil')
if z.read('mimetype') != b'application/epub+zip':
    errs.append('mimetype içeriği hatalı')

# XML well-formedness
for n in names:
    if n.endswith(('.xhtml', '.opf', '.ncx', '.xml')):
        try:
            ET.fromstring(z.read(n))
        except Exception as e:
            errs.append(f'XML hatası {n}: {e}')

# OPF manifest/spine
opf = ET.fromstring(z.read('EPUB/content.opf'))
NS = {'o': 'http://www.idpf.org/2007/opf'}
man = {it.get('id'): it.get('href') for it in opf.findall('.//o:manifest/o:item', NS)}
for iid, href in man.items():
    path = 'EPUB/' + href
    if path not in names:
        errs.append(f'manifest dosyası yok: {iid} -> {path}')
spine = [ir.get('idref') for ir in opf.findall('.//o:spine/o:itemref', NS)]
for sid in spine:
    if sid not in man:
        errs.append(f'spine idref manifestte yok: {sid}')

# nav/ncx bağlantıları
nav = z.read('EPUB/nav.xhtml').decode('utf-8')
for href in re.findall(r'href="([^"#]+)', nav):
    p = 'EPUB/' + href
    if p not in names:
        errs.append(f'nav hedefi yok: {href}')

# içerik sayıları
htmls = {n: z.read(n).decode('utf-8') for n in names if n.endswith('.xhtml')}
p_count = sum(len(re.findall(r'<p id="P\d+"', s)) for s in htmls.values())
note_count = len(re.findall(r'<li id="note-\d+"', htmls.get('EPUB/text/notes.xhtml', '')))
noteref_count = sum(len(re.findall(r'class="noteref"', s)) for s in htmls.values())

print(f'Dosya: {EPUB}')
print(f'ZIP girdisi: {len(names)}')
print(f'Manifest: {len(man)} öge, Spine: {len(spine)} öge')
print(f'Paragraf: {p_count}, dipnot: {note_count}, noteref: {noteref_count}')
print(f'Spine: {spine}')
if errs:
    print('\nHATALAR:')
    for e in errs:
        print(' -', e)
    sys.exit(1)
print('\nYapısal doğrulama: OK')
