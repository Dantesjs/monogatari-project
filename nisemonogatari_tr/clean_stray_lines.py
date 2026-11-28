# -*- coding: utf-8 -*-
"""Derlemeyi bozan markdown başlık/yorum satırlarını temizler."""
import os, re

TRANS = '/data/data/com.termux/files/home/monogatari-project/nisemonogatari_tr/translated'
FILES = (
    [f'karen_{i:02d}_tr.txt' for i in range(1, 7)]
    + ['tsukihi_01_tr.txt', 'tsukihi_02_a_tr.txt', 'tsukihi_02_b_tr.txt',
       'tsukihi_03_a_tr.txt'] + [f'tsukihi_03_b{i}_tr.txt' for i in range(1, 5)]
    + [f'tsukihi_{i:02d}_tr.txt' for i in range(4, 7)]
    + ['afterword_karen_tr.txt', 'afterword_tsukihi_tr.txt']
)
STAMP = re.compile(r'^\[\[(?:P\d+|SECTION \d+)\]\]')

for name in FILES:
    path = os.path.join(TRANS, name)
    with open(path, encoding='utf-8') as fh:
        lines = fh.read().splitlines()
    kept = [l for l in lines if STAMP.match(l)]
    removed = [l for l in lines if not STAMP.match(l)]
    if removed:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(kept) + '\n')
        print(f'{name}: {len(removed)} satır kaldırıldı -> {[r[:50] for r in removed]}')
print('Temizlik tamamlandı.')
