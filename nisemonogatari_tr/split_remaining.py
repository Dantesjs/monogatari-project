# -*- coding: utf-8 -*-
"""Kalan kaynak parçalarını küçük alt-parçalara böler (damga bütünlüğü korunur)."""
import os, re, math

WORK = '/data/data/com.termux/files/home/monogatari-project/nisemonogatari_tr'
CHUNKS = os.path.join(WORK, 'chunks')
SIZE = 130  # parça başına damga sayısı

TARGETS = ['tsukihi_01', 'tsukihi_02_b', 'tsukihi_03_a', 'tsukihi_04', 'tsukihi_05']
# tsukihi_03_b1 ve tsukihi_03_b3 zaten ~132 damga; bölmeye gerek yok.

STAMP = re.compile(r'^\[\[(?:P\d+|SECTION \d+)\]\]')

def split(base):
    path = os.path.join(CHUNKS, base + '.txt')
    lines = open(path, encoding='utf-8').read().splitlines()
    # damga başlayan satırların indeksleri
    idxs = [i for i, l in enumerate(lines) if STAMP.match(l)]
    n = len(idxs)
    npieces = math.ceil(n / SIZE)
    # eşit dağıt
    bounds = [round(k * n / npieces) for k in range(npieces + 1)]
    for k in range(npieces):
        start, end = bounds[k], bounds[k + 1]
        s, e = idxs[start], (idxs[end] if end < n else len(lines))
        out = lines[s:e]
        op = os.path.join(CHUNKS, f'{base}_p{k+1}.txt')
        with open(op, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(out) + '\n')
        first = re.match(r'\[\[(P\d+|SECTION \d+)\]\]', out[0]).group(1)
        last = re.findall(r'\[\[(?:P\d+|SECTION \d+)\]\]', '\n'.join(out))[-1]
        print(f'{os.path.basename(op)}: {end-start} damga, {first} .. {last}, {len(out)} satır')

for t in TARGETS:
    split(t)
