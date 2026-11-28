# -*- coding: utf-8 -*-
import os, zipfile, datetime

BASE_DIR = "/data/data/com.termux/files/home/monogatari-project/kizumonogatari_epub"
EPUB_OUT = "/data/data/com.termux/files/home/monogatari-project/04_Kizumonogatari_TR.epub"

# ==========================================
# SECTION 005 HTML
# ==========================================

sec5_html = """
<h3 id="P1340" class="section-no">005</h3>

<p id="P1341">Dramaturgy.</p>

<p id="P1342">Episode.</p>

<p id="P1343">Guillotinecutter.<a id="nr-56" href="notes.xhtml#note-56" epub:type="noteref" class="noteref"><sup>[56]</sup></a></p>

<p id="P1344">Kiss-shot’ın o kusursuz gövdesinden uzuvlarını parça parça koparıp çalan üç şahsın adları —anlaşılan— bunlardı.</p>

<p id="P1345">Gerçi Kiss-shot’tan bu üçlünün eşkâllerine dair tarifler dinlemiştim dinlemesine de; böyle şeyleri salt kuru lafla işitmek zihnimde pek bir şey canlandırmıyordu doğrusu.</p>

<p id="P1346">Sanki bambaşka bir lisanla anlatılıyor gibiydi; kafamdaki suretleri ziyadesiyle müphemdi. Lakin en mühim hakikat, zekâsı kıt birinin bile bir çırpıda kavrayabileceği kadar berraktı:</p>

<p id="P1347">Dramaturgy denen herif kadının sağ bacağını.</p>

<p id="P1348">Episode denen herif kadının sol bacağını.</p>

<p id="P1349">Guillotinecutter denen herif ise kadının iki kolunu birden.</p>

<p id="P1350">Koparıp — gasp etmişti.</p>

<p id="P1351">İşte o gece karşılaştığım o kadın tam da bu yüzden can çekişiyordu — can çekişmek de laf mı; benim kanımı içmemiş olsaydı Kiss-shot muhakkak ki ebediyen yok olup gidecekti.</p>

<p id="P1352">Ölümsüz bir varlık olmasına rağmen.</p>

<p id="P1353">Ölümün kıyısına yuvarlanmıştı.</p>

<p id="P1354">Bunu en iyi idrak eden de bizzat kendisiydi.</p>

<p id="P1355">O gece… ölmeyi peşinen kabullenmişti.</p>

<p id="P1356">Canını dişine takıp o üçlünün pençesinden zar zor kaçabilmişti ama bu kaçış onun son kurşunuydu besbelli.</p>

<p id="P1357">“Neden…”</p>

<p id="P1358">İzahati dinlerken gayriihtiyari lafını kestim.</p>

<p id="P1359">“Neden kollarını bacaklarını çaldılar ki?”</p>

<p id="P1360">“Ben bir vampirim! Sizin o insan milletinin —gerçi sen artık onlardan değilsin ya neyse— tabiriyle düpedüz bir canavarım ben!”</p>

<p id="P1361">Kiss-shot dünyanın en doğal şeyinden bahseder gibi konuştu:</p>

<p id="P1362">“Bir canavarın itlaf edilmesinden daha tabii ne olabilir ki?”</p>

<p id="P1363">“…………”</p>

<p id="P1364">“O üç kişi vampir avında ihtisas yapmış uzmanlardır —beni katletmeyi kendilerine meslek edinmiş cellatlardır. Vampir avcısı denen güruhun namını herhalde senin gibi bir cahil bile duymuştur?”</p>

<p id="P1365">Duymuşumdur… herhalde.</p>

<p id="P1366">Vampir mefhumuyla ayrılmaz bir ikili olarak zikredilen tiplerdi neticede.</p>

<p id="P1367">Detaylarını pek hatırlamasam da, genel kültür kırıntısı olarak kulak dolgunluğum vardı muhakkak.</p>

<p id="P1368">“Yani… seni alt ettiler öyle mi?”</p>

<p id="P1369">“Ağzından çıkanı kulağın duysun be gafil! Alt etmek de ne demekmiş; henüz defterimi dürebilmiş değiller! —Gerçi kolumu bacağımı kaptırmış olmam fena koydu tabii. Yenilenme kudretim de sıfıra indi sayılır… Bu cüce vaziyetimle savaşa tutuşmama imkân yok.”</p>

<p id="P1370">“Anladım.”</p>

<p id="P1371">“İşte bu yüzden,”</p>

<p id="P1372">Gayet pürüzsüz bir mantık silsilesiyle bağladı Kiss-shot:</p>

<p id="P1373">“Sen o üçüyle tek tek kozunu paylaşacak — ve benim uzuvlarımı tıpış tıpış geri alıp bana getireceksin!”</p>

<p id="P1374">“Efendim…?”</p>

<p id="P1375">Dona kaldım.</p>

<p id="P1376">“G-Geri getireceksin derken… Öyle bakkaldan ekmek alır gibi mi?”</p>

<p id="P1377">“Şu an sana bütün teferruatı anlatamam gerçi; lakin seni yeniden insan formuna döndürebilmem için benim tam kudretime kavuşmam şart. Yani mükemmel formuma ulaşmam icap eder. Bunun için de o kollar ve bacaklar mutlak bir zarurettir!”</p>

<p id="P1378">“İ-İyi de… Ben dövüşten falan zerre anlamam ki!”</p>

<p id="P1379">Katiyen bir kabahatim yokken suçlu bir çocuk gibi mazeret üretmeye başladım:</p>

<p id="P1380">“Sporla aram öyle pek parlak sayılmaz, cüssem de ortada işte. Ömrümde sokak kavgasına bile karışmışlığım yok benim… Hem dur bir dakika, en kötü senaryoda o adamlar beni de itlaf edip nalları diktirmez mi?”</p>

<p id="P1381">Şu anki durumumla ben de bir vampirdim ne de olsa.</p>

<p id="P1382">Böyle bir ihtimal fazlasıyla kuvvetliydi.</p>

<p id="P1383">Karşımdakiler vampir avlamayı meslek edinmiş üç azılı uzmandı ne de olsa — eskiden insan olduğumu anlayıp bana acısalar bile, binbir emekle kopardıkları o uzuvları öyle babalarının hayrına bana teslim edecek değillerdi ya!</p>

<p id="P1384">“Ahmak herif! O dediklerin insan olduğun devirlere aitti!”</p>

<p id="P1385">Kiss-shot bıkkınlıkla çıkıştı:</p>

<p id="P1386">“Sen şu an benim öz hizmetkârımsın! Sıfır noktasına kadar zayıflamış şu halimle bile beni bir kaşık suda boğmak senin için çocuk oyuncağıdır artık!”</p>

<p id="P1387">“…Nasıl yani? Şu an sen benden daha mı zayıf bir vampirsin yani?”</p>

<p id="P1388">“Tabii ki hayır be dangalak!”</p>

<p id="P1389">Yine fırçayı yedik.</p>

<p id="P1390">Hakikaten de fena halde barut fıçısı bir kızdı bu.</p>

<p id="P1391">“Lafımdan nasıl böyle ahmakça bir netice çıkardın sen? Şunu kafana sok: Ben vampir taifesinin en tepe noktasındaki kraliçeyim! Doğaüstü âlemde bana ‘Musibet Katili’ derler!”<a id="nr-57" href="notes.xhtml#note-57" epub:type="noteref" class="noteref"><sup>[57]</sup></a></p>

<p id="P1392">“Musibet Katili…”</p>

<p id="P1393">Kulağa ne kadar havalı gelse de bana pek bir şey ifade etmiyordu.</p>

<p id="P1394">Zaten musibet dediğin tam olarak neydi ki?</p>

<p id="P1395">Hortlak gibi bir şey miydi?</p>

<p id="P1396">Neyse ne.</p>

<p id="P1397">“Tamam, zayıflamış halinden şu an daha güçlü olduğumu varsaysak bile… Ama o üç herif, senin o tam güçlü, o 'mükemmel' halinden o uzuvları söküp almadı mı? E öyleyse—”</p>

<p id="P1398">“Üçü birden çullandığı için bir anlık gaflete düştüm sadece! Hepsini fazla küçümsedim — rehavete kapıldım. O ayardaki çömezleri üçü bir arada gelse bile çıtır çıtır yerim sanmıştım…”</p>

<p id="P1399">“Vay be…”</p>

<p id="P1400">“Hülasa!”</p>

<p id="P1401">Kiss-shot gururla göğsünü kabartıp fermanı bastı:</p>

<p id="P1402">“Teke tek kapıştığın müddetçe o üç sünepe senin eline su bile dökemez! Açık konuşmak gerekirse tereyağından kıl çeker gibi basit bir iştir bu! Alt tarafı bu kadarcık bir zahmetle insanlığına kavuşacaksan bedavadan biraz pahalı sayılır!”</p>

<p id="P1403">Böylesine kaba saba bir palavraya kandığımdan değildi elbet;</p>

<p id="P1404">Lakin neticede kendimi gecenin zifiri karanlığında sokakları arşınlarken buluvermiştim işte.</p>

<p id="P1405">Güneş batıp ortalık iyice karardıktan bir müddet sonraydı. Nihayet o enkazdan, o terk edilmiş dershane binasından dışarı çıkabilmiş ve nerede olduğumu tam olarak kavrayabilmiştim.</p>

<p id="P1406">O dershanenin bulunduğu mevki, yaşadığım taşra kasabasının en dış çeperinde, kuş uçmaz kervan geçmez bir köşedeydi — gerçi öyle bir noktada böylesi devasa bir harabenin bulunduğundan şimdiye kadar zerre haberim yoktu.</p>

<p id="P1407">Muhtemelen istasyon civarına açılan zincir dershanelerin rekabetine dayanamayıp kapıya kilit vurmuşlardı.</p>

<p id="P1408">Gizlenmek için fevkalade münasip bir sığınaktı doğrusu; Kiss-shot da amma keşifçi kızmış hani…</p>

<p id="P1409">Bu arada eve çoktan telefon etmiştim.</p>

<p id="P1410">Şansıma telefona ortanca kardeşim, yani büyük kız kardeşim Karen çıktı. Abilerinin bahar tatilini fırsat bilip 'öz benliğini bulma yolculuğuna' çıktığını evdekilere iletmesini tembihledim.<a id="nr-58" href="notes.xhtml#note-58" epub:type="noteref" class="noteref"><sup>[58]</sup></a></p>

<p id="P1411">Kız da hiç ikiletmeden yutmuştu numarayı.</p>

<p id="P1412">…Fakat düşününce, kız kardeşimin beni her an böyle manasız bir kendini arama yolculuğuna çıkabilecek tıynette bir lüzumsuz olarak görmesi ayrı bir hüzün vesilesiydi tabii.</p>

<p id="P1413">İnsanın gururu inciniyordu.</p>

<p id="P1414">Ve hemen ardından en küçük kız kardeşim Tsukihi’den bir e-posta damladı.</p>

<p id="P1415">Ortaokullu olduklarından henüz kendilerine ait cep telefonları yoktu; oturma odasındaki ortak masaüstü bilgisayardan döşenmişti mesajı:</p>

<p id="P1416"><em>‘Sevgili abiciğim… Bazen insanın yolunu kaybetmesi de gerekebilir elbet; lakin gün gelip de kalbinde ufacık bir ferahlık hissettiğinde lütfen hatırla: Tyltyl ile Mytyl, o Mavi Kuş’u en nihayetinde nerede bulmuşlardı sahi?’</em><a id="nr-59" href="notes.xhtml#note-59" epub:type="noteref" class="noteref"><sup>[59]</sup></a></p>

<p id="P1417">…………</p>

<p id="P1418">Ortaokullu veletten hayat dersi almıştım resmen…</p>

<p id="P1419">Böylesi felsefi bir vaazı okumak uğruna cep telefonumun bataryasını tükettiğime mi yanayım neye yanayım bilemedim.</p>

<p id="P1420">Sahi ya, şu telefonu bir yerlerde şarj etmem şarttı… Eve gidip şarj aletini alamayacağıma göre mecburen bir markete uğrayıp pilli acil şarj kitlerinden alacaktım. Zira o harabede priz falan hak getireydi.</p>

<p id="P1421">Şarj bitmeden bu hengâmeyi noktalayabilirsem ne âlâydı.</p>

<p id="P1422">“Eline su dökemezmiş peh… Sanki adamlar benim düşmanımmış gibi konuşuyor bir de! Senin düşmanın be kadın!”</p>

<p id="P1423">Yine de… sahiden o kadar basit bir iş miydi acaba?</p>

<p id="P1424">Başta pek inanasım gelmemişti gerçi; lakin yeni edindiğim vampir kuvvetimin hafife alınmayacak cinsten olduğu su götürmez bir gerçekti — bunu nasıl test ettiğimi detaylandırırsam mala zarar verme suçundan içeri tıkılabileceğim için şimdilik es geçiyorum.</p>

<p id="P1425">Yani…</p>

<p id="P1426">Madem harabeydi, birkaç duvara delik açmaktan kime ne zarar gelirdi ki?</p>

<p id="P1427">“Yine de… fena halde bir şeyleri gözden kaçırıyormuşum gibi geliyor bana.”</p>

<p id="P1428">Kiss-shot’ın o lafları içime bir kurt düşürmüştü.</p>

<p id="P1429">Dahası, işlerin bu denli tereyağından kıl çeker gibi tıkırında ilerlemesi de ayrı bir şüphe kaynağıydı.</p>

<p id="P1430"><em>‘Peki o üç herif nerede saklanıyor?’</em> diye sormuştum.</p>

<p id="P1431"><em>‘Bilmiyorum,’</em> demişti.</p>

<p id="P1432"><em>‘Bilmiyorum da ne demek yahu!’</em></p>

<p id="P1433"><em>‘Fuzuli evhama lüzum yok! Sen sokaklarda avare avare dolan yeter; onlar kokunu alıp seni kendi ayaklarıyla bulur zaten — vampir avında uzmanlaşmış adamlardan bahsediyoruz burada; bir vampirin izini sürmek onlar için çocuk oyuncağıdır!’</em></p>

<p id="P1434"><em>‘Öyle mi dersin?’</em></p>

<p id="P1435"><em>‘Gayet tabii! Burada uslu uslu oturduğun sürece bir şey olmaz gerçi; lakin vampir kuvvetinin zirveye çıktığı gece saatlerinde dışarıda volta atarsan — ışığa üşüşen pervaneler misali etrafını saracaklarından zerre şüphen olmasın!’</em></p>

<p id="P1436">“…………”</p>

<p id="P1437"><em>‘Şu sıralar köşe bucak beni arayıp kasabayı tavaf ediyor olmalılar… Kısmetse bu gece sabaha çıkmadan bu hesabı kapatırız!’</em></p>

<p id="P1438">Kıkır kıkır gülmüştü o an Kiss-shot.</p>

<p id="P1439">Oldukça sinsi ve tekinsiz bir gülüştü.</p>

<p id="P1440">Hımm.</p>

<p id="P1441">Bizim onları aramak zorunda kalmamamız büyük kolaylıktı gerçi… Zira bana kalsa bu koca kasabada çevremi kullanıp adam bulmaya kalkışmak imkânsızdı; sıfır çevreyle kimi kime soracaktım?</p>

<p id="P1442">Lakin — bu kadar pürüzsüz akması canımı sıkıyordu işte.</p>

<p id="P1443">Olaylara biraz daha şüpheci yaklaşmam gerekmez miydi? Bir vampire dönüştüğüm acı bir hakikat olsa bile — mesela.</p>

<p id="P1444">Hemen üzerine atlayıvermiştim gerçi ama… sahiden yeniden insan olabilecek miydim?</p>

<p id="P1445">Kiss-shot’ın kuyruklu bir yalan sıkmadığının garantisi neredeydi?</p>

<p id="P1446">Kollarını bacaklarını geri almak uğruna beni bir piyon gibi kullanıyor olamaz mıydı — kanımı sömürmek yetmemiş gibi şimdi de beni kelimenin tam anlamıyla el ayak niyetine sahaya sürüyor olmasındı sakın?</p>

<p id="P1447">Gerçi bunu ta başından beri saklamamıştı; ‘Bu bir emir değil şantajdır’ demişti.</p>

<p id="P1448">‘Gücüne muhtaç olacağım durumlar hasıl olacaktır’ demişti…</p>

<p id="P1449">…Fakat babasının hayrına yardım etmeyeceğimi bildiği için —beni gaza getirmek adına— 'yeniden insan olabilirsin' masalını uydurmuş olamaz mıydı?</p>

<p id="P1450">Önüme yem niyetine — koca bir yalan atmış olamaz mıydı?</p>

<p id="P1451">İnsanlığa dönmek için yanıp tutuşacağımı.</p>

<p id="P1452">Kiss-shot — adım gibi biliyordu.</p>

<p id="P1453">“…………”</p>

<p id="P1454">Yok yahu.</p>

<p id="P1455">Madem onun kölesiydim, böyle dolambaçlı hilelere başvurmadan bana çatır çatır emir yağdırabilirdi pekâlâ?</p>

<p id="P1456">…Dur bir dakika.</p>

<p id="P1457">Öyle değildi işte!</p>

<p id="P1458">Şu anki vaziyetinde vampir kudretini neredeyse tamamen yitirmişti — yani bana yalan söyleyip beni ikna etmedikçe bana hükmetmeye dermanı yoktu belki de!</p>

<p id="P1459">Mantıksız sayılmazdı hani…</p>

<p id="P1460">On yaşındaki o bücür haliyle bakınca bildiğin çocuk gibiydi gerçi.</p>

<p id="P1461">Lakin — o geceki olgun halini hatırlayınca, ne bileyim, son derece zeki ve kurnaz bir intiba bırakıyordu insanda.</p>

<p id="P1462">En azından kendi iddiasına inanacak olursak beş yüz yıldır nefes alıyordu bu kadın.</p>

<p id="P1463">Kafasının zehir gibi çalıştığına kalıbımı basardım.</p>

<p id="P1464">Hem zaten.</p>

<p id="P1465">En can alıcı suali sormayı unuttuğumu fark ediyordum şimdi.</p>

<p id="P1466">İnsanlığa dönme telaşına kapılıp asıl mühim mevzuları es geçmiştim — en başta, Kiss-shot gibi kadim bir Batılı vampirin Japonya’nın bu ücra taşra kasabasında ne halt karıştırdığını sormayı bile akıl edememiştim!</p>

<p id="P1467">Hortlak demek tuhaf kaçabilirdi belki;</p>

<p id="P1468">Lakin vampir dediğin en nihayetinde Batı mitolojisinin canavarı değil miydi?</p>

<p id="P1469">O üç avcıyı da peşine takıp bizzat buraya sürükleyen o değil miydi sanki?</p>

<p id="P1470">“…Of, kafam çorba oldu.”</p>

<p id="P1471">Nasıl bakarsanız bakın hepsi birer varsayımdan ibaretti.</p>

<p id="P1472">Kiss-shot arkamdan ne kuyu kazarsa kazsın, şu an için ona güvenmekten —onun dudaklarından dökülen vaade sığınmaktan— başka hiçbir çarem yoktu. İnisiyatif baştan aşağı o kadının elindeydi.</p>

<p id="P1473">Önce şu uzuvları toplayalım da — gerisini sonra düşünürdük.</p>

<p id="P1474">Dünya tersine dönse bile o üç vampir avcısı hikâyesi de yalan olacak değildi ya—</p>

<p id="P1475">Derken.</p>

<p id="P1476">Kiss-shot’ın talimatı uyarınca kendimi canlı bir yem gibi ortaya atıp kaldırımsız ıssız yolda avare avare adımlarken — tam bir üçyol ağzına vardığım o anda olanlar oldu.<a id="nr-60" href="notes.xhtml#note-60" epub:type="noteref" class="noteref"><sup>[60]</sup></a></p>

<p id="P1477">Ben…</p>

<p id="P1478">Kiss-shot Acerola-orion Heart-under-blade denen o vampirin, beş yüz yıllık ömrüne rağmen aslında feci derecede kalın kafalı olduğunu işte tam o saniyede idrak ediverdim.</p>

<p id="P1479"><em>‘Teke tek kapıştığın müddetçe o üç sünepe senin eline su bile dökemez’</em> diye ahkâm kesmişti ya hani;</p>

<p id="P1480">Yahu onların teker teker geleceğinin garantisini kim vermişti sana be kadın!?</p>

<p id="P1481">Dahası, bizzat sen, üçü birden çullandığı için mağlup olduğunu söylememiş miydin!?</p>

<p id="P1482">İşlerin tıkırında gitmesi bir yana — ben sahiden de iflah olmaz bir ahmaktım!</p>

<p id="P1483">Lakin — artık çok geçti.</p>

<p id="P1484">Sağ ön çaprazımdan.</p>

<p id="P1485">Boyu iki metreyi rahat aşan devasa bir adam bana doğru yaklaşmaktaydı. Üzerindeki kot pantolon benim için uyku tulumu niyetine kullanılabilirdi; giydiği tişörtü makasla kesseniz benim gibi beş adama fistan çıkardı.</p>

<p id="P1486">Uzayıp omzuna dökülen vahşi saçlarını zapt etmek adına kâküllerini siyah bir saç bandıyla arkaya doğru taramıştı.</p>

<p id="P1487">Saf kastan müteşekkil o dağ gibi adam, çelik gibi sert bir çehreyle dudaklarını sımsıkı kapatmış —elinde taşıdığı iki adet dalgalı devasa kılıcı savurarak— gözlerini üzerime dikmişti.<a id="nr-61" href="notes.xhtml#note-61" epub:type="noteref" class="noteref"><sup>[61]</sup></a></p>

<p id="P1488">Tarife harfiyen uyuyordu.</p>

<p id="P1489">O adam — Dramaturgy idi.</p>

<p id="P1490">Kiss-shot’tan sağ bacağı koparan cellat.</p>

<p id="P1491">“A-Aman Allahım…”</p>

<p id="P1492">Ve sol ön çaprazımdan.</p>

<p id="P1493">Dramaturgy’nin yanında neredeyse narin sayılabilecek, oldukça ince yapılı bir genç bana doğru adımlıyordu — çehresinde henüz çocuksu hatlar vardı gerçi; lakin üzerime diktiği o bakışlardaki vahşet şaka kaldırır cinsten değildi. Hani bakışlarıyla adam öldürür derler ya; öyle bir şey mümkün olsaydı şu an tahtalı köyü boylamıştım çoktan. Öylesine yırtıcı, öylesine dondurucu bir sanpaku bakışıydı.<a id="nr-62" href="notes.xhtml#note-62" epub:type="noteref" class="noteref"><sup>[62]</sup></a> Sırtına geçirdiği bembeyaz okul üniformasıyla (beyaz gakuran) ilk bakışta liseli bir velet gibi görünüyordu; lakin tek eliyle omzuna dayadığı o devasa gümüş haç bütün o masumiyeti yerle bir ediyordu. Hiçbir süsü püsü olmayan, sıradan bir gümüş kolyedeki haçın elli kat büyütülmüş hali gibiydi adeta. Çocuğun kendi boyunun üç katı büyüklüğünde, ağırlığı tonları aşabilecek absürt bir kütleydi. O haçı kutsal bir sembol olarak değil, kafatası ezen bir gürz gibi kullandığını tahmin etmek hiç de zor değildi.</p>

<p id="P1494">Delip geçen bakışlarıyla bana sırıtan o genç —omzundaki o devasa haçı sallaya sallaya— üzerime doğru geliyordu.</p>

<p id="P1495">Tarife harfiyen uyuyordu.</p>

<p id="P1496">O adam — Episode idi.</p>

<p id="P1497">Kiss-shot’tan sol bacağı koparan cellat.</p>

<p id="P1498">“N-Ne yapacağım ben…”</p>

<p id="P1499">Dahası, arkamdan.</p>

<p id="P1500">Ne ara geldiğini dahi fark edemediğim bir peder cübbesine bürünmüş, öndeki o iki izbandutun aksine ilk bakışta son derece uysal görünen üçüncü bir adam — sessizce arkama süzülüvermişti. Kirpiyi andıran diken diken saçları vardı; tekinsizlik saçan tek unsuru da o saçlarıydı zaten, zira umumi havası fazlasıyla munis ve sakindi. Açık mı kapalı mı olduğu anlaşılmayan o çekik çizgimsi gözlerinden iç dünyasını okumak imkânsızdı; lakin öndeki o iki canavarın aksine elinde ne bir kılıç ne de bir haç vardı; görünüşe göre zerre silah taşımıyordu. Gelgelelim bu peder kılıklı adamın en korkutucu tarafı tam da buydu işte. Zira elinde hiçbir silah olmamasına rağmen Kiss-shot’tan diğer ikisinin tam iki katı parça koparmış bir canavardı o!</p>

<p id="P1501">Peder kılıklı adam yüzünde en ufak bir tedirginlik emaresi olmaksızın —elleri bomboş halde— gayet doğal adımlarla bana doğru yaklaşıyordu.</p>

<p id="P1502">Tarife harfiyen uyuyordu.</p>

<p id="P1503">O adam — Guillotinecutter idi.</p>

<p id="P1504">Kiss-shot’tan sağ kolu ve sol kolu —yani iki kolunu birden söküp alan cellat.</p>

<p id="P1505">“—Resmen hapı yuttum…!”</p>

<p id="P1506">Vampir avının uzmanları.</p>

<p id="P1507">Dramaturgy, Episode, Guillotinecutter.</p>

<p id="P1508">O üç uzman — beni merkezlerine alarak çemberi kapatmışlardı.</p>

<p id="P1509">Kaderin cilvesi gibi bir üçyol ağzıydı.</p>

<p id="P1510">Kaçacak tek bir delik dahi yoktu — kapana kısılmış bir sıçandım.</p>

<p id="P1511">“Haa? Bu ne be? Gülmekten yarılır insan!”</p>

<p id="P1512">İlk ağzını açan omzundaki devasa haçla sırıtan o genç —Episode— oldu.</p>

<p id="P1513">Tipine yaraşır şekilde laubali ve çiğ bir üslubu vardı:</p>

<p id="P1514">“Heart-under-blade değil ki bu zibidi — kim lan bu velet?”</p>

<p id="P1515">“■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■”<a id="nr-63" href="notes.xhtml#note-63" epub:type="noteref" class="noteref"><sup>[63]</sup></a></p>

<p id="P1516">Episode’un bu sorusuna, ortada sıkışıp kalmış beni zerre tınlamayan o dağ gibi kas yığını —Dramaturgy— hırıltılı bir sesle karşılık verdi. Son derece ağırbaşlı ve mağrur bir tonlamaydı gerçi; lakin ağzından çıkan yabancı sözcüklerden tek bir kelime dahi anlayamadım.</p>

<p id="P1517">Benim bu şaşkınlığımı dert ettiğinden değil elbet ama,</p>

<p id="P1518">“Olmadı ama Dramaturgy Bey,”</p>

<p id="P1519">Arkamdaki o peder kılıklı adam —Guillotinecutter— söze girdi.</p>

<p id="P1520">Fevkalade yumuşak bir ses tonuydu:</p>

<p id="P1521">“Yerel vazifeler yerel lisanla icra edilir; teşkilatımızın temel kuralıdır bu.”</p>

<p id="P1522">“…………!”</p>

<p id="P1523">Arkama dönüp bakmaya yeltendim — lakin bu sefer de Dramaturgy ile Episode’a sırtımı dönmüş olacağımı fark edip kaskatı kesildim.</p>

<p id="P1524">Guillotinecutter da tıpkı diğer ikisi gibi beni yok sayarak devam etti:</p>

<p id="P1525">“Fakat tespitinizde yerden göğe kadar haklısınız Dramaturgy Bey. Kuvvetle muhtemel, hatta kesinlikle bu delikanlı Heart-under-blade Hanımefendi’nin hizmetkârı olmalı…”</p>

<p id="P1526">“Harbi mi diyorsun…?”</p>

<p id="P1527">Episode hoşnutsuzlukla homurdandı:</p>

<p id="P1528">“O kibirli vampir prensip olarak asla köle yaratmaz diye biliyorduk?”</p>

<p id="P1529">“Vaktiyle tek bir kişi yarattığı rivayet edilir gerçi.”</p>

<p id="P1530">“■■■… Köşeye sıkışınca… can havliyle kendine ayak işlerini görecek bir maşa yaratmış besbelli.”</p>

<p id="P1531">Dramaturgy bu sefer Japonca konuştu.</p>

<p id="P1532">Sırf kas yığını bir kaba kuvvet sanmıştım; meğer şıp diye kimliğimi çözüverecek kadar tilkiymiş herif.</p>

<p id="P1533">“Yani şimdi mevzu şu mu?” dedi Episode sırıtmaya devam ederek.</p>

<p id="P1534">Omzundaki o devasa haçı hafifçe yaylandırarak:</p>

<p]P1535">“Varlık enerjisini kaybettiği için yerini tespit etmekte zorlandığımız Heart-under-blade’in nerede saklandığını bu veledin etini sıkarak öğrenebiliriz, öyle mi?”</p>

<p id="P1536">“Aynen öyle oluyor efendim,” diyerek gayet sakin onayladı Guillotinecutter.</p>

<p id="P1537">Ve Dramaturgy de ekledi:</p>

<p id="P1538">“Bu delikanlıyı itlaf ettiğimizde alacağımız mükâfat Heart-under-blade’in kellesinden ayrı hesaplanacaktır muhakkak.”</p>

<p id="P1539">Doğmamış çocuğa don biçiyorlardı resmen.</p>

<p id="P1540">Ne kadar da safmışım…</p>

<p id="P1541">‘Eskiden insan olduğumu anlayıp bana acısalar bile’ mi demiştim ben?</p>

<p id="P1542">Nasıl bir hayalperestlikti bu böyle!</p>

<p id="P1543">İyimserliğin de bir hududu vardı yahu!</p>

<p id="P1544">Bu adamlar… az evvelden beri beni muhatap bile almıyorlardı.</p>

<p id="P1545">Beni resmen yok sayıyorlardı.</p>

<p id="P1546">Beni canlı bir varlık olarak dahi kabul etmiyorlardı.</p>

<p id="P1547">Varlık seviyesinde beni zerre ciddiye aldıkları yoktu!</p>

<p id="P1548">“Hımm,” dedi Guillotinecutter.</p>

<p id="P1549">“Peki ne yapıyoruz o vakit? Episode Beyefendi’nin buyurduğu üzere bu delikanlıdan Heart-under-blade Hanımefendi’nin mevkiini söke söke almak icap ediyorsa birazcık zahmete girmemiz gerekecek.”</p>

<p id="P1550">“Bana bırakın gitsin,” dedi Episode pişkin pişkin sırıtarak.</p>

<p id="P1551">“Sakat kalmayacağı kıvamda gebertiveririm ben onu!”</p>

<p id="P1552">“Hayır, vazifeyi ben üstleneceğim,” dedi Dramaturgy.</p>

<p id="P1553">“Bu kabil sorgu işlerine en yatkın olan şahsımdır. Bir vampirin dilinden en iyi ben anlarım.”</p>

<p id="P1554">“Benim için de bir mahzuru yok gerçi,” dedi Guillotinecutter o munis tavrıyla.</p>

<p id="P1555">“Siz muhterem beyefendiler de epeyce yoruldunuz neticede.”</p>

<p id="P1556">“K-Kendi kendinize gelin güvey olmayı kesin be!”</p>

<p id="P1557">Ben…</p>

<p id="P1558">Bütün cesaretimi toplayıp avazım çıktığı kadar haykırdım.</p>

<p id="P1559">Hiçbirinin yüzüne bakamadan.</p>

<p id="P1560">Kimseyle göz teması kuramadan haykırdım:</p>

<p id="P1561">“İ-İki çift laf etmeyi denesenize be vicdansızlar! Ne diye hemen beni itlaf etmenin pazarlığına tutuşuyorsunuz… Ben insanım ulan insan! Katil mi olacaksınız başıma—”</p>

<p id="P1562">“…………”</p>

<p id="P1563">“…………”</p>

<p id="P1564">“…………”</p>

<p id="P1565">Bir anlığına ortalığı derin bir sessizlik kapladığına bakılırsa feryadım bir şekilde kulaklarına ulaşmıştı.</p>

<p id="P1566">Lakin — hepsi bundan ibaretti.</p>

<p id="P1567">Sesim kulaklarına gitmişti ama manası beyinlerine zerre ulaşmamıştı.</p>

<p id="P1568">Hiçbiri bana tek kelimeyle dahi cevap vermeye tenezzül etmedi.</p>

<p id="P1569">“Öyleyse her zamanki usul,” dedi Dramaturgy.</p>

<p id="P1570">“Anlaştık. Kelle kapanın elinde kalsın!” dedi Episode.</p>

<p id="P1571">“Pekâlâ. Adil bir rekabet mesleki kabiliyetlerimizi daima biler,” dedi Guillotinecutter.</p>

<p id="P1572">Ve — o üç uzman.</p>

<p id="P1573">Üçü birden, neredeyse aynı salisede —üçyolun tam göbeğinde titreyen benim üzerime— fırlayıverdiler!<a id="nr-64" href="notes.xhtml#note-64" epub:type="noteref" class="noteref"><sup>[64]</sup></a> Üzerime çullandıkları o anki hareketlerini milim milim görebiliyordum; vampir gözlerimin bahşettiği dinamik görme yeteneği sayesindeydi bu şüphesiz. Karanlığı yarmak bir yana, mermiyi havada seçecek bir refleks hızım vardı — gelgelelim…</p>

<p id="P1574">Görebilmek ne boka yarıyordu ki!?</p>

<p id="P1575">Bu cehennem çemberinde elimden ne gelirdi sanki?</p>

<p id="P1576">“U-Uvaaaaaaaaaaaaaaaaah!”</p>

<p id="P1577">Yaptığım hareket —muhtemelen böylesi bir ölüm anında yapılabilecek en acizce hareketti— başımı iki elimin arasına alıp yere kapaklanarak cenin pozisyonu aldım. Ne bir savunmaydı bu ne de bir karşı koyuş; düpedüz acınası bir gerçeklikten kaçıştı.</p>

<p id="P1578">İmkânsızdı.</p>

<p id="P1579">Eşyanın tabiatına aykırıydı zaten.</p>

<p id="P1580">Ben neyime güvenmiştim ki?</p>

<p id="P1581">Bir çizgi romanın, bir filmin, bir dövüş oyununun kahramanı bile değilken — alt tarafı lise sıralarında çürüyen tembel bir veletken ne cüretle kalkıp vampir cellatlarıyla cenge tutuşmaya kalkmıştım?</p>

<p id="P1582">Ne bu, liseli süper güç savaşı mangası falan mıydı?<a id="nr-65" href="notes.xhtml#note-65" epub:type="noteref" class="noteref"><sup>[65]</sup></a></p>

<p id="P1583">Kazanmama imkân var mıydı yahu?</p>

<p id="P1584">Beton duvarı yumrukla delmişsem ne olmuş yani?</p>

<p id="P1585">Yükseğe zıplayabiliyorum, hızlı koşabiliyorum diye ne değişirdi?</p>

<p id="P1586">Böyle yetenekler dövüş bilmeyen bir eblehin elinde ne işe yarardı ki?</p>

<p id="P1587">Dedim ya, ömrümde tek bir sokak kavgasına bile karışmamış adamdım ben — kavga edecek bir tek arkadaşım bile olmamıştı ki benim! Dövüş sporlarının yanından bile geçmemiştim!</p>

<p id="P1588">Kahretsin… Lanet olsun.</p>

<p id="P1589">Bir kere feda ettiğim o candı halbuki.</p>

<p id="P1590">Kiss-shot’a kendi ellerimle teslim ettiğim o candı.</p>

<p id="P1591">Peki şimdi neden — neden canım bu kadar tatlı geliyordu!?</p>

<p id="P1592">“────!”</p>

<p id="P1593">…………!</p>

<p id="P1594">…………, …………</p>

<p]P1595">Lakin…</p>

<p id="P1596">Ne kadar beklersem bekleyeyim — o üç ölümcül darbe sırtıma bir türlü inmek bilmedi.</p>

<p id="P1597">Ne oluyordu… İşkence mi edeceklerdi?</p>

<p id="P1598">Yoksa bu acınası halimi görüp tiksinerek vaz mı geçmişlerdi? Hevesleri mi kaçmıştı — yok canım, imkânsızdı.</p>

<p id="P1599">İşkence etmek şöyle dursun, adamlar beni göz ucuyla bile görmüyordu ki…</p>

<p id="P1600">Dizlerimin arasına gömdüğüm başımı — usulca yukarı kaldırdım.</p>

<p id="P1601">Ve o an.</p>

<p id="P1602">“Hah hah ha…”</p>

<p id="P1603">Dünyadan bihaber, alabildiğine tasasız bir kahkaha çalındı kulaklarıma:</p>

<p id="P1604">“Böylesi sakin bir mahallenin göbeğinde kılıç sallamak, haç fırlatmak falan… Hakikaten pek bir enerjiksiniz maşallah gençler—”<a id="nr-66" href="notes.xhtml#note-66" epub:type="noteref" class="noteref"><sup>[66]</sup></a></p>

<p id="P1605">Dramaturgy’nin havada savrulan o iki devasa dalgalı kılıcını; sağ elinin işaret ve orta parmağı ile yüzük ve serçe parmağının arasına alıp havada sımsıkı kilitleyen…</p>

<p id="P1606">Episode’un o tonlarca ağırlıktaki gümüş haçını sağ ayağının tabanıyla sanki bir futbol topunu stop eder gibi havada durduran…</p>

<p id="P1607">Ve Guillotinecutter’ın o ölümcül hamlesini sol avucunu öne uzatarak tek bir temas dahi etmeksizin boşa çıkaran kişi —kimdi dersiniz?</p>

<p id="P1608">Oradan geçmekte olan hırpani bir amcadan başkası değildi.<a id="nr-67" href="notes.xhtml#note-67" epub:type="noteref" class="noteref"><sup>[67]</sup></a></p>

<p id="P1609">Tek ayağının üzerinde leylek gibi dengede durarak sözlerine devam etti adam:</p>

<p id="P1610">“—Pek neşelisiniz… Güzel bir şey mi oldu yoksa?”<a id="nr-68" href="notes.xhtml#note-68" epub:type="noteref" class="noteref"><sup>[68]</sup></a></p>
"""

# Update chapter1.xhtml
with open(f"{BASE_DIR}/EPUB/text/chapter1.xhtml", "r", encoding="utf-8") as f:
    current_ch1 = f.read()

if "</section>" in current_ch1:
    idx = current_ch1.rfind("</section>")
    new_ch1 = current_ch1[:idx] + sec5_html + "\n</section>\n</body>\n</html>"
    with open(f"{BASE_DIR}/EPUB/text/chapter1.xhtml", "w", encoding="utf-8") as f:
        f.write(new_ch1)
    print("Chapter 1 updated with Section 005.")

# ==========================================
# APPEND NOTES FOR SECTION 005
# ==========================================

notes_005 = """
<li id="note-56"><span class="note-num">56.</span> <b>ドラマツルギー、エピソード、ギロチンカッター (Üç Avcının İsimleri):</b> Nisio Isin'in teatral ve edebi kavramlardan türettiği uzman avcı isimleri: <i>Dramaturgy</i> (Dramatürji - tiyatro metni ve sahneleme teorisi), <i>Episode</i> (Bölüm / epizot / münferit olay) ve <i>Guillotinecutter</i> (Giyotin Bıçağı - Fransız Devrimi'nin infaz aygıtı). <a href="chapter1.xhtml#P1343" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-57"><span class="note-num">57.</span> <b>怪異殺し (Kaii-goroshi / Musibet Katili):</b> Kiss-shot'ın Monogatari evrenindeki en korkulan unvanı. Yalnızca insanları değil, diğer tüm doğaüstü musibetleri, hortlakları ve efsanevi yaratıkları da avlayıp yok edebilen en üst düzey yırtıcı olduğunu gösterir. <a href="chapter1.xhtml#P1391" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-58"><span class="note-num">58.</span> <b>自分探しの旅 (Kendini Bulma Yolculuğu):</b> Japon gençlik edebiyatında hiçbir amacı olmayan aylak gençlerin evden kaçışlarına kılıf olarak uydurdukları popüler bir klişe. Araragi'nin kız kardeşinin bu yalanı anında kabul etmesi, abisinin aylak imajını vurgular. <a href="chapter1.xhtml#P1410" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-59"><span class="note-num">59.</span> <b>チルチルとミチル・青い鳥 (Tyltyl, Mytyl ve Mavi Kuş):</b> Maurice Maeterlinck'in ünlü sembolist tiyatro oyunu <i>L'Oiseau bleu</i> (Mavi Kuş). Eserde iki kardeş mutluluk getiren Mavi Kuş'u aramak için dünyayı gezer ama sonunda onun zaten kendi evlerinde olduğunu anlarlar. Küçük kardeş Tsukihi'nin abisine gönderdiği bu edebi gönderme, ailenin içsel derinliğini yansıtır. <a href="chapter1.xhtml#P1416" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-60"><span class="note-num">60.</span> <b>三叉路 (Üçyol Ağzı / Kavşak Sembolizmi):</b> Dünya mitolojisinde kavşaklar (özellikle Hekate kültünde) doğaüstü karşılaşmaların, tekinsizliğin ve dönüm noktalarının mekânıdır. Eserde üç avcının Araragi'yi tam bir üçyol ağzında kıstırması bu mitolojik altyapıya dayanır. <a href="chapter1.xhtml#P1476" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-61"><span class="note-num">61.</span> <b>フランベルジュ・波打つ大剣 (Flamberge Kılıçları):</b> Dramaturgy'nin taşıdığı alev dalgalı iki devasa çift elli kılıç (flamberge / claymore). Kiss-shot'ın sağ bacağını jilet gibi kesen silah budur. <a href="chapter1.xhtml#P1487" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-62"><span class="note-num">62.</span> <b>三白眼 (Sanpaku Gözler):</b> Japon yüz okuma sanatında gözbebeğinin üstünde veya altında beyazlığın görünmesi durumu. Şiddete meyilli, psikotik ve tekinsiz karakterlerin anime/manga tasvirinde klasik bir belirteçtir. <a href="chapter1.xhtml#P1493" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-63"><span class="note-num">63.</span> <b>■■■ (Kurgusal / Sansürlü Yabancı Dil):</b> Nisio Isin eserde Dramaturgy'nin konuştuğu kadim dili harfler yerine siyah karelerle (■) vererek anlatıcının (Araragi) bu dili tamamen yabancı ve anlamsız bir hırıltı olarak duyduğunu betimler. <a href="chapter1.xhtml#P1515" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-64"><span class="note-num">64.</span> <b>動体視力 (Dinamik Görme Yeteneği):</b> Vampir reflekslerinin hızlanan zaman algısı. Araragi ölümcül saldırıları milisaniyelik yavaş çekimde görmesine rağmen bedensel dövüş tecrübesi olmadığı için hiçbir karşı hamle yapamaz. <a href="chapter1.xhtml#P1573" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-65"><span class="note-num">65.</span> <b>学園異能バトル (Okul Doğaüstü Savaş Klişesi):</b> Nisio Isin'in hafif roman (light novel) türünün 'sıradan liseli çocuk bir anda süper güçler kazanıp dünyayı kurtarır' klişesini Araragi'nin çaresizliği üzerinden acımasızca tiye alması. <a href="chapter1.xhtml#P1582" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-66"><span class="note-num">66.</span> <b>白刃取り (Shiraha-dori - Çıplak Elle Kılıç Yakalama):</b> Samuray dövüş sanatlarında inen kılıcı avuç içi veya parmak aralarıyla havada durdurma efsanevi tekniği. <a href="chapter1.xhtml#P1604" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-67"><span class="note-num">67.</span> <b>通りすがりのおっさん (Oshino Meme):</b> Monogatari serisinin kilit karakteri olan <b>Oshino Meme</b>'nin sahneye ilk efsanevi girişi. Üzerindeki aloha gömleği, sigarası ve umursamaz tavrıyla üç uzmanı tek bir hamlede durdurur. <a href="chapter1.xhtml#P1608" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-68"><span class="note-num">68.</span> <b>何かいいことでもあったのかい (Meşhur Giriş Aforizması):</b> Oshino Meme'nin tüm seri boyunca her sahneye girişinde kullandığı imza niteliğindeki aforizması: <i>"Nanika ii koto demo atta no kai?"</i> (Pek neşelisiniz, güzel bir şey mi oldu yoksa?). <a href="chapter1.xhtml#P1610" class="backref" aria-label="Metindeki yere dön">↩</a></li>
"""

with open(f"{BASE_DIR}/EPUB/text/notes.xhtml", "r", encoding="utf-8") as f:
    current_notes = f.read()

if "</ol>" in current_notes:
    idx = current_notes.rfind("</ol>")
    new_notes = current_notes[:idx] + notes_005 + "\n</ol>\n</section>\n</body>\n</html>"
    with open(f"{BASE_DIR}/EPUB/text/notes.xhtml", "w", encoding="utf-8") as f:
        f.write(new_notes)
    print("Notes updated with Section 005.")

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
<li><a href="chapter1.xhtml#P0931">004 — Alevler İçinde Diriliş ve Harabe Dershane</a></li>
<li><a href="chapter1.xhtml#P1340">005 — Üç Cellat ve Gizemli Kurtarıcı</a></li>
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
<li><a href="text/chapter1.xhtml#P0931">004 — Alevler İçinde Diriliş ve Harabe Dershane</a></li>
<li><a href="text/chapter1.xhtml#P1340">005 — Üç Cellat ve Gizemli Kurtarıcı</a></li>
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
<navPoint id="np-6" playOrder="6">
<navLabel><text>004 — Alevler İçinde Diriliş</text></navLabel>
<content src="text/chapter1.xhtml#P0931"/>
</navPoint>
<navPoint id="np-7" playOrder="7">
<navLabel><text>005 — Üç Cellat ve Kurtarıcı</text></navLabel>
<content src="text/chapter1.xhtml#P1340"/>
</navPoint>
</navPoint>
<navPoint id="np-8" playOrder="8">
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
