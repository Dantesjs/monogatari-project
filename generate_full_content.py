# -*- coding: utf-8 -*-
import os, zipfile, datetime

BASE_DIR = "/data/data/com.termux/files/home/monogatari-project/kizumonogatari_epub"
EPUB_OUT = "/data/data/com.termux/files/home/monogatari-project/04_Kizumonogatari_TR.epub"

# ==========================================
# 1. CHAPTER 1 (Sections 001 and 002)
# ==========================================

ch1_html = """<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="tr">
<head>
<meta charset="utf-8"/>
<title>Sıfırıncı Bölüm: Koyomi Vamp</title>
<link rel="stylesheet" type="text/css" href="../styles/main.css"/>
</head>
<body>
<section epub:type="chapter" id="koyomi_vamp">
<h1 class="chapter-title">Sıfırıncı Bölüm<br/>Koyomi Vamp</h1>
<p class="chapter-sub">傷物語 — 第零話　こよみヴァンプ</p>

<h3 id="P0001" class="section-no">001</h3>

<p id="P0002">Sanırım artık Kiss-shot Acerola-orion Heart-under-blade’den bahsetmemin zamanı geldi.<a id="nr-1" href="notes.xhtml#note-1" epub:type="noteref" class="noteref"><sup>[1]</sup></a> Üzerimde böyle bir vazife olduğuna eminim. Lise ikinci sınıftan üçüncü sınıfa geçişin o tekinsiz arafında, bahar tatilinde tanıştım onunla.<a id="nr-2" href="notes.xhtml#note-2" epub:type="noteref" class="noteref"><sup>[2]</sup></a> Sarsıcı bir karşılaşmaydı; hatta düpedüz yıkıcıydı. Neresinden bakarsanız bakın, feleğin çemberinden payıma düşen kör talihimdi işte.<a id="nr-3" href="notes.xhtml#note-3" epub:type="noteref" class="noteref"><sup>[3]</sup></a> Elbette ben bu felaketten kazara kaçamamış olsam bile, eğer kaçabilseydim, benim yerime başka birinin aynı akıbete uğrayacağını söyleyemem; muhtemelen öyle bir şey olmazdı. Başıma gelenleri yalnızca “şanssızlık” diye yaftalamak son derece sorumsuz bir lafebeliği de olabilir; dürüstçe çıkıp kabahatin bende olduğunu söylemem gerekir belki de. Nihayetinde tüm o olaylar silsilesi, sırf ben, <em>ben</em> olduğum için yaşandı.</p>

<p id="P0003">Olaylar silsilesi…</p>

<p id="P0004">Büyük bir ehemmiyet atfetmeden, bir çırpıda “olaylar silsilesi” deyiverdim gerçi; fakat böyle bir ifade kullandığımda işin içine tam olarak nelerin girip nelerin çıkması gerektiğinden pek emin değilim doğrusu. Hadise tam nerede patlak verdi, hangi dönemeçlerden geçti ve nihayetinde nasıl son buldu? Kesin bir sınır çizmek elimden gelmez. Lafazanlık olsun diye ya da ucuz kelime oyunlarına sığınarak söylemiyorum;<a id="nr-4" href="notes.xhtml#note-4" epub:type="noteref" class="noteref"><sup>[4]</sup></a> hadisenin bugün bile bitmemiş olabileceğine, hatta belki henüz başlamadığına dahi tüm samimiyetimle inanıyorum.</p>

<p id="P0005">Ne de olsa ben bu hadiseyi yalnızca kendi gözlerimin ardından gözlemleyebilirdim. Bu yüzden benim haricimdeki insanlar için o olaylar silsilesinin hakikatte ne mana taşıdığını —veya ne mana taşımadığını— ebediyen öğrenemeyeceğim. “Onları” dinleme fırsatım olsaydı belki vaziyeti bir nebze kavrayabilirdim; fakat o zaman da bana anlatılanların gerçeğin ta kendisi olup olmadığını asla bilemezdim.</p>

<p id="P0006">Ortada hakikat diye bir şey yok; yalnızca algı var.</p>

<p id="P0007">Ve belki de bu kadarı kâfidir.</p>

<p id="P0008">Yine de (en azından bundan zerre şüphe duymuyorum), meselenin tam göbeğindeki o kadın —Kiss-shot Acerola-orion Heart-under-blade— tamı tamına böyle bir varlıktı işte.</p>

<p id="P0009">Yalnızca gözlemcisi için bir anlam ifade eder.</p>

<p id="P0010">Gözlemcisine göre anlamı değişir.</p>

<p id="P0011">Gözlemcilerin zihnindeki anlamlar asla birbiriyle örtüşmez.</p>

<p id="P0012">İşte budur — vampir dediğin şey.</p>

<p id="P0013">Gerçi bir vampirin ne mene bir varlık olduğuna dair uzun uzadıya ahkâm kesmeye lüzum yok herhalde. Çizgi romanlar, filmler, oyunlar sağ olsun; iliğine kadar sömürülmüş, posası çıkarılmış bir maden ocağıdır bu.<a id="nr-5" href="notes.xhtml#note-5" epub:type="noteref" class="noteref"><sup>[5]</sup></a> Bu toprakların öz kültürü olmasa da, Japonların kahir ekseriyeti için ziyadesiyle aşina bir figürdür. Devrini bir buçuk tur tamamlayıp artık hafiften bayatlamış bir mefhum denebilir hatta.</p>

<p id="P0014">Fakat o bahar tatilinde…</p>

<p id="P0015">Devrini bir buçuk tur tamamlamış o köhne mefhum, yani bir vampir, gelip bana saldırdı.</p>

<p id="P0016">Basiretsizlik denebilir buna.<a id="nr-6" href="notes.xhtml#note-6" epub:type="noteref" class="noteref"><sup>[6]</sup></a></p>

<p id="P0017">Doğrusunu isterseniz, katıksız bir ahmaklıktı.</p>

<p id="P0018">Ve bir başkasının değil, bizzat kendi ahmaklığım yüzünden — iki hafta boyunca cehennemi tatmak zorunda kaldım.</p>

<p id="P0019">Bahar tatilini başından sonuna, tepeleme tüketen bir cehennemdi.</p>

<p id="P0020">Cehennemvari bir şakaydı; şaka gibi bir cehennemdi.</p>

<p id="P0021">O olaylar silsilesinin nereden başlayıp nasıl evrildiği ve nasıl bittiği —daha önce de belirttiğim gibi— benim için çözümsüz bir paradoks, ebedi bir muammadır. Ancak o biricik cehennemin ne vakit başlayıp ne vakit bittiği benim açımdan gün gibi aşikârdır:</p>

<p id="P0022">Yirmi altı Mart’tan, yedi Nisan’a kadar.</p>

<p id="P0023">Yani bahar tatili.</p>

<p id="P0024">Kiss-shot Acerola-orion Heart-under-blade… Zamanı geldiğinde onun gibi varlıklara <em>musibet (kaii)</em> dendiğini öğrenecektim.<a id="nr-7" href="notes.xhtml#note-7" epub:type="noteref" class="noteref"><sup>[7]</sup></a></p>

<p id="P0025">Musibet.</p>

<p id="P0026">Hortlak.</p>

<p id="P0027">İnsanlıktan çıkmış hilkat garibesi.</p>

<p id="P0028">Öyleyse, o gün, o saatte, o yerde onu tam da bu şekilde gözlemlemiş olmam — o cehennemi tecrübe etmemin başlıca müsebbibiydi sanırım.</p>

<p id="P0029">Bir gözlemci sıfatıyla fena halde yetersizdim.</p>

<p id="P0030">Ve nihayetinde, sahiden de ahmaktım.</p>

<p id="P0031">O kadından bahsetmeye niyetlendiğim an, kaçınılmaz olarak kendi ahmaklığımı da hiçbir şey saklamadan faş etmek durumunda kalıyorum. Dışarıdan bakıldığında bu halim acınası bir mazoşizm gibi görünebilir; gelgelelim, ne olursa olsun o vampiri anlatmak zorundayım.</p>

<p id="P0032">Ondan aldığım yaraların hikâyesini.<a id="nr-8" href="notes.xhtml#note-8" epub:type="noteref" class="noteref"><sup>[8]</sup></a></p>

<p id="P0033">Onu yaraladığım o hikâyeyi.</p>

<p id="P0034">Anlatmak mecburiyetindeyim.</p>

<p id="P0035">Anlatmak boynumun borcudur.</p>

<p id="P0036">Bu benim mesuliyetim.</p>

<p id="P0037">…Giriş kısmını epey uzattığımın farkındayım, lakin mazur görmenizi istirham ederim. Sorumluluktan falan allame gibi dem vurduğuma bakmayın; nihayetinde basiretsiz bir soytarının mesuliyetidir bu.<a id="nr-9" href="notes.xhtml#note-9" epub:type="noteref" class="noteref"><sup>[9]</sup></a> Nerede tökezleyeceğim hiç belli olmaz. Lafı gevelemeyi bırakıp açık konuşmak gerekirse, bu hikâyenin sonunu getirebileceğime dair içimde zerre özgüven yok. İşte tam da bu yüzden lafı eveleyip geveliyor, kendimce makul görünen girizgâhlar ardına sığınıyorum.</p>

<p id="P0038">Fakat bunun da bir sınırı var elbet. Bir kere anlatmaya koyuldum mu, yokuş aşağı yuvarlanan bir kaya misali arkası gelecektir; durdurması anlatmaktan daha müşkül olur.<a id="nr-10" href="notes.xhtml#note-10" epub:type="noteref" class="noteref"><sup>[10]</sup></a> Yine de her ihtimale karşı, olur da dirayetim yetmezse diye, bu hikâyenin akıbetini peşinen, en baştan ilan etmek isterim:</p>

<p id="P0039">Vampire dair bu hikâye bir hezimetle biter.<a id="nr-11" href="notes.xhtml#note-11" epub:type="noteref" class="noteref"><sup>[11]</sup></a></p>

<p id="P0040">Herkesin bedbaht olmasıyla nihayete erer.</p>

<p id="P0041">Ki bu dahi yalnızca cehennemin sonudur; o olaylar silsilesi aslında hâlâ bitmemiştir belki de. Nasıl olursa olsun, o kadına karşı olan mesuliyetim, ömrümün sonuna kadar üzerimden kalkmayacaktır.</p>

<h3 id="P0042" class="section-no">002</h3>

<p id="P0043">“Çünkü arkadaş edinirsen insanlık mukavemetin düşer.”<a id="nr-12" href="notes.xhtml#note-12" epub:type="noteref" class="noteref"><sup>[12]</sup></a></p>

<p id="P0044">Galiba tam olarak böyle bir laf etmiştim.</p>

<p id="P0045">Hafızamı yokladığımda o güne dönüyorum; bahar tatilinin hemen arifesinde, yirmi beş Mart Cumartesi günü, kapanış töreninin yapıldığı o ılık öğleden sonraya… Okuduğum özel Naoetsu Lisesi’nin etrafında, hiçbir gaye gütmeksizin başıboş adımlarla aylaklık ediyordum.</p>

<p id="P0046">Hiçbir okul kulübüne veya sosyal faaliyete zerre bulaşmamış biriyim ne de olsa.</p>

<p id="P0047">Sahiden de zerre işim gücüm olmadan, avare avare dolanıyordum sokaklarda.</p>

<p id="P0048">Yarından itibaren bahar tatili başlayacak diye sevinçten havalara uçtuğumu sanmayın; katiyen öyle bir durum yoktu.</p>

<p id="P0049">Yalnızca bahar tatili değil; yaz tatili, kış tatili yahut Altın Hafta olsun; bu kabil uzun soluklu tatiller bir öğrenci milleti için genel geçer bir saadet vesilesi olmalıdır şüphesiz. Ben de nihayetinde üçüncü dönemin bitmesinden ve tatil rejimine girmekten memnundum memnun olmasına; gelgelelim, böylesine uzun tatillerin can sıkıntısından patladığım, zamanı nereye harcayacağımı bilemediğim bir boşluğa dönüştüğü de acı bir hakikatti.</p>

<p id="P0050">Hele de bahar tatilinde ödev mödev verilmediğinden…</p>

<p id="P0051">Evde oturmak nedense içimi daraltıyordu.</p>

<p id="P0052">Hal böyle olunca —kapanış töreni bitip sınıfta karneleri aldıktan sonra “yeni dönemde görüşürüz” temennileriyle sınıf dağıldığında— doğruca eve dönmekte tereddüt etmiş; lakin gidecek başka hiçbir yerim de olmadığından, şüpheli şahıslar misali okulun çevresinde amaçsızca dolanıp durmaya başlamıştım.</p>

<p id="P0053">Özel bir maksadım yoktu.</p>

<p id="P0054">Vakit geçirmekten ziyade, düpedüz zamanı katletmekti benimkisi.</p>

<p id="P0055">Aslına bakarsanız okula bisikletle gidip gelirim; fakat bisikletimi hâlâ okulun park yerinde bırakmıştım — bu da eve dönmeye pek niyetim olmadığının açık bir göstergesiydi.</p>

<p id="P0056">Yürüyüş desen yürüyüştü gerçi.</p>

<p id="P0057">Tabii ki ben öyle sağlıklı yaşam meraklısı biri falan değildim.</p>

<p id="P0058">Zaman öldüreceksem bunu okulun içinde de yapabilirdim pekâlâ; lakin tıpkı evde rahat edemediğim gibi okulun içi de ayrı bir boğucuydu — kapanış töreninin yapıldığı öğleden sonra olmasına karşın kulüp faaliyetlerini sürdürenlerin sayısı azımsanmayacak kadar çoktu.</p>

<p id="P0059">Kendini bir şeylere adayıp canla başla çabalayan insanlara tahammül edemem.</p>

<p id="P0060">Gerçi bizim okul spor kulüpleri konusunda öyle pek de hırslı sayılmazdı. Geçen yıl nasıl olduysa bir yanlışlık eseri okula kaydolmuş canavar gibi dev bir çaylağın katıldığı kız basketbol takımı müstesnaydı tabii;<a id="nr-13" href="notes.xhtml#note-13" epub:type="noteref" class="noteref"><sup>[13]</sup></a> onun haricindeki tüm spor kollarında genel hava “katılmak kazanmaktan mühimdir” gevşekliğindeydi.</p>

<p id="P0061">İşte bu minvalde, pek de geçerli bir sebep olmaksızın okulun etrafında tavaf eder gibi turladıktan sonra, karnımın da guruldamaya başlamasıyla artık bisikletimi alıp eve dönme vaktinin geldiğini düşünmeye başlamıştım ki — tam o esnada hiç umulmadık biriyle karşılaşıverdim.</p>

<p id="P0062">Bahar tatilinde olduğumuz için kendimi hâlâ ikinci sınıf mı yoksa artık üçüncü sınıf mı saymalıyım pek emin değilim; ancak her halükarda bizim dönemin meşhur siması —Hanekawa Tsubasa— tam karşımdan bana doğru yürümekteydi.<a id="nr-14" href="notes.xhtml#note-14" epub:type="noteref" class="noteref"><sup>[14]</sup></a></p>

<p id="P0063">İki elini başının arkasına götürmüştü. Bir an ne yaptığını kestiremedim; meğer arkadaki örgüsünü düzeltiyormuş. Uzunca saçlarını arkada tek bir örgü halinde toplamıştı. Günümüzde saç örgüsü başlı başına ender rastlanan bir şeyken, bir de bunun üstüne kâküllerini cetvelle çizilmiş gibi dümdüz kestirmişti.</p>

<p id="P0064">Üzerinde okul üniforması vardı.</p>

<p id="P0065">En ufak bir tadilat görmemiş, dizin tam on santim altına inen nizami bir etek.</p>

<p id="P0066">Siyah bir fular.</p>

<p id="P0067">Bluzunun üzerine giyilmiş, okul tüzüğüne harfiyen uygun süveter.</p>

<p id="P0068">Yine tüzük kurallarına birebir uyan beyaz çoraplar ve standart okul pabuçları.</p>

<p id="P0069">Tepeden tırnağa tam bir örnek öğrenci manzarasıydı.</p>

<p id="P0070">Ve nitekim kendisi sahiden de örnek bir öğrenciydi.</p>

<p id="P0071">Örnek öğrencilerin şahı, mümessillerin mümessiliydi.<a id="nr-15" href="notes.xhtml#note-15" epub:type="noteref" class="noteref"><sup>[15]</sup></a></p>

<p id="P0072">Gerek birinci sınıfta gerekse ikinci sınıfta onunla hiç aynı şubede olmadık; bu yüzden onun beni tanımasına imkân yoktu şüphesiz. Fakat ben onun sınıf başkanlığındaki dillere destan titizliğini ta uzaktan işitmiştim.</p>

<p id="P0073">Dedikodulara bu denli sağır olan benim kulağıma kadar çalındığına göre, anlatılanları yarı yarıya kırpsanız dahi hakikaten takdire şayan bir başkanlık sergilemiş olmalıydı.</p>

<p id="P0074">Üçüncü sınıfta da sınıf başkanlığı yapacağına kalıbımı basardım.</p>

<p id="P0075">Üstelik akademik başarısı da muazzamdı.</p>

<p id="P0076">Kulağa garip gelse de anormal derecede zekiydi. Beş anabilim dalı, altı dersten oluşan sınavlarda altı yüz tam puan almak onun için çocuk oyuncağıydı. Gerçi herkes sınava girdiğinde birinin birinci, birinin de sonuncu olması eşyanın tabiatı gereğidir; ne var ki Hanekawa Tsubasa iki yıl boyunca zirvedeki yerini bir an olsun kaptırmamıştı.</p>

<p id="P0077">Naoetsu Lisesi gibi üniversiteye hazırlayan hususi bir okula kapağı atana kadar iyi hoş gidip de sonrasında bir 'ah' demeden dökülen, bir 'of' demeden sefilleşen benim gibi biriyle kıyaslandığında yerle gök kadar fark vardı aramızda; taban tabana zıt iki kutuptuk adeta.<a id="nr-16" href="notes.xhtml#note-16" epub:type="noteref" class="noteref"><sup>[16]</sup></a></p>

<p id="P0078">Hımm.</p>

<p id="P0079">İster istemez bir anlığına dikkatim ona kaydı.</p>

<p id="P0080">Farklı sınıflarda olduğumuzdan gıyaben bilsem de yüzünü neredeyse hiç görmezdim — kapanış töreninin bittiği şu saatte onunla böyle tesadüfen karşılaşmak beni hafiften şaşırtmıştı.</p>

<p id="P0081">Neyse.</p>

<p id="P0082">Kaderin bir cilvesi işte, alelade bir tesadüf.</p>

<p id="P0083">Anlaşılan okul kapısından yeni çıkmıştı; zaten biraz düşünecek olursanız ben de sabahtan beri okulun etrafında fırdolayı dolandığıma göre karşılaşmamızda öyle mucizevi bir yan yoktu.</p>

<p id="P0084">Hanekawa tarafında ise beni fark ettiğine dair en ufak bir emare yoktu elbette.</p>

<p id="P0085">Örgüsünü hizalamaya öyle bir dalmıştı ki görüş alanına girdiğimi bile sanmıyordum — girmiş olsaydım dahi Hanekawa ile aramızda birbirimize bir baş selamı verecek kadar bile hukuk yoktu.</p>

<p id="P0086">Hah hah ha.</p>

<p id="P0087">Hatta Hanekawa gibi tertipli ve örnek bir tip, benim gibi hayatı lakaytça yaşayan ipsiz sapsız birinden muhtemelen köşe bucak nefret ederdi.</p>

<p id="P0088">O ne kadar disiplinliyse, ben o kadar başıboştum.</p>

<p id="P0089">Beni hiç tanımaması çok daha evlaydı.</p>

<p id="P0090">En iyisi hiçbir şey olmamış gibi yanımdan geçip gitmesine izin vermekti.</p>

<p id="P0091">Durduk yere kaçıp göçmeye de lüzum yoktu hani.</p>

<p id="P0092">Ben de sanki onu hiç görmemişim gibi adımlarımı bozmadan yürümeye devam ettim — aramızda birbirimizi selamsız sabahsız teğet geçmemize topu topu beş adımlık mesafe kalmıştı ki, tam o anda olanlar oldu.</p>

<p id="P0093">Ben…</p>

<p id="P0094">O anı muhtemelen ömrümün sonuna dek unutamayacağım.</p>

<p id="P0095">Hiçbir işaret vermeksizin —ansızın bir rüzgâr patladı.</p>

<p id="P0096">“Ah!”</p>

<p id="P0097">Gayriihtiyari dudaklarımdan dökülen ses bu oldu.</p>

<p id="P0098">Hanekawa’nın dizinin on santim altına kadar inen o pileli eteğinin ön kısmı, rüzgârın şiddetiyle tepeye kadar savruluvermişti.</p>

<p id="P0099">Normal şartlarda bir kız refleksiyle eteğini derhal bastırması gerekirdi — gelgelelim talihin en berbat cilvesiyle tam o esnada iki eli de başının arkasındaydı ve örgüsünü düzeltmek gibi hassas bir işle meşguldü. Benim durduğum zaviyeden bakıldığında, ellerini ensesinde kavuşturmuş, sanki hafiften fiyakalı bir poz veriyormuş gibi bir intiba uyanıyordu.</p>

<p id="P0100">İşte tam o vaziyetteyken etek havalandı.</p>

<p id="P0101">Ve altındaki her şey çırılçıplak gözler önüne serildi.</p>

<p id="P0102">Katiyen gösterişli değildi — fakat üzerine kilitlenen bakışları başka bir yana çevirmeye asla müsaade etmeyecek kadar zarif ve asil bir iç çamaşırıydı.</p>

<p id="P0103">Tertemiz, lekesiz, bembeyaz bir renkti.</p>

<p id="P0104">Öyle cüretkâr veya daracık bir kesimi yoktu; bilakis kumaş yüzeyi epeyce genişti. Kenarları hayli enli, kumaşı ise gayet tok ve kaliteliydi — zerre kışkırtıcı değildi ve bu manada bakıldığında belki de dişilikten nasibini almamış sayılabilirdi.</p>

<p id="P0105">Ne var ki o beyazlığın safiyeti karşısında gözlerim adeta kamaştı.</p>

<p id="P0106">Ve asla sıradan değildi.</p>

<p id="P0107">Tam orta kısmında, beyaz zemin üzerine beyaz iplikle ince ince işlenmiş karmaşık bir nakış göze çarpıyordu — muhtemelen zarif bir çiçek motifiydi. İki tarafa simetrik yayılan bu desen, çamaşırın umumi ahengine kusursuz bir zarafet katmıştı. Ve nakışın hemen üzerinde, merkezde minik bir fiyonk yer alıyordu.</p>

<p id="P0108">O küçücük fiyonk bütün manzaraya ayrı bir asalet bahşetmişti.</p>

<p id="P0109">Dahası, o minik fiyonkun hemen üstünde, kızın pürüzsüz alt karnı ve son derece sevimli göbek deliği görünüyordu. Böylesi mahrem hatlar bile pervasızca açığa çıkacak derecede cüretkâr savrulmuştu etek. Eteğin içine sokulmuş olan okul bluzunun etek uçları bile milim milim gözlemlenebiliyordu. Bir bluzun etek ucunun bu derece baştan çıkarıcı görünebileceği kırk yıl düşünsem aklıma gelmezdi.</p>

<p id="P0110">Ayrıca eteğin astar kumaşı da benim için yepyeni bir keşifti. Her gün etrafta görüp de dokunulmaz bir sır gibi meçhul kalan 'etek' denen giysinin iç mimarisini ilk defa o an idrak etmiştim.</p>

<p id="P0111">Her şeyden öte, havalanan kısmın yalnızca eteğin ön tarafı olması muazzam bir lütuftu.</p>

<p id="P0112">Bembeyaz iç çamaşırı ve o çamaşırın beyazlığıyla yarışan, kâfi derecede dolgun ve sütbeyaz uylukları; arkadaki lacivert eteğin fon oluşturmasıyla öyle bir kontrast yakalamıştı ki göz alıcı bir parlaklıkla öne fırlıyordu. Sıradan kızlara kıyasla hayli uzun olan o nizamı etek, bu vaziyette adeta nadide bir sanat eserini sergilemek üzere arkaya çekilmiş kadife bir sahne perdesini andırıyordu.</p>

<p id="P0113">Ellerini ensesinde kavuşturmuş o duruşu da eklenince; sanki iftihar ettiği o mahrem güzelliği bana bilhassa sergiliyormuş gibi — neticede kız tam olarak böyle bir manzaraya bürünmüştü.</p>

<p id="P0114">O kız…</p>

<p id="P0115">Hanekawa Tsubasa kılını bile kıpırdatmadı.</p>

<p id="P0116">Şaşkınlıktan dili tutulmuş olmalıydı.</p>

<p id="P0117">Kollar ensede o heykelimsi duruşunu muhafaza ederek, eteğin rüzgârda dalgalanmasına boyun eğmiş; çehresi dahi taş kesilmişti.</p>

<p id="P0118">Hakikatte bir saniyeden bile kısa sürmüş olmalıydı.</p>

<p id="P0119">Fakat benim için koca bir saate bedeldi — hatta ömrümün tam orada nihayete erebileceği hissine kapıldım. Abartmıyorum; o tek bir saniyenin içinde koca bir ömrü tecrübe ettim.</p>

<p id="P0120">Gözbebeklerimin yüzeyi kuruyana dek…</p>

<p id="P0121">Bütün varlığım onun belden aşağısındaki o manzaraya kilitlendi.</p>

<p id="P0122">Yok, biliyorum elbet — böyle durumlarda bir kadına hürmeten başını usulca öte yana çevirmenin asgari nezaket kuralı olduğunu bal gibi biliyorum.</p>

<p id="P0123">Normalde ben de öyle yapardım nitekim.</p>

<p id="P0124">Merdiven çıkarken önümde bir kız varsa, gözlerimi sadece kendi ayakkabılarıma dikmeye azami dikkat gösteren biriyimdir.</p>

<p id="P0125">Lakin zihnen en ufak bir hazırlığımın olmadığı bir anda gökten zembille inen böylesi bir saadet karşısında bir centilmen gibi davranabilecek kadar olgunlaşmış bir erkek değildim henüz.</p>

<p id="P0126">Hanekawa’nın o silueti retinama kazınmıştı adeta.</p>

<p id="P0127">Muhtemelen şu an ölecek olsam ve kornealarım bir başkasına nakledilse; o talihli şahıs ömrünün geri kalanında Hanekawa’nın iç çamaşırının hayaliyle yaşamak zorunda kalırdı.</p>

<p id="P0128">Öylesine sarsıcıydı.</p>

<p id="P0129">İşte örnek bir talebenin iç çamaşırı böyle bir şeydi.</p>

<p id="P0130">“………………”</p>

<p id="P0131">Dur bir dakika yahu.</p>

<p id="P0132">Örnek öğrencinin donunu daha ne kadar tasvir edeceksin be adam?</p>

<p id="P0133">Nihayet aklım başıma geldiğinde Hanekawa’nın eteği çoktan eski yerine inmişti bile.</p>

<p id="P0134">Hakikaten de bir anlık bir hadiseydi.</p>

<p id="P0135">Ve Hanekawa…</p>

<p id="P0136">Yüzündeki o donakalmış ifadeyle — doğrudan bana bakıyordu.</p>

<p id="P0137">Gözlerini dikmiş, dik dik süzüyordu beni.</p>

<p id="P0138">“Şey… Kem küm…”</p>

<p id="P0139">Eyvahlar olsun.</p>

<p id="P0140">Vaziyeti nasıl toparlayacaktım?</p>

<p id="P0141">Böyle bir durumda ne denirdi ki?</p>

<p id="P0142">“B-Ben… Vallahi hiçbir şey görmedim?”</p>

<p id="P0143">Kuyruklu bir yalana sığınmayı denedim.</p>

<p id="P0144">Fakat Hanekawa sıktığım bu bariz yalana zerre tepki vermeksizin gözlerini benden ayırmadı. Örgü operasyonunu tamamlamış olmalı ki kollarını nihayet aşağı indirdi ve iş işten geçtikten sonra eteğinin önünü eliyle pıt pıt silkeledi.</p>

<p id="P0145">Hakikaten tam anlamıyla iş işten geçtikten sonra tabii.</p>

<p id="P0146">Sonra bir saniyeliğine bakışlarını benden kaçırıp göğe doğru çevirdi; ardından tekrar bana dönerek,</p>

<p id="P0147">“Ehehe…”</p>

<p id="P0148">Diyerek mahcupça gülümsedi.</p>

<p id="P0149">…Vay canına.</p>

<p id="P0150">Burada gülüyor muydu sahiden?</p>

<p id="P0151">Hakikaten yüreği geniş kızmış — mümessillerin mümessili olmak boşuna değil.</p>

<p id="P0152">“Nasıl desem bilmem ki…”</p>

<p id="P0153">Tıp, tıp, tıp…</p>

<p id="P0154">İki ayağını bitiştirip dizlerini yaylandırarak yaylana yaylana bana doğru yaklaştı Hanekawa.</p>

<p id="P0155">Aramızdaki on adımlık mesafeyi üç adıma kadar indirdi.</p>

<p id="P0156">Biraz fazla yakın bir mesafeydi bu.</p>

<p id="P0157">“Görünmesini istemediğin şeyleri gizlemek adına etek dediğin şeyin güvenlik seviyesi feci derecede düşük, değil mi? Acaba altına şort çekip bir güvenlik duvarı mı (firewall) kursaydım?”</p>

<p id="P0158">“Ş-Şey… Bilmem ki…”</p>

<p id="P0159">Böyle metaforlarla konuşması beni daha da köşeye sıkıştırıyordu.</p>

<p id="P0160">Ne yani, ben virüs müydüm şimdi?</p>

<p id="P0161">Kızın şansına mıdır nedir, etrafta Naoetsu Lisesi öğrencileri dahil in cin top oynuyordu.</p>

<p id="P0162">Sadece ben ve Hanekawa vardık.</p>

<p id="P0163">Yani onun iç çamaşırını gören yegâne kul bendim.</p>

<p id="P0164">Bu hakikat içimde tuhaf bir üstünlük gururu uyandırmadı değil; lakin mevzu o değildi.</p>

<p id="P0165">“Hani bir ara Murphy Kanunları meşhurdu ya,” dedi Hanekawa. “Oraya bir madde daha eklemek lazım belki de: 'İki elini arkaya bağladığın an, eteğin önden savrulacağı tutar' diye… Arkadan gelecek tehlikeyi kollarsın kollamasına da, ön taraf hiç umulmadık bir kör noktadır bazen.”</p>

<p id="P0166">“Ha… Haklı olabilirsin.”</p>

<p id="P0167">Bana neydi ki?</p>

<p id="P0168">Daha doğrusu fena halde mahcuptum.</p>

<p id="P0169">Hanekawa’nın böyle bir kastı olsun veya olmasın, üstü kapalı bir şekilde suçlanıyormuşum gibi hissediyordum — gerçi manzarayı doya doya seyretmiş bir adam olarak şimdi kalkıp günahsız ayaklarına yatmam inandırıcı gelmeyebilir; lakin bir kızın 'görünmesini istemeyeceği' mahrem bir şeye kasıtsız da olsa şahit olmanın üzerime yüklediği suçluluk hissi fazlasıyla sahiciydi.</p>

<p id="P0170">Üstelik bu kız böylesine mütebessim bir çehreyle…</p>

<p id="P0171">Meseleyi uzatmaya çalışıyordu sanki.</p>

<p id="P0172">“Ş-Şey, kafana takma sen. Görmedim derken yalan söyledim gerçi ama gölgede kaldığı için öyle net bir şey göremedim zaten.”</p>

<p id="P0173">Bu da kuyruklu bir yalandı tabii.</p>

<p id="P0174">Akıllara ziyan bir netlikte görmüştüm.</p>

<p id="P0175">“Hımm, öyle mi?”</p>

<p id="P0176">Hanekawa başını yana eğdi.</p>

<p id="P0177">“Kabak gibi gördüysen dobra dobra söylemen bir kız olarak içimi daha çok rahatlatırdı doğrusu.”</p>

<p id="P0178">“Y-Yok, öyle demeyi canıgönülden isterdim ama hakikatleri çarpıtamam ne yazık ki.”</p>

<p id="P0179">“Demek öyle. Çarpıtamazsın demek.”</p>

<p id="P0180">“Aynen öyle, içini rahatlatamadığım için üzgünüm. Keşke elimden yalan söylemek gelseydi.”</p>

<p id="P0181">Az evvelden beri yalandan başka bir şey konuşmayan bir adamın laflarıydı bunlar.</p>

<p id="P0182">“Yaklaşık dört sayfa boyunca eteğimin altındaki her detayın inceden inceye tasvir edildiğini hissetmem bir yanılsama mı acaba?”<a id="nr-17" href="notes.xhtml#note-17" epub:type="noteref" class="noteref"><sup>[17]</sup></a></p>

<p id="P0183">“Yanılsama yanılsama, hem de katmerlisinden! Ben az önce sadece tabiatın eşsiz zarafetini ve pitoresk bir manzarayı tasvir ediyordum.”</p>

<p id="P0184">Bu söylediğim kısmen doğru sayılırdı hani.</p>

<p id="P0185">“Neyse. Ben müsaadenizi isteyeyim.”</p>

<p id="P0186">Elini hafifçe kaldırıp bu sohbeti daha fazla sürdürmeye niyetim olmadığını belirterek önüme doğru bir adım attım.</p>

<p id="P0187">Hızlı adımlarla uzaklaşmaya başladım.</p>

<p id="P0188">Aman ne bileyim ben.</p>

<p id="P0189">Hanekawa şimdi eve dönecektir dönmesine de; acaba yolda giderken 'falanca çocuk donumu gördü' diye arkadaşlarına mesaj atıp dedikodumu mu yapacaktı? Örnek bir öğrenci böyle basitliklere tenezzül etmez diye düşünüyordum gerçi; ama tam da örnek bir öğrenci olduğu için hırsından yapabileceği de aklıma gelmiyor değildi. Gerçi Hanekawa benim adımı sanımı bilmezdi ama… aynı dönemde olduğumuzu herhalde çakmıştır.</p>

<p id="P0190">Hafiften aşırı alınganlık kokan bu kuruntularla adımlarımı biraz yavaşlatmıştım ki,</p>

<p id="P0191">“Biraz beklesene yahu!”</p>

<p id="P0192">Arkamdan bir ses yükseldi.</p>

<p id="P0193">Hanekawa’ydı.</p>

<p id="P0194">İnanılır gibi değil; peşime düşmüştü.</p>

<p id="P0195">“Anca yetiştim. Ne kadar hızlı yürüyormuşsun öyle.”</p>

<p id="P0196">“…Sen eve gitmiyor muydun?”</p>

<p id="P0197">“Hımm? Eninde sonunda gideceğim tabii. Asıl Araragi-kun neden okula geri dönmeye çalışıyor?”</p>

<p id="P0198">“………………”</p>

<p id="P0199">Adımı noktası virgülüne biliyordu.</p>

<p id="P0200">Nasıl yani?</p>

<p id="P0201">Yakama isimlik falan takmış değildim ki?</p>

<p id="P0202">“…Şey, yani, bisikletimi almaya dönüyordum.”</p>

<p id="P0203">“Aha! Demek bisikletle gidip geliyorsun.”</p>

<p id="P0204">“Öyle sayılır… Evim ne çok yakın ne çok uzak olunca—”</p>

<p id="P0205">Yok yahu, mevzu o değildi.</p>

<p id="P0206">Bisikletle geldiğimi bilmiyordu anlaşılan.</p>

<p id="P0207">“…Sen benim adımı nereden biliyorsun?”</p>

<p id="P0208">“Aşk olsun! Bilmeyeceğim de ne olacak? Aynı okuldayız ya.”</p>

<p id="P0209">Gayet doğal bir şeymiş gibi söyleyiverdi Hanekawa.</p>

<p id="P0210">Aynı okuldayız diye…</p>

<p id="P0211">'Sanki aynı sınıftayız' der gibi konuşuyordu.</p>

<p id="P0212">“Gerçi Araragi-kun beni tanımıyor olabilir ama Araragi-kun okulda epey meşhur biridir bir kere.”</p>

<p id="P0213">“Ne?”</p>

<p id="P0214">İster istemez şaşkınlıkla sordum.</p>

<p id="P0215">Meşhur olan sensin be kızım!</p>

<p id="P0216">Hele benim gibi biri Özel Naoetsu Lisesi’nde yol kenarındaki alelade bir çakıl taşından farksızdır — sınıf arkadaşlarım bile tam adımı doğru dürüst telaffuz edebilir mi şüpheliyim.</p>

<p id="P0217">“Hı? Ne oldu ki Araragi-kun?”</p>

<p id="P0218">“…………”</p>

<p id="P0219">“Solunda tepeciği olan ‘mümkün’ün ‘ka’sı; iyi çocuğun ‘iyi’sinin iki kez tekrarı ve ağaç kütüğünün ‘ki’siyle yazılan Araragi-kun.<a id="nr-18" href="notes.xhtml#note-18" epub:type="noteref" class="noteref"><sup>[18]</sup></a> İlk adın da ayları yılları gösteren takvimin ‘Koyomi’si, değil mi? Yani Araragi Koyomi-kun.”</p>

<p id="P0220">“…………”</p>

<p id="P0221">Soyadımdan adıma, kanjilerine kadar ezbere biliyordu.</p>

<p id="P0222">Yok artık…</p>

<p id="P0223">Yüzümle adımı bu kadar net bildiğine göre; elinde bir Death Note olsa beni anında tahtalı köye gönderir bu kız…<a id="nr-19" href="notes.xhtml#note-19" epub:type="noteref" class="noteref"><sup>[19]</sup></a></p>

<p id="P0224">Gerçi aynı şey benim açımdan da geçerliydi ya, neyse.</p>

<p id="P0225">“Sen de… Hanekawa’sın.”</p>

<p id="P0226">Bir intikam hevesiyle ya da inat olsun diye değil; lafının altında ezilmemek adına başımı sallamayıp karşılık verdim.</p>

<p id="P0227">“Hanekawa Tsubasa.”</p>

<p id="P0228">“Vay canına!”</p>

<p id="P0229">Hanekawa abartılı bir hayret ifadesi takındı.</p>

<p id="P0230">“Harikasın. Benim gibi birinin adını biliyorsun demek.”</p>

<p id="P0231">“İkinci sınıfın birinci dönem sonu sınavlarında beden eğitimi ve sanat dahil bütün derslerde yalnızca tek bir boşluk doldurma sorusunu yanlış yapan Hanekawa Tsubasa.”</p>

<p id="P0232">“Aaa? Yok artık… İnanmıyorum, bunu nereden biliyorsun sen?”</p>

<p id="P0233">Hanekawa daha da şaşırdı.</p>

<p id="P0234">Görünüşe göre rol yapmıyordu.</p>

<p id="P0235">“Yoksa… Yoksa Araragi-kun benim gizli hayranım ya da sapığım falan mısın? Hah hah, yok canım, bu kadarı fazla paranoyakça oldu galiba?”</p>

<p id="P0236">“…Alakası yok.”</p>

<p id="P0237">Anlaşılan bu kız meşhur olduğunun cidden farkında değildi.</p>

<p id="P0238">Kendini ‘sıradan biri’ sanıyordu besbelli.</p>

<p id="P0239">Tek meziyeti birazcık çalışkan olmak olan sıradan bir kız, öyle mi?</p>

<p id="P0240">Bir de kalkmış benim gibi birini meşhur sayıyor ya, pes doğrusu — gerçi ben de okulun yüz karası tembeli olarak bir nebze nam salmış olabilirim tabii.</p>

<p id="P0241">Yine de bunu yüzüne vurmanın bir faydası yoktu…</p>

<p id="P0242">Ben de lafı yuvarlamayı seçtim:</p>

<p id="P0243">“Uzaylı bir arkadaşımdan duydum.”</p>

<p id="P0244">“Ne? Araragi-kun, senin arkadaşın var mı ki?”</p>

<p id="P0245">“Önce uzaylı var mı yok mu diye sorsana be kadın!”</p>

<p id="P0246">Neredeyse ilk defa konuştuğum birine lafı yapıştırıvermiştim.</p>

<p id="P0247">Fakat art niyet gütmese bile hakikaten insafsız bir soruydu.</p>

<p id="P0248">“Ay, şey…”</p>

<p id="P0249">Faka bastığını nihayet anlamış olacak ki Hanekawa mahcup bir tavırla toparlamaya çalıştı:</p>

<p id="P0250">“Araragi-kun hep tek tabanca takılan, dünyadan elini eteğini çekmiş yalnız bir kurttur diye düşünmüştüm de.”</p>

<p id="P0251">“Hangi filmin karizmatik kahramanıymış o öyle?”</p>

<p id="P0252">Beni güya tanıyordu ama…</p>

<p id="P0253">Belli ki pek de tanıdığı yoktu.</p>

<p id="P0254">“Arkadaşımın olmadığı doğru gerçi. Benim gibi arkadaş fukarası birinin bile adını bildiğine bakılırsa, asıl meşhur olanın sen olduğunu anla işte.”</p>

<p id="P0255">“Aman, bırak şunu rica ederim.”</p>

<p id="P0256">Hanekawa burada hafifçe yüzünü ekşitti.</p>

<p id="P0257">Eteğinin altı pervasızca açıldığında mahcup bir kıkırdamayla geçiştiren kız, şimdi rahatsız olmuştu.</p>

<p id="P0258">“Böyle şakalardan pek hazzetmem. Dalga geçmesen iyi edersin.”</p>

<p id="P0259">“…Peki öyle olsun.”</p>

<p id="P0260">İtiraz etsem tartışmaya döneceğinden başımı sallayıp geçtim.</p>

<p id="P0261">Hey gidi hey.</p>

<p id="P0262">Okul kapısının önündeki yaya geçidinde kırmızı ışık yandığı için durdum — Hanekawa da hemen yanımda durdu.</p>

<p id="P0263">…………</p>

<p id="P0264">Bu kız niye hâlâ peşimden geliyordu ki?</p>

<p id="P0265">Okulda bir şey mi unutmuştu?</p>

<p id="P0266">“Baksana Araragi-kun,”</p>

<p id="P0267">Ben kuruntularla boğuşurken,</p>

<p id="P0268">Hanekawa ansızın lafa girdi.</p>

<p id="P0269">“Sen vampirlere inanır mısın?”</p>

<p id="P0270">“…………”</p>

<p id="P0271">Nereden çıktı şimdi bu, diye düşündüm.</p>

<p id="P0272">Ve bir sonraki saniyede jetonum düştü.</p>

<p id="P0273">Ha, anlaşıldı; her ne kadar istifini bozmamış gibi dursa da donunu görmüş olmamdan fena halde utanmıştı besbelli.</p>

<p id="P0274">Gayet insani bir durum tabii.</p>

<p id="P0275">Ben öyle pek meşhur sayılmam ama Hanekawa beni tanıyordu — üstelik arkadaş çevremin olmadığını (yani yalnızlığımı) dahi biliyordu.</p>

<p id="P0276">Muhtemelen hakkımda pek de tekin olmayan dedikodular duymuştu.</p>

<p id="P0277">Haliyle örnek bir öğrenci olarak iç çamaşırını bana alenen inceletmiş… pardon, kazara göstermiş olmasını büyük bir falso olarak değerlendirmesi son derece doğaldı.</p>

<p id="P0278">İşte bu yüzden durumu telafi etmek için peşime takılmıştı.</p>

<p id="P0279">Olayın hemen ardından arkasını dönüp kaçmak yerine peşimden gelip laklak ederek o anıyı zihnimden silmeyi amaçlıyordu muhakkak.</p>

<p id="P0280">Hah.</p>

<p id="P0281">Çok safsın be örnek öğrenci.</p>

<p id="P0282">Vampir falan gibi marjinal konular açtın diye benim hafızam formatlanacak değil ya.</p>

<p id="P0283">“Vampirler n’olmuş ki?”</p>

<p id="P0284">Yine de gönlü olsun diye lafına uymaya karar verdim. İç çamaşırını seyretmiş olmanın diyeti sayılacaksa, iki dakika havadan sudan muhabbet etmek bedavadan biraz pahalı bir bedeldi neticede.</p>

<p id="P0285">“Hani şu sıralar ufak bir dedikodu dolaşıyor ya… Şu an bu kasabada bir vampir varmış. O yüzden geceleri tek başına dışarı çıkmamak gerekiyormuş.”</p>

<p id="P0286">“Muallak… Ve bir o kadar da inandırıcılıktan uzak bir dedikoduymuş,” dedim açıkça.</p>

<p id="P0287">“Böyle kuş uçmaz kervan geçmez bir taşra kasabasında vampirin ne işi var Allah aşkına?”</p>

<p id="P0288">“Kim bilir.”</p>

<p id="P0289">“Vampir dediğin ecnebi hortlağı değil miydi?”</p>

<p id="P0290">“Hortlaktan biraz farklı sanırım ama…”</p>

<p id="P0291">“Mesele vampirse tek başına dolaşmışsın ya da on kişi kol kola gezmişsin ne fark eder ki? Her türlü pestilini çıkarır.”</p>

<p id="P0292">“O da doğru tabii,” diyerek kıkırdadı Hanekawa.</p>

<p id="P0293">Pek şen şakrak bir gülüşü vardı.</p>

<p id="P0294">…Bilemiyorum, kafamdaki imajla pek uyuşmuyordu.</p>

<p id="P0295">Deminden beri içimde bir tezat duygusu vardı.</p>

<p id="P0296">Örnek öğrenci, mümessillerin mümessili falan deyince burnundan kıl aldırmayan kibirli bir tip bekliyordum doğrusu.</p>

<p id="P0297">Oysa kız acayip cana yakındı.</p>

<p id="P0298">“Ama epeyce görgü tanığı varmış.”</p>

<p id="P0299">“Görgü tanığı mı? İlginç. O zaman çağır bakalım şu meşhur Kin-san’ı da dinleyelim!”<a id="nr-20" href="notes.xhtml#note-20" epub:type="noteref" class="noteref"><sup>[20]</sup></a></p>

<p id="P0300">“Yok canım, Kin-san falan değil mevzu.”</p>

<p id="P0301">Kızlar arasında, diye ekledi Hanekawa.</p>

<p id="P0302">“Sadece bizim okulun kızları değil — bu civardaki liselere giden kızların dilinde dolaşan meşhur bir laf. Daha doğrusu sadece kızlar arasında yayılan bir efsane.”</p>

<p id="P0303">“Yalnızca kızların bildiği efsaneler… Bir yerlerden tanıdık geliyor ama.”</p>

<p id="P0304">Yine de vampir meselesi…</p>

<p id="P0305">Nasıl kök salmıştı acaba böyle bir dedikodu?</p>

<p id="P0306">“Sapsarı saçlı, fevkalade güzel bir kadınmış… Ve insanın iliklerini donduracak kadar buz gibi bakan bir vampirmiş.”<a id="nr-21" href="notes.xhtml#note-21" epub:type="noteref" class="noteref"><sup>[21]</sup></a></p>

<p id="P0307">“Detaylar pek bir somutmuş maşallah. Ama sırf bunlardan vampir olduğu nereden çıkmış ki? Sarı saçlı diye göze batan alelade bir turist olmasın sakın?”</p>

<p id="P0308">Burası nihayetinde kırsalın göbeğinde ücra bir kasabaydı.</p>

<p id="P0309">Taşranın en dış çeperi.</p>

<p id="P0310">Saçını kumrala boyatmış birini bile zor görürdünüz.</p>

<p id="P0311">“Fakat,” dedi Hanekawa.</p>

<p id="P0312">“Sokak lambasının ışığı altında sarı saçları göz kamaştıracak kadar parıldarken… hiç gölgesi yokmuş.”<a id="nr-22" href="notes.xhtml#note-22" epub:type="noteref" class="noteref"><sup>[22]</sup></a></p>

<p id="P0313">“Hadi ya…”</p>

<p id="P0314">Vampir.</p>

<p id="P0315">Sıkça duyulan, günümüzde artık bayatlamış bir kelimeydi gerçi ve ben de öyle allamesi sayılmazdım. Gelgelelim bunu ben de bir yerlerde duymuştum — vampirlerin gölgesi olmazdı.</p>

<p id="P0316">Güneş ışığından nefret ettikleri için miydi neydi?</p>

<p id="P0317">Yine de gece vakti sonuçta.</p>

<p id="P0318">Sokak lambasının aydınlattığı bir yerde göz yanılması olması pek muhtemeldi — zaten sokak lambası dekoru bile başlı başına ucuz bir korku filmi klişesi değil miydi?</p>

<p id="P0319">Yalan kokan, düpedüz ucuz bir numara.</p>

<p id="P0320">“Haklısın,” dedi Hanekawa, kabalık kokan bu sözlerime hiç gocunmadan hak verircesine.</p>

<p id="P0321">Hem konuşmayı hem dinlemeyi iyi beceriyordu.</p>

<p id="P0322">“Bence de son derece ahmakça bir dedikodu. Yine de bu söylenti sayesinde kızların geceleri tek başına tekinsiz sokaklara çıkmaması asayiş açısından gayet faydalı bir şey, değil mi?”</p>

<p id="P0323">“Orası öyle tabii.”</p>

<p id="P0324">“Ama ben…”</p>

<p id="P0325">Ses tonunu hafifçe düşürdü Hanekawa.</p>

<p id="P0326">“Sahiden bir vampir varsa onunla bizzat tanışmak isterdim.”</p>

<p id="P0327">“…Neden ki?”</p>

<p id="P0328">Galiba…</p>

<p id="P0329">Tahminimde fena halde yanılmıştım.</p>

<p id="P0330">Sırf donunu gördüğüm anıyı sildirmek için böylesi boş bir laklaka giriştiğini sanmıştım; fakat buna rağmen Hanekawa’nın sesindeki o tuhaf ciddiyet fazla sahiciydi.</p>

<p id="P0331">Zaten 'yalnızca kızların bildiği bir efsaneyi' kapkara okul üniforması içindeki bir erkek talebeye anlatması da başlı başına garipti.</p>

<p id="P0332">“Kanını emip seni gebertirler yahu?”</p>

<p id="P0333">“Öldürülmek istemem elbet. Haklısın, tanışmak doğru kelime olmadı belki de. Ama işte… insan türünün fevkinde, insanüstü bir varlığın mevcudiyetini bilmek iyi gelirdi sanki.”</p>

<p id="P0334">“İnsanüstü derken? Tanrı gibi bir şey mi?”</p>

<p id="P0335">“İllaki tanrı olması şart değil.”</p>

<p id="P0336">Hanekawa kelimelerini tartarcasına bir müddet sustu; fakat çok geçmeden,</p>

<p id="P0337">“Yoksa bunca şeyin bir karşılığı olmaz, değil mi?” dedi.<a id="nr-23" href="notes.xhtml#note-23" epub:type="noteref" class="noteref"><sup>[23]</sup></a></p>

<p id="P0338">Farkında bile değildik.</p>

<p id="P0339">Trafik ışığı çoktan yeşile dönmüştü.</p>

<p id="P0340">Fakat ne ben ne de Hanekawa kımıldadık.</p>

<p id="P0341">Açık konuşmak gerekirse…</p>

<p id="P0342">Hanekawa’nın ne dediğini bir kenara bırakın, ne demek istediğini dahi zerre anlayamamıştım — lafları arasında mantıksal hiçbir bağ yok gibiydi.</p>

<p id="P0343">“Aman, olmaz böyle!”</p>

<p id="P0344">Yüzümdeki o şaşkın ifadeyi fark etmiş olacak ki telaşla lafı değiştirdi:</p>

<p id="P0345">“Araragi-kun meğer ne kadar da tatlı dilli, konuşması rahat biriymişsin sen. Çenem düştü de saçma sapan şeyler geveledim galiba.”</p>

<p id="P0346">“Ş-Şey… Yok canım, mühim değil.”</p>

<p id="P0347">“Böyle cana yakın bir Araragi-kun’un hiç arkadaşının olmaması çok acayip ama. Neden hiç arkadaş edinmiyorsun ki?”</p>

<p id="P0348">Gayet dobra bir soruydu.</p>

<p id="P0349">Muhtemelen zerre art niyeti yoktu.</p>

<p id="P0350">Bu kadarını kestirebiliyordum.</p>

<p id="P0351">‘Edinmiyorum değil, edinemiyorum’ diye acizliğimi itiraf etmek de gururuma dokundu.</p>

<p id="P0352">Bu yüzden —o an ağzımdan şu meşhur laf döküldü işte:</p>

<p id="P0353">“Çünkü arkadaş edinirsen insanlık mukavemetin düşer.”</p>

<p id="P0354">“…Efendim?”</p>

<p id="P0355">Hanekawa buna karşılık boş gözlerle yüzüme baka kaldı.</p>

<p id="P0356">“Kusura bakma, tam anlayamadım?”</p>

<p id="P0357">“Şey… Yani, nasıl desem…”</p>

<p id="P0358">Hapı yutmuştum.</p>

<p id="P0359">Fiyakalı bir aforizma patlatmıştım patlatmasına da, arkasını getiremiyordum.</p>

<p id="P0360">“Yani diyorum ki, bir arkadaşın olduğunda sürekli onu dert edinmek zorundasın, değil mi? Arkadaşın incinse senin de canın yanar; o kederlense sen de kahrolursun. Bir nevi zaafların çoğalır. Bu da insan olarak zayıflamak demektir.”</p>

<p id="P0361">“…Ama arkadaşın mutlu olursa sen de mutlu olursun; o neşelenirse sen de neşelenirsin. Mutlak bir zayıflama sayılmaz ki bu? Zaafın arttığı gibi kazancın da artıyor neticede.”</p>

<p id="P0362">“Yok,” diyerek başımı iki yana salladım.</p>

<p id="P0363">“Arkadaşım eğlense ona gıpta ederim; o mutlu olsa kıskançlıktan çatlardım.”</p>

<p id="P0364">“…Karakterin cüceymiş meğer.”</p>

<p id="P0365">Lafı gediğine koyuverdi Hanekawa.</p>

<p id="P0366">Sana ne be kardeşim.</p>

<p id="P0367">“Senin dediğin doğru olsa bile kâr-zarar sıfırlanıyor demektir; ha varmış ha yokmuş aynı kapıya çıkar. Üstelik şu fani dünyada dertler sevinçlerden fersah fersah fazla olduğuna göre — neticede her halükarda eksiye düşersin!”</p>

<p id="P0368">“Ne kadar da çarpık bir zihniyet…”</p>

<p id="P0369">Konuşması rahat biri olduğunu söylemiştim ya, geri alıyorum.</p>

<p id="P0370">Böyle dedi Hanekawa.</p>

<p id="P0371">Fazlasıyla kısa ömürlü bir övgü olmuştu — neyse, sağlık olsun.</p>

<p id="P0372">Böylesi yanlış anlamaların erkenden çözülmesi evladır her zaman.</p>

<p id="P0373">“Ben aslında… bitki olmak isterdim,” dedim.</p>

<p id="P0374">“Bitki mi?”<a id="nr-24" href="notes.xhtml#note-24" epub:type="noteref" class="noteref"><sup>[24]</sup></a></p>

<p id="P0375">“Konuşmak zorunda kalmazsın en azından. Yürümek falan da gerekmez.”</p>

<p id="P0376">“Hımm…”</p>

<p id="P0377">Hanekawa yine de başıyla onayladı beni.</p>

<p id="P0378">“Ama yine de canlı kalmak istiyorsun yani?”</p>

<p id="P0379">“Efendim?”</p>

<p id="P0380">“Böyle durumlarda insanlar genelde cansız bir nesne olmak isterler ya hani; taş gibi, demir gibi.”</p>

<p id="P0381">Hiç beklemediğim bir yerden vurulmuş gibi hissettim.</p>

<p id="P0382">Bitki olmak istediğim ta ezelden beri içimden geçirdiğim samimi bir temenniydi; fakat böyle felsefi bir istikametten itiraz geleceği aklımın ucundan geçmemişti.</p>

<p id="P0383">Vay be.</p>

<p id="P0384">Doğru söze ne denir — cansız nesne ha?</p>

<p id="P0385">Hakikaten bitkiler de nihayetinde canlıydı.</p>

<p id="P0386">“Ben şimdi kütüphaneye uğrayayım diyordum,” dedi Hanekawa birden.</p>

<p id="P0387">“Hı?”</p>

<p id="P0388">“Araragi-kun ile konuşurken canım acayip kütüphaneye gitmek istedi birden.”</p>

<p id="P0389">“…………”</p>

<p id="P0390">Nasıl bir kafa yapısıydı bu böyle?</p>

<p id="P0391">Gerçi eve döneceğini söylerken belirli bir programı da yoktu anlaşılan. İkimizin de bolca vakti vardı gerçi; ama o vakti öldürmek için okul etrafında fırdolayı dönmek nire, kütüphaneye koşmak nire…</p>

<p id="P0392">Tembel teneke ile örnek öğrenciyi ayıran kalın duvar tam da buydu herhalde.</p>

<p id="P0393">“Yarın pazar olduğu için kütüphane kapalı, o yüzden bugün halletmem lazım.”</p>

<p id="P0394">“Hımm, anladım.”</p>

<p id="P0395">“Araragi-kun, sen de gelsene benimle?”</p>

<p id="P0396">“Ne işim var benim orada?” Acı acı gülümsedim.</p>

<p id="P0397">Kütüphane…</p>

<p id="P0398">Bu kasabada kütüphane denen bir müessesenin varlığından bile bihaberdim.</p>

<p id="P0399">“Kütüphanede ne yapılır ki?”</p>

<p id="P0400">“Ders çalışılır herhalde!”</p>

<p id="P0401">“Herhalde mi…”</p>

<p id="P0402">Bu kez ben geri adım attım.</p>

<p id="P0403">“Kusura bakma ama, ödevin dahi verilmediği şu mübarek bahar tatilinde kendi ayağımla gidip gönüllü ders çalışacak kadar kafayı yemedim henüz.”</p>

<p id="P0404">“Ama seneye üniversite sınavına gireceğiz?”</p>

<p id="P0405">“Sınavı falan geç… Ben mezun olup olamayacağımdan bile şüpheliyim. Bu saatten sonra ne yapsam nafile. Yeni dönemde derslere geç kalmamaya çalışayım, yeter bana.”</p>

<p id="P0406">“…Hımm, öyle mi?”</p>

<p id="P0407">Hanekawa nedense hevesi kırılmış gibi mırıldandı.</p>

<p id="P0408">Benimle gelmeye can attığı da yoktu gerçi.</p>

<p id="P0409">Fakat üzerine başka bir laf etmedi.</p>

<p id="P0410">Tuhaf kızdı vesselam.</p>

<p id="P0411">Burnu havada kibirli bir tip değildi belki ama sahiden de gizemliydi.</p>

<p id="P0412">Trafik ışığı kırmızı ile yeşil arasında gidip geliyordu.</p>

<p id="P0413">Şu an kırmızıydı.</p>

<p id="P0414">Bir sonraki yeşilde yollarımızı ayırmak en temizi olacaktı — ayrılmak için bundan daha münasip bir an bulunamazdı.</p>

<p id="P0415">Hanekawa da öyle düşünüyordur muhakkak.</p>

<p id="P0416">Halden anlamayacak kadar anlayışsız bir kız değildi herhalde.</p>

<p id="P0417">“Araragi-kun. Cep telefonun var mı?”</p>

<p id="P0418">“Var tabii, o kadar da değil.”</p>

<p id="P0419">“Versene bir baksam?”</p>

<p id="P0420">Elini uzattı.</p>

<p id="P0421">Niyetini kestiremesem de dediğini ikiletmeyip cebimden telefonu çıkarıp Hanekawa’nın avucuna bıraktım.</p>

<p id="P0422">“A, yeni modelmiş.”</p>

<p id="P0423">“Geçen gün değiştirdim. İki yıl aradan sonra yenileyince envaiçeşit karmaşık özellik eklemişler; elimde kaldı alet, kullanamıyorum.”</p>

<p id="P0424">“Gencecik çocuksun, böyle aciz konuşma lütfen! Şimdiden böyleysen büyüyünce medeniyetin fersah fersah gerisinde kalırsın valla. Devir dijital devri; teknolojiden anlamazsan günlük hayatını bile idame ettiremezsin.”</p>

<p id="P0425">“Öyle bir şey olursa dağa çıkarım ben de. Medeniyet helak olup çöktüğü vakit bu kasabaya muzaffer bir şekilde geri dönerim.”</p>

<p id="P0426">“Kaç yaşına kadar yaşamayı planlıyorsun acaba?”</p>

<p id="P0427">“Ölümsüz müsün nesin sen?” diyerek bıkkınlıkla söylendi Hanekawa.<a id="nr-25" href="notes.xhtml#note-25" epub:type="noteref" class="noteref"><sup>[25]</sup></a></p>

<p id="P0428">Ve der demez telefonda tuşlara basmaya koyuldu.</p>

<p id="P0429">Mümessillerin mümessili, kurallar abidesi bir hanımefendi olsa da nihayetinde liseli bir genç kızdı; parmakları klavyede şimşek gibi dans ediyordu.</p>

<p id="P0430">Öyle gizlim saklım bir hususi bilgim yoktu gerçi ama… Elin telefonunu böyle çat diye kurcalamak da neyin nesiydi?</p>

<p id="P0431">Yoksa… eteği havalandığında gizlice kamerayla fotoğrafını çektiğimden falan mı şüpheleniyordu?</p>

<p id="P0432">Öyleyse tepe tepe arasındı valla.</p>

<p id="P0433">Böylesi yüz kızartıcı bir töhmetten aklanmayı canıgönülden isterdim.</p>

<p id="P0434">Yahu bu kız milleti de her şeyi ne kadar büyütüyor! Erkek milleti olsa pantolonun fermuarı açık kalsa bile ‘seksi komando taktiği uyguluyorum’ der işin içinden sıyrılıverirdi.<a id="nr-26" href="notes.xhtml#note-26" epub:type="noteref" class="noteref"><sup>[26]</sup></a></p>

<p id="P0435">…Sıyrılabilir miydi sahiden?</p>

<p id="P0436">“Teşekkür ederim, buyur al.”</p>

<p id="P0437">Çok geçmeden telefonu elime geri tutuşturdu Hanekawa.</p>

<p id="P0438">“Öyle bir fotoğraf bulamadın, değil mi?” dedim diklenerek.</p>

<p id="P0439">Hanekawa,</p>

<p id="P0440">“Ha?” diyerek başını eğdi.</p>

<p id="P0441">“Fotoğraf derken?”</p>

<p id="P0442">“…Yok bir şey.”</p>

<p id="P0443">Hoppala.</p>

<p id="P0444">Fena halde yanılmıştım yine.</p>

<p id="P0445">Peki ne yapmıştı o zaman?</p>

<p id="P0446">Yüzümdeki şaşkınlığı okumuş olacak ki, elimde tuttuğum ama cebime koymaya fırsat bulamadığım telefonu parmağıyla işaret ederek konuştu:</p>

<p id="P0447">“Kendi numaramı ve e-posta adresimi kaydettim.”</p>

<p id="P0448">“Anlamadım?”</p>

<p id="P0449">“Tüh, çok yazık! Galiba bir arkadaş edindin Araragi-kun.”<a id="nr-27" href="notes.xhtml#note-27" epub:type="noteref" class="noteref"><sup>[27]</sup></a></p>

<p id="P0450">Ve…</p>

<p id="P0451">Tek kelime dahi etmeme fırsat tanımadan, yaya geçidinden koşa koşa karşıya geçti — ışık çoktan yeşile dönmüştü meğer.</p>

<p id="P0452">Tam da böyle bir ayrılık planlayan bendim; gelgelelim inisiyatifi benden önce kapıvermişti — Bir dakika ya? Hani kütüphaneye gidecekti bu kız? Gerçi benimle konuşurken karar verdiğine göre başlangıçtaki rotanın tersine dönmesinde şaşılacak bir şey yoktu.</p>

<p id="P0453">Karşı kaldırıma geçince arkasını dönüp “Görüşürüz!” diyerek el salladı Hanekawa.</p>

<p id="P0454">Refleks icabı ben de elimi kaldırıverdim.</p>

<p id="P0455">(Muhtemelen eblehçe) el salladığımı görünce Hanekawa topuklarının üzerinde dönüp okul kapısının hemen önünden sağa kıvrıldı ve gayet neşeli adımlarla yürüyüp gitti — köşeyi dönünce silueti tamamen kayboldu.</p>

<p id="P0456">Gittiğinden emin olduktan sonra elimdeki cep telefonuna baktım.</p>

<p id="P0457">Sahiden de…</p>

<p id="P0458">Rehberde ‘Hanekawa Tsubasa’ yazıyordu.</p>

<p id="P0459">Telefon numarası, e-posta adresi.</p>

<p id="P0460">Rehber fonksiyonunu şimdiye kadar hiç kullanmamıştım. İhtiyacım olan numaraların hepsi aklımdaydı — gerçi bunu hafızam kuvvetli diye övünmek için söylemiyorum. Hatırladığım numaralar alt tarafı ev telefonu ile anamın babamın cep telefonundan ibaretti; övünülecek bir tarafı yoktu yani. Kalan her şey için gelen-giden arama kayıtları fazlasıyla yetiyordu.</p>

<p id="P0461">Basbayağı arkadaşım yoktu işte.</p>

<p id="P0462">Bu yüzden…</p>

<p id="P0463">Bu ‘Hanekawa Tsubasa’, şu telefona kaydedilen ilk telefon numarası oluvermişti.</p>

<p id="P0464">“Ne ayaktı bu kız şimdi…?”</p>

<p id="P0465">Yaptığı hareketler kavrayışımın fersah fersah ötesindeydi.</p>

<p id="P0466">Arkadaş mı?</p>

<p id="P0467">Arkadaş olduk öyle mi?</p>

<p id="P0468">Ciddi miydi bu kız?</p>

<p id="P0469">Zaten adını gıyaben bilsem de ilk defa konuştuğum bir erkek olarak, genç bir kızın böylesine pat diye numarasını vermesi ne derece münasipti — yoksa benim kafa yapım mı fazla antika kalmıştı?</p>

<p id="P0470">Bilemiyorum.</p>

<p id="P0471">Fakat —hiçbir şeyi anlamasam da anladığım tek bir hakikat vardı:</p>

<p id="P0472">Hanekawa Tsubasa.</p>

<p id="P0473">Örnek öğrencilerin şahı — mümessillerin mümessili.</p>

<p id="P0474">Burnu havada kibirli bir tip olmak şöyle dursun…</p>

<p id="P0475">“…Acayip iyi bir kızmış yahu.”</p>

<p id="P0476">Mümessillerin mümessili.</p>

<p id="P0477">Hanekawa Tsubasa.</p>

<p id="P0478">Kapanış töreninin o ılık öğleden sonrasında bu şekilde teğet geçtiğim o kızla, bundan kısa bir süre sonra —bahar tatilinin tam göbeğinde— tekrar karşılaşacaktım; lakin o an bunu tahmin etmeme zerre imkân yoktu.</p>

<p id="P0479">İçimde en ufak bir önsezi bile…</p>

<p id="P0480">Zerre uyanmamıştı.</p>

</section>
</body>
</html>
"""

with open(f"{BASE_DIR}/EPUB/text/chapter1.xhtml", "w", encoding="utf-8") as f:
    f.write(ch1_html)

# ==========================================
# 2. NOTES (notes.xhtml)
# ==========================================

notes_html = """<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="tr">
<head>
<meta charset="utf-8"/>
<title>Çevirmen Notları</title>
<link rel="stylesheet" type="text/css" href="../styles/main.css"/>
</head>
<body>
<section id="notes">
<h1>Çevirmen Notları</h1>
<p class="note-intro">Bu notlar, Nisio Isin'in Kizumonogatari eserinde yer alan kelime oyunlarını, Japon kültürel referanslarını, deyimleri ve Alpha Çeviri Ekibi'nin yerelleştirme tercihlerini açıklamaktadır. Metindeki yerine dönmek için her notun sonundaki simgeye (↩) tıklayabilirsiniz.</p>

<ol class="notes-list">
<li id="note-1"><span class="note-num">1.</span> <b>Kiss-shot Acerola-orion Heart-under-blade:</b> Nisio Isin’in eser boyunca kurduğu en zekice kelime oyunlarından biridir. Yazar, karakterin adındaki <b>"Heart-under-blade"</b> (Kılıcın/Bıçağın Altındaki Kalp) unvanını doğrudan Japonca <b>忍 (Shinobu)</b> kanjisinden türetmiştir. Bu kanji yapısal olarak üstte <b>刃 (kılıç/bıçak - yaiba)</b> ve altta <b>心 (kalp - kokoro)</b> sembollerinin birleşimiyle yazılır. Yani "kalbin üstündeki bıçak" veya "bıçağın altındaki kalp" birebir <i>Shinobu</i> demektir. Serinin devamında Oshino Meme’nin karaktere “Shinobu Oshino” adını vermesi bu kelime oyununa dayanır. <a href="chapter1.xhtml#P0002" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-2"><span class="note-num">2.</span> <b>春休みの狭間 (Bahar Tatili Arafı / Dar Boğazı):</b> Japonya’da akademik takvim Batı ve Türk eğitim sisteminden farklı olarak Nisan başında başlar ve Mart sonunda biter. Dolayısıyla lise 2’den lise 3’e geçiş, 25 Mart - 7 Nisan arasındaki iki haftalık bahar tatiline (春休み - <i>haruyasumi</i>) denk gelir. Bu dönem öğrencinin ne 2. ne de tam olarak 3. sınıf sayıldığı, statüsüz bir “araftır” (<i>hazama</i> - iki sınır arasındaki dar aralık/boşluk). <a href="chapter1.xhtml#P0002" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-3"><span class="note-num">3.</span> <b>運が悪かった (Feleğin Çemberi / Baht Kötülüğü):</b> Motamot karşılığı "şansım kötüydü" şeklindedir. Ancak metindeki kaderci ve kendini suçlayan havayı Türkçede daha güçlü hissettirmek adına <i>"feleğin çemberinden payıma düşen kör talihimdi"</i> ve <i>"şanssızlık"</i> karşıtlığıyla yerelleştirilmiştir. <a href="chapter1.xhtml#P0002" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-4"><span class="note-num">4.</span> <b>外連味 (Kerenmi - Laf Cambazlığı / Ucuz Numara):</b> Geleneksel Kabuki tiyatrosundan türeyen bu terim; sırf seyirciyi şaşırtmak, ucuz alkış toplamak veya gösteriş yapmak amacıyla sahnelenen yapay numaralar ve söz cambazlıkları anlamına gelir. Araragi burada felsefe yaparken ucuz bir lafebeliği veya retorik numarası yapmadığını, samimi olduğunu vurgular. <a href="chapter1.xhtml#P0004" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-5"><span class="note-num">5.</span> <b>散々に掘り尽くされた鉱脈 (Maden Eğretilemesi):</b> Kelimesi kelimesine <i>"tükenene kadar kazılmış bir maden damarı"</i>. Popüler kültürde vampir temasının aşırı tüketilmişliğini anlatmak için Türkçedeki <i>"posası çıkarılmış / iliğine kadar sömürülmüş bir maden ocağı"</i> deyimiyle harmanlanmıştır. <a href="chapter1.xhtml#P0013" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-6"><span class="note-num">6.</span> <b>間が抜けている (Zamanlama &amp; Ahmaklık Nüktesi):</b> Japoncadaki <i>ma</i> (間) kelimesi zamanlama, durak, ritim ve boşluk demektir. <i>Ma ga nukete iru</i> ise "zamanlaması/ritmi şaşmış, basireti bağlanmış, ayarsız" anlamına gelir ve hemen ardındaki <i>manuke</i> (間抜け - ahmak, budala) sözcüğüne kök bağlar. Bu sözcük bağı metinde "basiretsizlik" ve "katıksız bir ahmaklık" geçişiyle korunmuştur. <a href="chapter1.xhtml#P0016" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-7"><span class="note-num">7.</span> <b>怪異 (Kaii - Musibet), 化物 (Bakemono - Hortlak), 人外者 (Jingaimono - İnsan Dışı):</b> Monogatari evreninin temel kavramı olan <i>Kaii</i>, genellikle İngilizceye "oddity / aberration" olarak çevrilir. Türkçede doğaüstü musibet, tekinsiz dert ve tekinsiz gariplik anlamını karşılamak üzere <i>"musibet"</i> kelimesi tercih edilmiştir. <a href="chapter1.xhtml#P0024" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-8"><span class="note-num">8.</span> <b>傷物語 (Kizumonogatari - Çift Yönlü Yara İtirafı):</b> Kitabın başlığı olan <i>Kizu</i> (傷 - yara/kusur) ve <i>Monogatari</i> (物語 - hikâye), Araragi’nin ağzından iki yönlü bir itirafla çözümlenir: "彼女から受けた傷の物語を。僕が彼女を傷つけた物語を。" Yani Kizumonogatari sadece Araragi'nin aldığı yaraların değil, aynı zamanda o kadına açtığı yaraların da hikâyesidir. <a href="chapter1.xhtml#P0032" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-9"><span class="note-num">9.</span> <b>道化 (Douke - Soytarı / Pandomimci):</b> Araragi’nin kendini değersizleştirme ve alaycı özeleştiri tonunun bir yansımasıdır. Kendisini büyük laflar eden ama sahnedeki beceriksiz bir soytarıdan farkı olmayan biri olarak nitelemektedir. <a href="chapter1.xhtml#P0037" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-10"><span class="note-num">10.</span> <b>坂道を転がる石 (Yokuş Aşağı Yuvarlanan Taş):</b> Durdurulamaz bir sürecin başladığını ifade eden bilinen bir Japon deyimi (坂道を転がる石のように). Türkçede "yokuş aşağı yuvarlanan bir kaya gibi" tabiriyle pürüzsüzleştirilmiştir. <a href="chapter1.xhtml#P0038" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-11"><span class="note-num">11.</span> <b>バッドエンド (Bad End / Hezimet):</b> Hafif roman ve görsel roman kültüründeki doğrudan ödünçleme ifadedir. Edebi ağırlığı korumak adına hem "hezimet" hem de "herkesin bedbaht olması" vurgusuyla zenginleştirilmiştir. <a href="chapter1.xhtml#P0039" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-12"><span class="note-num">12.</span> <b>人間強度 (Ningen Kyoudo - İnsanlık Mukavemeti):</b> Araragi'nin nihilist dünya görüşünün omurgası. <i>Kyoudo</i> (強度) kelimesi malzeme biliminde ve mühendislikte metallerin çekme, kırılma veya eğilme mukavemetini ifade eder. Araragi bu terimi insan ruhunun direncini tanımlamak için kullanarak kendine has bir felsefi aforizma üretmiştir. <a href="chapter1.xhtml#P0043" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-13"><span class="note-num">13.</span> <b>怪物みたいな大型ルーキー (Canavar Dev Çaylak):</b> Kız basketbol takımına yeni katılan bu meşhur çaylak, serinin ilk kitabı Bakemonogatari'de tanıştığımız <b>Kanbaru Suruga</b>'dan başkası değildir (Suruga Maymunu bölümü). <a href="chapter1.xhtml#P0060" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-14"><span class="note-num">14.</span> <b>羽川翼 (Hanekawa Tsubasa İsim İması):</b> Hanekawa'nın adındaki <i>Hane</i> (羽 - kanat/tüy) ve <i>Tsubasa</i> (翼 - kanat) kelimeleri baştan aşağı kanat ve uçma motifleriyle bezelidir. Bu durum daha sonraki Nekomonogatari ve Tsubasa Tiger bölümlerinde onun özgürleşme arzusunun sembolüne dönüşür. <a href="chapter1.xhtml#P0062" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-15"><span class="note-num">15.</span> <b>委員長の中の委員長 (Mümessillerin Mümessili):</b> Hanekawa'nın aşırı mükemmeliyetçi, kuralcı, okul tüzüğüne milimetrik uyan imajını vurgulayan Nisio Isin'e has pekiştirme kalıbı. <a href="chapter1.xhtml#P0071" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-16"><span class="note-num">16.</span> <b>あっという間に・いっという間に (Fonetik Söz Oyunu):</b> Japoncada "あっという間" (a-tto iu ma), bir 'a' sesi çıkarmaya kalmadan, yani 'göz açıp kapayıncaya kadar' demektir. Nisio Isin Japon alfabesinin (a-i-u-e-o) ikinci harfini kullanarak "いっという間に" (i-tto iu ma - bir 'i' demeye kalmadan) şeklinde kendi şaka kalıbını türetmiştir. Türkçeye "bir 'ah' demeden dökülen, bir 'of' demeden sefilleşen" şeklinde adapte edilmiştir. <a href="chapter1.xhtml#P0077" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-17"><span class="note-num">17.</span> <b>四ページに亘って描写 (Dördüncü Duvarın Kırılması):</b> Nisio Isin’in meşhur üstkurmaca (meta-fiction) tekniğidir. Karakter, okurun elinde tuttuğu kitabın sayfa sayısından haberdardır ve eteğin açılma sahnesinin sahiden de romanda yaklaşık dört sayfa sürdüğünü yüzsüzce itiraf eder. <a href="chapter1.xhtml#P0182" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-18"><span class="note-num">18.</span> <b>阿良々木 暦 (Araragi Koyomi Kanji Çözümlemesi):</b> Hanekawa'nın ezberden yaptığı ayrım: Solunda tepecik radikali olan 阝 (kozatohen) + 可 (ka) = 阿; ardından 良 (iyi) karakteri ve tekrar işareti 々 (yoi-yoi); ve 木 (ki - ağaç). Adı olan Koyomi (暦) ise doğrudan yıl-ay takvimi demektir. <a href="chapter1.xhtml#P0219" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-19"><span class="note-num">19.</span> <b>デスノート (Death Note):</b> Tsugumi Ohba ve Takeshi Obata'nın efsanevi manga serisine doğrudan popüler kültür göndermesidir. Ölüm Defteri kuralı uyarınca kurbanın yüzünü ve gerçek adını bilmek onu öldürmek için yeterlidir. <a href="chapter1.xhtml#P0223" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-20"><span class="note-num">20.</span> <b>遠山の金さん (Touyama no Kinsan Nüktesi):</b> Klasik Japon tarihi polisiye dizisi kahramanı yargıç Toyama no Kinshiro (Kin-san). Görgü tanıklarını mahkemede sorgulamasıyla ünlüdür. Araragi "tanık ifadesi" (mokugeki shougen) lafını duyunca sanki Kin-san mahkemesindeymiş gibi şaka yapar. <a href="chapter1.xhtml#P0299" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-21"><span class="note-num">21.</span> <b>金髪のすごく綺麗な女の人 (Sarışın Güzel Kadın):</b> Kasabada dolaşan dedikodudaki bu kadın, eserin ana figürü olan Kiss-shot Acerola-orion Heart-under-blade'dir. <a href="chapter1.xhtml#P0306" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-22"><span class="note-num">22.</span> <b>影がなかった (Gölgesi Olmayan Vampir):</b> Klasik vampir folklöründe aynada yansımama ve gölge düşürmeme inanışlarına Nisio Isin'in getirdiği modern şehir efsanesi yorumu. <a href="chapter1.xhtml#P0312" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-23"><span class="note-num">23.</span> <b>でないと、報われないじゃない (Karşılık Bulamamak):</b> Hanekawa'nın ailevi travmalarına, evde gördüğü duygusal baskıya ve mükemmeliyetçi maskesinin altında sakladığı derin yaralara ilk ipucudur. Kendisine acı çektiren dünyadan daha yüce bir varlık görme arzusu bu travmadan beslenir. <a href="chapter1.xhtml#P0337" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-24"><span class="note-num">24.</span> <b>植物になりたい (Bitki Olma Arzusu):</b> Araragi'nin insan ilişkilerinden kaçış ve pasif varoluş özlemi. Hanekawa'nın "taş veya demir gibi cansız bir nesne yerine yine de bir canlı olmayı seçiyorsun" tespiti aralarındaki zihinsel farkı ortaya koyar. <a href="chapter1.xhtml#P0374" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-25"><span class="note-num">25.</span> <b>不死身ですか (Ölümsüz Müsün Sen?):</b> Müthiş bir önsezi ve kehanet (foreshadowing). Araragi bu konuşmadan yalnızca saatler sonra Kiss-shot ile karşılaşacak ve gerçekten de yarı-ölümsüz bir vampire dönüşecektir. <a href="chapter1.xhtml#P0427" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-26"><span class="note-num">26.</span> <b>セクシーコマンドー (Seksi Komando):</b> Kyosuke Usuta'nın ünlü absürt mizah mangası <i>Sexy Commando Gaiden: Sugoi yo!! Masaru-san</i>'a gönderme. Ana karakter Masaru fermuar açıp rakibin dikkatini dağıtarak dövüşmektedir. <a href="chapter1.xhtml#P0434" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-27"><span class="note-num">27.</span> <b>ざーんねん。友達、できちゃったね (Arkadaş Edindik İşte):</b> Hanekawa'nın Araragi'nin kendini soyutladığı "insanlık mukavemeti" kalesini tek bir hamlede, sıcak bir tebessümle yerle bir ettiği kırılma anı. <a href="chapter1.xhtml#P0449" class="backref" aria-label="Metindeki yere dön">↩</a></li>
</ol>
</section>
</body>
</html>
"""

with open(f"{BASE_DIR}/EPUB/text/notes.xhtml", "w", encoding="utf-8") as f:
    f.write(notes_html)

# ==========================================
# 3. İÇİNDEKİLER (icerindekiler.xhtml)
# ==========================================

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

# ==========================================
# 4. NAV.XHTML
# ==========================================

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

# ==========================================
# 5. TOC.NCX
# ==========================================

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
</navPoint>
<navPoint id="np-5" playOrder="5">
<navLabel><text>Çevirmen Notları</text></navLabel>
<content src="text/notes.xhtml"/>
</navPoint>
</navMap>
</ncx>
"""

with open(f"{BASE_DIR}/EPUB/toc.ncx", "w", encoding="utf-8") as f:
    f.write(ncx_html)

# ==========================================
# 6. CONTENT.OPF
# ==========================================

now_iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

opf_html = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="tr">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:title id="title">Kizumonogatari — Türkçe Çeviri</dc:title>
<dc:creator id="author">西尾維新 (Nisio Isin)</dc:creator>
<dc:contributor>VOFAN (çizim)</dc:contributor>
<dc:contributor>Alpha Çeviri Ekibi (Türkçe yerelleştirme ve çevirmen notları)</dc:contributor>
<dc:language>tr</dc:language>
<dc:identifier id="bookid">urn:uuid:e8b61c8a-7c91-4e08-9a3c-5528eb1e9678</dc:identifier>
<dc:publisher>Çeviri: Alpha Çeviri Ekibi</dc:publisher>
<dc:description>傷物語 第零話「こよみヴァンプ」 Türkçe yerelleştirilmiş edisyonu, ayrıntılı kelime oyunları ve kültürel dipnotlarla birlikte.</dc:description>
<meta refines="#title" property="title-type">main</meta>
<meta property="dcterms:modified">{now_iso}</meta>
<meta name="cover" content="cover"/>
</metadata>
<manifest>
<item id="icerindekiler" href="text/icerindekiler.xhtml" media-type="application/xhtml+xml"/>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
<item id="c1" href="text/chapter1.xhtml" media-type="application/xhtml+xml"/>
<item id="notes" href="text/notes.xhtml" media-type="application/xhtml+xml"/>
<item id="css" href="styles/main.css" media-type="text/css"/>
<item id="cover" href="cover.jpg" media-type="image/jpeg" properties="cover-image"/>
</manifest>
<spine toc="ncx">
<itemref idref="icerindekiler"/>
<itemref idref="c1"/>
<itemref idref="notes"/>
</spine>
</package>
"""

with open(f"{BASE_DIR}/EPUB/content.opf", "w", encoding="utf-8") as f:
    f.write(opf_html)

# ==========================================
# 7. EPUB PACKAGE CREATION
# ==========================================

if os.path.exists(EPUB_OUT):
    os.remove(EPUB_OUT)

with zipfile.ZipFile(EPUB_OUT, "w") as z:
    # Mimetype must be first, uncompressed
    z.write(f"{BASE_DIR}/mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)
    
    # Rest can be deflated
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

print(f"SUCCESS: EPUB created at {EPUB_OUT} ({os.path.getsize(EPUB_OUT)} bytes).")
