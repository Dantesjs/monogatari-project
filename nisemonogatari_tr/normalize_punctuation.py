# -*- coding: utf-8 -*-
"""Denetçi bulgularına göre noktalama/üslup normalizasyonu."""
import os, re

TRANS = '/data/data/com.termux/files/home/monogatari-project/nisemonogatari_tr/translated'
FILES = (
    [f'karen_{i:02d}_tr.txt' for i in range(1, 7)]
    + ['tsukihi_01_tr.txt', 'tsukihi_02_a_tr.txt', 'tsukihi_02_b_tr.txt',
       'tsukihi_03_a_tr.txt'] + [f'tsukihi_03_b{i}_tr.txt' for i in range(1, 5)]
    + [f'tsukihi_{i:02d}_tr.txt' for i in range(4, 7)]
    + ['afterword_karen_tr.txt', 'afterword_tsukihi_tr.txt']
)

stats = {}
for name in FILES:
    path = os.path.join(TRANS, name)
    txt = open(path, encoding='utf-8').read()
    orig = txt
    # 1) ham uzun çizgi ve çift em tire -> tek em tire
    txt = txt.replace('──', '—')
    txt = re.sub(r'—{2,}', '—', txt)
    # 2) ASCII üç nokta -> korunacak Japonca üç nokta çifti (kılavuz kuralı)
    txt = txt.replace('...', '……')
    stats[name] = {
        'dash': orig.count('──') + len(re.findall(r'—{2,}', orig)),
        'dots': orig.count('...'),
    }
    if txt != orig:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(txt)

# 3) Gövdedeki Japon tırnak (yalnızca P0117; notlardakiler bilinçli)
p = os.path.join(TRANS, 'tsukihi_01_tr.txt')
t = open(p, encoding='utf-8').read()
t = t.replace('[[P0117]] 「Hmm. O zaman kim acaba…… Bir yerden duymuş gibi geliyor ya.」',
              '[[P0117]] "Hmm. O zaman kim acaba…… Bir yerden duymuş gibi geliyor ya."')
open(p, 'w', encoding='utf-8').write(t)

# 4) Denetçi önerileri
p = os.path.join(TRANS, 'karen_03_tr.txt')
t = open(p, encoding='utf-8').read()
t = t.replace('[[P3206]] "Tsubasa-san, diye.', '[[P3206]] "Tsubasa-san," diye.')
open(p, 'w', encoding='utf-8').write(t)

p = os.path.join(TRANS, 'tsukihi_06_tr.txt')
t = open(p, encoding='utf-8').read()
t = t.replace('ciddi……Karen\'ın tarzını taklit ediyorsan', 'Yahu……Karen\'ın tarzını taklit ediyorsan')
open(p, 'w', encoding='utf-8').write(t)

for name, s in stats.items():
    if s['dash'] or s['dots']:
        print(f'{name}: {s["dash"]} tire, {s["dots"]} üç-nokta normalize edildi')
print('Normalizasyon tamamlandı.')
