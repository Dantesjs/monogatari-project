# -*- coding: utf-8 -*-
"""tsukihi_01 parçalarını tek çeviri dosyasında birleştirir."""
import os, re

TRANS = '/data/data/com.termux/files/home/monogatari-project/nisemonogatari_tr/translated'
parts = [os.path.join(TRANS, f'tsukihi_01_p{i}_tr.txt') for i in range(1, 10)]

lines = []
for p in parts:
    with open(p, encoding='utf-8') as fh:
        chunk = [l for l in fh.read().splitlines() if l.strip()]
    lines += chunk

out = os.path.join(TRANS, 'tsukihi_01_tr.txt')
with open(out, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')

ids = [re.match(r'\[\[(P\d+|SECTION \d+)\]\]', l).group(1) for l in lines]
print(f'tsukihi_01_tr.txt: {len(lines)} satır, {len(ids)} damga')
print(f'ilk={ids[0]} son={ids[-1]}')
