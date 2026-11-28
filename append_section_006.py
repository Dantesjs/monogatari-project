#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kizumonogatari - Bölüm 006 ekleme betiği"""

import zipfile, shutil, os, re

EPUB_DIR = "/data/data/com.termux/files/home/monogatari-project/kizumonogatari_epub"
EPUB_OUT = "/data/data/com.termux/files/home/monogatari-project/04_Kizumonogatari_TR.epub"
DOWNLOADS = "/storage/emulated/0/Download/Monogatari Türkçe/04_Kizumonogatari_TR.epub"

chapter_path = os.path.join(EPUB_DIR, "EPUB/text/chapter1.xhtml")
notes_path   = os.path.join(EPUB_DIR, "EPUB/text/notes.xhtml")
nav_path     = os.path.join(EPUB_DIR, "EPUB/nav.xhtml")
ncx_path     = os.path.join(EPUB_DIR, "EPUB/toc.ncx")
opf_path     = os.path.join(EPUB_DIR, "EPUB/content.opf")

# ── 006 HTML ──────────────────────────────────────────────────────────────────
sec6_html = """
      <h3 id="P1611" class="section-no">006</h3>

      <p id="P1612">Dershane harabeleri.</p>

      <p id="P1613">İşte şimdi buradaydık.</p>

      <p id="P1614">Öğretmensiz, öğrencisiz, tahta-kalem-silgi-derslik kavramlarının yalnızca hayaletinin soluk bir gölgesi olarak var olmaya devam eden bu yer; soyulmuş duvarları, çökmeye hazır tavanlarıyla gerçek bir hayalet evinden farksızdı.</p>

      <p id="P1615">Hâlâ üçümüzde.</p>

      <p id="P1616">Ben, Kiss-shot Acerola-orion Heart-under-blade —— ve Oshino Meme.</p>

      <p id="P1617">Üçümüz oturmuş, karanlığın içinde oturmuştuk. Kiss-shot sırtını duvara vermiş, küçük dizlerini göğsüne çekmiş; ben sırtımı başka bir duvara vermiş sızdım sayılırdım. Oshino'ya gelince —— bu adam sanki hiç yorulmuyormuş gibi, düz betona uzanmış tavan sıvalarını süzüyordu.</p>

      <p id="P1618">Rüzgâr esiyordu. Duvarlardan süzülen soğuk bir rüzgâr.</p>

      <p id="P1619">Üç avcı, Oshino'nun araya girmesiyle çekip gitmişti. Dramatik bir sahne yoktu: kapıyı çarpıp gitmediler, yemin edip dönmediler. Sadece —— gittiler. Sanki hiç gelmemiş gibi.</p>

      <p id="P1620">Ve sonra Oshino bize dönüp "İçeride konuşalım mı?" demişti.</p>

      <p id="P1621">O kadar.</p>

      <p id="P1622">O kadar mı kolaydı?</p>

      <p id="P1623">Üç vampir avcısı, bu adamın bir sözüyle çekip gitmişti.</p>

      <p id="P1624">—— ama geriye ne kaldı?</p>

      <p id="P1625">Kiss-shot'ın kolları, bacakları hâlâ yoktu.</p>

      <p id="P1626">Ben hâlâ vampirdim.</p>

      <p id="P1627">Çözülen hiçbir şey yoktu. Yalnızca tehlike bir adım geri çekilmişti —— ve bu adımın bedeli henüz belirsizdi.</p>

      <p id="P1628">「……demek istenileni anlamıyorum」</p>

      <p id="P1629">dedim.</p>

      <p id="P1630">「Denge tutuyorum」</p>

      <p id="P1631">dedi Oshino.</p>

      <p id="P1632">Sonunda —— adam buna yakın bir şey söyledi.</p>

      <p id="P1633">「Yani, bu benim işim」</p>

      <p id="P1634">「…………」</p>

      <p id="P1635">「Bu taraf ile o taraf arasında köprü」<a epub:type="noteref" href="notes.xhtml#note-69" id="ref-69" class="noteref"><sup>[69]</sup></a></p>

      <p id="P1636">Şunla birlikte —— diye sürdürdü Oshino.</p>

      <p id="P1637">「Söylememek de olmaz, vampir biraz sorunlu —— o tarafın varlığı olarak bile fazla güçlü. Üstelik bir de "怪異殺し"<a epub:type="noteref" href="notes.xhtml#note-70" id="ref-70" class="noteref"><sup>[70]</sup></a> var. Az önce Araragi-kun'un anlatımından anladığım kadarıyla, o üç kişinin üçü birden o çocuğa saldırmış olmasını sanki alçakça bir şeymiş gibi konuşuyordun; ama öyle değil. O çocuk —— Heart-under-blade —— buna değer bir varlık」</p>

      <p id="P1638">「Öyle övülünce utanırım」</p>

      <p id="P1639">Kiss-shot bunu söylerken göğsünü kabartıyordu.</p>

      <p id="P1640">Kabartılacak bir şey olmasa da kabartıyordu.</p>

      <p id="P1641">Pek de övülmüş sayılmaz gibi hissettim ama, neyse.</p>

      <p id="P1642">Asıl mesele Oshino'nun kimliğiydi.</p>

      <p id="P1643">「Kendini tanıt —— sonra yapacaksın demiştin」</p>

      <p id="P1644">「Oshino Meme.<a epub:type="noteref" href="notes.xhtml#note-71" id="ref-71" class="noteref"><sup>[71]</sup></a> Sabit ikametgâhı olmayan özgür ruhun tekiyim」</p>

      <p id="P1645">dedi.</p>

      <p id="P1646">「Söylüyorum ki, 妖怪変化<a epub:type="noteref" href="notes.xhtml#note-72" id="ref-72" class="noteref"><sup>[72]</sup></a> konusunda otorite sayılırım —— hahaha. O üçünden farklı olarak, doğaüstü avlamak pek de uzmanlık alanım sayılmaz」</p>

      <p id="P1647">「Uzmanlık alanın değil mi diyorsun」</p>

      <p id="P1648">「Daha açık söylersem: sevmiyorum」</p>

      <p id="P1649">「Ama —— bu senin işin değil mi?」</p>

      <p id="P1650">「Uzmanlığım denge tutmak demekti zaten. Tarafsız bir konumdan müzakere etmek. Zorla bir tanım yapacak olsam, arabulucu diyebilirsin」</p>

      <p id="P1651">Arabulucu?</p>

      <p id="P1652">Bu taraf ile o taraf arasında —— köprü?</p>

      <p id="P1653">Bu taraf neresi —— o taraf neresi?</p>

      <p id="P1654">Bu taraf insanlar, o taraf canavarlar mı?</p>

      <p id="P1655">Peki o zaman şu an ben —— hangi taraftayım?</p>

      <p id="P1656">「Canavar. Güzel. Ben 怪異 diyorum ama」</p>

      <p id="P1657">「怪異——」</p>

      <p id="P1658">「Ve o çocuk 怪異殺し olarak biliniyor —— ne anlama geldiğini anlarsın.怪異'den enerji emebilen, nadir bir vampir türü. Dolayısıyla ünlü bir çocuk ——」</p>

      <p id="P1659">「İsteyerek ünlü olmadım ki」</p>

      <p id="P1660">Bu sefer Kiss-shot şımarık bir çocuk gibi söyledi.</p>

      <p id="P1661">On yaş civarı gerçekten zor bir çağ, diye düşündüm —— ama sonra, bu herifin yaşı göründüğü gibi değil ki, diye düzelttim kendimi.</p>

      <p id="P1662">İnsanı görünüşüyle yargılama dersen de, buna alışmak zaman alır tabii ki…… Bu yüzden bir an önce tam güç moduna dönmesini istiyorum açıkçası.</p>

      <p id="P1663">「Bilip de konuşma —— çocuk」<a epub:type="noteref" href="notes.xhtml#note-73" id="ref-73" class="noteref"><sup>[73]</sup></a></p>

      <p id="P1664">Kiss-shot Oshino'ya "çocuk" diye sesleniyordu.</p>

      <p id="P1665">Gerçekten beş yüz yaşındaysa, hiç de yanlış değil.</p>

      <p id="P1666">Üstelik Oshino'nun Kiss-shot'a "o çocuk", "şu çocuk" diye seslenmesi de alabildiğince küstahça aslında.</p>

      <p id="P1667">Ama Oshino hiç aldırmıyordu; "çocuk" denilmesine de.</p>

      <p id="P1668">「Haklısın, Heart-under-blade」</p>

      <p id="P1669">dedi.</p>

      <p id="P1670">「Dedikodularla insanı yargılamamalı —— karşındaki insan da olsa, insan olmayan da olsa. Ama yine de, az önce sizin konuşmanızı yarı yarıya dinledim —— oldukça çetrefilli bir iş gibi görünüyor. Bu kadar karmaşık bir şey olacağını düşünmezdim」</p>

      <p id="P1671">「Çetrefilli falan değil. Gayet basit bir mesele」</p>

      <p id="P1672">「Uzun ömürlü bir vampirin zaman algısıyla bakarsan, öyledir —— ama biz insanlar için sıkıntılı. Değil mi, Araragi-kun?」</p>

      <p id="P1673">「え」</p>

      <p id="P1674">Vay canına.</p>

      <p id="P1675">Bu adam —— her şeyi bilip.</p>

      <p id="P1676">Olağanmış gibi —— beni insan sayıverdi.</p>

      <p id="P1677">Bu tarafta —— dedi.</p>

      <p id="P1678">「…………」</p>

      <p id="P1679">「Hm? Ne oldu, tepkin yavaş —— Araragi-kun, sen insan olmak istiyorsun, değil mi? Yanılıyor muyum?」</p>

      <p id="P1680">「Yok, öyle ama ——」</p>

      <p id="P1681">「İnsan olmak isteyen insandır」</p>

      <p id="P1682">Temelde böyle, dedi Oshino —— ve bu kez Kiss-shot'a baktı.</p>

      <p id="P1683">Yan bakış.</p>

      <p id="P1684">「Üstelik —— senden hoşlandım, Heart-under-blade. Buyur ettiğin Araragi-kun'u düzgünce insana döndürme niyetin için」<a epub:type="noteref" href="notes.xhtml#note-74" id="ref-74" class="noteref"><sup>[74]</sup></a></p>

      <p id="P1685">「Fı」</p>

      <p id="P1686">Ama bu kez, açıkça övülmüşken Kiss-shot oturmuş somurtuyordu.</p>

      <p id="P1687">「Arabulucu falan bilmem —— gereksiz şeyleri söyleme çocuk. Ben eskiden beri işe karışanları sevmezdim」</p>

      <p id="P1688">「İşe karışmak? Benden en uzak kelime o. Ben daha çok çekingen sayılırım. Neyse. İşe karışmak istemiyorum ama ——」</p>

      <p id="P1689">Oshino Meme —— sırtüstü uzanmış halde söylüyordu.</p>

      <p id="P1690">Hiç ikna edici olmayan bir duruşla, söylüyordu.</p>

      <p id="P1691">「—— isterseniz, aranıza girebilirim」</p>

      <p id="P1692">「Ah —— araya girmek dedin」</p>

      <p id="P1693">Bu taraf ile o taraf arasına —— araya?</p>

      <p id="P1694">「O —— üç kişinin arasına mı?」</p>

      <p id="P1695">「Başka ne olabilir ki」</p>

      <p id="P1696">Oshino başıyla onayladı.</p>

      <p id="P1697">「Aslında —— bu dershane harabesini tanıtmış ve 結界<a epub:type="noteref" href="notes.xhtml#note-75" id="ref-75" class="noteref"><sup>[75]</sup></a> kurmuş olmam yeterli sayılırdı; ama bu da bir kader diyeyim. Ne yaparsın —— araya gireyim mi girmeyeyim mi?」</p>

      <p id="P1698">「Y —— yardım edecek misin demek istiyorsun?」</p>

      <p id="P1699">「Yardım etmiyorum. Sadece güç veriyorum」</p>

      <p id="P1700">dedi Oshino.</p>

      <p id="P1701">「Şu haliyle denge biraz bozuk gibi —— bu hâl zorbalık gibi görünüyor. Az önce de söyledim, benim o üçünün yaptığı türden "temizleme"yi pek sevmiyorum ——」</p>

      <p id="P1702">「O zaman —— sen bizim tarafımızda mısın?」</p>

      <p id="P1703">「Değilim. Ne taraflarındasın ne karşınızdayım」</p>

      <p id="P1704">Tarafsızım, dedi Oshino.</p>

      <p id="P1705">「"Aranıza gireceğim" dedim —— yani, ortaya gireceğim demek. Oradan sonrası sizin elinizde. Asıl hareketi yapan ben değilim. Olayın tam ortasındaki kişiler kendi elleriyle kor içindeki kestaneyi almak zorunda<a epub:type="noteref" href="notes.xhtml#note-76" id="ref-76" class="noteref"><sup>[76]</sup></a> —— ben ne nedene ne sonuca müdahil olurum. En fazla süreci ayarlarım」</p>

      <p id="P1706">「…………」</p>

      <p id="P1707">Kiss-shot'a baktım —— Kiss-shot da Oshino'nun bu tavrı karşısında şaşkın görünüyordu.</p>

      <p id="P1708">Bu adam ne oluyor?</p>

      <p id="P1709">Hiç aldırmadan —— sanki bu doğalmış gibi.</p>

      <p id="P1710">İşleri idare etmeye çalışıyor —— mu?</p>

      <p id="P1711">「Ah, tabii ki ben de iş olarak yaptığımdan bedava olmaz. Ne de olsa gezgin bir serserim, yol parası önemli. Bakalım —— iki yüz bin TL olsa nasıl?」<a epub:type="noteref" href="notes.xhtml#note-77" id="ref-77" class="noteref"><sup>[77]</sup></a></p>

      <p id="P1712">「İ, iki yüz……!?」</p>

      <p id="P1713">Şaşkınlıkla bağırdım; Oshino sakin kaldı.</p>

      <p id="P1714">「Olduğunda ödeme, isterim yok. Yani, şimdi değil sonra. Bu kadarını talep etmesem —— denge tutmaz」</p>

      <p id="P1715">「…… a, ama」</p>

      <p id="P1716">İnanmaktan başka çarem yoktu —— yine de.</p>

      <p id="P1717">Gerçekten bu adama güvenilir miydi?</p>

      <p id="P1718">Bu —— tesadüfen yoldan geçen adama mı?</p>

      <p id="P1719">Bu dershane harabesini Kiss-shot'a göstermesi de, beni o üçünden kurtarması da —— 結界'yi bir yana bıraksak bile, güvenmeye yetecek kadar şey yapmış sayılabilir; ama yine de ——</p>

      <p id="P1720">Yine de bir şekilde şüpheli.</p>

      <p id="P1721">「……Somut planı dinleyelim」</p>

      <p id="P1722">Kiss-shot —— yalnızca on yedi küsur yıl yaşamış olan benden farklı olarak, Oshino ile başa baş gidebiliyordu.</p>

      <p id="P1723">Öyle —— girdi konuya.</p>

      <p id="P1724">「Arabulucu desen de kolay değil —— o üçünü ikna edemezsin. Tarafsız diyorsun ya, demek ki benim kollarımı bacaklarımı geri almak senin işin değil —— değil mi?」</p>

      <p id="P1725">「Orasına kadar ben karışamam —— fazla işe karışmış olurum. Plan da henüz tam oturmadı」</p>

      <p id="P1726">Oshino beklenmedik şekilde rahat bir şey söyledi.</p>

      <p id="P1727">Ama bu, düzgün hazırlanmış bir plandan daha güvenilir hissettirdi.</p>

      <p id="P1728">Rahatlık hissettiriyordu.</p>

      <p id="P1729">「Yapabileceğim şey, baş eğip yalvarmak. Samimiyetle —— yalvaramıyorsam tehlikeli yollara başvurmak zorunda kalırım; ama neyse ki konuşulabilecek türden insanlardı」</p>

      <p id="P1730">「Oyun —— mu dersin?」</p>

      <p id="P1731">「Ama önce o üçünü birbirinden ayırmak lazım. Birer birer karşılaşılırsa sorun yok —— değil mi, Heart-under-blade? Senin okumanın bu olduğunu varsayıyorum. O zaman bunu gerçekleştirelim」</p>

      <p id="P1732">Tabii ki, dedi Oshino.</p>

      <p id="P1733">「Sizin bir miktar…… belli riskler almanız gerekecek —— bunu lütfen kabulleniverirsiniz」</p>

      <p id="P1734">「Yok, o zaten başından belliydi. Kararlıyım —— tabii ki ben ve hizmetçim de」</p>

      <p id="P1735">Kararım benim yerime verilmişti.</p>

      <p id="P1736">Benim kararım olmasına rağmen……</p>

      <p id="P1737">「Peki ya çocuk, o üçüyle nasıl müzakere edeceksin?」</p>

      <p id="P1738">「Dediğim gibi, baş eğip yalvaracağım —— ne de olsa konuşulabilecek türden insanlardı」</p>

      <p id="P1739">Oshino şaka gibi bir şey söyledi.</p>

      <p id="P1740">O üç kişi için "konuşulabilecek türden" demek —— onlar hiçbir şekilde diyalog kurmaya açık değildi ki. Bu adam ne kadar barışçıl biriydi?</p>

      <p id="P1741">「Ayrıntılar ticari sır sayılır…… ama sahayı ben hazırlayayım. Ve Araragi-kun, Heart-under-blade'in kollarını bacaklarını onlardan geri alır. İki kol iki bacak geri gelirse —— Heart-under-blade gücünü toparlar, o zaman da Araragi-kun insana döner」</p>

      <p id="P1742">「…… geri almak, ha」</p>

      <p id="P1743">Yine de en zor kısmı ben yapacaktım.</p>

      <p id="P1744">Birer birer karşılaşmak desen de —— o üç kişi.</p>

      <p id="P1745">Dramaturgy, Episode, Guillotinecutter.</p>

      <p id="P1746">Dalgalı çift büyük kılıç, dev haç, kimliği belirsiz adam.</p>

      <p id="P1747">Dürüst olursam, kazanabileceğime hiç inanmıyordum……</p>

      <p id="P1748">Kendim için yapmam gerektiğinden yapmak zorundayım; ama bu gece olduğu gibi hazırlıksız saldıramazdım.</p>

      <p id="P1749">Hatta bu gece fazla düşünmemişim.</p>

      <p id="P1750">Sakin görünmeye çalışırken aslında panikte idim.</p>

      <p id="P1751">Ben de —— ve aynı şekilde Kiss-shot da.</p>

      <p id="P1752">O yüzden.</p>

      <p id="P1753">Yeniden karşı karşıya gelinirse —— bir tür plan şart.</p>

      <p id="P1754">「Hey, hizmetçi」</p>

      <p id="P1755">Kiss-shot —— bana seslendi.</p>

      <p id="P1756">「…… ne var, Kiss-shot」</p>

      <p id="P1757">「İnsan parasına sahip değilim —— iki yüz bin ne anlama geliyor pek bilmiyorum, ama sen bu borcu taşıyabilir misin」</p>

      <p id="P1758">「…………」</p>

      <p id="P1759">「Merak etme. Bu çocuğun becerisi gerçek —— burası gösterildi, sen kurtarıldı, bunların hepsini dışarıda bıraksan bile. Şu an ne kadar güçsüz olsam bile bunu anlayabilirim」</p>

      <p id="P1760">「Ama —— düşmanı değil, tarafsızı değil, orta noktayı?」</p>

      <p id="P1761">「En başından müttefik beklemiyordum, bulunduğum yeri bilen bu herifin düşman olması halinde zaten her şey biterdi. Düşünmenin faydası yok…… tarafsız diyorsa ne istesek bu」</p>

      <p id="P1762">「…… ah」</p>

      <p id="P1763">Böyle bir bakış açısı da vardı.</p>

      <p id="P1764">Ne kadar sert ve hesaplı.</p>

      <p id="P1765">Üstelik, bu kadar açıkça söylememek bir yana, Oshino'nun müzakeresi başarısız olsa bile eksi olmazdı zaten.</p>

      <p id="P1766">Soğuk olan yalnızca gözler değilmiş.</p>

      <p id="P1767">O yüzden —— bir sorun kalırsa, sadece bir tanesi.</p>

      <p id="P1768">Yoldan geçen bir adam.</p>

      <p id="P1769">Yoldan geçmek.</p>

      <p id="P1770">Ama —— Oshino'nun oradan geçmesi gerçekten tesadüf müydü, diye soruyordum kendime.</p>

      <p id="P1771">Kiss-shot gidecek bir yer bulamayıp bocaladığında orada bulunması, benim o üçü tarafından avlandığım anda orada bulunması —— yine de bu kadar çok tesadüf olmaz değil mi?</p>

      <p id="P1772">Orada bir niyet olduğunu varsayalım —— bunun bize ne etkisi olacak bilinmez, Oshino'nun çıkarı ne olabilir bilinmez —— ama yine de fazla fazla tesadüf gibi geliyordu.</p>

      <p id="P1773">Ama —— bu kadar olabilirdi de.</p>

      <p id="P1774">Gerçekleşmiş bir tesadüf olduğundan, geçmişe bakıp öyle yorumluyorum belki —— bu kapıyı araladığımda, sömestr sonu töreninin bittiği öğleden sonra, okul çevresinde dolaşırken okul kapısından çıkan Hanekawa ile çarpışmam bile sıradan bir tesadüf değilmiş gibi gelirdi.<a epub:type="noteref" href="notes.xhtml#note-78" id="ref-78" class="noteref"><sup>[78]</sup></a></p>

      <p id="P1775">Düşününce o gece Hanekawa ile karşılaşmasaydım, o gece eve kaçıp kitabevine gitmeyecektim, yani Kiss-shot ile karşılaşmayacaktım da —— fazla düşünüyorum herhalde.</p>

      <p id="P1776">Belki "şansım varmış" diyip geçebilirdim.</p>

      <p id="P1777">Şimdilik.</p>

      <p id="P1778">……Bu kadar hafif meşrep bir adamla karşılaşmış olmayı "şans" kelimesiyle ifade etmek istemez bir yanım kesinlikle vardı ama……</p>

      <p id="P1779">Canını kurtaran kişiye kesinlikle söylemek istemediğim şeyler var, dürüst olursam —— bu adamın en nefret ettiğim insan tipinin ta kendisi olduğu gerçeği bunların başında geliyordu.</p>

      <p id="P1780">Yine de.</p>

      <p id="P1781">Yine de ben kararlılıkla ağzımı açıp söyledim.</p>

      <p id="P1782">「Öyle birikimim yok ama…… "olduğunda ödeme, isterim yok" diyorsan ve kefil de istemiyorsan…… ben taşırım」</p>

      <p id="P1783">Ne yapayım.</p>

      <p id="P1784">Bu yaşta borçlu olmak ne kadar acı —— ama çaresiz.<a epub:type="noteref" href="notes.xhtml#note-79" id="ref-79" class="noteref"><sup>[79]</sup></a></p>

      <p id="P1785">「Tamam~! Hahaha. İyi iş~, diyeyim」</p>

      <p id="P1786">Oshino gülünç derecede rahat bir sesle söyledi.</p>

      <p id="P1787">「Ben de bugünden itibaren burada kalacağım. Tanışalım. Hani, aslında bu şehre geldiğimden beri bu yere gözüm takılmıştı. 義を見てせざるは勇なきなり<a epub:type="noteref" href="notes.xhtml#note-80" id="ref-80" class="noteref"><sup>[80]</sup></a> deyip Heart-under-blade'e bıraktım; ama bu şehirde bunun üzerinde bir harabe yokmuş. Neyse —— ne yaparsın? Önümüzdeki günlere karşı morali yükseltmek için el ele tutuşup bir daire oluşturalım mı?」</p>

      <p id="P1788">Sırtüstü uzanmış, bu konuşmadan en uzak duruşuyla bunu söyleyen Oshino'nun çağrısına —— elbette, ne ben ne Kiss-shot kulak astı.</p>

      <p id="P1789">Saat farkında olmadan gece yarısını çoktan geçmişti.</p>

      <p id="P1790">Tarih, 29 Mart'a dönmüştü.</p>

      <p id="P1791">Yarın demek —— zaten bugün yarındı.</p>
"""

# ── 006 DİPNOTLAR ────────────────────────────────────────────────────────────
sec6_notes = """    <li id="note-69">
      <span class="note-num">[69]</span>
      <strong>「Bu taraf ile o taraf arasında köprü」(こちらとあちらの橋渡し)</strong> — Oshino'nun Monogatari serisindeki en belirleyici ifadesi. "Bu taraf" (こちら) insan dünyası, "o taraf" (あちら) doğaüstü âlem demektir. Oshino, insanlar ile怪異 arasında tarafsız bir aracı olarak konumlandırır kendini; bu ilke serinin ilerleyen kitaplarında tekrar tekrar yankılanır. <a href="chapter1.xhtml#ref-69" class="backref">↩</a>
    </li>
    <li id="note-70">
      <span class="note-num">[70]</span>
      <strong>怪異殺し (かいいごろし — Kaii Goroshi, "Anomali Katili")</strong> — Kiss-shot'ın tüm doğaüstü âlemde tanındığı unvanı. Sıradan vampirler yalnızca insanlık enerjisini emmesine karşın, Kiss-shot diğer 怪異'lerden de güç devşirebildiği için bu lakapla anılır. 怪異 kelimesi Türkçe'de tam karşılığı bulunmayan bir kavramdır: anomali, mucize, canavar ve hayalet kavramlarını aynı anda barındırır; serinin ilerleyen bölümlerinde ayrıntılı incelenecektir. <a href="chapter1.xhtml#ref-70" class="backref">↩</a>
    </li>
    <li id="note-71">
      <span class="note-num">[71]</span>
      <strong>忍野メメ (Oshino Meme) — İsim Oyunu</strong> — Yazar Nisio Isin'in neredeyse tüm Monogatari karakterleri için kurduğu derin isim oyununu burada da görmekteyiz. 忍 (Shinobu) kanji'si hem "gizlenmek / katlanmak" anlamına gelir hem de serinin ilerleyen bölümünde Kiss-shot'ın alacağı Türkçe isimle (Shinobu) doğrudan bağlantılıdır —— sanki Oshino, isminde Kiss-shot'ın geleceğini taşıyormuş gibi. 野 (no) "alan, kır, yaban" demektir; メメ (Meme) ise anlamsız tekrarlı bir hece olup Batı'daki "meme" kavramıyla tesadüfi bir ses benzerliği taşır. Tüm isim bir bütün olarak "yabanda gizlice dolaşan anlamsız adam" izlenimi verir. <a href="chapter1.xhtml#ref-71" class="backref">↩</a>
    </li>
    <li id="note-72">
      <span class="note-num">[72]</span>
      <strong>妖怪変化 (ようかいへんげ — Yōkai Henge)</strong> — "Dönüşen yokai"; şekil değiştirebilen ya da gerçek doğasını gizleyebilen doğaüstü varlıkları tanımlar. Oshino bu terimi 怪異'nin daha eski, geleneksel Japon folklorundan gelen karşılığı olarak kullanır. Kendisini bu alanda "otorite" sayması, akademik mi yoksa deneyimsel mi olduğu konusundaki muğlaklığı kasıtlıdır. <a href="chapter1.xhtml#ref-72" class="backref">↩</a>
    </li>
    <li id="note-73">
      <span class="note-num">[73]</span>
      <strong>「小僧」(こぞう — Kozō, "Çocuk / Küçük Budala")</strong> — Genellikle küçümseme içeren bir hitap biçimi; Japonca'da yaşça küçük ya da deneyimsiz biri için kullanılır. Kiss-shot'ın Oshino'ya böyle seslenmesi, beş yüz yıllık geçmişini göz önünde bulundurduğumuzda nesnel bir doğruluk taşır. Türkçe'de tam karşılığı "çocuk" değil, "küçük it", "serseri çocuk" gibi ifadeler olabilirdi; ancak metnin tonu ve hâlâ çocuk görünümündeki Kiss-shot'ın ağzından çıktığı göz önüne alınarak "çocuk" tercih edilmiştir. <a href="chapter1.xhtml#ref-73" class="backref">↩</a>
    </li>
    <li id="note-74">
      <span class="note-num">[74]</span>
      <strong>「眷属とした阿良々木くんを、ちゃんと人間に戻してあげようという、きみの心意気」</strong> — Oshino'nun burada Kiss-shot'a "buyur ettiğin Araragi-kun'u gönüllü olarak insana döndürme niyetin için" demesi kritik bir ayrıntı. Çünkü bir vampir normalde kendisine hizmet eden bir insan vasisi (眷属 — kendzoku) yaratır ve bunu bozma zorunluluğu yoktur; Kiss-shot'ın bu niyeti, onun insan değerlerine olan derin bağını ortaya koyar. <a href="chapter1.xhtml#ref-74" class="backref">↩</a>
    </li>
    <li id="note-75">
      <span class="note-num">[75]</span>
      <strong>結界 (けっかい — Kekkai, "Kutsal Bariyer")</strong> — Japon spiritüel geleneğinde ruhsal sınırları çizen koruyucu bariyer. Basit bir "engel" değil, kutsal bir mekânı gündelik dünyadan ayıran manevi bir perdedir; tapınak sınırlarından ritüel alanlarına kadar Japon kültüründe geniş bir kullanım alanına sahiptir. Oshino'nun bu tekniğe hâkim olması, onun sıradan bir insan olmadığına işaret eder. <a href="chapter1.xhtml#ref-75" class="backref">↩</a>
    </li>
    <li id="note-76">
      <span class="note-num">[76]</span>
      <strong>「火中の栗を拾う」(かちゅうのくりをひろう)</strong> — "Kor içindeki kestaneyi almak" deyimi; Türkçe'deki "ateşten paluze çıkarmak" ya da "körün elinden ekmek almak" ifadelerine yakın. Tehlikeli bir işi kişinin kendisinin yapması gerektiğini, başkasının riske girmeyeceğini anlatır. Oshino bu deyimi kasıtlı olarak seçer: o yalnızca "sahayı hazırlar", gerçek tehlikeyle yüzleşmek Araragi'ye düşer. <a href="chapter1.xhtml#ref-76" class="backref">↩</a>
    </li>
    <li id="note-77">
      <span class="note-num">[77]</span>
      <strong>二百万円 (nikihyaku-man-en — İki Milyon Yen) → Türkçe'de iki yüz bin TL olarak yerelleştirilmiştir</strong> — Orijinal metinde 2.000.000 Yen'dir; günümüz kurlarında yaklaşık 500.000 TL'ye denk gelse de, lise öğrencisinin gözünden "astronomik bir borç" izlenimi verecek şekilde iki yüz bin TL olarak yerelleştirilmiştir. Oshino bu bedeli tespit ederken "denge" diyor olması, onun ideolojisinin ekonomik boyutunu da özetler: serbest yardım denge bozar; bedel ise dengeyi korur. <a href="chapter1.xhtml#ref-77" class="backref">↩</a>
    </li>
    <li id="note-78">
      <span class="note-num">[78]</span>
      <strong>Hanekawa ile sömestr sonu karşılaşması — Kelebek Etkisi</strong> — Araragi burada derin bir varoluşsal soruyla yüzleşir: Hanekawa ile o öğleden sonra karşılaşmasaydı, o gece kitabevine gitmeyecekti; kitabevine gitmeseydi Kiss-shot ile hiç karşılaşmayacaktı. Nisio Isin bu an aracılığıyla "tesadüfün tesadüf gibi görünmemesi" sorununu gündeme getirir — belirsiz bir kader anlayışının izine düşer, ama hiçbir şeyi kesin yanıtlamaz. Monogatari serisinde Hanekawa'nın her kritik anda "doğru yerde bulunması" tesadüf değil, yapısal bir motif olarak işlev görür. <a href="chapter1.xhtml#ref-78" class="backref">↩</a>
    </li>
    <li id="note-79">
      <span class="note-num">[79]</span>
      <strong>「この歳で借金持ちとは悲しい限り」("Bu yaşta borçlu olmak ne kadar acı")</strong> — Araragi'nin alışılmış iç sesi; trajik bir durumu melankolik değil, kuru bir mizahla yorumlar. Nisio Isin'in bu alaycı anlatı sesi, Monogatari serisinin en belirgin üslup özelliklerinden biridir ve Türkçe çeviride de korunmaya özen gösterilmiştir. <a href="chapter1.xhtml#ref-79" class="backref">↩</a>
    </li>
    <li id="note-80">
      <span class="note-num">[80]</span>
      <strong>「義を見てせざるは勇なきなり」(ぎをみてせざるはゆうなきなり)</strong> — Konfüçyüs'ten alınan klasik Çin-Japon deyimi: "Yapılması gereken doğruyu görüp yapmamak, cesaretsizliktir." Türkçe'deki "gördüğüm yerde yapardım ama elimden çıkmış iş" ile kısmen örtüşür. Oshino bunu dershane harabesini önceden gözlemleyip Kiss-shot'a bırakmasını meşrulaştırmak için kullanır —— ama tam olarak neyi "haklı gördüğünü" belirsiz bırakır; bu da onun karakterindeki stratejik muğlaklığın bir parçasıdır. <a href="chapter1.xhtml#ref-80" class="backref">↩</a>
    </li>"""

# ── CHAPTER1.XHTML GÜNCELLE ───────────────────────────────────────────────────
with open(chapter_path, "r", encoding="utf-8") as f:
    ch = f.read()

insert_before = "    </section>"
idx = ch.rfind(insert_before)
ch = ch[:idx] + sec6_html + "\n" + ch[idx:]
with open(chapter_path, "w", encoding="utf-8") as f:
    f.write(ch)
print("chapter1.xhtml güncellendi")

# ── NOTES.XHTML GÜNCELLE ──────────────────────────────────────────────────────
with open(notes_path, "r", encoding="utf-8") as f:
    nt = f.read()

insert_before_notes = "  </ol>"
last = nt.rfind(insert_before_notes)
nt = nt[:last] + sec6_notes + "\n" + nt[last:]
with open(notes_path, "w", encoding="utf-8") as f:
    f.write(nt)
print("notes.xhtml güncellendi")

# ── NAV.XHTML GÜNCELLE ────────────────────────────────────────────────────────
with open(nav_path, "r", encoding="utf-8") as f:
    nav = f.read()

old_nav = '        </ol>\n      </nav>'
new_nav_entry = '          <li><a href="text/chapter1.xhtml#P1611">006 — Denge</a></li>\n'
nav = nav.replace(old_nav, '        ' + new_nav_entry + '      </ol>\n      </nav>')
with open(nav_path, "w", encoding="utf-8") as f:
    f.write(nav)
print("nav.xhtml güncellendi")

# ── TOC.NCX GÜNCELLE ─────────────────────────────────────────────────────────
with open(ncx_path, "r", encoding="utf-8") as f:
    ncx = f.read()

new_ncx_entry = """  <navPoint id="navPoint-7" playOrder="7">
    <navLabel><text>006 — Denge</text></navLabel>
    <content src="text/chapter1.xhtml#P1611"/>
  </navPoint>
"""
ncx = ncx.replace("</navMap>", new_ncx_entry + "</navMap>")
with open(ncx_path, "w", encoding="utf-8") as f:
    f.write(ncx)
print("toc.ncx güncellendi")

# ── EPUB REPACKAGE ────────────────────────────────────────────────────────────
if os.path.exists(EPUB_OUT):
    os.remove(EPUB_OUT)

import os
orig_dir = os.getcwd()
os.chdir(EPUB_DIR)
os.system(f'zip -X "{EPUB_OUT}" mimetype')
os.system(f'zip -rg "{EPUB_OUT}" META-INF EPUB')
os.chdir(orig_dir)

size = os.path.getsize(EPUB_OUT)
print(f"EPUB oluşturuldu: {EPUB_OUT} ({size:,} bytes)")

# ── İNDİRİLENLER KOPYALA ─────────────────────────────────────────────────────
os.makedirs(os.path.dirname(DOWNLOADS), exist_ok=True)
shutil.copy2(EPUB_OUT, DOWNLOADS)
print(f"Kopyalandı: {DOWNLOADS}")
