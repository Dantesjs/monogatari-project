# -*- coding: utf-8 -*-
import os, zipfile, datetime

BASE_DIR = "/data/data/com.termux/files/home/monogatari-project/kizumonogatari_epub"
EPUB_OUT = "/data/data/com.termux/files/home/monogatari-project/04_Kizumonogatari_TR.epub"

# ==========================================
# SECTION 003 HTML
# ==========================================

sec3_html = """
<h3 id="P0481" class="section-no">003</h3>

<p id="P0482">Ve sonra…</p>

<p id="P0483">Ve işte, o hatıranın sıcaklığı dahi henüz soğumamışken, tam da o günün gecesinde olanlar oldu.</p>

<p id="P0484">Gece.</p>

<p id="P0485">Zifiri karanlığa gömülmüş kasabanın sokaklarında yine tabana kuvvet yürüyordum. Gündüz vakti bisiklete binmeyip okulun çevresinde amaçsızca turlamamın elle tutulur bir sebebi yoktu belki; lakin şu an, tam da bu gece saatinde bisiklete binmememin gayet bariz ve somut bir gerekçesi vardı.</p>

<p id="P0486">Sırası gelmişken belirteyim, iki tane bisikletim vardır.<a id="nr-28" href="notes.xhtml#note-28" epub:type="noteref" class="noteref"><sup>[28]</sup></a></p>

<p id="P0487">Biri okula gidip gelirken kullandığım sepetli külüstür şehir bisikleti — diğeri ise gözüm gibi baktığım favori dağ bisikletim.</p>

<p id="P0488">İkincisi, hiçbir işim gücüm olmasa dahi sırf sürmek için bineceğim kadar bayıldığım bir aletti; gelgelelim bu gece ona binmeme imkân yoktu. Giriş kapısının hemen içine sıkıca kilitlenerek muhafaza edilen o dağ bisikleti yerinde yeller eserse, dışarı çıktığımı evdekilerden birinin çakması kaçınılmaz olurdu.</p>

<p id="P0489">Eskiden nasıldı bilinmez ama şimdilerde ailem beni tamamen kendi halime bırakmış durumdaydı.</p>

<p id="P0490">Boş vermişlerdi de denebilirdi pekâlâ.</p>

<p id="P0491">Dolayısıyla iki kız kardeşimin aksine bana konulmuş bir eve dönüş saati yahut gece dışarı çıkma yasağı falan yoktu (gerçi o iki cadının böyle kurallara uymaya zerre niyeti yoktu ya, o ayrı mevzu);<a id="nr-29" href="notes.xhtml#note-29" epub:type="noteref" class="noteref"><sup>[29]</sup></a> lakin benim gibi birinin bile evdekilere çaktırmadan dışarı süzülmek istediği zamanlar oluyordu işte.</p>

<p id="P0492">Somutlaştırmak gerekirse: Erotik dergi almaya çıktığım zamanlar gibi.</p>

<p id="P0493">“…………”</p>

<p id="P0494">Yok yani, şey.</p>

<p id="P0495">Kulağa biraz acınası ve kepaze gelebilir ama müsaade edin de kendimi savunayım.</p>

<p id="P0496">Öğleden sonra gördüğüm Hanekawa’nın o iç çamaşırı bir türlü aklımdan çıkmıyordu.</p>

<p id="P0497">…Batağa saplandıkça kendi mezarımı mı kazıyorum acaba?</p>

<p id="P0498">Fakat vaziyet tamı tamına buydu işte.</p>

<p id="P0499">Ömrümün sonuna kadar unutamam falan diye büyük laflar etmiştim gerçi; ama o görüntünün zihnime bu denli silinmez bir netlikle kazınacağını ben bile tahmin edememiştim.</p>

<p id="P0500">Hanekawa’dan ayrıldıktan sonra bile o iç çamaşırı beynimin kıvrımlarından bir türlü defolup gitmedi. Gündüz de aklımdan geçirmiştim; lakin aradan on saatten fazla süre geçmesine rağmen şu an kornealarım birine nakledilseydi o adamcağız hâlâ Hanekawa’nın donunun hayaliyle sayıklardı muhakkak.</p>

<p id="P0501">Kahretsin.</p>

<p id="P0502">Sonrasında dünya kadar laklak etmiştik halbuki; zihnimde en çok yer eden şeyin bir iç çamaşırı olması ne menem bir rezilliktir? Hatırası henüz taze falan değil; düpedüz o manzaradan başka hiçbir şeyi hatırlamadığım ortaya çıkıyordu.</p>

<p id="P0503">Oysa ne kadar da iyi bir kızdı.</p>

<p id="P0504">Hanekawa fevkalade iyi bir kızdı halbuki!</p>

<p id="P0505">İşte bu hakikat, zerre taşımamam gereken o suçluluk azabını daha da körüklüyordu.</p>

<p id="P0506">Ruhumu mengenede sıkıyordu adeta.</p>

<p id="P0507">Hanekawa o kadar temiz kalpli biriyken, benim ona karşı böylesine aşağılık şehvet kırıntıları beslemem reva mıydı…</p>

<p id="P0508">Fakat eğri oturup doğru konuşalım şimdi.</p>

<p id="P0509">Kanlı canlı bir kız iç çamaşırını gözlerimle en son ne zaman görmüştüm acaba? Özel Naoetsu Lisesi her ne kadar üniversiteye hazırlayan elit bir lise olsa da talebelerin yarısı liseli kızlardan müteşekkildi. Moda icabı eteğini kısa giyenler de yok değildi hani. Dolayısıyla teğet geçerken anlık bir parıltı yakalamışlığım olmuştur elbet; fakat bu derece alenen, en ufak bir kusur olmaksızın böylesine net bir kız çamaşırı görmek… Vallahi ortaokulda bile başıma gelmiş şey değildi.</p>

<p id="P0510">İlkokul yıllarına kadar geriye gidersek… O kadarına da gerek yok herhalde.</p>

<p id="P0511">Demek ki hayatımda bir ilkti bu…</p>

<p id="P0512">Nasıl desem, seksenli yılların romantik komedi mangalarını andıran bir sahneydi düpedüz.<a id="nr-30" href="notes.xhtml#note-30" epub:type="noteref" class="noteref"><sup>[30]</sup></a></p>

<p id="P0513">Aramızda en ufak bir bağ olamayacağını düşündüğüm Hanekawa Tsubasa ile böyle bir sahneyle aşk rotasına (flag) gireceğimi kırk yıl düşünsem tahmin edemezdim.<a id="nr-31" href="notes.xhtml#note-31" epub:type="noteref" class="noteref"><sup>[31]</sup></a></p>

<p id="P0514">Lanet olsun.</p>

<p id="P0515">Kural hatasıydı yahu böylesi.</p>

<p id="P0516">Bir kız bir erkeğin donunu görse muhtemelen böyle zihinsel hezeyanlara kapılmazdı değil mi? Haksızlıktı bu resmen.</p>

<p id="P0517">Gerçi aşk rotası falan desem de biraz mantıklı düşününce alt tarafı sokakta birbirimizi teğet geçmiştik işte.</p>

<p id="P0518">Ortada hakiki bir tanışma bile yoktu.</p>

<p id="P0519">Hanekawa öğleden sonra benimle konuştuklarını şu an muhtemelen çoktan unutmuştur bile.</p>

<p id="P0520">Dolayısıyla sahiden de üzerime vazife olmayan fuzuli bir suçluluktu benimkisi… İşte bu kabil detaylara takılmam da ruhumun ne kadar cüce olduğunu gösteriyordu.</p>

<p id="P0521">Gelgelelim ne olursa olsun… Akşam yemeğini yerken 'bu böyle gitmez' diye karar vermiştim. Önümdeki günler boyunca, hatta belki de ömrümün sonuna kadar bu suçluluk azabıyla yaşamak zorunda kalma ihtimali tüylerimi ürpertiyordu.</p>

<p id="P0522">İyi bir kızdı.</p>

<p id="P0523">Öyle olmasa bile ‘arkadaşımdı’ artık.</p>

<p id="P0524">İşte bu yüzden nefret ediyordum ya — insanlık mukavemetim yerle bir oluyordu.</p>

<p id="P0525">Böyle saçma bir dert yüzünden kıvranmak zorunda kalmak da neyin nesiydi?</p>

<p id="P0526">Hal böyle olunca penceremin dışındaki manzara zifiri karanlığa büründüğü vakit, kapıma 'Ders Çalışıyor' levhasını asıp parmak uçlarımda sessizce süzülerek evden firar ediverdim.</p>

<p id="P0527">Bu kasabanın yegâne büyük kitapçısına gidip erotik dergi satın almak üzere.</p>

<p id="P0528">Ve o mukaddes vazifeyi başarıyla ifa etmiş, iki adet kuşe kâğıt gravür dergisini poşetime tıkıştırmış, şu an eve dönüş yoluna koyulmuştum bile.</p>

<p id="P0529">Elbette ben tezgâhtara şirin veya entelektüel görünmek uğruna erotik derginin yanına edebi bir roman iliştiren o sahte delikanlılardan değildim. Öyle riyakârlıklara girişeceğime iki tane erotik dergi alırdım daha iyi. Ben böyle bir adamdım işte. Hanekawa mümessillerin mümessiliyse, ben de delikanlıların delikanlısıydım!</p>

<p id="P0530">Tabii dükkânda tanıdık biri var mı diye etrafı kolaçan etmeyi de ihmal etmemiştim hani.</p>

<p id="P0531">Hülasa…</p>

<p id="P0532">Bu erotik dergileri satır satır hatmederek zihnimdeki o görüntüyü formatlama, üzerine yeni veriler yazma niyetindeydim.<a id="nr-32" href="notes.xhtml#note-32" epub:type="noteref" class="noteref"><sup>[32]</sup></a> Gündüz vakti Hanekawa’nın beni kovalarken güttüğü o 'hafızayı unutturma' taktiğini kendimce tersyüz edip uyguluyordum. O esnada Hanekawa’nın laklak etmesiyle görüntünün silinmeyeceğini düşünmüştüm gerçi; fakat erotizmi başka bir erotizmle ezmek teorik olarak gayet makul bir kurtuluş reçetesiydi.</p>

<p id="P0533">Hafızadan tamamen silemesem bile üzerine yeni görüntüler yazabilirdim.</p>

<p id="P0534">Görüntü 'tek ve eşsiz' (only one) olduğu için bu kadar kıvranıyordum; onu 'sıradan görüntülerden biri' (one of them) haline getirirsem hafızamdaki tesiri de zamanla buharlaşıp giderdi muhakkak.</p>

<p id="P0535">Kanlı canlı bir kız ile kâğıt üzerindeki fotoğraf arasında dağlar kadar fark vardı elbet; lakin o açığı da adet fazlalığıyla kapatacaktım.</p>

<p id="P0536">Olay anındaki vaziyeti göz önüne alarak satın aldığım iki dergi de bilhassa 'liseli kızlar ve iç çamaşırı' temalı olanlardandı. Mart ayının başında zaten birkaç dergi almış olduğumdan bu ekstra masraf cüzdanımı epey bir yaralamıştı; fakat denize düşen yılana sarılırdı ne de olsa.</p>

<p id="P0537">Kafamın zonklamasından evlaydı.</p>

<p id="P0538">Başka çarem yoktu.</p>

<p id="P0539">Hanekawa hakkında daha fazla müstehcen hayaller kurmaya tahammülüm kalmamıştı.</p>

<p id="P0540">Suçluluktan geberip giderdim yoksa.</p>

<p id="P0541">Can sıkıntısı adam öldürür derler; meğer insan suçluluk azabından da ölebiliyormuş.<a id="nr-33" href="notes.xhtml#note-33" epub:type="noteref" class="noteref"><sup>[33]</sup></a></p>

<p id="P0542">Ah be güzelim…</p>

<p id="P0543">Keşke o an suratımın ortasına okkalı bir tokat aşk etseydin de beni bu azaptan kurtarsaydın…</p>

<p id="P0544">“…Yine de arkadaş meselesi tuhaf tabii,”</p>

<p id="P0545">Bir elimde iki adet erotik derginin bulunduğu kâğıt poşeti sıkıca göğsüme bastırırken, diğer elimle cep telefonumun rehberine bakarak kendi kendime mırıldandım.</p>

<p id="P0546">“Hiç… ihtiyacım yoktu halbuki.”</p>

<p id="P0547">Fakat insan düşünmeden edemiyordu.</p>

<p id="P0548">Biri yüzünüze karşı öyle şeyler söyleyince ister istemez sorguluyordunuz.</p>

<p id="P0549">Ben ne ara böyle bir adama dönüşmüştüm sahi?</p>

<p id="P0550">Ortaokuldayken insanlarla gayet normal iletişim kurabilen biriydim sanırım — ilkokul yıllarını saymıyorum bile. Öyleyse her şey liseye geçip de dökülmeye başladığım o günden beri mi sarpa sarmıştı?</p>

<p id="P0551">Fazlasıyla anlaşılır bir durumdu aslında.</p>

<p id="P0552">Haddimi aşıp yüksek puanlı bir lisenin sınavlarına girmiş; şans eseri kapağı atmış; sonra da tempoya ayak uyduramayıp çuvallamıştım… Etrafımdaki insanlarla kafa yapım bir türlü uyuşmamıştı.</p>

<p id="P0553">Tam bir fiyaskoydu.</p>

<p id="P0554">Yoksa öyle değil miydi?</p>

<p id="P0555">İşleri yoluna koymak için önümde sayısız fırsat olmuş olmalıydı.</p>

<p id="P0556">Notlarım yerlerde sürünse bile kimse beni dışlamamış, hor görmemişti — arkadaş edinmek için önümde kucak dolusu imkân vardı.</p>

<p id="P0557">Bunu bizzat elimin tersiyle iten bendim; başkası değil.</p>

<p id="P0558">“Hımm…”</p>

<p id="P0559">Bazen içinden çıkamıyordum.</p>

<p id="P0560">Arkadaş istemediğimi söylerken, acaba bu yalnızlığıma kılıf uydurduğum ucuz bir savunma mekanizmasından mı ibaretti?</p>

<p id="P0561">Paçayı kurtarma çabası mıydı?</p>

<p id="P0562">Arkadaş…</p>

<p id="P0563">Olmayınca da bir şekilde yuvarlanıp gidiyordu insan.</p>

<p id="P0564">Arkadaşı olmayanlar kendi gibilerle takılabilirdi pekâlâ. Nitekim benim gibi tipler yok da değildi hani — uç bir misal vermek gerekirse birinci ve ikinci sınıfta aynı sırada okuduğum halde ağzından tek kelime laf çıktığını görmediğim öğrenciler vardı.</p>

<p id="P0565">Demek ki böyle de olabiliyordu.</p>

<p id="P0566">Böyle bir hayat tarzı da mümkündü.</p>

<p id="P0567">Fakat…</p>

<p id="P0568">“Arkadaş falan istediğim yok; hele bir sevgili edinmeyi rüyamda dahi görmedim… Peki bu müstehcen hayaller neden bir türlü yakamı bırakmıyor be kardeşim?”</p>

<p id="P0569">Büyük bir muammaydı.</p>

<p id="P0570">Alt tarafı bir parça kumaş yüzünden bu denli darmadağın olmuş, günün sonunda piyasadaki nakit akışına katkıda bulunmuştum.</p>

<p id="P0571">Öyle baksanıza, kumaştı alt tarafı yahu!</p>

<p id="P0572">Eskiden 'kızlar neden böyle muzır şeyleri giyip kendilerini süsler ki? Sapık mıdır nedir bunlar?' diye hayret ederdim; meğer kafam tersine çalışıyormuş.</p>

<p id="P0573">Satılıyor işte sağda solda.</p>

<p id="P0574">…Bir dakika ya!</p>

<p id="P0575">Gidip onu satın alırsam düpedüz suç işlemiş olurdum!</p>

<p id="P0576">Suç olmasa bile suçun kıyısından geçerdi!</p>

<p id="P0577">Yok sahiden — bitki olmak lazımdı.</p>

<p id="P0578">Bitki olsaydım böylesi sefil arzulardan fersah fersah uzak kalırdım.</p>

<p id="P0579">Taş ya da demir olmak derseniz…</p>

<p id="P0580">O kadarına yine de içim elvermiyordu.</p>

<p id="P0581">Bu da mı karakterimin cüceliğindendi acaba?</p>

<p id="P0582">“…Vay canına, saat kaç olmuş öyle!”</p>

<p id="P0583">Kitapçının kapanmasına dakikalar kala içeri dalmıştım dalmasına da, avare avare yürürken vakit epeyce ilerlemişti — daha doğrusu gün devrilmişti bile.</p>

<p id="P0584">Takvimler artık yirmi altı Mart’ı gösteriyordu.</p>

<p id="P0585">Şu an, tam da bu saniyeden itibaren bahar tatili resmen başlamıştı.</p>

<p id="P0586">Telefonu cebime tıkıştırıp adımlarımı hızlandırdım — o koca kitapçı evden yürünerek gidilecek mesafede değildi normalde. Doğrusunu söylemek gerekirse okula oldukça yakın bir mevkideydi; yani bisikletle gittiğim mesafeyi yaya tepmekle eşdeğerdi.</p>

<p id="P0587">Vaktin uzaması son derece tabiydi.</p>

<p id="P0588">Yine de biraz fazla oyalanmıştım.</p>

<p id="P0589">Eve alelacele dönmemi gerektirecek hayati bir mesele yoktu gerçi; lakin fazla geç kalmak da sakattı… Kız kardeşlerimin odama destursuz dalmayacağının garantisi yoktu.</p>

<p id="P0590">O iki cadı, odada olmadığımı ve dağ bisikletinin yerinde durduğunu görür görmez bütün vaziyeti tereyağından kıl çeker gibi çözebilirdi… Böyle muzırlıklarda kafaları zehir gibi çalışırdı nitekim.</p>

<p id="P0591">Sahi ya, kız kardeşlerimin iç çamaşırını görmüşlüğüm vardı elbette. Banyodan sonra evin içinde donla gezerdi o arsızlar. Ama o kadarı klasman dışıydı tabii ki.</p>

<p id="P0592">Neyse ne.</p>

<p id="P0593">Firarımın açığa çıkıp çıkmamasını bir yana bıraksak bile saat hayli ilerlemiş, ortalık evden çıktığımdan katbekat karanlık bir zindana dönmüştü. Bir de arabanın teki çarpıp ezseydi tam kepazelik olurdu.</p>

<p id="P0594">Sadece benim değil, erotik dergi almış her erkeğin yüreğini saran kadim bir endişedir bu: Poşette müstehcen dergilerle yürürkenki kadar teyakkuzda olunması gereken başka hiçbir güzergâh yoktur fani dünyada.<a id="nr-34" href="notes.xhtml#note-34" epub:type="noteref" class="noteref"><sup>[34]</sup></a></p>

<p id="P0595">Bir kaza geçirsen de cesedinin üst başı aransa bir düşünsene!</p>

<p id="P0596">Liseli kızlar ve iç çamaşırları!</p>

<p id="P0597">Hele bir de Hanekawa bir yanlışlık eseri bunu duyarsa… kesinlikle yanlış anlardı.</p>

<p id="P0598">Vallahi öyle değil!</p>

<p id="P0599">Bu dergiler bilakis senin bekaretini benden korumak için aldığım emniyet tedbirleriydi… katiyen kötü bir niyetim yoktu!</p>

<p id="P0600">…Gerçi böylesi manasız kuruntular insanı hafiften eğlendirmiyor da değildi hani.</p>

<p id="P0601">Zifiri karanlık tehlikeliydi tehlikeli olmasına da, nihayetinde kuş uçmaz kervan geçmez bir taşra kasabasında araba sayısı iki elin parmaklarını geçmezdi; farları ta uzaktan parıldardı zaten. Kuruntudan ibaretti anlayacağınız — gelgelelim…</p>

<p id="P0602">Yine de ortalık biraz fazla mı karanlıktı ne?</p>

<p id="P0603">Başımı kaldırıp göğe baktığımda sebebi anladım.</p>

<p id="P0604">Sokak lambaları sönmüştü.</p>

<p id="P0605">Beş metre aralıklarla dikilmiş sokak lambalarının neredeyse hiçbiri yanmıyordu — neredeyse falan değil, bütün hat boyunca sadece tek bir tanesi ışık saçıyordu.</p>

<p id="P0606">Arıza mı vardı acaba?</p>

<p id="P0607">Fakat bu kadar lambanın aynı anda patlaması akıl kârı değildi… Elektrikler mi kesilmişti yoksa? O zaman da tek bir lambanın yanması saçmalıktı.</p>

<p id="P0608">Böyle şeyler düşünerek…</p>

<p id="P0609">Böyle şeyler düşünerek fakat üzerinde fazla da durmaksızın, 'olur böyle şeyler' diyerek adımlarımı sürdürdüm.</p>

<p id="P0610">Eve aceleyle dönmem için sebep yok demiştim gerçi; fakat aslına bakarsanız bir an evvel odama çekilip poşetteki o nadide eserleri tedkik etmek gibi mukaddes bir vazifem vardı.</p>

<p id="P0611">Her şeyden önce ifa edilmesi gereken o vazife—</p>

<p id="P0612">“Hey gafil…”</p>

<p id="P0613">Bu yüzden…</p>

<p id="P0614">“Baksana… Şuradaki gafil. Sana derim!”</p>

<p id="P0615">Böyle bir ses işittiğimde duymazdan gelip geçmeliydim… Gafil mi?<a id="nr-35" href="notes.xhtml#note-35" epub:type="noteref" class="noteref"><sup>[35]</sup></a></p>

<p id="P0616">Ne biçim bir antik çağ hitabıydı bu böyle?</p>

<p id="P0617">Gayriihtiyari tepki veriverdim.</p>

<p id="P0618">Sesin geldiği istikamete döndüm — ve işte tam o saniyede dilim tutuldu.</p>

<p id="P0619">Civarda yanan yegâne sokak lambasının tam altı.</p>

<p id="P0620">O cılız sarı ışığın aydınlattığı yerde — ‘o kadın’ uzanıyordu.</p>

<p id="P0621">“Lütfedip… bana yardım etmene müsaade edeceğim.”<a id="nr-36" href="notes.xhtml#note-36" epub:type="noteref" class="noteref"><sup>[36]</sup></a></p>

<p id="P0622">Bu ücra taşraya katiyen yakışmayan sapsarı altın saçlar.</p>

<p id="P0623">Kusursuz hatlara sahip bir çehre — buz gibi bakan gözler.</p>

<p id="P0624">Üzerine şık bir gece elbisesi geçirmişti — lakin o elbise de bu kasabaya zerre uymuyordu.</p>

<p id="P0625">Fakat elbisenin uyumsuzluğu bambaşka bir sebeptendi.</p>

<p id="P0626">O elbise… Vaktiyle şüphesiz son derece asil, saraylara layık görkemli bir giysi olmalıydı; gelgelelim şu an eski ihtişamından eser kalmamıştı.</p>

<p id="P0627">Parça pinçik edilmişti.</p>

<p id="P0628">Yırtık pırtık olmuştu.</p>

<p id="P0629">Paçavradan farksız bir haldeydi.</p>

<p id="P0630">Yer bezi bile bundan daha haysiyetli dururdu herhalde — tersinden bakacak olursak, bu hale gelmesine rağmen kumaşın kalitesi o paçavraların arasından bile kendini belli ediyordu.</p>

<p id="P0631">“Sağır mısın be adam… Bana yardım etmene izin veriyorum dedim ya!”</p>

<p id="P0632">‘Kadın’ — gözlerini dikmiş beni süzüyordu.</p>

<p id="P0633">O keskin ve dondurucu bakışlar karşısında iliklerime kadar ürperdim; fakat normal şartlar altında bu kadar korkmama hiç gerek yoktu belki de.</p>

<p id="P0634">Zira ‘o kadın’ tükenmişliğin zirvesindeydi.</p>

<p id="P0635">Sırtını sokak lambasının direğine dayamış.</p>

<p id="P0636">Asfalt zemine yığılıp kalmıştı.</p>

<p id="P0637">Yok — oturmuş demek bile fazla iyimser bir tabirdi.</p>

<p id="P0638">Düpedüz yığılmıştı işte.</p>

<p id="P0639">Öyle bir vaziyetteki kadının elinden dik dik bakmaktan başka bir şey gelemezdi zaten.</p>

<p id="P0640">…Hayır.</p>

<p id="P0641">Tükenmiş olmasa dahi, yere yığılmamış olsa dahi — ‘o kadın’ bana dik dik bakmanın ötesinde tek bir hamle bile yapamazdı.</p>

<p id="P0642">Evvelemirde, hamle yapacak elleri yoktu ortada.</p>

<p id="P0643">Sağ kolu dirseğinden.</p>

<p id="P0644">Sol kolu omuz kökünden.</p>

<p id="P0645">Kopup gitmişti.<a id="nr-37" href="notes.xhtml#note-37" epub:type="noteref" class="noteref"><sup>[37]</sup></a></p>

<p id="P0646">“…………!”</p>

<p id="P0647">Yalnızca bu da değil.</p>

<p id="P0648">Belden aşağısı da aynı dehşetengiz manzarayı sergiliyordu.</p>

<p id="P0649">Sağ bacağı diz kapağının hizasından.</p>

<p id="P0650">Sol bacağı kalçasının dibinden.</p>

<p id="P0651">Kesilip atılmıştı.</p>

<p id="P0652">Yalnızca sağ bacağının kesik yeri tuhaf bir şekilde pürüzsüzdü — cerrahi bir bıçakla jilet gibi biçilmişti adeta. Diğer sağ kol, sol kol ve sol bacak gibi vahşice parçalanmış, koparılmış bir intiba bırakmıyordu.</p>

<p id="P0653">Fakat…</p>

<p id="P0654">Böyle bir durumda kesiklerin niteliği teferruattan ibaretti.</p>

<p id="P0655">Hülasa, ‘o kadın’ dört uzvunun dördünden de tamamen mahrum kalmıştı.</p>

<p id="P0656">İşte bu halde — sokak lambasının altında yere serilmişti.</p>

<p id="P0657">Tükenmişlik falan değil.</p>

<p id="P0658">Düpedüz can çekişiyordu.</p>

<p id="P0659">“H-Hey… Sen… İyi misin?”</p>

<p id="P0660">Hani yüreği ağzına gelmek, kalbi deli gibi çarpmak derler ya.</p>

<p id="P0661">Bunun sadece edebi bir mecaz olduğunu sanırdım; meğer insan sahiden de o dehşeti etinde kemiğinde hissedebiliyormuş.</p>

<p id="P0662">Göğüs kafesimi delecek kadar şiddetle çarpıyordu kalbim.</p>

<p id="P0663">Kalbim — adeta çıldırmıştı.</p>

<p id="P0664">Yaklaşan felaketi haber verircesine.</p>

<p id="P0665">Bir yangın çanı gibi gümbürdüyordu.</p>

<p id="P0666">“D-Derhal ambulans çağırayım—”</p>

<p id="P0667">Dört uzvu birden kesilmiş birine kıyasla yerdeki kan miktarı akıl almaz derecede azdı.</p>

<p id="P0668">O panikle böylesi bir garipliği akıl edecek durumda bile değildim; az önce cebime koyduğum telefonu alelacele çıkardım — lakin parmaklarım öyle zangırdıyordu ki tuşlara basamıyordum.</p>

<p id="P0669">Sahi ambulansın numarası kaçtı yahu?</p>

<p id="P0670">117 miydi?</p>

<p id="P0671">115 miydi?</p>

<p id="P0672">Kahretsin, bilseydim rehbere acil servis numarasını kaydederdim—</p>

<p id="P0673">“Ambulans mı… Öyle saçmalıklara lüzum yok.”</p>

<p id="P0674">‘O kadın’…</p>

<p id="P0675">Bütün uzuvları koparılmış o feci vaziyette dahi bilincini kaybetmemiş, fevkalade otoriter —ve bir o kadar da arkaik— bir ses tonuyla sesleniyordu bana.</p>

<p id="P0676">“Dedim ya… Kanını ver bana!”</p>

<p id="P0677">“…………”</p>

<p id="P0678">Telefonun tuşlarına basan parmağım — havada donakaldı.</p>

<p id="P0679">Ve o an…</p>

<p id="P0680">Öğleden sonra Hanekawa ile ettiğimiz o muhabbet şimşek gibi çaktı beynimde.</p>

<p id="P0681">Yalnızca kızların arasında dolaşan dedikodu.</p>

<p id="P0682">Neydi o?</p>

<p id="P0683">Ne konuşmuştuk biz?</p>

<p id="P0684">Gece vakti…</p>

<p id="P0685">Geceleri tek başına sokaklarda dolaşmamak gerekiyormuş…</p>

<p id="P0686">“…Sarı saçlar.”</p>

<p id="P0687">Sarı saçlar.</p>

<p id="P0688">Sarı saçları…</p>

<p id="P0689">Sokak lambasının altında parıldayan göz kamaştırıcı sarı saçlar — ve…</p>

<p id="P0690">Gölgesi yok.</p>

<p id="P0691">Bütün sokak lambalarının söndüğü o zifiri karanlıkta tek yanan lambanın altındaki ‘o kadın’, adeta sahnede tek başına spot ışığı altında kalmış bir başrol oyuncusu gibiydi — ve o ışığın altında parıldayan saçları sahiden de gözlerimi alıyordu; gelgelelim…</p>

<p id="P0692">Sahiden de.</p>

<p id="P0693">‘O kadının’ gölgesi yoktu.</p>

<p id="P0694">Mecazi anlamda falan değil.</p>

<p id="P0695">Asfaltta en ufak bir gölge dahi düşmüyordu.</p>

<p id="P0696">“Benim adım…”</p>

<p id="P0697">Ve — ‘o kadın’ konuştu:</p>

<p id="P0698">“Benim adım Kiss-shot Acerola-orion Heart-under-blade… Demirkanlı, sıcakkanlı ve soğukkanlı vampirim ben!”<a id="nr-38" href="notes.xhtml#note-38" epub:type="noteref" class="noteref"><sup>[38]</sup></a></p>

<p id="P0699">O paçavraya dönmüş giysilerin içinde.</p>

<p id="P0700">Dört uzvunu kaybetmiş halde.</p>

<p id="P0701">Buna rağmen tepeden bakan mağrur bir edayla söyledi bunları.</p>

<p id="P0702">Aralanan dudaklarının arasından — iki adet sivri ve bembeyaz köpekdişi görünüyordu.</p>

<p id="P0703">Jilet gibi — sivri dişler.</p>

<p id="P0704">“Senin o değersiz kanını etim ve canım niyetine mideme indireceğim. O yüzden — kanını sun bana!”</p>

<p id="P0705">“…Vampir dediğin şey,”</p>

<p id="P0706">Soluğumu tutarak konuştum.</p>

<p id="P0707">“Ölümsüz olması gerekmez miydi yahu?”</p>

<p id="P0708">“Çok fazla kan kaybettim. Ne kendimi iyileştirebiliyorum ne de biçim değiştirebiliyorum artık. Bu gidişle… ölüp gideceğim.”</p>

<p id="P0709">“…………”</p>

<p id="P0710">“Senin gibi fani bir beşer parçasının — benim kanım ve etim olabilme şerefine erişmesi senin için büyük bir lütuftur!”</p>

<p id="P0711">Bacaklarımın zangırtısını durduramıyordum.</p>

<p id="P0712">Neler oluyordu böyle?</p>

<p id="P0713">Nasıl bir belanın ortasına düşmüştüm ben?</p>

<p id="P0714">Neden karşımda ansızın kanlı canlı bir vampir belirmiş — ve neden gözlerimin önünde geberip gidiyordu?</p>

<p id="P0715">Var olmaması gereken vampir karşımdaydı.</p>

<p id="P0716">Ölümsüz olması gereken vampir can çekişiyordu.</p>

<p id="P0717">Nasıl bir kâbustu bu?</p>

<p id="P0718">“H-Hey…”</p>

<p id="P0719">Dehşetten ağzımı bile açamadığımı görünce ‘kadın’ kaşlarını çattı.</p>

<p id="P0720">Daha doğrusu acıdan kıvrandığı için yüzünü ekşitmiş olmalıydı.</p>

<p id="P0721">Kolay mıydı; elini kolunu bacağını kaybetmişti ne de olsa.</p>

<p id="P0722">“N… Neyin tereddüdü bu? Beni kurtarma şerefine nail oluyorsun işte! Bundan daha büyük bir mükâfat var mıdır sence? Bir şey yapmana lüzum yok — boynunu uzat yeter; kalan her şeyi ben hallederim.”</p>

<p id="P0723">“…K-Kan derken… Kan nakli falan yapsak kurtarmaz mı?”</p>

<p id="P0724">Kendi ahmaklığıma ben bile inanamıyordum.</p>

<p id="P0725">Aklımı yitirmiştim besbelli.</p>

<p id="P0726">Ne biçim bir şakaydı bu böyle?</p>

<p id="P0727">‘Kadın’… Kiss-shot Acerola-orion Heart-under-blade de benim gibi düşünmüş olacak ki cevap vermeye tenezzül etmedi.</p>

<p id="P0728">Yok.</p>

<p id="P0729">Cevap verecek dermanı bile kalmamıştı artık.</p>

<p id="P0730">“N-Ne kadar lazım peki?”</p>

<p id="P0731">Bu soru somut olduğu için olsa gerek, ‘kadın’ cevap verdi:</p>

<p id="P0732">“…Şimdilik senin o tek bedenin kadar kan alırsam bu badireyi atlatırım.”<a id="nr-39" href="notes.xhtml#note-39" epub:type="noteref" class="noteref"><sup>[39]</sup></a></p>

<p id="P0733">“Demek bir beden… İyi de be kadın!”</p>

<p id="P0734">O zaman ben nalları dikerim ya!</p>

<p id="P0735">Diye…</p>

<p id="P0736">Tam lafı yapıştıracaktım ki — kelimeler boğazıma tıkandı.</p>

<p id="P0737">Bu kadının bana bakan gözleri.</p>

<p id="P0738">O buz gibi gözler.</p>

<p id="P0739">Bir insanın —yiyeceğe baktığı o gözlerdi.</p>

<p id="P0740">Şaka yapmıyordu; zerre alay etmiyordu.</p>

<p id="P0741">Değersiz bir — beşer parçası.</p>

<p id="P0742">Bu yaratık can çekişiyordu.</p>

<p id="P0743">Ve beni yiyip yutarak — hayatta kalmayı amaçlıyordu.</p>

<p id="P0744">Benden yardım dilenmiyordu.</p>

<p id="P0745">Beni avlayıp mideye indirerek.</p>

<p id="P0746">Kendi canını kurtarmaya çalışıyordu sadece.</p>

<p id="P0747">“………………”</p>

<p id="P0748">Doğru ya.</p>

<p id="P0749">Ben ne saçmalıyordum — aklım neredeydi benim?</p>

<p id="P0750">Bu kadını kurtarmak sanki kaçınılmaz bir görevmiş gibi ne diye kafa yoruyordum ki?</p>

<p id="P0751">Aptallıktı bu.</p>

<p id="P0752">Vampirdi bu yaratık yahu!</p>

<p id="P0753">Basbayağı bir canavardı işte.</p>

<p id="P0754">Kollarını bacaklarını nasıl kaybettiğini, neden burada geberdiğini bilmiyordum ama her halükarda altında pis bir iş yattığı kesindi.</p>

<p id="P0755">Bulaşıp da başımı belaya sokmanın âlemi neydi?</p>

<p id="P0756">Akıllı adam beladan uzak durmaz mıydı?<a id="nr-40" href="notes.xhtml#note-40" epub:type="noteref" class="noteref"><sup>[40]</sup></a></p>

<p id="P0757">Ortada kaplan yavrusu bile yokken kaplan inine girmenin ne manası vardı?</p>

<p id="P0758">Bu yaratık insan değildi — insan-dışı bir hilkat garibesiydi.</p>

<p id="P0759">İnsan türünün fevkinde bir mevcudiyet.</p>

<p id="P0760">Hanekawa tam olarak böyle tarif etmişti.</p>

<p id="P0761">“Ne duruyorsun… Kanını ver. Kanını ver bana! Çabuk ol… Çabuk davran dedim! Ne diye uyuşuk uyuşuk dikiliyorsun be sersem!”</p>

<p id="P0762">“…………”</p>

<p id="P0763">En ufak bir şüphe duymaksızın.</p>

<p id="P0764">Bunu yapmamın eşyanın tabiatı gereği olduğunu söyleyen o vampire karşı — hışımla.</p>

<p id="P0765">Bir adım geri çekildim.</p>

<p id="P0766">Sorun yoktu.</p>

<p id="P0767">Kaçabilirdim… Bal gibi de kaçıp kurtulabilirdim.</p>

<p id="P0768">Karşımdaki ister vampir olsun ister hortlak.</p>

<p id="P0769">Kolları bacakları kesilmiş bu vaziyetteyken arkamdan yetişmesine imkân yoktu — zaten peşime düşmesi bile fizik kurallarına aykırıydı.</p>

<p id="P0770">Tabanları yağlamam yeterdi.</p>

<p id="P0771">Hayatım boyunca en iyi yaptığım şey buydu zaten.</p>

<p id="P0772">Sırf bunu yaparak bu kâbus gibi gerçeği reddedebilirdim.</p>

<p id="P0773">Ve…</p>

<p id="P0774">Diğer ayağımı da bir adım geriye attım ki—</p>

<p id="P0775">“Y… Yalan söylüyorsun değil mi?”</p>

<p id="P0776">Tam o anda.</p>

<p id="P0777">O kadının gözleri — birdenbire yapayalnız ve alabildiğine çaresiz bir hal aldı.</p>

<p id="P0778">Az önceki o dondurucu kibir, sanki hiç var olmamışçasına eriyip gitmişti.</p>

<p id="P0779">“Beni kurtarmayacak mısın… sahiden?”</p>

<p id="P0780">“…………”</p>

<p id="P0781">Elbisesi paramparça.</p>

<p id="P0782">Kolları ve bacakları vahşice gövdesinden koparılmış.</p>

<p id="P0783">Sokak lambasının altında tek bir gölgesi dahi olmayan bir canavar.</p>

<p id="P0784">Lakin… ben.</p>

<p id="P0785">Sapsarı altın saçlara sahip o kadını inanılmaz derecede güzel buldum.</p>

<p id="P0786">Büyüleyiciydi.</p>

<p id="P0787">Bütün ruhumla — vurulmuştum ona.</p>

<p id="P0788">Gözlerimi ondan bir türlü alamıyordum.</p>

<p id="P0789">Daha fazla geriye adım atamadım.</p>

<p id="P0790">Korkudan dizlerim kilitlendiği için değil.</p>

<p id="P0791">Basbayağı, adım atamıyordum işte.</p>

<p id="P0792">“İ… İstemiyorum!”</p>

<p id="P0793">O mağrur ve kibirli üslubu un ufak olmuştu — kadın, saçlarıyla aynı renkteki o altın sarısı gözlerinden iri iri gözyaşları dökmeye başladı.<a id="nr-41" href="notes.xhtml#note-41" epub:type="noteref" class="noteref"><sup>[41]</sup></a></p>

<p id="P0794">Küçük bir çocuk gibi.</p>

<p id="P0795">Hıçkıra hıçkıra ağlamaya başlamıştı.</p>

<p id="P0796">“İstemiyorum, istemiyorum, ölmek istemiyorum! Yok olmak istemiyorum, silinip gitmek istemiyorum! Lütfen, biri beni kurtarsın! Yalvarırım, yalvarırım kurtarın beni! Eğer beni kurtarırsanız ne derseniz yaparım, söz veriyorum ne isterseniz yaparım!”</p>

<p id="P0797">İnsanın ciğerini dağlayacak bir feryatla haykırıyordu.</p>

<p id="P0798">Arsızca.</p>

<p id="P0799">Beni bile görmüyordu artık gözü.</p>

<p id="P0800">Aklını yitirmişçesine — feryat figan ağlıyordu.</p>

<p id="P0801">Yırtınıyordu adeta.</p>

<p id="P0802">“Ölmek istemiyorum, yok olmak istemiyorum! Kimse yok mu, biri bana yardım etsin, yalvarırım—”</p>

<p id="P0803">Bir vampire yardım edecek bir ahmak…</p>

<p id="P0804">Dünyada bulunabilir miydi?</p>

<p id="P0805">Ne kadar yırtınırsa yırtınsın — yufka yüreklilik etmemeliydim.</p>

<p id="P0806">Ölüm vardı işin ucunda yahu!</p>

<p id="P0807">Bir insanın bütün kanı demekti bu.</p>

<p id="P0808">Kızılay’a kan vermekten bile ölesiye tırsmış bir adamdım ben!</p>

<p id="P0809">Böyle şeylerden — ben nefret etmez miydim zaten?</p>

<p id="P0810">Kendi cinsimden bir insanın derdini sırtlanmaktan köşe bucak kaçarken, bir de kalkıp bir canavarın mesuliyetini yüklenmek intihardan farksızdı.</p>

<p id="P0811">Hele bir de vampiri sırtlanmayı dene bakalım…</p>

<p id="P0812">İnsanlık mukavemetin kim bilir kaç kat dibe vururdu!</p>

<p id="P0813">“Hüüngggg!”</p>

<p id="P0814">Gözlerinden süzülen yaşlar — yavaş yavaş kan kırmızısına dönmeye başlamıştı.</p>

<p id="P0815">Bilemiyordum.</p>

<p id="P0816">Kestiremiyordum ama bu belki de — ölümün habercisiydi.</p>

<p id="P0817">Bir vampir için nihai ölüm.</p>

<p id="P0818">Kandan gözyaşları.</p>

<p id="P0819">“Özür dilerim, çok özür dilerim, affedin beni, affedin beni, affedin beni…”</p>

<p id="P0820">Nihayetinde feryatları bir yalvarıştan bir özür silsilesine dönüşüverdi.</p>

<p id="P0821">Kime özür diliyordu acaba?</p>

<p]P0822">Kimin önünde af diliyordu?</p>

<p id="P0823">Fakat — bakamıyordum artık.</p>

<p id="P0824">O muazzam varlığın meçhul bir kudretin karşısında böyle yerlerde sürünerek af dilemesine yüreğim elvermiyordu.</p>

<p id="P0825">Galiba…</p>

<p id="P0826">Bu varlık böyle bir zilleti hak etmiyordu.</p>

<p id="P0827">Böylesine kepaze bir ölümü — asla tatmaması gerekirdi.</p>

<p id="P0828">“Aaaaaaaahhhhh!”</p>

<p id="P0829">İş işten geçtikten sonra.</p>

<p id="P0830">Avazım çıktığı kadar — haykırarak koşmaya başladım.</p>

<p id="P0831">Kilitlenen bacaklarımı zorla harekete geçirip — arkamı döndüğüm gibi var gücümle ileriye fırladım.</p>

<p id="P0832">Arkamdan hâlâ o af dileyen feryatları yankılanıyordu.</p>

<p id="P0833">O sesi benden başka duyan yok muydu?</p>

<p id="P0834">O çığlıkları işitip de oraya koşan tek bir kul dahi çıkmayacak mıydı?</p>

<p id="P0835">Kiss-shot Acerola-orion Heart-under-blade.</p>

<p id="P0836">Onu kurtarmaya kimse yeltenmeyecek miydi?</p>

<p id="P0837">…Tabii ki yeltenmeyecekti.</p>

<p id="P0838">İşin ucunda kendi canı vardı.</p>

<p id="P0839">Üstelik karşısındaki bir canavardı.</p>

<p id="P0840">Bir vampirdi yahu.</p>

<p id="P0841">Kurtarmaya ne lüzum vardı ki — öyle değil mi?</p>

<p id="P0842">“…Bal gibi biliyorum ulan!”</p>

<p id="P0843">Biraz ilerideki çöp konteynerinin yanına varınca kucağımdaki kâğıt poşeti var gücümle çöplerin üzerine fırlattım.</p>

<p id="P0844">İçinde iki adet erotik derginin bulunduğu o poşeti.</p>

<p id="P0845">Çöpü sabah çıkarmak edep kuralıydı gerçi ve pazar günü çöp toplanmayacağı da aşikârdı. Yine de konteyneri seçmem asgari vicdanımın eseriydi işte.</p>

<p id="P0846">Muhtemelen şanslı bir ortaokullu velet bulup nasiplenirdi.</p>

<p id="P0847">Yazık olmuştu paralara; fakat artık benim onlara zerre ihtiyacım kalmamıştı.</p>

<p id="P0848">Bırakın ihtiyacı, üzerimde bulunması bile ayıptı.</p>

<p id="P0849">Birazdan tahtalı köyü boylayacak bir adamın elinde erotik dergiyle ne işi olurdu be — ah!</p>

<p id="P0850">Erotik dergi aldığın dönüş yolu kadar temkinli olunması gereken başka hiçbir yol yoktur — bunu bal gibi biliyordum halbuki.</p>

<p id="P0851">İnsanlık mukavemetim tam şu saniyede yerin dibine batmıştı.</p>

<p id="P0852">“…………”</p>

<p id="P0853">Topuklarımın üzerinde dönüp o lambaya doğru deli gibi geri koşarken — gözlerimden gayriihtiyari yaşlar boşanıyordu.</p>

<p id="P0854">Annem, babam.</p>

<p id="P0855">Ve iki kız kardeşim.</p>

<p id="P0856">İnsan ilişkilerinden fellik fellik kaçan benim gibi birinin böyle bir anda hatırlayacağı insanlar alt tarafı bu kadardı işte — ve topu topu dört kişi olmalarına rağmen ağlamama fazlasıyla yetiyordu.</p>

<p id="P0857">Öyle pek birbirine düşkün bir aile sayılmazdık.</p>

<p id="P0858">Bilhassa liseye geçip derslerde çuvalladığımdan beri ebeveynlerimle aramda tuhaf, ama kapatılamaz bir uçurum açılmıştı.</p>

<p id="P0859">Onlardan çekindiğimden veya nefret ettiğimden değil.</p>

<p id="P0860">Onlar da bana karşı öyle hissetmiyordu eminim.</p>

<p id="P0861">Yalnızca, bir uçurum vardı işte.</p>

<p id="P0862">Ergenlikte sıkça rastlanan şeylerdendi.</p>

<p id="P0863">Böyle avuturdum kendimi; fakat işlerin bu noktaya varacağını bilseydim onlarla oturup adamakıllı iki çift laf ederdim hiç değilse.</p>

<p id="P0864">Evden gizlice sıvışıp ebediyen sırra kadem basmak ha?</p>

<p id="P0865">Ah… dergileri çöpe atmış olsam bile kız kardeşlerim erotik dergi almaya çıktığım esnada başıma bir iş geldiğini şıp diye anlardı muhakkak.</p>

<p id="P0866">Neyse ne.</p>

<p id="P0867">Ne kadar cadı olsalar da ailelerinin böylesi bir kepazeliğini el âleme ifşa etmezlerdi herhalde.</p>

<p id="P0868">Sizi çok sevmiştim be çılgın kardeşlerim.</p>

<p id="P0869">“…………”</p>

<p id="P0870">Gözyaşlarımı sildim.</p>

<p id="P0871">Aslına bakarsanız aklıma gelecek insan sayısının bu kadar az olması büyük bir şanstı — kazara bir de arkadaş falan edinmiş olsaydım vaktim çoktan tükenmiş olurdu.</p>

<p id="P0872">Tersinden bakarsak, kurabildiğim insan ilişkileri bu kadarcık sığ olduğu için tam da şu an böylesi pervasız bir tercihte bulunabiliyordum belki de.</p>

<p id="P0873">Ve sokak lambasının dibine geri döndüm.</p>

<p id="P0874">Sarı saçlı vampir hâlâ oradaydı.</p>

<p id="P0875">O da artık ağlamayı bırakmıştı.</p>

<p id="P0876">Çığlık da atmıyordu.</p>

<p id="P0877">Hık, hık… diye içini çekiyordu çekmesine ama.</p>

<p id="P0878">Artık kadere teslim olmuş, vazgeçmiş gibiydi.</p>

<p id="P0879">“Pes etme salak!”</p>

<p id="P0880">Böyle bağırarak kadına doğru atıldım — önünde dizlerimin üzerine çöktüm ve ardından.</p>

<p id="P0881">Kendi boynumu hırsla kadının ağzına doğru uzattım.</p>

<p id="P0882">“Kalan her şeyi… sen halledecektin ya ulan!”</p>

<p id="P0883">“…Ha?”</p>

<p id="P0884">Kadın — gözlerini fal taşı gibi açtı.</p>

<p id="P0885">Yüzü baştan aşağı derin bir hayretle kaplanmıştı.</p>

<p id="P0886">“S-Sahi mi… Sahiden olur mu?”</p>

<p id="P0887">“Olur mu ne demek be densiz herif, canıma minnet sanki!”</p>

<p id="P0888">Kahretsin, kahretsin, kahretsin…</p>

<p id="P0889">Neden?</p>

<p id="P0890">Olaylar nasıl bu noktaya gelmişti?</p>

<p id="P0891">“Nedenini falan düşünmeye ne hacet; gün gibi aşikâr işte! Şimdiye kadar hiçbir baltaya sap olamamış, hayatı laylaylom yaşamış lüzumsuzun tekiyim ben!”</p>

<p id="P0892">Avazım çıktığı kadar haykırıyordum.</p>

<p id="P0893">Aklıma ne gelirse haykırıyordum.</p>

<p id="P0894">“Dişimi tırnağıma takıp hayatta kalmamı gerektirecek tek bir sebep bile yok! Kendi canıma öncelik vermemi gerektirecek hiçbir gerekçe yok! Benim gibi bir velet geberip gitse şu koca dünyada zerre yaprak kımıldamaz be!”</p>

<p id="P0895">Ne asil.</p>

<p id="P0896">Ne de güzel.</p>

<p id="P0897">Benim hayatım böylesine sefil bir paçavradan ibaretse…</p>

<p id="P0898">Karşımdaki bu eşsiz güzelliği yaşatmak uğruna—</p>

<p id="P0899">Benim ölmem gerekmez miydi?</p>

<p id="P0900">Mantıklı olan tek netice bu değil miydi?</p>

<p id="P0901">Ben alt tarafı beş para etmez bir insan müsveddesiydim.</p>

<p id="P0902">Vampir ise insan türünün fevkinde yüce bir mevcudiyetti — öyle değil miydi?</p>

<p id="P0903">“—Bir sonraki hayatımda kesinlikle her şeyi kusursuz yapacağım! İşini bilen, insan ilişkilerini tereyağından kıl çeker gibi idare eden, saçma sapan şeylere suçluluk duymayan, tereddütsüz harekete geçebilen, burnunun dikine gitmekten gocunmayan, bütün pislikleri başkalarının üzerine yıkabilen gamsız bir herif olarak yeniden doğacağım — o yüzden!”</p>

<p id="P0904">Gözlerimi kadına dikerek haykırdım.</p>

<p id="P0905">Hiç değilse…</p>

<p id="P0906">Bunu kendi hür irademle söylemek, alt tabakadan bir beşer olarak son gurur kırıntımdı.</p>

<p id="P0907">“Ben seni kurtaracağım — em kanımı!”<a id="nr-42" href="notes.xhtml#note-42" epub:type="noteref" class="noteref"><sup>[42]</sup></a></p>

<p id="P0908">“…………”</p>

<p id="P0909">“Hepsini al! Tek bir damlası kalmayana dek — kurut beni!”</p>

<p id="P0910">“…Ah.”</p>

<p id="P0911">O kadın…</p>

<p id="P0912">Kiss-shot Acerola-orion Heart-under-blade —belki de asırlardır süren ömründe ilk defa— kendi dışındaki fani bir mevcudiyete teşekkür etti.</p>

<p id="P0913">“Teşekkür ederim…”</p>

<p id="P0914">Saplandı.</p>

<p id="P0915">Boynuma saplanan o jilet gibi keskin iki dişle birlikte — şahdamarımın delindiğini hissettim.</p>

<p id="P0916">Bilincim, adeta bir girdaba kapılmışçasına ışık hızıyla siliniverdi.</p>

<p id="P0917">Ve o sönüp giden bilincimin son kırıntısıyla, aklıma düştü.</p>

<p id="P0918">Hanekawa Tsubasa.</p>

<p id="P0919">O kızın hayali.</p>

<p id="P0920">'Kazara bir de arkadaş falan edinmiş olsaydım vaktim çoktan tükenmiş olurdu' demiştim ya hani…</p>

<p id="P0921">Direkten dönmüştüm resmen.</p>

<p id="P0922">O kızı birazcık daha erken hatırlasaydım belki de bu fedakârlığa vaktim yetmeyecekti — hey gidi hey.</p>

<p id="P0923">Neyse ne.</p>

<p id="P0924">Topu topu on dakikacık bir sohbet dahi olsa, Hanekawa ile yollarımızın kesiştiği o sıcacık hatırayı bağrıma basarak ölmek — o kadar da fena sayılmazdı hani. Yok canım, Hanekawa’nın iç çamaşırı hatırası falan değil bu seferki; sahiden öyle değil.</p>

<p id="P0925">Ne olursa olsun, son nefeste bari bu kadar yüzsüzlük etmeyelim değil mi?</p>

<p id="P0926">Bırakın da giderayak iki paralık fiyakamız kalsın.</p>

<p id="P0927">İşte böylece bendenizin, yani Araragi Koyomi’nin on yedi küsur yıllık o kısacık ömrü; alelacele, ne bir işaret ne bir haber vermeksizin nihayete erdi — daha doğrusu, öyle olması gerekirdi.</p>
"""

# Now update chapter1.xhtml
with open(f"{BASE_DIR}/EPUB/text/chapter1.xhtml", "r", encoding="utf-8") as f:
    current_ch1 = f.read()

# Replace the closing </section></body></html> with sec3_html + closing
if "</section>" in current_ch1:
    idx = current_ch1.rfind("</section>")
    new_ch1 = current_ch1[:idx] + sec3_html + "\n</section>\n</body>\n</html>"
    with open(f"{BASE_DIR}/EPUB/text/chapter1.xhtml", "w", encoding="utf-8") as f:
        f.write(new_ch1)
    print("Chapter 1 updated with Section 003.")

# ==========================================
# APPEND NOTES FOR SECTION 003
# ==========================================

notes_003 = """
<li id="note-28"><span class="note-num">28.</span> <b>ママチャリ・マウンテンバイク (Mamachari ve Dağ Bisikleti):</b> <i>Mamachari</i> (ママチャリ - anne bisikleti), Japonya'da önünde alışveriş sepeti olan standart, ağır şehir bisikletlerine verilen popüler addır. Araragi okula giderken bu sıradan bisikleti, hususi gezilerinde ise pahalı dağ bisikletini (mountain bike) kullanır. <a href="chapter1.xhtml#P0486" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-29"><span class="note-num">29.</span> <b>ふたりの妹 (İki Kız Kardeş - Ateş Kardeşler):</b> Araragi'nin ortaokula giden küçük kız kardeşleri Karen ve Tsukihi'dir (Monogatari serisinde Tsuganoki Ortaokulu'nun adalet savaşçıları "Fire Sisters" olarak bilinirler). <a href="chapter1.xhtml#P0491" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-30"><span class="note-num">30.</span> <b>八〇年代のラブコメ漫画 (80'ler Romantik Komedi Mangaları):</b> Rumiko Takahashi'nin <i>Urusei Yatsura</i> veya Mitsuru Adachi'nin <i>Touch</i> gibi klasik serilerinde sıkça görülen kaza eseri iç çamaşırı görme ve bunun üzerine filizlenen aşk klişelerine doğrudan edebi gönderme. <a href="chapter1.xhtml#P0512" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-31"><span class="note-num">31.</span> <b>フラグが立つ (Aşk Rotası / Flag Kalkması):</b> Görsel roman (visual novel) ve anime kültüründe bir karakterle romantik veya trajik bir olay örgüsünün (route) tetiklendiğini belirten terim ("bayrak kalkması"). <a href="chapter1.xhtml#P0513" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-32"><span class="note-num">32.</span> <b>オンリーワン・ワンオブゼム (Only One ve One of Them):</b> Japon popüler kültüründe ve SMAP grubunun meşhur şarkısında geçen "eşsiz ve biricik" (Only One) kavramına Nisio Isin'in alaycı dokunuşu. Araragi, Hanekawa'nın görüntüsü tek olduğu için acı çektiğini; çok sayıda erotik dergi alarak onu "onlardan biri" (One of them) seviyesine indirgemeye çalıştığını söyler. <a href="chapter1.xhtml#P0532" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-33"><span class="note-num">33.</span> <b>退屈は人を殺す (Can Sıkıntısı Adam Öldürür):</b> Batı felsefesinde (Kierkegaard, Pascal) sıkça geçen can sıkıntısının ölümcüllüğü temasına Araragi'nin "suçluluk azabı da insanı öldürür" şeklindeki nihilist eklemesi. <a href="chapter1.xhtml#P0541" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-34"><span class="note-num">34.</span> <b>エロ本を買った帰り (Erotik Dergi Dönüşü Paranoyası):</b> Japon gençlik edebiyatında sıkça işlenen klasik bir mizah unsuru. Kaza geçirip hastanelik olduğunda ailesinin ve arkadaşlarının poşetteki dergileri bulması korkusu. <a href="chapter1.xhtml#P0594" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-35"><span class="note-num">35.</span> <b>うぬ (Unu - Ey Gafil!):</b> Kiss-shot'ın kullandığı feodal, son derece eski ve tepeden bakan arkaik ikinci tekil şahıs hitabı. Türkçede bu tını "ey gafil" ve "bak hele şuraya" söyleyişleriyle karşılanmıştır. <a href="chapter1.xhtml#P0615" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-36"><span class="note-num">36.</span> <b>儂を助けさせてやる (Yardım Etmene Müsaade Ediyorum):</b> Kiss-shot'ın yardım isterken dahi kibrinden ödün vermeyen, canını kurtarmayı karşısındakine bahşedilmiş bir lütuf gibi sunan asil vampir psikolojisi. <a href="chapter1.xhtml#P0621" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-37"><span class="note-num">37.</span> <b>四肢切断 (Koparılmış Dört Uzuv):</b> Kiss-shot'ın bu hale gelmesinin ardında üç uzman vampir avcısı (Dramaturgy, Episode ve Guillotinecutter) bulunmaktadır. Serinin ilerleyen bölümlerinde bu avcılarla yapılacak düellolar bu uzuvları geri almak içindir. <a href="chapter1.xhtml#P0645" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-38"><span class="note-num">38.</span> <b>鉄血にして熱血にして冷血の吸血鬼 (Demirkanlı, Sıcakkanlı ve Soğukkanlı):</b> Kiss-shot'ın tam unvanı: <i>Tekketsu ni shite nekketsu ni shite reiketsu no kyuuketsuki</i>. Eserdeki en ünlü ahenkli ritim kalıplarından biridir. <a href="chapter1.xhtml#P0698" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-39"><span class="note-num">39.</span> <b>うぬ一人分 (Bir İnsanlık Kan):</b> Kiss-shot'ın hayatta kalabilmek için ihtiyaç duyduğu asgari kan miktarı bir yetişkinin tüm kan hacmine eşittir; bu da donörün mutlak ölümü anlamına gelir. <a href="chapter1.xhtml#P0732" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-40"><span class="note-num">40.</span> <b>君子危うきに近寄らず・虎穴に入らずんば (Japon/Çin Atasözleri):</b> Araragi'nin korkudan kaçarken zihninde sıraladığı atasözleri: "Erdemli kişi tehlikeye yaklaşmaz" ve "Kaplan inine girmeyen kaplan yavrusu tutamaz" (burada yavru olmadığı için girmenin manasızlığına yorulur). <a href="chapter1.xhtml#P0756" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-41"><span class="note-num">41.</span> <b>吸血鬼の落涙 (Vampirin Can Korkusu):</b> 500 yıldır yaşayan efsanevi vampir kraliçesinin ölüm karşısında kibrini tamamen kaybedip küçük bir çocuk gibi hüngür hüngür ağlaması ve kanlı gözyaşları dökmesi sahnesi eserin en çarpıcı kırılma anıdır. <a href="chapter1.xhtml#P0793" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-42"><span class="note-num">42.</span> <b>僕がお前を助けてやる (Araragi'nin Kurtarıcı Kompleksi):</b> Araragi'nin tüm seri boyunca sürecek olan kendi hayatını hiçe sayıp başkaları uğruna kendini feda etme (self-sacrifice) psikolojisinin doğduğu ilk andır. <a href="chapter1.xhtml#P0907" class="backref" aria-label="Metindeki yere dön">↩</a></li>
"""

with open(f"{BASE_DIR}/EPUB/text/notes.xhtml", "r", encoding="utf-8") as f:
    current_notes = f.read()

if "</ol>" in current_notes:
    idx = current_notes.rfind("</ol>")
    new_notes = current_notes[:idx] + notes_003 + "\n</ol>\n</section>\n</body>\n</html>"
    with open(f"{BASE_DIR}/EPUB/text/notes.xhtml", "w", encoding="utf-8") as f:
        f.write(new_notes)
    print("Notes updated with Section 003.")

# ==========================================
# UPDATE TOC / NAV / NCX
# ==========================================

# icerindekiler.xhtml
icerik_html = """<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="tr">
<head>
<meta charset="utf-8"/>
<title>İçindekiler</title>
<link rel="stylesheet" type="text/css" href="../styles/main.css"/>
</head>
<body>
<section id="icerindekiler">
<h1>İçindekiler</h1>
<p class="note-intro">Kizumonogatari: Sıfırıncı Bölüm — Koyomi Vamp</p>
<ol class="toc-list">
<li><a href="chapter1.xhtml#koyomi_vamp">Sıfırıncı Bölüm: Koyomi Vamp (こよみヴァンプ)</a>
<ol class="subtoc-list">
<li><a href="chapter1.xhtml#P0001">001 — Giriş ve Cehennemin Başlangıcı</a></li>
<li><a href="chapter1.xhtml#P0042">002 — İnsanlık Mukavemeti ve Bahar Rüzgârı</a></li>
<li><a href="chapter1.xhtml#P0481">003 — Gece Firarı ve Demirkanlı Vampir</a></li>
</ol>
</li>
<li><a href="notes.xhtml#notes">Çevirmen ve Yerelleştirme Notları</a></li>
</ol>
</section>
</body>
</html>
"""
with open(f"{BASE_DIR}/EPUB/text/icerindekiler.xhtml", "w", encoding="utf-8") as f:
    f.write(icerik_html)

# nav.xhtml
nav_html = """<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="tr">
<head>
<meta charset="utf-8"/>
<title>İçindekiler</title>
<link rel="stylesheet" type="text/css" href="styles/main.css"/>
</head>
<body>
<nav epub:type="toc" id="toc">
<h1>İçindekiler</h1>
<ol>
<li><a href="text/icerindekiler.xhtml">İçindekiler</a></li>
<li><a href="text/chapter1.xhtml#koyomi_vamp">Sıfırıncı Bölüm: Koyomi Vamp</a>
<ol>
<li><a href="text/chapter1.xhtml#P0001">001 — Giriş ve Cehennemin Başlangıcı</a></li>
<li><a href="text/chapter1.xhtml#P0042">002 — İnsanlık Mukavemeti ve Bahar Rüzgârı</a></li>
<li><a href="text/chapter1.xhtml#P0481">003 — Gece Firarı ve Demirkanlı Vampir</a></li>
</ol>
</li>
<li><a href="text/notes.xhtml#notes">Çevirmen Notları</a></li>
</ol>
</nav>
<nav epub:type="landmarks" id="landmarks" hidden="">
<h2>Rehber</h2>
<ol>
<li><a epub:type="cover" href="cover.jpg">Kapak</a></li>
<li><a epub:type="toc" href="text/icerindekiler.xhtml">İçindekiler</a></li>
<li><a epub:type="bodymatter" href="text/chapter1.xhtml">Metin</a></li>
</ol>
</nav>
</body>
</html>
"""
with open(f"{BASE_DIR}/EPUB/nav.xhtml", "w", encoding="utf-8") as f:
    f.write(nav_html)

# toc.ncx
ncx_html = """<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="tr">
<head>
<meta name="dtb:uid" content="urn:uuid:e8b61c8a-7c91-4e08-9a3c-5528eb1e9678"/>
<meta name="dtb:depth" content="2"/>
<meta name="dtb:totalPageCount" content="0"/>
<meta name="dtb:maxPageNumber" content="0"/>
</head>
<docTitle>
<text>Kizumonogatari — Türkçe Çeviri</text>
</docTitle>
<docAuthor>
<text>西尾維新 (Nisio Isin)</text>
</docAuthor>
<navMap>
<navPoint id="np-1" playOrder="1">
<navLabel><text>İçindekiler</text></navLabel>
<content src="text/icerindekiler.xhtml"/>
</navPoint>
<navPoint id="np-2" playOrder="2">
<navLabel><text>Sıfırıncı Bölüm: Koyomi Vamp</text></navLabel>
<content src="text/chapter1.xhtml"/>
<navPoint id="np-3" playOrder="3">
<navLabel><text>001 — Giriş</text></navLabel>
<content src="text/chapter1.xhtml#P0001"/>
</navPoint>
<navPoint id="np-4" playOrder="4">
<navLabel><text>002 — İnsanlık Mukavemeti</text></navLabel>
<content src="text/chapter1.xhtml#P0042"/>
</navPoint>
<navPoint id="np-5" playOrder="5">
<navLabel><text>003 — Demirkanlı Vampir</text></navLabel>
<content src="text/chapter1.xhtml#P0481"/>
</navPoint>
</navPoint>
<navPoint id="np-6" playOrder="6">
<navLabel><text>Çevirmen Notları</text></navLabel>
<content src="text/notes.xhtml"/>
</navPoint>
</navMap>
</ncx>
"""
with open(f"{BASE_DIR}/EPUB/toc.ncx", "w", encoding="utf-8") as f:
    f.write(ncx_html)

# ==========================================
# REBUILD EPUB ZIP
# ==========================================

if os.path.exists(EPUB_OUT):
    os.remove(EPUB_OUT)

with zipfile.ZipFile(EPUB_OUT, "w") as z:
    z.write(f"{BASE_DIR}/mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)
    for root, dirs, files in os.walk(f"{BASE_DIR}/META-INF"):
        for file in files:
            full_path = os.path.join(root, file)
            arcname = os.path.relpath(full_path, BASE_DIR)
            z.write(full_path, arcname, compress_type=zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(f"{BASE_DIR}/EPUB"):
        for file in files:
            full_path = os.path.join(root, file)
            arcname = os.path.relpath(full_path, BASE_DIR)
            z.write(full_path, arcname, compress_type=zipfile.ZIP_DEFLATED)

print(f"REBUILD SUCCESS: EPUB now {os.path.getsize(EPUB_OUT)} bytes.")
