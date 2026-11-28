# -*- coding: utf-8 -*-
"""Monogatari TR EPUB'lerini ReadEra'da ayrı bir seride toplar.

Seri adı: monogatari(türkce)
Okuma sırası (kaynak Kodansha Box setiyle aynı):
  01 Bakemonogatari, 04 Kizumonogatari, 05 Nisemonogatari
ReadEra, EPUB OPF içindeki `calibre:series` ve `calibre:series_index`
alanlarını okuyarak seri grubunu ve sıralamayı belirler.
"""
import os, re, shutil, zipfile

FOLDER = '/storage/emulated/0/Download/Monogatari Türkçe'
SERIES = 'monogatari(türkce)'

BOOKS = [
    ('01_Bakemonogatari_TUM_BOLUMLER_TR.epub', '1',  '01 - Bakemonogatari (Türkçe)'),
    ('04_Kizumonogatari_TR.epub',               '4',  '04 - Kizumonogatari (Türkçe)'),
    ('05-06_Nisemonogatari_TR.epub',            '5',  '05 - Nisemonogatari (Türkçe)'),
]

def patch_epub(path, index, new_title):
    tmp = path + '.series.tmp'
    with zipfile.ZipFile(path, 'r') as zin:
        opf_name = next(n for n in zin.namelist() if n.lower().endswith('.opf'))
        opf = zin.read(opf_name).decode('utf-8')

        # Eser adını seri numarasıyla başlat (Japonca ciltlerle aynı biçim)
        opf = re.sub(r'(<dc:title[^>]*>).*?(</dc:title>)',
                     lambda m: m.group(1) + new_title + m.group(2),
                     opf, count=1, flags=re.S)

        # Varsa eski seri alanlarını kaldır
        opf = re.sub(r'\s*<meta name="calibre:series"[^>]*/>', '', opf)
        opf = re.sub(r'\s*<meta name="calibre:series_index"[^>]*/>', '', opf)
        opf = re.sub(r'\s*<meta property="belongs-to-collection"[^>]*>.*?</meta>', '', opf, flags=re.S)
        opf = re.sub(r'\s*<meta refines="#series-monogatari[^"]*"[^>]*>.*?</meta>', '', opf, flags=re.S)

        series_meta = (
            f'    <meta name="calibre:series" content="{SERIES}"/>\n'
            f'    <meta name="calibre:series_index" content="{index}"/>\n'
            f'    <meta property="belongs-to-collection" id="series-monogatari">{SERIES}</meta>\n'
            f'    <meta refines="#series-monogatari" property="collection-type">series</meta>\n'
            f'    <meta refines="#series-monogatari" property="group-position">{index}</meta>\n'
        )
        opf = opf.replace('</metadata>', series_meta + '  </metadata>', 1)

        with zipfile.ZipFile(tmp, 'w') as zout:
            # mimetype her zaman ilk ve sıkıştırılmamış olmalı
            if 'mimetype' in zin.namelist():
                zout.writestr('mimetype', zin.read('mimetype'), compress_type=zipfile.ZIP_STORED)
            for item in zin.infolist():
                if item.filename == 'mimetype':
                    continue
                data = zin.read(item.filename)
                if item.filename == opf_name:
                    data = opf.encode('utf-8')
                zout.writestr(item, data)
    os.replace(tmp, path)
    return opf_name

for name, idx, title in BOOKS:
    path = os.path.join(FOLDER, name)
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    opf_name = patch_epub(path, idx, title)
    print(f'{name}: {SERIES} #{idx}, başlık="{title}" ({opf_name})')
print('Seri metadata tamamlandı.')
