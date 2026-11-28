# -*- coding: utf-8 -*-
"""Nisemonogatari TR: Karen Bee + Tsukihi Phoenix -> tek EPUB.
Önceki Bakemonogatari/Kizumonogatari TR EPUB yapısını örnek alır.
"""
import os, re, zipfile, datetime, html
from xml.sax.saxutils import escape

BASE = '/data/data/com.termux/files/home/monogatari-project'
WORK = os.path.join(BASE, 'nisemonogatari_tr')
TRANS = os.path.join(WORK, 'translated')
OUT = os.path.join(BASE, '05-06_Nisemonogatari_TR.epub')
BUILD = os.path.join(WORK, 'epub_build')

for d in [os.path.join(BUILD, 'META-INF'), os.path.join(BUILD, 'EPUB/text'), os.path.join(BUILD, 'EPUB/styles'), os.path.join(BUILD, 'EPUB/images')]:
    os.makedirs(d, exist_ok=True)

# ---------- 1. Çeviri satırlarını oku ----------
KAREN_CHUNKS = [f'karen_{i:02d}' for i in range(1, 7)]
TSUKIHI_CHUNKS = ['tsukihi_01', 'tsukihi_02_a', 'tsukihi_02_b', 'tsukihi_03_a',
                  'tsukihi_03_b1', 'tsukihi_03_b2', 'tsukihi_03_b3', 'tsukihi_03_b4',
                  'tsukihi_04', 'tsukihi_05', 'tsukihi_06']

notes = []  # (num, text, chapter_file, pid)
NOTE_START = 1

def render_chapter(chunks, chapter_file, bolum_id, title_main, title_sub):
    lines = []
    for c in chunks:
        path = os.path.join(TRANS, c + '_tr.txt')
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        lines += open(path, encoding='utf-8').read().splitlines()
    out = []
    last_sec = None
    section_ids = []
    for line in lines:
        if not line.strip():
            continue
        m = re.match(r'\[\[SECTION (\d+)\]\]', line)
        if m:
            sec = m.group(1)
            if sec != last_sec:
                sid = f'SEC{sec}'
                out.append(f'<h3 id="{sid}" class="section-no">{sec}</h3>')
                section_ids.append(sid)
                last_sec = sec
            continue
        m = re.match(r'\[\[(P\d+)\]\]\s?(.*)', line)
        if not m:
            raise ValueError('Beklenmeyen satır: ' + line[:120])
        pid, body = m.group(1), m.group(2)
        # dipnotları ayır, HTML kaçırma
        parts, pos = [], 0
        for nm in re.finditer(r'\[\[N: (.*?)\]\]', body):
            parts.append(escape(body[pos:nm.start()]))
            num = NOTE_START + len(notes)
            notes.append((num, nm.group(1), f'{chapter_file}', pid))
            parts.append(f'<a id="nr-{num}" href="notes.xhtml#note-{num}" epub:type="noteref" '
                         f'class="noteref"><sup>[{num}]</sup></a>')
            pos = nm.end()
        parts.append(escape(body[pos:]))
        out.append(f'<p id="{pid}">{"".join(parts)}</p>')
    title_html = escape(title_main).replace(': ', ':<br/>', 1)
    doc = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="tr">\n'
        f'<head><meta charset="utf-8"/><title>{escape(title_main)}</title>'
        '<link rel="stylesheet" type="text/css" href="../styles/main.css"/></head>\n'
        '<body>\n'
        f'<section epub:type="chapter" id="{bolum_id}">\n'
        f'<h1 class="chapter-title">{title_html}</h1>\n'
        f'<p class="chapter-sub">{escape(title_sub)}</p>\n'
        + '\n'.join(out) + '\n'
        '</section>\n</body>\n</html>\n'
    )
    with open(os.path.join(BUILD, 'EPUB/text', chapter_file), 'w', encoding='utf-8') as fh:
        fh.write(doc)
    return section_ids

karen_secs = render_chapter(KAREN_CHUNKS, 'chapter1.xhtml', 'karen_bee',
    'Altıncı Bölüm: Karen Arısı', '偽物語 （上） — 第六話　かれんビー')
tsukihi_secs = render_chapter(TSUKIHI_CHUNKS, 'chapter2.xhtml', 'tsukihi_phoenix',
    'Son Bölüm: Tsukihi Anka', '偽物語 （下） — 最終話　つきひフェニックス')

# Afterword'lar (yazarın kendi sesi) — ayrı bölümler olarak eklenir
AW_KAREN = os.path.join(TRANS, 'afterword_karen_tr.txt')
AW_TSUKIHI = os.path.join(TRANS, 'afterword_tsukihi_tr.txt')
if os.path.exists(AW_KAREN):
    render_chapter(['afterword_karen'], 'afterword_karen.xhtml', 'afterword_karen',
        'Yazarın Notu: Üst Cilt', '偽物語（上） — あとがき')
if os.path.exists(AW_TSUKIHI):
    render_chapter(['afterword_tsukihi'], 'afterword_tsukihi.xhtml', 'afterword_tsukihi',
        'Yazarın Notu: Alt Cilt', '偽物語（下） — あとがき')

# ---------- 2. Çevirmen notları ----------
notes_html = ['<?xml version="1.0" encoding="utf-8"?>',
 '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="tr">',
 '<head><meta charset="utf-8"/><title>Çevirmen Notları</title>',
 '<link rel="stylesheet" type="text/css" href="../styles/main.css"/></head>',
 '<body><section epub:type="chapter" id="cevirmen-notlari">',
 '<h1>Çevirmen Notları</h1><ol class="note-list">']
for num, ntext, cfile, pid in notes:
    notes_html.append(f'<li id="note-{num}" epub:type="footnote" role="doc-footnote">'
                      f'<span class="note-num">{num}.</span> {escape(ntext)} '
                      f'<a href="{cfile}#{pid}" class="backref" aria-label="Metindeki yere dön">↩</a></li>')
notes_html += ['</ol></section></body></html>', '']
with open(os.path.join(BUILD, 'EPUB/text/notes.xhtml'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(notes_html))

# ---------- 3. İçindekiler ----------
ARCS = [
    ('Altıncı Bölüm: Karen Arısı', 'chapter1.xhtml', 'karen_bee', karen_secs),
    ('Son Bölüm: Tsukihi Anka', 'chapter2.xhtml', 'tsukihi_phoenix', tsukihi_secs),
]
if os.path.exists(AW_KAREN):
    ARCS.append(('Yazarın Notu: Üst Cilt', 'afterword_karen.xhtml', 'afterword_karen', ['P0001']))
if os.path.exists(AW_TSUKIHI):
    ARCS.append(('Yazarın Notu: Alt Cilt', 'afterword_tsukihi.xhtml', 'afterword_tsukihi', ['P0001']))
idx = ['<?xml version="1.0" encoding="utf-8"?>',
 '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="tr">',
 '<head><meta charset="utf-8"/><title>İçindekiler</title>',
 '<link rel="stylesheet" type="text/css" href="../styles/main.css"/></head>',
 '<body><section id="icerindekiler"><h1>İçindekiler</h1><ol class="toc-list">']
for title, cf, bid, secs in ARCS:
    idx.append(f'<li><a href="{cf}#{bid}">{escape(title)}</a><ol class="subtoc-list">')
    for i, sid in enumerate(secs, 1):
        idx.append(f'<li><a href="{cf}#{sid}">{i:03d}</a></li>')
    idx.append('</ol></li>')
idx.append('<li><a href="notes.xhtml">Çevirmen Notları</a></li>')
idx += ['</ol></section></body></html>', '']
with open(os.path.join(BUILD, 'EPUB/text/icerindekiler.xhtml'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(idx))

# ---------- 4. nav.xhtml ----------
nav = ['<?xml version="1.0" encoding="utf-8"?>',
 '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="tr">',
 '<head><meta charset="utf-8"/><title>İçindekiler</title></head><body>',
 '<nav epub:type="toc" id="toc"><h1>İçindekiler</h1><ol>',
 '<li><a href="text/icerindekiler.xhtml">İçindekiler</a></li>']
for title, cf, bid, secs in ARCS:
    nav.append(f'<li><a href="text/{cf}">{escape(title)}</a><ol>')
    for i, sid in enumerate(secs, 1):
        nav.append(f'<li><a href="text/{cf}#{sid}">{i:03d}</a></li>')
    nav.append('</ol></li>')
nav.append('<li><a href="text/notes.xhtml">Çevirmen Notları</a></li>')
nav += ['</ol></nav>',
 '<nav epub:type="landmarks" hidden="hidden"><h2>Rehber</h2><ol>',
 '<li><a epub:type="bodymatter" href="text/chapter1.xhtml">Metin</a></li>',
 '<li><a href="text/notes.xhtml">Çevirmen Notları</a></li></ol></nav>',
 '</body></html>', '']
with open(os.path.join(BUILD, 'EPUB/nav.xhtml'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(nav))

# ---------- 5. toc.ncx ----------
ncx = ['<?xml version="1.0" encoding="utf-8"?>',
 '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="tr"><head>',
 '<meta name="dtb:uid" content="urn:uuid:NISEMONOGATARI-TR-TUM"/>',
 '<meta name="dtb:depth" content="2"/><meta name="dtb:totalPageCount" content="0"/>',
 '<meta name="dtb:maxPageNumber" content="0"/></head>',
 '<docTitle><text>Nisemonogatari — Türkçe Çeviri</text></docTitle><navMap>']
po = 1
ncx.append(f'<navPoint id="np{po}" playOrder="{po}"><navLabel><text>İçindekiler</text></navLabel><content src="text/icerindekiler.xhtml"/></navPoint>')
po += 1
for title, cf, bid, secs in ARCS:
    ncx.append(f'<navPoint id="np{po}" playOrder="{po}"><navLabel><text>{escape(title)}</text></navLabel><content src="text/{cf}"/>')
    po += 1
    for i, sid in enumerate(secs, 1):
        ncx.append(f'<navPoint id="np{po}" playOrder="{po}"><navLabel><text>{i:03d}</text></navLabel><content src="text/{cf}#{sid}"/></navPoint>')
        po += 1
    ncx.append('</navPoint>')
ncx.append(f'<navPoint id="np{po}" playOrder="{po}"><navLabel><text>Çevirmen Notları</text></navLabel><content src="text/notes.xhtml"/></navPoint>')
ncx += ['</navMap></ncx>', '']
with open(os.path.join(BUILD, 'EPUB/toc.ncx'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(ncx))

# ---------- 6. content.opf ----------
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
opf = ['<?xml version="1.0" encoding="UTF-8"?>',
 '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">',
 '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">',
 '<dc:identifier id="bookid">urn:uuid:nisemonogatari-tr-tum</dc:identifier>',
 '<dc:title>Nisemonogatari — Türkçe Çeviri</dc:title>',
 '<dc:creator>Nisio Isin</dc:creator>',
 '<dc:language>tr</dc:language>',
 '<dc:description>偽物語 第六話「かれんビー」と最終話「つきひフェニックス」の Türkçe çevirisi, açıklayıcı çevirmen notlarıyla birlikte.</dc:description>',
 '<meta property="dcterms:modified">' + now + '</meta>',
 '</metadata>',
 '<manifest>',
 '<item id="icerindekiler" href="text/icerindekiler.xhtml" media-type="application/xhtml+xml"/>',
 '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
 '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
 '<item id="c1" href="text/chapter1.xhtml" media-type="application/xhtml+xml"/>',
 '<item id="c2" href="text/chapter2.xhtml" media-type="application/xhtml+xml"/>',
]
if os.path.exists(AW_KAREN):
    opf.append('<item id="aw_karen" href="text/afterword_karen.xhtml" media-type="application/xhtml+xml"/>')
if os.path.exists(AW_TSUKIHI):
    opf.append('<item id="aw_tsukihi" href="text/afterword_tsukihi.xhtml" media-type="application/xhtml+xml"/>')
opf += [
 '<item id="notes" href="text/notes.xhtml" media-type="application/xhtml+xml"/>',
 '<item id="css" href="styles/main.css" media-type="text/css"/>',
 '<item id="cover" href="images/cover.jpg" media-type="image/jpeg" properties="cover-image"/>',
 '</manifest>',
 '<spine toc="ncx"><itemref idref="icerindekiler"/><itemref idref="c1"/><itemref idref="c2"/>',
]
if os.path.exists(AW_KAREN):
    opf.append('<itemref idref="aw_karen"/>')
if os.path.exists(AW_TSUKIHI):
    opf.append('<itemref idref="aw_tsukihi"/>')
opf += ['<itemref idref="notes"/></spine>', '</package>', '']
with open(os.path.join(BUILD, 'EPUB/content.opf'), 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(opf))

# ---------- 7. container.xml, mimetype, CSS ----------
with open(os.path.join(BUILD, 'META-INF/container.xml'), 'w', encoding='utf-8') as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n'
             '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
             '<rootfiles><rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/>'
             '</rootfiles></container>')
with open(os.path.join(BUILD, 'mimetype'), 'w', encoding='utf-8') as fh:
    fh.write('application/epub+zip')

CSS = '''body { font-family: serif; line-height: 1.6; margin: 1em; }
h1.chapter-title { text-align: center; font-size: 1.6em; margin: 2em 0 0.3em; }
p.chapter-sub { text-align: center; color: #666; font-size: 0.9em; margin-bottom: 2em; }
h3.section-no { text-align: center; color: #888; font-size: 1em; margin: 2em 0 1em; }
p { text-indent: 1em; margin: 0.4em 0; }
p:first-of-type { text-indent: 0; }
.noteref { text-decoration: none; }
.noteref sup { color: #a00; font-size: 0.7em; }
.note-list { line-height: 1.5; }
.note-num { font-weight: bold; }
.backref { text-decoration: none; color: #888; }
#cevirmen-notlari h1 { page-break-before: always; }
.toc-list, .subtoc-list { line-height: 1.8; }
'''
with open(os.path.join(BUILD, 'EPUB/styles/main.css'), 'w', encoding='utf-8') as fh:
    fh.write(CSS)

# ---------- 8. Kapak (kaynak EPUB'lerden) ----------
import zipfile as zf
cover_src = None
for epub, candidates in [
    (os.path.join(os.environ['HOME'], '.monogatari_epub_backup/06 Nisemonogatari, Part 2.epub'), ['OEBPS/cover.jpeg', 'cover.jpeg']),
    (os.path.join(os.environ['HOME'], '.monogatari_epub_backup/05 Nisemonogatari, Part 1.epub'), ['images/91quUZ9ApuL._SL1500_.jpg', 'images/00001.jpeg']),
]:
    try:
        z = zf.ZipFile(epub)
        for c in candidates:
            if c in z.namelist():
                cover_src = z.read(c)
                break
    except Exception:
        pass
    if cover_src:
        break
if cover_src:
    with open(os.path.join(BUILD, 'EPUB/images/cover.jpg'), 'wb') as fh:
        fh.write(cover_src)

# ---------- 9. ZIP ----------
tmp = OUT + '.tmp'
with zipfile.ZipFile(tmp, 'w') as zo:
    zo.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
    for root, dirs, files in os.walk(BUILD):
        for f in files:
            full = os.path.join(root, f)
            rel = os.path.relpath(full, BUILD)
            if rel == 'mimetype':
                continue
            zo.write(full, rel, compress_type=zipfile.ZIP_DEFLATED)
os.replace(tmp, OUT)
print(f'EPUB oluşturuldu: {OUT}')
print(f'Bölüm sayısı: 2, alt bölüm: Karen {len(karen_secs)}, Tsukihi {len(tsukihi_secs)}')
print(f'Çevirmen notu: {len(notes)}')
