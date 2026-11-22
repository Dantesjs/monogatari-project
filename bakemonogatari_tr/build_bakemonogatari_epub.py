# -*- coding: utf-8 -*-
"""Bakemonogatari TR EPUB: Suruga Maymunu + Nadeko Yılanı ekle, 5 bölümü sırala."""
import zipfile, re, os, html, datetime
from xml.sax.saxutils import escape

BASE = '/data/data/com.termux/files/home/monogatari-project'
SRC_EPUB = os.path.join(BASE, '01_Bakemonogatari_TUM_BOLUMLER_TR.epub')
WORK = os.path.join(BASE, 'bakemonogatari_tr')
TRANSLATED = os.path.join(WORK, 'translated')

z = zipfile.ZipFile(SRC_EPUB)
parts = {n: z.read(n) for n in z.namelist()}
text = {n: v.decode('utf-8') for n, v in parts.items() if n.endswith(('.xhtml', '.opf', '.ncx'))}

# 1) Eski chapter3 (Tsubasa) -> chapter5; tüm iç referansları güncelle
old = text.pop('EPUB/text/chapter3.xhtml')
text['EPUB/text/chapter5.xhtml'] = old
for n in list(text):
    text[n] = text[n].replace('chapter3.xhtml', 'chapter5.xhtml').replace('bolum3', 'bolum5')

# 2) Yeni bölümleri üret
NOTE_START = 482
notes = []  # (num, text, chapter_file, pid)

def render_chapter(chunks, title, subtitle, bolum):
    lines = []
    for c in chunks:
        lines += open(os.path.join(TRANSLATED, c + '_tr.txt'), encoding='utf-8').read().splitlines()
    out = []
    last_sec = None
    for line in lines:
        if not line.strip():
            continue
        m = re.match(r'\[\[SECTION (\d+)\]\]', line)
        if m:
            sec = m.group(1)
            if sec != last_sec:
                out.append(f'<h3 id="SEC{sec}" class="section-no">{sec}</h3>')
                last_sec = sec
            continue
        m = re.match(r'\[\[(P\d+)\]\]\s?(.*)', line)
        if not m:
            raise ValueError('Beklenmeyen satır: ' + line[:120])
        pid, body = m.group(1), m.group(2)
        # Metni parça parça kaçır; dipnot HTML'ini kaçırma (aksi halde literal görünür).
        parts, pos = [], 0
        for nm in re.finditer(r'\[\[N: (.*?)\]\]', body):
            parts.append(escape(body[pos:nm.start()]))
            num = NOTE_START + len(notes)
            notes.append((num, nm.group(1), f'chapter{bolum}.xhtml', pid))
            parts.append(f'<a id="nr-{num}" href="notes.xhtml#note-{num}" epub:type="noteref" '
                         f'class="noteref"><sup>[{num}]</sup></a>')
            pos = nm.end()
        parts.append(escape(body[pos:]))
        out.append(f'<p id="{pid}">{"".join(parts)}</p>')
    chapter_file = f'chapter{bolum}.xhtml'
    title_main, _, title_sub = title.partition(': ')
    title_html = escape(title_main) + ('<br/>' + escape(title_sub) if title_sub else '')
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="tr">\n'
        f'<head><meta charset="utf-8"/><title>{escape(title)}</title>'
        '<link rel="stylesheet" type="text/css" href="../styles/main.css"/></head>\n'
        '<body>\n'
        f'<section epub:type="chapter" id="bolum{bolum}">\n'
        f'<h1 class="chapter-title">{title_html}</h1>\n'
        f'<p class="chapter-sub">{escape(subtitle)}</p>\n'
        + '\n'.join(out) + '\n'
        '</section>\n</body>\n</html>\n'
    ), [x for x in out if x.startswith('<h3')]

suruga_chunks = ['suruga_01','suruga_02','suruga_03','suruga_04','suruga_05',
                 'suruga_06','suruga_07a','suruga_08b','suruga_09']
nadeko_chunks = ['nadeko_01','nadeko_02a','nadeko_03b','nadeko_04','nadeko_05',
                 'nadeko_06','nadeko_07']
suruga_html, suruga_secs = render_chapter(suruga_chunks,
    'Üçüncü Bölüm: Suruga Maymunu', '化物語 （中） — 第三話　するがモンキー', 3)
nadeko_html, nadeko_secs = render_chapter(nadeko_chunks,
    'Dördüncü Bölüm: Nadeko Yılanı', '化物語 （中） — 第四話　なでこスネイク', 4)
text['EPUB/text/chapter3.xhtml'] = suruga_html
text['EPUB/text/chapter4.xhtml'] = nadeko_html

# 3) Dipnotları genişlet
notes_html = text['EPUB/text/notes.xhtml']
add = ''
for num, ntext, cfile, pid in notes:
    add += (f'<li id="note-{num}"><span class="note-num">{num}.</span> {escape(ntext)} '
            f'<a href="{cfile}#{pid}" class="backref" aria-label="Metindeki yere dön">↩</a></li>\n')
assert '</ol>' in notes_html
notes_html = notes_html.replace('</ol>', add + '</ol>', 1)
text['EPUB/text/notes.xhtml'] = notes_html

# 4) Bölüm/alt bölüm dizinleri
ARCS = [
    (1, 'Birinci Bölüm: Hitagi Yengeci', 'chapter1.xhtml', 'bolum1',
     ['P0001','P0029','P0172','P0444','P0766','P1274','P1705','P1816']),
    (2, 'İkinci Bölüm: Mayoi Salyangozu', 'chapter2.xhtml', 'bolum2',
     ['P1828','P1862','P2390','P2670','P3006','P3340','P3962','P4180','P4395']),
    (3, 'Üçüncü Bölüm: Suruga Maymunu', 'chapter3.xhtml', 'bolum3',
     [f'SEC{i:03d}' for i in range(1,10)]),
    (4, 'Dördüncü Bölüm: Nadeko Yılanı', 'chapter4.xhtml', 'bolum4',
     [f'SEC{i:03d}' for i in range(1,8)]),
    (5, 'Beşinci Bölüm: Tsubasa Kedisi', 'chapter5.xhtml', 'bolum5',
     ['P0001','P0016','P0509','P1534','P1980','P2496','P2967','P4321']),
]

nav = ('<?xml version="1.0" encoding="utf-8"?>\n'
 '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="tr">\n'
 '<head><meta charset="utf-8"/><title>İçindekiler</title></head>\n<body>\n'
 '<nav epub:type="toc" id="toc">\n<h1>İçindekiler</h1>\n<ol>\n'
 '<li><a href="text/icerindekiler.xhtml">İçindekiler</a></li>\n')
for _, title, cf, _, anchors in ARCS:
    nav += f'<li><a href="text/{cf}">{escape(title)}</a>\n<ol>\n'
    for i, a in enumerate(anchors, 1):
        nav += f'<li><a href="text/{cf}#{a}">{i:03d}</a></li>\n'
    nav += '</ol>\n</li>\n'
nav += ('</ol>\n</nav>\n<nav epub:type="landmarks" hidden="hidden">\n<h2>Rehber</h2>\n'
        '<ol><li><a epub:type="bodymatter" href="text/chapter1.xhtml">Metin</a></li></ol>\n'
        '</nav>\n</body>\n</html>\n')
text['EPUB/nav.xhtml'] = nav

ncx = ('<?xml version="1.0" encoding="utf-8"?>\n'
 '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="tr">\n<head>\n'
 '<meta name="dtb:uid" content="urn:uuid:BACKEMONOGATARI-TR-TUM"/>\n'
 '<meta name="dtb:depth" content="2"/>\n<meta name="dtb:totalPageCount" content="0"/>\n'
 '<meta name="dtb:maxPageNumber" content="0"/>\n</head>\n'
 '<docTitle><text>Bakemonogatari — Türkçe Çeviri (Tüm Bölümler)</text></docTitle>\n<navMap>\n')
po = 1
ncx += f'<navPoint id="np{po}" playOrder="{po}"><navLabel><text>İçindekiler</text></navLabel><content src="text/icerindekiler.xhtml"/></navPoint>\n'
po += 1
for _, title, cf, _, anchors in ARCS:
    ncx += (f'<navPoint id="np{po}" playOrder="{po}"><navLabel><text>{escape(title)}</text></navLabel>'
            f'<content src="text/{cf}"/>\n')
    po += 1
    for i, a in enumerate(anchors, 1):
        ncx += (f'<navPoint id="np{po}" playOrder="{po}"><navLabel><text>{i:03d}</text></navLabel>'
                f'<content src="text/{cf}#{a}"/></navPoint>\n')
        po += 1
    ncx += '</navPoint>\n'
ncx += '</navMap>\n</ncx>\n'
text['EPUB/toc.ncx'] = ncx

idx = ('<?xml version="1.0" encoding="utf-8"?>\n'
 '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="tr">\n'
 '<head><meta charset="utf-8"/><title>İçindekiler</title>\n'
 '<link rel="stylesheet" type="text/css" href="../styles/main.css"/></head>\n<body>\n'
 '<section id="icerindekiler">\n<h1>İçindekiler</h1>\n'
 '<p class="note-intro">Beş bölüm ve alt bölümler; dilediğiniz yerden başlayabilirsiniz.</p>\n'
 '<ol class="toc-list">\n')
for i, title, cf, bid, anchors in ARCS:
    idx += f'<li><a href="{cf}#{bid}">{escape(title)}</a>\n<ol class="subtoc-list">\n'
    for j, a in enumerate(anchors, 1):
        idx += f'<li><a href="{cf}#{a}">{j:03d}</a></li>\n'
    idx += '</ol>\n</li>\n'
idx += '</ol>\n</section>\n</body>\n</html>\n'
text['EPUB/text/icerindekiler.xhtml'] = idx

# 5) OPF
opf = text['EPUB/content.opf']
manifest = '<manifest>\n' + ''.join(
    f'<item id="{i}" href="{h}" media-type="{m}"{extra}/>\n' for i,h,m,extra in [
      ('icerindekiler','text/icerindekiler.xhtml','application/xhtml+xml',''),
      ('nav','nav.xhtml','application/xhtml+xml',' properties="nav"'),
      ('ncx','toc.ncx','application/x-dtbncx+xml',''),
      ('c1','text/chapter1.xhtml','application/xhtml+xml',''),
      ('c2','text/chapter2.xhtml','application/xhtml+xml',''),
      ('c3','text/chapter3.xhtml','application/xhtml+xml',''),
      ('c4','text/chapter4.xhtml','application/xhtml+xml',''),
      ('c5','text/chapter5.xhtml','application/xhtml+xml',''),
      ('notes','text/notes.xhtml','application/xhtml+xml',''),
      ('css','styles/main.css','text/css',''),
      ('cover','cover.jpg','image/jpeg',' properties="cover-image"'),
    ]) + '</manifest>\n'
spine = ('<spine toc="ncx">\n' + ''.join(
    f'<itemref idref="{x}"/>\n' for x in
    ['icerindekiler','c1','c2','c3','c4','c5','notes']) + '</spine>\n')
opf = re.sub(r'<manifest>.*?</manifest>', manifest, opf, flags=re.S)
opf = re.sub(r'<spine.*?</spine>', spine, opf, flags=re.S)
opf = re.sub(r'<dc:description>.*?</dc:description>',
    '<dc:description>化物語 第一話「ひたぎクラブ」、第二話「まよいマイマイ」、第三話「するがモンキー」、第四話「なでこスネイク」、第五話「つばさキャット」 Türkçe çevirisi, açıklayıcı çevirmen notlarıyla birlikte.</dc:description>',
    opf, flags=re.S)
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
opf = re.sub(r'<meta property="dcterms:modified">.*?</meta>',
             f'<meta property="dcterms:modified">{now}</meta>', opf)
text['EPUB/content.opf'] = opf

# 6) Yaz
outparts = dict(parts)
for n, s in text.items(): outparts[n] = s.encode('utf-8')
tmp = SRC_EPUB + '.tmp'
with zipfile.ZipFile(tmp, 'w') as zo:
    zo.writestr('mimetype', outparts['mimetype'], compress_type=zipfile.ZIP_STORED)
    for n, v in outparts.items():
        if n == 'mimetype': continue
        zo.writestr(n, v, compress_type=zipfile.ZIP_DEFLATED)
os.replace(tmp, SRC_EPUB)
print(f'EPUB güncellendi: {SRC_EPUB}')
print(f'Yeni dipnot: {len(notes)} (note-{NOTE_START}..note-{NOTE_START+len(notes)-1})')
print(f'Suruga alt bölüm: {len(suruga_secs)}, Nadeko alt bölüm: {len(nadeko_secs)}')
