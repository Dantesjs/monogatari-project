# -*- coding: utf-8 -*-
"""Mekanik doğrulama: kaynak/çeviri paragraf eşlemesi, damga bütünlüğü."""
import os, re, sys

WORK = '/data/data/com.termux/files/home/monogatari-project/nisemonogatari_tr'
CHUNKS = os.path.join(WORK, 'chunks')
TRANS = os.path.join(WORK, 'translated')

pairs = []
for name in sorted(os.listdir(CHUNKS)):
    if not name.endswith('.txt'):
        continue
    base = name[:-4]
    src = os.path.join(CHUNKS, name)
    tr = os.path.join(TRANS, base + '_tr.txt')
    if not os.path.exists(tr):
        print(f'EXMISSING  {base}: çeviri dosyası yok')
        continue
    pairs.append((base, src, tr))

def ids(path):
    out = []
    for line in open(path, encoding='utf-8'):
        m = re.match(r'\[\[(P\d+|SECTION \d+)\]\]', line)
        if m:
            out.append(m.group(1))
    return out

errors = 0
for base, src, tr in pairs:
    a, b = ids(src), ids(tr)
    if a != b:
        errors += 1
        print(f'MISMATCH   {base}: kaynak {len(a)} damga, çeviri {len(b)} damga')
        # ilk fark
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                print(f'           ilk fark #{i}: {x} != {y}')
                break
        if len(a) != len(b):
            print(f'           uzunluk farkı: kaynak son {a[-3:]}, çeviri son {b[-3:]}')
    else:
        print(f'OK         {base}: {len(a)} damga eşleşti')

print(f'\nToplam: {len(pairs)} çift, {errors} hata')
sys.exit(1 if errors else 0)
