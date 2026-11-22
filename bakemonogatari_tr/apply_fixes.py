# -*- coding: utf-8 -*-
import glob,re,os
BASE=os.path.dirname(os.path.abspath(__file__))
files={os.path.basename(p)[:-4]:p for p in glob.glob(os.path.join(BASE,'translated','*_tr.txt'))}
data={k:open(v,encoding='utf-8').read() for k,v in files.items()}

# (scope prefix or '*', P-id or None for global, old, new)
FIX=[]
def f(scope,pid,old,new): FIX.append((scope,pid,old,new))
# --- Suruga: terminology / meaning ---
f('suruga','P0123','sınıfında en iyi notlara sahip','sınıf düzeyinde en iyi notlara sahip')
f('suruga','P0505','sınıfının en iyisi seviyesindeki notları','yılın en iyisi düzeyinde notları')
f('suruga','P0748','sınıf birincisi Hanekawa','yılın birincisi Hanekawa')
f('suruga','P0786','sınıflarımız farklı olsa da','sınıf düzeylerimiz farklı olsa da')
f('suruga','P1545','Sınıfımız da kulübümüz de farklıydı','Sınıf düzeyimiz de kulübümüz de farklıydı')
f('suruga','P1594','bu yıl atlamasından değil','sınıf düzeyleri farklı olduğu için değil')
f('suruga','P0984','başarı testi bitene kadar','yeterlilik sınavı bitene kadar')
f('suruga',None,'seviye sınavı','yeterlilik sınavı')
f('suruga',None,'yetkinlik sınavı','yeterlilik sınavı')
f('suruga','P0706','spora dönüştüğün dönemdeki seni','spor yaptığın dönemdeki seni')
f('suruga','P0657','gal game','galge')
f('suruga','P1509','spor bursu falanla','sporcu kontenjanı falanla')
f('suruga','P0613','Tavsiyeyi alabileceğim muhtemelen.','Tavsiyeyle giriş yapabileceğim muhtemelen.')
f('suruga','P0071','Kafaya takılan her şeyi unutabiliyorum.','Kafam kötü olan her şeyi unutabiliyorum.')
f('suruga','P0653','Sözde sözleşme, garantisi yok.','Lafta kalan söz, garantisi yok.')
f('suruga','P0794','"tak, tak, tak, tak, tak, tak"','"tap, tap, tap, tap, tap, tap"')
f('suruga','P1822','sol elimin öyle bir hâle geldiğini de bilmiyordum','senin sol elinin öyle bir hâle geldiğini de bilmiyordum')
f('suruga','P1791','Kanbaru\'nun bisiklete binmekten vazgeçmesinin','Kanbaru\'nun bisiklette iki kişi binmekten vazgeçmesinin')
f('suruga','P1911','sonunda kemerimin elini bıraktı','sonunda elini kemerimden çekti')
f('suruga','P1720','tuhaf bir şekilde bayat değildi','tuhaf biçimde sinikleşmemişti')
f('suruga','P1828','Kara kalpli bir inat.','Kara yürekli bir vazgeçmeyiş.')
f('suruga','P1985','Birinci dilek tuttuğumda, ikinci dileğim hazırdı ama—','Birinci dilek işe yararsa, ikinci dileğimi çoktan belirlemiştim ama—')
f('suruga','P2200','bu adam hayret verici','bu şey gerçekten şaşırtıcı')
f('suruga','P2675','"İyi ya, iyi ya, iyi ya, iyi ya, iyi ya, iyi ya, iyi ya."','"Ne cüret! Ne cüret, ne cüret, ne cüret, ne cüret, ne cüret, ne cüret!"')
f('suruga','P2753','Ölümü bin kez hak ettin.','Ölümü on bin kez hak ettin.')
f('suruga','P2865',"Hasarın iyileşmesi de 'tık tık' gibi bir şeydi sanki.",'Hasarla iyileşme başa baş gidiyor gibi bir şeydi sanki.')
f('suruga','P2879','biraz doğal kaçtığı','biraz doğal olmayan (yapay) bir hâlde olduğu')
f('suruga','P0024','ikili örgülü','ikili atkuyruğu')
f('suruga','P0021','"A…… Aryaryagi-san?"','"A…… Aryaryagi-san"')
f('suruga','P0408','Isırıp durdum!','Isırıp gördüm!')
f('suruga','P1337','o doğaüstü güç meselesini','o olağanüstü güç meselesini')
f('suruga','P1338','Doğaüstü güç.','Olağanüstü güç.')
f('suruga','P1643','Sizi bir vampirin saldırdığını duydum','Size bir vampirin saldırdığını duydum')
# small suruga
for pid,old,new in [
 ('P1718','Valhalla ikilisisiniz','Valhalla ikilisiniz'),
 ('P1726','cinsel konulardan ilgi duyar','cinsel konulara ilgi duyar'),
 ('P1758','Az önce beri','Bir süredir'),
 ('P1868','giymeği','giymeyi'),
 ('P1655',"o'nun",'onun'),
 ('P1944','Kırı kutusu','kiri kutusu'),
 ('P2021','adımlar','çabaları'),
 ('P2099','yağmurluklu yaratık beni defalarca saldıracak','yağmurluklu yaratık bana defalarca saldıracak'),
 ('P2243','Dilek, dileği gibi yerine gelmeli','Dilek, dilediği gibi yerine gelmeli'),
 ('P2285','refleksler','hareket yetisi'),
 ('P2379','kasırga önlemleri','tayfun önlemleri'),
 ('P2422','yarı beline kadar devrildi','bedeninin yarısıyla devrildi'),
 ('P2561','ağlak şeytan','feryatçı şeytan'),
 ('P2606','«く» harfi gibi','V biçiminde'),
]: f('suruga',pid,old,new)
# --- Nadeko ---
f('nadeko','P0636','Böyle önemsenince','Böyle kaba muamele görünce')
f('nadeko','P0231','Senjōgahara sizin için hayran olduğunuz bir senpai olsa da','Senjōgahara senin için hayran olduğun bir senpai olsa da')
f('nadeko','P0307','az da olsa bir oni\'nin kanı','azımsanmayacak kadar oni kanı')
f('nadeko','P0661','diye düşünerek tapınağa vardım; beş dakika sonra... ki bu da','diye düşünürken beş dakika sonra tapınağa vardım; ki bu da')
f('nadeko','P0810','sınıf yedincisi toplam puanı','yılın yedincisi toplam puanı')
f('nadeko','P1329','sınıflar farklı ama','sınıf düzeyleri farklı ama')
f('nadeko','P1329','Notları sınıfın en iyisi çünkü.','Notları yılın en iyisi çünkü.')
f('nadeko','P0166','Yedi harf.','Yedi kana.')
f('nadeko','P0167','«Araragi-senpai» ise sekiz harf.','«Araragi-senpai» ise sekiz kana.[[N: Japonca yazıda あららぎこよみ yedi, あららぎせんぱい sekiz karaktardır; Araragi burada kana sayısını kasteder.]]')
f('nadeko','P1374','bu, pek de rastlanır bir tavırdı.','bu, Oshino için pek de rastlanır bir tavır değildi.')
f('nadeko','P1703','Yoksa anlaşılmadı mı?','Belli oldu mu?')
f('nadeko','P1397','Ödül parası gözüne girip','Ödül parası peşinde')
f('nadeko','P1427','"Hı-hı" diye','"Hayır" diye')
f('nadeko','P1576','tam da yetişkin olduğun için, bir genç kızın çıplaklığı karşısında uygunsuz duyguların olabileceği gerçeğini, ileride işine yarar diye bilmekte fayda var.','Koyomi abin yetişkin olduğu için, genç kızın çıplaklığı karşısında uygunsuz hisler olabilir; bunu ileride işine yarar diye bilmen iyi olur.')
f('nadeko','P1871','Keyfine düşkünlük değil, bu sadece kafasına esmesi.','Kaprisli diyelim, ama aslında bu sadece bencilce.')
f('nadeko','P2530','Onu tersinden kınayan kişi','Ona kin besleyen kişi')
for pid,old,new in [
 ('P0540','hop hop hop diye','hop hop hop hop diye'),
 ('P1094','Beş-altı çalma sesi.','Yaklaşık beş çalma sesi.'),
 ('P1145','üzerinden on dakika geçti','üzerinden on dakikadan fazla geçti'),
 ('P1007','erken emekli oldu','erken ayrıldı'),
 ('P1096','adamın adıyla soyadıyla öz tanıtım yaptı','hemen adını soyadını söyleyip kendini tanıttı'),
 ('P2497','Tam bu yüzden hissediyorum.','Tam bu yüzden acıyla hissediyorum.'),
 ('P2519','Kış gelsin bahar gelir','Kış gelirse bahar gelir'),
 ('P2520','Gece gelsin sabah gelir','Gece gelirse sabah gelir'),
 ('P2476','Yılan—gidiyor','Yılan—dönüyor'),
]: f('nadeko',pid,old,new)

log=[]
for scope,pid,old,new in FIX:
    targets=[k for k in data if k.startswith(scope)] if scope!='*' else list(data)
    if pid: targets=[k for k in targets if re.match(rf'^{re.escape(scope)}_\d+[ab]?_tr$',k)]  # restrict by prefix
    hits=0
    for k in targets:
        # if pid given, only edit the file containing that pid
        if pid and f'[[{pid}]]' not in data[k]: continue
        if old in data[k]:
            data[k]=data[k].replace(old,new); hits+=1
    if not hits: log.append(f'NOT FOUND [{scope} {pid or "GLOBAL"}] {old[:70]!r} -> {new[:70]!r}')
    else: log.append(f'OK [{scope} {pid or "GLOBAL"}] x{hits}: {old[:50]!r} -> {new[:50]!r}')

# global formatting across all files
for k in data:
    data[k]=data[k].replace('——','—')
    data[k]=re.sub(r'\s*—\s*','—',data[k])
    data[k]=data[k].replace('『','«').replace('』','»')

for k,v in data.items():
    open(files[k],'w',encoding='utf-8').write(v)
open(os.path.join(BASE,'fix_log.txt'),'w',encoding='utf-8').write('\n'.join(log)+'\n')
print('\n'.join(log))
print('FAILED:',sum(1 for x in log if x.startswith('NOT FOUND')))
