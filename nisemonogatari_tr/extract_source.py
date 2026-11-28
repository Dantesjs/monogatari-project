# -*- coding: utf-8 -*-
"""Nisemonogatari (上/下) source extractor.
Strips ruby furigana, emits [[SECTION nnn]] and [[Pnnnn]] tagged lines,
splits into ~50 KB chunks for translation.
"""
import zipfile, re, html, os

BASE = '/data/data/com.termux/files/home'
OUT  = os.path.join(BASE, 'monogatari-project/nisemonogatari_tr')
os.makedirs(os.path.join(OUT, 'source'), exist_ok=True)
os.makedirs(os.path.join(OUT, 'chunks'), exist_ok=True)
os.makedirs(os.path.join(OUT, 'translated'), exist_ok=True)

SRC = [
    ('karen',  os.path.join(BASE, '.monogatari_epub_backup/05 Nisemonogatari, Part 1.epub'),
     r'text/part0008_split_\d+\.html', '第六話　かれんビー'),
    ('tsukihi', os.path.join(BASE, '.monogatari_epub_backup/06 Nisemonogatari, Part 2.epub'),
     r'OEBPS/part(?:0007|0008|0009|0010|0011|0012|0013|0014|0015|0016|0017|0018|0019)\.xhtml', '最終話　つきひフェニックス'),
]

def clean(s):
    # remove ruby furigana, keep base text
    s = re.sub(r'<ruby[^>]*>(.*?)<rt[^>]*>.*?</rt>(.*?)</ruby>', r'\1\2', s, flags=re.S)
    s = re.sub(r'<rt[^>]*>.*?</rt>', '', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    s = s.replace('\u3000', ' ').strip()
    return s

for tag, epub, pattern, title in SRC:
    z = zipfile.ZipFile(epub)
    files = sorted([n for n in z.namelist() if re.search(pattern, n)])
    lines = []
    pid = 0
    sec = 0
    for f in files:
        s = z.read(f).decode('utf-8', errors='replace')
        # Part 2 uses <h1 class="heading_s2b">003</h1> for section numbers
        for hm in re.finditer(r'<h1[^>]*>\s*([0-9０-９]{3})\s*</h1>', s):
            num = int(hm.group(1).translate(str.maketrans('０１２３４５６７８９','0123456789')))
            if num != sec:
                sec = num
                lines.append(f'[[SECTION {sec:03d}]]')
        for pm in re.finditer(r'<p(?:\s[^>]*)?>(.*?)</p>', s, flags=re.S):
            t = clean(pm.group(1))
            if not t:
                continue
            # section number like ００１ on its own line
            m = re.fullmatch(r'([０-９]{3})', t)
            if m:
                num = int(m.group(1).translate(str.maketrans('０１２３４５６７８９','0123456789')))
                if num != sec:
                    sec = num
                    lines.append(f'[[SECTION {sec:03d}]]')
                continue
            pid += 1
            lines.append(f'[[P{pid:04d}]] {t}')
    src_path = os.path.join(OUT, 'source', f'{tag}_source.txt')
    with open(src_path, 'w', encoding='utf-8') as fh:
        fh.write(f'# {title}\n')
        fh.write('\n'.join(lines) + '\n')
    print(f'{tag}: {pid} paragraphs, {sec} sections -> {src_path}')

# split into chunks ~45k chars by paragraph boundaries
CHUNK = 45000
for tag, _, _, _ in SRC:
    src_path = os.path.join(OUT, 'source', f'{tag}_source.txt')
    txt = open(src_path, encoding='utf-8').read().splitlines()
    header = [l for l in txt if l.startswith('#')]
    body = [l for l in txt if not l.startswith('#')]
    cur, size, idx = [], 0, 1
    for line in body:
        cur.append(line); size += len(line) + 1
        if size >= CHUNK:
            p = os.path.join(OUT, 'chunks', f'{tag}_{idx:02d}.txt')
            with open(p, 'w', encoding='utf-8') as fh:
                fh.write('\n'.join(header + cur) + '\n')
            print(' chunk', p, size)
            cur, size, idx = [], 0, idx + 1
    if cur:
        p = os.path.join(OUT, 'chunks', f'{tag}_{idx:02d}.txt')
        with open(p, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(header + cur) + '\n')
        print(' chunk', p, size)
