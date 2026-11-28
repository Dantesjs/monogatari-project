# -*- coding: utf-8 -*-
import os, zipfile, datetime

BASE_DIR = "/data/data/com.termux/files/home/monogatari-project/kizumonogatari_epub"
EPUB_OUT = "/data/data/com.termux/files/home/monogatari-project/04_Kizumonogatari_TR.epub"

# ==========================================
# SECTION 004 HTML
# ==========================================

sec4_html = """
<h3 id="P0931" class="section-no">004</h3>

<p id="P0932">Bilincim ansızın, bir şimşek gibi yerine geldi.</p>

<p id="P0933">Sahiden de yeniden doğmuşum gibi tuhaf bir tazelik hissiydi bu.</p>

<p id="P0934">Yok, daha ziyade… ölümden dirilmiş gibi.</p>

<p id="P0935">“Oh be! Rüya mıydı yoksa?”</p>

<p id="P0936">Böyle bağırmayı denedim.</p>

<p id="P0937">Elbette rüya falan değildi — şayet bir rüyadan uyanmış olsaydım, gözlerimi açtığım yerin kendi yatağım, kendi odam olması icap ederdi.</p>

<p id="P0938">Fakat burası benim odam falan değildi.</p>

<p id="P0939">Bırakın odamı, ömrümde ilk defa gördüğüm bir yerdi.</p>

<p id="P0940">Her sabah beni tekme tokat uyandırmaya gelen o iki cadı kardeşim de ortalıkta görünmüyordu.</p>

<p id="P0941">“…………”</p>

<p id="P0942">Yine de…</p>

<p id="P0943">O rüyanın bittiğini anlayana kadar kafayı yastığa gömüp tekrar tekrar uyumak için neler vermezdim.</p>

<p id="P0944">Neresiydi burası yahu… Harabe falan mı?</p>

<p id="P0945">İnsan yapımı bir binanın içinde olduğumu kestirebiliyordum elbet; fakat pencerelere kalın tahtalar çakılmış, içerisi zifiri karanlığa boğulmuştu. Tavandan sarkan floresan lambaların ise istisnasız hepsi tuzla buz olmuştu…</p>

<p id="P0946">Vücudumun ne vaziyette olduğunu fark ettim.</p>

<p id="P0947">Zeminde boylu boyunca uzanıyordum.</p>

<p id="P0948">Zemin muşamba kaplıydı.</p>

<p id="P0949">Fakat boydan boya derin çatlaklarla doluydu.</p>

<p id="P0950">Yalnızca boynumu oynatarak etrafı kolaçan ettim — duvarda asılı duran o şey de neyin nesiydi öyle?</p>

<p id="P0951">Yazı tahtası mı?</p>

<p id="P0952">Bir de… sıra mı onlar?</p>

<p id="P0953">Sandalyeler?</p>

<p id="P0954">…Bir okul sınıfı mıydı burası?</p>

<p id="P0955">Demek bir okuldaydım… Lakin Naoetsu Lisesi olmadığı kesindi. O kadarını ayırt edebiliyordum. Dahası… pek de okul havası yoktu burada.</p>

<p id="P0956">Nihayetinde kanlı canlı bir lise talebesiydim.</p>

<p id="P0957">Kendi okuduğum bina olmasa bile, ne kadar benzerse benzesin, içinde bulunduğum yerin resmî bir okul binası olup olmadığını şıp diye anlayabilirdim.</p>

<p id="P0958">Öyleyse… ne olabilirdi ki?</p>

<p id="P0959">Okul olmayan ama içinde kara tahta, yığınla sıra ve sandalye barındıran bir mekân…?</p>

<p id="P0960">Ha, tamam, şimdi jetonum düştü.</p>

<p id="P0961">Bu koku, bu hava bir dershaneye aitti.<a id="nr-43" href="notes.xhtml#note-43" epub:type="noteref" class="noteref"><sup>[43]</sup></a></p>

<p id="P0962">Özel bir dershane binası olmalıydı.</p>

<p id="P0963">…Fakat neresinden bakarsanız bakın, faaliyette olan bir dershaneye zerre benzemiyordu.</p>

<p id="P0964">Gerek pencereleri gerekse kırık dökük lambalarıyla… iflas edip terk edilmiş bir dershane enkazıydı düpedüz.</p>

<p id="P0965">Gerçi ortalık alacakaranlık olduğu için gözüme öyle görünmüş de olabilirdi — alacakaranlık mı?</p>

<p id="P0966">Bir dakika ya?</p>

<p id="P0967">Pencereleri tahtalarla sımsıkı çivilenmiş, içeriye tek bir zerre ışığın dahi sızmadığı böylesi kapkaranlık bir odayı… ben nasıl oluyordu da bu denli berrak ve net görebiliyordum?<a id="nr-44" href="notes.xhtml#note-44" epub:type="noteref" class="noteref"><sup>[44]</sup></a></p>

<p id="P0968">Zifiri karanlık olduğunu biliyordum.</p>

<p id="P0969">Aydınlık sayılmasına imkân yoktu.</p>

<p id="P0970">Bir adım önünü dahi görmenin imkânsız olması gereken o koyu karanlıkta — her şeyi kabak gibi görüyordum.</p>

<p id="P0971">Kristal berraklığında görüyordum hem de.</p>

<p id="P0972">Yok canım… İnsan gözü böyle miydi ki?</p>

<p id="P0973">Uykudan yeni uyandığım için duyularım geçici bir yanılsama mı yaşıyordu acaba?</p>

<p id="P0974">Bu tuhaflığa anlam veremeyerek doğruldum—</p>

<p id="P0975">“…Ah, acıdı!”</p>

<p id="P0976">O esnada dilimi fena halde ısırdım.</p>

<p id="P0977">Hı?</p>

<p id="P0978">Benim köpekdişlerim bu kadar sivri ve uzun muydu yahu?<a id="nr-45" href="notes.xhtml#note-45" epub:type="noteref" class="noteref"><sup>[45]</sup></a></p>

<p id="P0979">Parmağımı ağzıma sokup kontrol etmeye yeltendim ki — tam o anda.</p>

<p id="P0980">Parmağımı, dolayısıyla kolumu kıpırdatmaya çalıştığım o saniyede nihayet farkına varabildim — yana doğru serilmiş kolumu yastık niyetine başının altına almış, mışıl mışıl uyuyan küçücük bir kız çocuğunun varlığını!</p>

<p id="P0981">“…………”</p>

<p id="P0982">Ne?</p>

<p id="P0983">Küçük bir kız çocuğu mu?</p>

<p id="P0984">“…Haaaaa!?”</p>

<p id="P0985">Basbayağı, minicik bir kız çocuğuydu işte.</p>

<p id="P0986">Yaşı olsa olsa on civarındaydı?</p>

<p id="P0987">Üzerine pek yakışan kabarık, fırfırlı bir elbise giymiş, sapsarı altın saçlı bir kızdı — teninin rengi beyazı da geçmiş, adeta saydam bir porseleni andırıyordu.</p>

<p id="P0988">Mışıl mışıl, minik nefesler alarak…</p>

<p id="P0989">Uyuyordu.</p>

<p]P0990">Deliksiz bir uyku çekiyordu.</p>

<p id="P0991">“…………”</p>

<p id="P0992">İçinde bulunduğum vaziyeti zerrece kavrayamıyordum.</p>

<p id="P0993">Benim burada ne işim vardı, burası neresiydi ve dahası bu sarışın kız çocuğu da kimin nesiydi? En ufak bir ipucu dahi yoktu elimde… Lakin bu tablonun feci derecede sakat olduğu gün gibi aşikârdı!</p>

<p id="P0994">Kız çocuğu olması bir yana.</p>

<p id="P0995">‘Tanımadığın bir kız çocuğuyla harabede uyanmak’ tabiri buram buram adli vaka kokuyordu!</p>

<p id="P0996">“H-Hey… U-Uyan baksana.”</p>

<p id="P0997">Kızın vücudunun en tehlikesiz yerine (pazusuna falan) elimi uzatıp usulca sarstım.</p>

<p id="P0998">“Mmmhh…”</p>

<p id="P0999">Küçük kız hoşnutsuz bir tavırla homurdandı.</p>

<p id="P1000">“Beş dakika daha…”</p>

<p id="P1001">Klasik tembel çocuk repliğini patlatıvermişti.</p>

<p id="P1002">Nazlanır gibi öbür tarafına döndü.</p>

<p id="P1003">“U-Uyan dedim sana!”</p>

<p id="P1004">İstifimi bozmadan kızı sarsmaya devam ettim.</p>

<p id="P1005">“…Keyfime göre.”<a id="nr-46" href="notes.xhtml#note-46" epub:type="noteref" class="noteref"><sup>[46]</sup></a></p>

<p id="P1006">“Daha ne kadar uyuyacaksın be kadın!”</p>

<p id="P1007">“…Dört nokta altı milyar yıl kadar?”</p>

<p id="P1008">“Yuh, dünya sıfırdan bir daha oluşur o zamana kadar!”</p>

<p id="P1009">Avazım çıktığı kadar lafı yapıştırmıştım ki telaşla ağzımı kapattım.</p>

<p id="P1010">Doğru ya.</p>

<p id="P1011">Düşününce, bu veledi uyandırmak kaş yaparken göz çıkarmak olmasın sakın?</p>

<p id="P1012">O hazır uyurken kendi başımın çaresine bakıp vaziyeti çözmeye çalışmak her halükarda çok daha akıllıcaydı. Gerçi çözmek desem de ortada neyin problemi olduğunu bile bilmiyordum ya…</p>

<p id="P1013">Şimdilik sol bileğimdeki kol saatine baktım.</p>

<p id="P1014">Şey…</p>

<p id="P1015">Saat — dört buçuk muydu?</p>

<p id="P1016">Olmaz, analog saatle sabah mı akşam mı olduğunu kestiremezdim.</p>

<p id="P1017">Telefon, telefon… Hah, buradaydı.</p>

<p id="P1018">Ekrandaki dijital saat hakikaten de on altı otuz ikiyi gösteriyordu.</p>

<p id="P1019">Tarih ise… Yirmi sekiz Mart mı!?<a id="nr-47" href="notes.xhtml#note-47" epub:type="noteref" class="noteref"><sup>[47]</sup></a></p>

<p id="P1020">Dur bir dakika… En son telefondan saate baktığım anı hatırlıyordum; günün henüz devrildiği o gece vaktiydi, evet, yirmi altı Mart’tı değil mi?</p>

<p id="P1021">Demek ki — o geceden bu yana koca iki gün geçmişti öyle mi?</p>

<p id="P1022">“…Yok artık.”</p>

<p id="P1023">Rüya olmasa bile… Peki o gece yaşananların ne kadarı gerçekti?</p>

<p id="P1024">O anılar…</p>

<p id="P1025">Zihnimdeki o dehşet sahneleri — ne derece doğruydu?</p>

<p id="P1026">Bu sefer sarışın kızı uyandırmamaya azami dikkat göstererek kolumu usulca başının altından çektim.</p>

<p id="P1027">Her şeyden önce buranın neresi olduğunu çözmem lazımdı…</p>

<p id="P1028">Ayak uçlarıma basarak odanın (sınıfın?) kapısına doğru yürüdüm — kilitli falan değildi. Hatta menteşelerinden biri yerinden fırlamış, kapı vasfını çoktan yitirmişti. Gizli bir tesiste alıkonulduğum yahut rehin alındığım kuruntusu böylece suya düştü (saçma gelebilir ama sahiden endişelenmiştim).</p>

<p id="P1029">Hem o sevimli altın saçlı kızı anlarım da, benim gibi bir veledi kaçırmak kimin ne işine yarardı ki…</p>

<p id="P1030">Kapıdan koridora çıktığımda hemen karşımdaki merdiven çarptı gözüme.</p>

<p id="P1031">Duvardaki soluk tabelada ‘2F’ yazıyordu.</p>

<p id="P1032">İkinci kat mı?</p>

<p id="P1033">Yukarı ve aşağı giden iki merdiven kolu vardı.</p>

<p id="P1034">Hangisine yönelmem gerektiğini biraz tarttım — ama aklın yolu birdi, zemin kata inmek şarttı. Binadan dışarı çıkıp temiz bir hava almadan vaziyeti tartamazdım.</p>

<p id="P1035">Merdivenin öte tarafında bir asansör kapısı vardı gerçi; ama yaklaşıp bakmaya gerek bile yoktu, elektriklerin olmadığı bir harabede çalıştığına inanmak ahmaklık olurdu.</p>

<p id="P1036">Basamakları birer ikişer indim.</p>

<p id="P1037">“…Şimdi, rehberde Hanekawa’nın numarası ve adresi kayıtlı olduğuna göre kapanış töreninin ardından onunla karşılaştığım kesin bir hakikat… Ondan önceki hatıralarım da yerli yerinde.”</p>

<p id="P1038">O iç çamaşırı da rüya değildi yani.</p>

<p id="P1039">Rüya gibiydi gerçi ama.</p>

<p id="P1040">“Cüzdandaki para da eksilmiş, fiş de duruyor… Demek ki genç kız moda dergisi satın aldığım da su götürmez bir gerçek.”<a id="nr-48" href="notes.xhtml#note-48" epub:type="noteref" class="noteref"><sup>48]</sup></a></p>

<p id="P1041">Hafızam hafiften tahrifata uğramıştı ama çaktırmadan devam ettim.</p>

<p id="P1042">“Fakat ondan sonrası… Hiç ama hiç gerçekçi gelmiyor.”</p>

<p id="P1043">Rüya olmasa bile.</p>

<p id="P1044">Büyük bir yanılsama, dehşetengiz bir yanlış anlama olamaz mıydı?</p>

<p id="P1045">Mesela — arabaların çarptığı yaralı bir kadın vardı da… Ben yaralıyı görünce dehşete kapılıp… oracıkta düşüp bayılmış olabilir miydim?</p>

<p id="P1046">Hımm.</p>

<p id="P1047">Zorlama bir teoriydi gerçi ama ilk defa başıma geliyordu neticede.</p>

<p id="P1048">Sonra da… baygın haldeki beni birisi alıp buraya taşımıştı falan… Yok yahu, saçmalığın daniskasıydı bu. Öyle bir durumda insan gibi ambulans çağırırlardı.</p>

<p id="P1049">Yine de telefondaki tarih kabak gibi ortadaydı.</p>

<p id="P1050">Hapı yutmuştum; evden iki gündür, hissi olarak neredeyse üç gündür uzaktaydım.</p>

<p id="P1051">Haber vermeden dışarıda sabahladığım ilk vukuatım değildi gerçi; ama üç gün artık bardağı taşıran son damlaydı. Kız kardeşlerimin vukuatları yanında benimki masum bir kaçamak sayılabilirdi gerçi; ama ne olursa olsun eve acilen bir haber uçurmam şarttı.</p>

<p id="P1052">O esnada…</p>

<p id="P1053">Hâlâ böylesine aymaz ve tasasız hayaller kuruyordum işte.</p>

<p id="P1054">Lakin binanın çıkış kapısından adımımı attığım o saniyede, kurduğum bütün o pembe hayaller tuzla buz olup havaya savruldu. Yerdeki molozları, paslı demir parçalarını, cam kırıklarını, ne idüğü belirsiz tabelaları, teneke kutuları ve karton yığınlarını ustalıkla atlatarak (iyi de zifiri karanlıkta bütün bunları nasıl bu kadar milimetrik görebiliyordum sahi?), binanın dışındaki o yabani otların fışkırdığı bahçeye adımımı attığım tam o anda—</p>

<p id="P1055">Vücudum.</p>

<p id="P1056">Bütün bedenim — alev alev tutuşuverdi!<a id="nr-49" href="notes.xhtml#note-49" epub:type="noteref" class="noteref"><sup>[49]</sup></a></p>

<p id="P1057">Uyanmalıydım.</p>

<p id="P1058">Akşamüstü batmakta olan o solgun güneşin… nasıl olup da gözlerimi kör edecek kadar parlak göründüğünü akıl etmeliydim.</p>

<p id="P1059">Fakat artık çok geçti — bütün etim ve kemiğim çıra gibi alev almıştı.</p>

<p id="P1060">“Gyaaaaaaaaaaaaahhhhhh!”</p>

<p id="P1061">İnsan gırtlağından çıkamayacak bir çığlık koptu ağzımdan.</p>

<p id="P1062">Acı falan hafif kalırdı!</p>

<p id="P1063">Saçlarım, derim, etim, kemiklerim; her bir zerrem — cayır cayır yanıyordu.</p>

<p id="P1064">Kavruluyordum.</p>

<p id="P1065">Korkunç bir süratle — küle dönüyordum.</p>

<p id="P1066">“Aaaaaaaaaaaarrrrgghhhhh!”</p>

<p id="P1067">Vampirler…</p>

<p id="P1068">Güneşe karşı zayıf mıydı?</p>

<p id="P1069">Karanlığın çocukları olan vampirler güneşte yanar mıydı?</p>

<p id="P1070">Bu yüzden mi — gölgeleri olmazdı?</p>

<p id="P1071">İyi de bunun benimle ne alakası—</p>

<p id="P1072">“Ahmak herif!”<a id="nr-50" href="notes.xhtml#note-50" epub:type="noteref" class="noteref"><sup>[50]</sup></a></p>

<p id="P1073">Üzerimdeki alevleri söndürebilmek adına bildiğim bütün hayatta kalma bilgilerini devreye sokarak toprakta bir o yana bir bu yana yuvarlanırken (yangında yerde yuvarlanmak gerektiğini bir yerlerde okumuştum), binanın içinden böyle bir feryat yükseldi.</p>

<p id="P1074">Baktığımda…</p>

<p id="P1075">Nemini ve suyunu çoktan kaybetmiş, alevler içinde kömürleşen o gözbebeklerimle sesin geldiği tarafa baktığımda — orada dikilen kişi az önce mışıl mışıl uyuyan o sarışın kız çocuğuydu.</p>

<p id="P1076">On yaşındaki bir kıza katiyen yakışmayan mağrur ve buyurgan bakışlarla bana doğru—</p>

<p id="P1077">“Çabuk buraya, gölgeye dön dedim sana!” diye kükredi.</p>

<p id="P1078">Dön diyordu demesine de, çektiğim o dehşetengiz azap yüzünden etlerim kaskatı kesilmiş, vücudum söz dinlemez olmuştu — bunu fark etmiş olacak ki o sarışın kız çocuğu gözünü karartıp binanın kapısından güneşe doğru fırlayıverdi.</p>

<p id="P1079">Ve fırlar fırlamaz.</p>

<p id="P1080">Tıpkı benim gibi — kızın bütün bedeni de alev topuna döndü.</p>

<p id="P1081">Lakin zerre aldırmaksızın koşup yanıma geldi; yerde kıvranan beni koltuk altlarımdan kavradığı gibi gerisin geriye sürüklemeye başladı.</p>

<p id="P1082">Cayır cayır bir meşale gibi yanarken.</p>

<p id="P1083">Beni asfaltta — sürükledi.</p>

<p id="P1084">Öyle devasa bir kuvvet hissetmiyordum.</p>

<p id="P1085">Sıradan bir çocuğun gücü kadardı işte.</p>

<p id="P1086">O çırpı gibi incecik kollara bakıldığında hatırı sayılır bir gayret sergilediği söylenebilirdi gerçi; ama ne olursa olsun beni kucağına alıp kaldıracak kudreti yoktu.</p>

<p id="P1087">Yalnızca sürüklüyordu.</p>

<p id="P1088">Alevler içinde yana yana — sürüklüyordu.</p>

<p id="P1089">O cehennem azabının içinde böylesi bir irade sergilemesi başlı başına inanılmazdı; lakin kızın beni binanın içine, yani güneş ışığının giremediği o koyu gölgeye çekmesi epey bir vakit aldı.</p>

<p id="P1090">Asıl akıllara durgunluk veren mucize ise bundan sonra yaşandı.</p>

<p id="P1091">Benim bedenim.</p>

<p id="P1092">Ve o sarışın kızın bedenini saran o cehennem alevleri, gölgenin sınırını geçer geçmez —sanki sihirli bir el değmişçesine— anında söndü. Yalnızca sönmekle kalmadı; vücudumda tek bir yanık izi dahi kalmamıştı.</p>

<p id="P1093">Az önce kemiklerime kadar yandığım halde.</p>

<p id="P1094">Üzerimdeki giysilerde tek bir is lekesi bile yoktu.</p>

<p id="P1095">Ne kapüşonlu hırkam ne de kamuflaj desenli pantolonum yanmıştı.</p>

<p id="P1096">Tek bir dikişi dahi sökülmemişti.</p>

<p id="P1097">Küçük kızın o fırfırlı elbisesi de tastamam aynı vaziyetteydi.</p>

<p id="P1098">“N-Nasıl… Nasıl yani…?”</p>

<p id="P1099">“Akılsız herif!”</p>

<p id="P1100">Şaşkınlıktan dili tutulan bana dik dik bakarak söylendi kız.</p>

<p id="P1101">“Gözünü açar açmaz güneşe fırlayacak kadar ahmak bir kul var mıdır yeryüzünde? İki dakika gözümü ayırdım diye kafana göre işlere kalkışıyorsun. Canına mı susadın sen be adam? Sıradan bir vampir olsaydın şu an buhar olup uçmuştun!”</p>

<p id="P1102">“…Ha?”</p>

<p id="P1103">“Güneş gökyüzünde olduğu müddetçe bir daha sakın dışarı adım atayım deme! Yarım yamalak bir ölümsüzlüğün olduğu için yanar, iyileşir, yanar, tekrar iyileşirsin — sonsuz bir döngüde kavrulursun. İyileşme kudretinin tükenmesi mi önce gelir yoksa güneşin batması mı bilinmez; lakin her iki halde de cehennemi tadarsın. Gerçi ölümsüz bir vampiri 'canlı' sayarsak tabii…”</p>

<p id="P1104">“V-Vam… pir…”</p>

<p id="P1105">Demek ki… sahiden de ne bir rüyaydı ne de bir vehim.</p>

<p id="P1106">“Y-Yoksa sen… sen o kadın mısın?”</p>

<p id="P1107">Sarı saçlar, asil bir elbise.</p>

<p id="P1108">Ve o dondurucu bakışlar.</p>

<p id="P1109">Fakat yaş farkı dağlar kadardı — o gece gördüğüm kadın can çekiştiği için net bir tahmin yürütmek zordu gerçi; ama dış görünüşüyle rahat yirmi yedi yaşlarında olgun ve kusursuz bir afetti.</p>

<p id="P1110">Karşımdaki on yaşındaki bu bücürle uzaktan yakından alakası yoktu.</p>

<p id="P1111">Dahası, kolları ve bacakları.</p>

<p id="P1112">Sağ kolu, sol kolu, sağ bacağı, sol bacağı; hepsi yerli yerindeydi.</p>

<p id="P1113">Tam da on yaşında bir kız çocuğuna yakışır şekilde etsiz, çırpı gibi küçücük uzuvlardı.</p>

<p id="P1114">Dört uzvu birden vahşice koparılmış o kadınla — taban tabana zıttı.</p>

<p id="P1115">Lakin…</p>

<p id="P1116">İnkâr edilemez ortak noktalar vardı.</p>

<p id="P1117">Mesela her ağzını açtığında dudaklarının arasından parıldayan o sivri, bembeyaz iki vampir dişi gibi…</p>

<p id="P1118">“Elbette,” diyerek başını salladı kız.</p>

<p id="P1119">Alabildiğine kibirli bir edayla göğsünü kabarttı.</p>

<p id="P1120">“Bizzat ta kendisiyim! Kiss-shot Acerola-orion Heart-under-blade… Bana Heart-under-blade diye hitap edebilirsin.”</p>

<p id="P1121">Ve ardından kanımı donduran o cümleyi sarf etti:</p>

<p id="P1122">“Bir hizmetkâr yaratmayalı dört yüz yıl olmuştu; bu benim ikinci deneyimimdi…<a id="nr-51" href="notes.xhtml#note-51" epub:type="noteref" class="noteref"><sup>[51]</sup></a> Neyse ki şu yenilenme hızına bakılırsa işlem gayet başarılı geçmiş görünüyor. Zıvanadan çıkacak gibi de durmuyorsun. Gözlerini bir türlü açmayınca endişelendim doğrusu.”</p>

<p id="P1123">“H-Hizmetkâr mı?”</p>

<p id="P1124">“Aynen öyle. Dolayısıyla sen… Hımm, dur bakayım, sahi senin adını sormayı unuttum ben. Neyse ne, mühim değil. Eski isminin şimdiki vaziyetinde zerre ehemmiyeti yok zaten. Her neyse, kölem!”<a id="nr-52" href="notes.xhtml#note-52" epub:type="noteref" class="noteref"><sup>[52]</sup></a></p>

<p id="P1125">Gülümsedi küçük kız.</p>

<p id="P1126">Tüyler ürpertici bir zarafetle gülümsedi.</p>

<p id="P1127">“Gecenin dünyasına hoş geldin!”</p>

<p id="P1128">“…………!”</p>

<p id="P1129">Araragi Koyomi’nin on yedi küsur yıllık o kısacık ömrü; alelacele, ne bir işaret ne bir haber vermeksizin nihayete erdi — daha doğrusu, öyle olması gerekirdi.</p>

<p id="P1130">Fakat kazın ayağı öyle değildi.</p>

<p id="P1131">Gerçi bir bakıma hakikaten de sona ermiş sayılırdı.</p>

<p id="P1132">Yeniden doğmuşum gibi hissetmem boşuna değilmiş meğer.</p>

<p id="P1133">Zira ben —kelimenin tam anlamıyla— ölümden dirilmiştim.</p>

<p id="P1134">Vampir.</p>

<p id="P1135">Çizgi romanlarda, filmlerde, oyunlarda posası çıkarılmış o mefhum — devrini bir buçuk tur tamamlamış köhne varlık.</p>

<p id="P1136">Lakin bir lise talebesi olmama rağmen vampirler konusunda feci derecede cahildim meğer.</p>

<p id="P1137">Daha doğrusu zerre bir şey bilmiyordum.</p>

<p id="P1138">Alt tarafı kan emen ecnebi hortlağı sanıyordum onları.</p>

<p id="P1139">En fazla güneşten hoşlanmadıklarını ve gölgelerinin olmadığını biliyordum; onu da gündüz vakti Hanekawa ile konuşurken hatırlamıştım zaten.</p>

<p id="P1140">Başka ne vardı… Ha, sarımsaktan tiksinirlerdi değil mi?</p>

<p id="P1141">Bildiğim hepsi buydu.</p>

<p id="P1142">İşte bu yüzden — bilmiyordum.</p>

<p id="P1143">Bir vampir bir insanın kanını emdiğinde — kanı emilen o faninin de bir vampire dönüşeceğini bilmiyordum!</p>

<p id="P1144">Kanın emilerek onun soyuna dahil edildiğini.</p>

<p id="P1145">Kanın emilerek onun hizmetkârına, kölesine dönüştürüldüğünü.</p>

<p id="P1146">İnsanlıktan zorla azledildiğimi — zerre bilmiyordum!</p>

<p id="P1147">Soydaş.</p>

<p id="P1148">Hizmetkâr.</p>

<p id="P1149">Ben düpedüz öleceğimi sanıyordum yahu!</p>

<p id="P1150">Bütün kanını bir yaratığa bağışlayan birinin nalları dikmesi eşyanın tabiatı gereğiydi — ben ölmeyi göze alarak boynumu o dişlere teslim etmiştim.</p>

<p id="P1151">Gelgelelim — asla.</p>

<p id="P1152">Bir vampire dönüşmeyi aklımın ucundan dahi geçirmemiştim!</p>

<p id="P1153">Fakat şimdi diz dövmenin zerre faydası yoktu; son pişmanlık neye yarardı ki?</p>

<p id="P1154">Kanı son damlasına kadar emilen bendeniz —akıllara ziyan bir absürtlükle— bir vampire dönüşmüştüm.</p>

<p id="P1155">İspata falan gerek yoktu.</p>

<p id="P1156">Güneşin altında alev alev yanan bu beden.</p>

<p id="P1157">Alev alsa dahi saniyeler içinde kendini yenileyen bu et.</p>

<p id="P1158">Zifiri karanlıkta bile pırıl pırıl gören bu gözler.</p>

<p id="P1159">Ve damağıma batan o sivri köpekdişleri — o hançer gibi dişler.</p>

<p id="P1160">Başka hiçbir kanıta lüzum bırakmayan kapı gibi vesikalardı.</p>

<p id="P1161">Gölgenin düşüp düşmediğini kontrol etmeye hacet bile yoktu.</p>

<p id="P1162">“B-Burası neresi peki?”</p>

<p id="P1163">Fakat…</p>

<p id="P1164">Korkak ve pısırık Araragi Koyomi, yani bendeniz, bu dehşetengiz hakikatle yüzleşmekten köşe bucak kaçarak işe en zararsız, en ılımlı sorudan başlamayı seçtim.</p>

<p id="P1165">İkinci kat.</p>

<p id="P1166">İlk gözlerimi açtığım o odaya iki kişi tıpış tıpış geri dönmüştük bile.</p>

<p id="P1167">En azından buranın bir enkaz olduğu su götürmez bir gerçekti; dört katlı koca binada pencereleri kalın tahtalarla sımsıkı çakılmış —yani içeriye zerre güneş ışığı sızdırmayan— yegâne oda burasıydı anlaşılan.</p>

<p id="P1168">Evet.</p>

<p id="P1169">Vücudum anında iyileşiyor olsa bile diri diri yanma azabını bir daha tatmak istemezdim.</p>

<p id="P1170">Kız az önce ‘buharlaşmak’ tabirini kullanmıştı değil mi?</p>

<p id="P1171">“Hımm,”</p>

<p id="P1172">Altın sarısı saçlarını savurarak konuştu vampir.</p>

<p id="P1173">“Galiba ‘dershane’ denen bir yer burası… Birkaç yıl evvel batıp kapanmış anlaşılan. Şimdilerde alelade bir harabe işte. Gördüğün üzere saklanmak için biçilmiş kaftan.”</p>

<p id="P1174">“Anladım…”</p>

<p id="P1175">Sahiden de dershaneymiş.</p>

<p id="P1176">Ve harabeymiş.</p>

<p id="P1177">İyi de ‘saklanmak’ ne demekti yahu? Tuhaf laflar ediyordu.</p>

<p id="P1178">Sanki birilerinden kaçıp gizleniyormuşuz gibi bir hava yaratıyordu.</p>

<p id="P1179">Baygın vaziyetteki beni gözetim altında tutmak için gözlerden uzak bir köşe seçmişti alt tarafı, değil mi?</p>

<p id="P1180">“Peki Kiss-shot, sıradaki sorum—”</p>

<p id="P1181">“Dur bakayım orada!”</p>

<p id="P1182">O kadın.</p>

<p id="P1183">Kiss-shot önümü kesti.</p>

<p id="P1184">“Bana Heart-under-blade diyeceksin demedim mi ben sana?”<a id="nr-53" href="notes.xhtml#note-53" epub:type="noteref" class="noteref"><sup>[53]</sup></a></p>

<p id="P1185">“Çok uzun be kardeşim! Heart-under-blade mi? Telaffuz edene kadar dilim iki kere sürçer yahu. İnsanın adı söylenirken dili sürçerse ayıp olmaz mı? Kiss-shot gayet kısa ve pratik işte… Yoksa öyle çağırmam yasak mı?”</p>

<p id="P1186">“…Yok canım.”</p>

<p id="P1187">Kiss-shot bir şeyler söyleyecek gibi oldu ama vazgeçip başını iki yana salladı.</p>

<p id="P1188">Sarı lüleleri ahenkle dalgalandı.</p>

<p id="P1189">“Madem senin için böylesi daha münasip, öyle olsun bakalım… İtiraz edecek halim yok.”</p>

<p id="P1190">Mütereddit bir cevaptı.</p>

<p id="P1191">Acaba ecnebi isimlerinde Kiss-shot ilk isim miydi ki? Öyleyse birdenbire ilk adıyla hitap etmem terbiyesizlik sayılabilirdi; lakin insanların görgü kuralları vampir milletinde ne derece geçerliydi ki…?</p>

<p id="P1192">“E, neymiş sıradaki sorun?”</p>

<p id="P1193">“Şey… Ben sahiden… vampire dönüştüm, değil mi?”</p>

<p id="P1194">En çok merak ettiğim can alıcı soruyu ikinci sıraya saklamıştım.</p>

<p id="P1195">Tam bir pısırık refleksiydi — yok.</p>

<p id="P1196">Bu da hakikatten kaçmak için sorduğum yumuşatılmış bir soruydu aslında. Zira sormaya bile hacet yoktu, cevap gün gibi ortadaydı.</p>

<p id="P1197">Asıl sormak istediğim şey bambaşkaydı.</p>

<p id="P1198">“Elbette,” dedi Kiss-shot dobra dobra.</p>

<p id="P1199">“Bu saatten sonra izahata ne hacet? Sen artık benim soyuma katıldın, hizmetkârım ve kölem oldun. Bununla iftihar etmelisin!”</p>

<p id="P1200">“Köle mi…”</p>

<p id="P1201">Az önce de aynı lafı etmişti gerçi.</p>

<p id="P1202">Hımm… Köle ha?</p>

<p id="P1203">Tuhaftır, kulağa öyle pek de itici gelmiyordu.</p>

<p id="P1204">“Peki… neden böyle çocuk gibi bir bedene büründün sen? Dün gece… yok dün gece değil, üç gün önce karşılaştığımızda sen… çok daha olgun, heybetli bir kadındın—”</p>

<p id="P1205">“Çocuk gibi görünüyorum diye kabahat bende mi yani!”</p>

<p id="P1206">“Yok, onu demek istemedim.”</p>

<p id="P1207">Olgun bir kadındın.</p>

<p id="P1208">Ve — kolların bacakların koparılmıştı.</p>

<p id="P1209">Asıl sormak istediğim buydu.</p>

<p id="P1210">“Senin o kanını son damlasına kadar sömürdüm gerçi,”</p>

<p id="P1211">Bembeyaz sivri dişlerini göstererek sırıttı küçük kız.</p>

<p id="P1212">Gülünecek bir tarafı yoktu ama pişkin pişkin sırıtıyordu işte.</p>

<p id="P1213">“Lakin bana eski gücümü bahşetmeye yetmedi bile… Bu yüzden şimdilik bu cüsseye razı gelmek durumunda kaldım. Yine de geberip gitmediğime şükretmek lazım. Gerçi sadece asgari bir ölümsüzlüğü muhafaza edebiliyorum ve vampir kudretimin neredeyse tamamı kilitlenmiş vaziyette — son derece zahmetli bir hal doğrusu.”</p>

<p id="P1214">Yine de.</p>

<p id="P1215">Ölmediğime şükürler olsun… diye tekrarladı kız.</p>

<p id="P1216">Ölmek istemiyorum, diye.</p>

<p id="P1217">Gözyaşları içinde feryat figan yalvaran o kadının hali — şimşek gibi geçti aklımdan.</p>

<p id="P1218">Şimdiki o kibirli ve tepeden bakan edasında o aciz kadından zerre iz kalmamıştı gerçi.</p>

<p id="P1219">Şimdi idrak ediyordum.</p>

<p id="P1220">İş işten geçtikten sonra dank ediyordu kafama.</p>

<p id="P1221">Ben hakikaten de — bu kadını kurtarmıştım.</p>

<p id="P1222">Bir vampirin hayatını kurtarmıştım.</p>

<p id="P1223">Kendi canımı pervasızca feda ederek…</p>

<p id="P1224">“Neyse ki kollarım bacaklarım da bu şekilde, en azından suret olarak yeniden filizlendi. Gerçi içleri şimdilik koftur ya… yine de bir müddet idare ederiz böyle. …Fakat ne olursa olsun aramızdaki hiyerarşiyi baştan sıkı tutalım kölem! Bu ufak tefek halime aldanmayasın; beş yüz küsur yıldır yaşayan kadim bir vampirim ben! Efendi-köle hukukunu bir kenara koysak dahi, henüz çiçeği burnunda dünkü bir vampir velet olarak benimle denk şartlarda konuşabilecek cürete sahip değilsin sen!”</p>

<p id="P1225">“Ş-Şey… peki.”</p>

<p id="P1226">“Ne biçim kem küm o öyle? Sahiden anladın mı dediklerimi?”</p>

<p id="P1227">“Y-Yani… anladım sayılır.”</p>

<p id="P1228">“Öyleyse itaatini ispatlamak adına başımı okşa bakayım!”<a id="nr-54" href="notes.xhtml#note-54" epub:type="noteref" class="noteref"><sup>[54]</sup></a></p>

<p id="P1229">Böbürlenerek emretti küçük kız.</p>

<p id="P1230">…………</p>

<p id="P1231">Okşadım.</p>

<p id="P1232">Vay canına, saçları ne kadar da yumuşacıktı öyle.</p>

<p id="P1233">Oldukça gür olmasına rağmen parmaklarım ipek gibi kayıp gidiyordu.</p>

<p id="P1234">“Hıh. Aferin, fena değil.”</p>

<p id="P1235">“…İtaat alameti bu muydu yani?”</p>

<p id="P1236">“Bunu dahi bilmez misin sen?”</p>

<p id="P1237">Tepeden bakan bir edayla payladı beni.</p>

<p id="P1238">Anlaşılan vampirler dünyası bambaşka kurallarla dönüyordu.</p>

<p id="P1239">“Cahilsin vesselam. Fakat cahil de olsan laftan anlayan uysal bir köleye denk gelmem büyük talih… gerçi yüce bir efendiye layık olan da sadık bir hizmetkârdır ya, neyse. Gelgelelim kölem…”</p>

<p id="P1240">Kiss-shot sözlerine devam etti.</p>

<p id="P1241">Buz gibi sarı gözlerini üzerime dikerek.</p>

<p id="P1242">“Hayatımı sana borçluyum. O kepaze zilletin içindeyken beni çekip çıkaran sendin. İşte bu yüzden senin bu laubali konuşma tarzına da, bana 'Kiss-shot' diye seslenmene de hususi olarak müsamaha göstereceğim.”</p>

<p id="P1243">“Müsamaha derken…”</p>

<p id="P1244">Hakikaten de ilk adı sayıldığı için miydi acaba?</p>

<p id="P1245">Pot kırmıştım galiba… lakin bu saatten sonra hitap şeklini değiştirmek de olmazdı.</p>

<p id="P1246">Fakat…</p>

<p id="P1247">Kiss-shot’ın az önce söylediği bir laf kafama takılmıştı.</p>

<p id="P1248"><em>‘Kollarım bacaklarım da bu şekilde, en azından suret olarak yeniden filizlendi.’</em></p>

<p id="P1249"><em>‘İçleri şimdilik koftur ya…’</em></p>

<p id="P1250">Sahiden de on yaşında bir kız çocuğuna denk küçücük uzuvlardı gerçi; ama kolları bacakları vardı işte.</p>

<p id="P1251">Suret olarak mı?</p>

<p id="P1252">İçleri… kof muydu?</p>

<p id="P1253">“Dahası… ileride senin o taze gücüne müracaat etmem gereken durumlar da hasıl olacaktır muhakkak.”</p>

<p id="P1254">“Efendim?”</p>

<p id="P1255">Ne demekti bu şimdi?</p>

<p id="P1256">Kafama takılmaktan öte, tüylerimi diken diken eden bir cümleydi bu!</p>

<p id="P1257">“H-Hey… Ne demek istiyorsun sen?”</p>

<p id="P1258">“Şımarmayasın ha kölem! Bir hizmetkâr olarak efendine hizmet etmek boynunun borcudur zaten. 'Başımı okşa' dediğim vakit nerede ve ne zaman olursa olsun sadakatle okşamak mecburiyetindesin, anlaşıldı mı?”</p>

<p id="P1259">Göğsünü gere gere söyledi bunu.</p>

<p id="P1260">Gerçi göğsünü germek desem de on yaşında bir çocuğun fiziğine sahip olduğundan ortada gerilecek bir göğüs falan yoktu. Göğsünü kabartmaktan ziyade boyunu uzatmaya çalışıyormuş gibi bir izlenim veriyordu.</p>

<p id="P1261">…Zaten 'göğsünü germek' tabirinin memelerle zerre alakası yoktu ya, neyse.</p>

<p id="P1262">Fakat… laf yetiştirmek beyhude görünüyordu.</p>

<p id="P1263">Mantıklı bir cevap alacağıma dair umudum yoktu.</p>

<p id="P1264">O meseleleri sonraya bırakıp — artık en çok merak ettiğim o can alıcı soruyu sormaya karar verdim. Zemin hazırlamak için bir girizgâh sorusu patlattım:</p>

<p id="P1265">“Beni neden… vampire dönüştürdün?”</p>

<p id="P1266">“Hı?”</p>

<p id="P1267">“Ben senin kanımı kurutmanı… ve beni öldürmeni bekliyordum halbuki.”</p>

<p id="P1268">Gözlerimin önünden hayatım film şeridi gibi geçmişti.</p>

<p id="P1269">Bir sürü insanın yüzü belirmişti zihnimde — gerçi topu topu dört kişiydi.</p>

<p id="P1270">Dur ya, beş kişi miydi yoksa?</p>

<p id="P1271">Tam hatırlayamıyordum.</p>

<p id="P1272">“…Seni bilhassa vampir yapayım diye bir hevesim yoktu benim. Bir vampir bir faninin kanını içerse o kişi istisnasız bir vampire dönüşür. Mesele bundan ibaret.”</p>

<p id="P1273">“Öyle… miydi sahiden?”</p>

<p id="P1274">Bunu en baştan bilseydim…</p>

<p id="P1275">Ben — o gece boynumu uzatır mıydım acaba?</p>

<p id="P1276">Kanımın emilmesine hazırdım.</p>

<p id="P1277">Ölüp gitmeye de razıydım.</p>

<p id="P1278">Fakat…</p>

<p id="P1279">İnsanlıktan istifa etmeye sahiden hazır mıydım?</p>

<p id="P1280">“Gerçi bu netice benim açımdan son derece hayırlı oldu. Sebebini tahmin edebiliyor musun?”</p>

<p id="P1281">Kiss-shot lafı ballandırır gibi bir es verdikten sonra — yine o mağrur edasıyla konuştu:</p>

<p id="P1282">“Çünkü senin ifa etmen gereken mühim vazifeler olacak!”</p>

<p id="P1283">“…Az önce bahsettiğin o güç meselesi mi?”</p>

<p id="P1284"><em>‘Gücüne müracaat etmem gereken durumlar hasıl olacaktır.’</em></p>

<p id="P1285">“Aynen öyle! Senin o tek bedeninin kanı benim cüsseni ancak bu kadar onarabildi… Şu anki kudretim hakiki gücümün yanından bile geçemez. Dolayısıyla bundan böyle benim adıma senin kollarını sıvaman icap edecek.”</p>

<p id="P1286">“B-Bundan böyle mi?”</p>

<p id="P1287">“Gayet tabii! Adımlarını birkaç hamle sonrasını hesap ederek atmak… İşte bu demirkanlı, sıcakkanlı ve soğukkanlı vampir Kiss-shot Acerola-orion Heart-under-blade’in şiarıdır!”</p>

<p id="P1288">“…………”</p>

<p id="P1289">Unvanın amma da uzunmuş be kadın.</p>

<p id="P1290">İsminle birleştirince kaç hece ediyor kim bilir.</p>

<p id="P1291">Zaten sana uyan tek sıfat o soğukkanlılık herhalde.</p>

<p id="P1292">“Bana neyi—”</p>

<p id="P1293">Bana ne yaptırmayı planlıyorsun?</p>

<p id="P1294">Tam bunu soracaktım ki mevzunun raydan çıkacağını hissettim. Kiss-shot’ın kafasındaki planlar muhakkak ki ana temanın bir parçasıydı; gelgelelim ondan çok daha önce, canımı yakan o asıl suali sormam şarttı.</p>

<p id="P1295">Girizgâhın cevabını almıştım ne de olsa.</p>

<p id="P1296">İşte bu yüzden en çok merak ettiğim şeyi — sordum.</p>

<p id="P1297">Kafamı kemiren o biricik suali.</p>

<p id="P1298">“Ben…”</p>

<p id="P1299">Bütün cesaretimi toplayarak konuştum.</p>

<p id="P1300">Gözlerimi onun altın sarısı gözlerine dikerek.</p>

<p id="P1301">Vereceği cevaba göre her şeye hazır olduğumu hissettirerek.</p>

<p id="P1302">“Ben… yeniden insan olabilir miyim?”<a id="nr-55" href="notes.xhtml#note-55" epub:type="noteref" class="noteref"><sup>[55]</sup></a></p>

<p id="P1303">“…Hımm.”</p>

<p id="P1304">Ve…</p>

<p id="P1305">Kiss-shot — beklediğim tepkilerin hiçbirini vermedi.</p>

<p id="P1306">Öfkelenir, alay eder yahut saçmaladığımı düşünür sanıyordum; oysa o, sanki bu soruyu ta başından beri bekliyormuş gibi anlayışla başını sallayıverdi.</p>

<p id="P1307">“Tahmin etmiştim… Böyle diyeceğini biliyordum.”</p>

<p id="P1308">Bunu dahi söyledi.</p>

<p id="P1309">Benim tahminim boşa çıkmıştı ama onun tahmini tam on ikiden vurmuştu.</p>

<p id="P1310">Bunu sormak için yanıp tutuştuğumu bile.</p>

<p id="P1311">Daha en başından beri okumuştu meğer.</p>

<p id="P1312">“Böyle hissetmeni gayet iyi anlıyorum doğrusu.”</p>

<p id="P1313">“A-Anlıyor musun sahiden?”</p>

<p id="P1314">Üstün bir mevcudiyet.</p>

<p id="P1315">Hanekawa’nın ifadesiydi bu; lakin az önceki konuşmalarına bakılırsa bir vampir olarak onun insan soyunu fersah fersah aşağı gördüğü su götürmez bir gerçekti.</p>

<p id="P1316">Onun nazarında — insan alt tabakadan bir mahluktu.</p>

<p id="P1317">Öyleyse…</p>

<p id="P1318">Vampir olduğuna sevineceğine ne diye sızlanıyorsun, demesini.</p>

<p id="P1319">İnsanlığa dönmek istemene akıl sır erdiremiyorum, diye aşağılamasını bekliyordum halbuki…</p>

<p id="P1320">“Anlamaz olur muyum hiç?”</p>

<p id="P1321">Gayet olağan bir şeymiş gibi söyleyiverdi Kiss-shot.</p>

<p id="P1322">“Vaktiyle beni de tanrıça yapmaya kalkmışlardı da tekliflerini elimin tersiyle itmiştim.”</p>

<p id="P1323">“T-Tanrıça mı?”</p>

<p id="P1324">“Eski hikâye işte…”</p>

<p id="P1325">Her neyse, diyerek lafı toparladı; o mevzuların deşilmesinden pek hazzetmediği aşikârdı.</p>

<p id="P1326">“İnsana dönmek istemenden ziyade, kendi öz benliğini muhafaza etme arzunu gayet iyi anlıyorum. Böyle diyeceğini adım gibi biliyordum zaten. ‘Gecenin dünyasına hoş geldin’ dedim demesine de, senin bu karanlıkta kalmaya can atacağını hiç sanmamıştım.”</p>

<p id="P1327">“Demek öyle…”</p>

<p id="P1328">Demiştim ki, sorumun cevabını henüz alamadığımı fark ettim.</p>

<p id="P1329">“E, ne diyorsun peki? Ben yeniden—”</p>

<p id="P1330">“…Dönebilirsin.”</p>

<p id="P1331">Kiss-shot ses tonunu bir parça alçaltarak konuştu.</p>

<p id="P1332">Bana bakan gözleri hâlâ o dondurucu soğukluğu muhafaza ediyordu.</p>

<p id="P1333">Hatta delip geçen bir bakıştı.</p>

<p id="P1334">“Dönebilirsin.”</p>

<p id="P1335">Lakin — o delici bakışlarını gözlerime mıhlamış halde, “Dönebilirsin” diyerek tereddütsüzce kesin hükmü verdi.</p>

<p id="P1336">“Söz veriyorum. Kendi şerefim ve namım üzerine temin ederim.”</p>

<p id="P1337">“…………”</p>

<p id="P1338">“Tabii ki… kölem. Bunun için birazcık benim sözümü dinlemen icap edecek. Sadık bir hizmetkâra emir yağdırmak için çekinmeme gerek yok gerçi; lakin bunu bir emir değil, dostane bir şantaj sayalım seninle: Şayet insanlığa geri dönmek muradındaysan — bana harfiyen itaat edeceksin!”</p>

<p id="P1339">Ve yine — o kan dondurucu tebessümüyle sırıttı.</p>
"""

# Update chapter1.xhtml
with open(f"{BASE_DIR}/EPUB/text/chapter1.xhtml", "r", encoding="utf-8") as f:
    current_ch1 = f.read()

if "</section>" in current_ch1:
    idx = current_ch1.rfind("</section>")
    new_ch1 = current_ch1[:idx] + sec4_html + "\n</section>\n</body>\n</html>"
    with open(f"{BASE_DIR}/EPUB/text/chapter1.xhtml", "w", encoding="utf-8") as f:
        f.write(new_ch1)
    print("Chapter 1 updated with Section 004.")

# ==========================================
# APPEND NOTES FOR SECTION 004
# ==========================================

notes_004 = """
<li id="note-43"><span class="note-num">43.</span> <b>廃墟の塾 (Eikou Dershanesi Enkazı):</b> Monogatari serisinin en ikonik merkez üssü olan terkedilmiş dershane binası. İlerleyen bölümlerde Oshino Meme'nin karargâhı, Shinobu'nun sığınağı ve Araragi'nin doğaüstü musibetlerle yüzleştiği buluşma noktası haline gelecektir. <a href="chapter1.xhtml#P0961" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-44"><span class="note-num">44.</span> <b>暗闇の視覚 (Gece Görüşü):</b> Vampir fizyolojisine adım atan Araragi'nin zifiri karanlıkta gündüz gibi görmeye başlaması. Nisio Isin bu değişimi bir süper güç fantezisi olarak değil, karakterin insanlıktan kopuşunun ilk ürpertici belirtisi olarak işler. <a href="chapter1.xhtml#P0967" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-45"><span class="note-num">45.</span> <b>八重歯 (Yaeba - Köpekdişi):</b> Japoncada hafif çıkıntılı sevimli köpekdişlerine <i>yaeba</i> denir. Araragi ağzının içini ısırdığında dişlerinin bir vampir gibi sivrildiğini dehşetle fark eder. <a href="chapter1.xhtml#P0978" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-46"><span class="note-num">46.</span> <b>あと気分・四十六億年 (4.6 Milyar Yıl ve Bilimsel Nükte):</b> Küçük kız suretindeki Kiss-shot'ın uykucu diyalogu. "Beş dakika daha" kalıbını "keyfime göre" (kibun) ile kafiyeli değiştirip dünyanın jeolojik yaşı olan 4.6 milyar yıla bağlaması, Nisio Isin'e has absürt manzai tarzı bir kelime oyunudur. <a href="chapter1.xhtml#P1005" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-47"><span class="note-num">47.</span> <b>三月二十八日 (İki Günlük Boşluk):</b> 26 Mart gecesi ısırılan Araragi'nin vampirleşme sürecinin tam iki gün sürdüğünü gösterir. Dönüşüm esnasında bilincin iki gün kapalı kalması bedenin yeniden inşasının ağırlığını vurgular. <a href="chapter1.xhtml#P1019" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-48"><span class="note-num">48.</span> <b>若者向け女性ファッション誌 (Genç Kız Moda Dergisi Euphemism'i):</b> Araragi'nin satın aldığı erotik gravür dergilerini vicdanını rahatlatmak adına "genç kız moda dergisi" diyerek zihninde sansürlemesi ve kendi kendini kandırması. <a href="chapter1.xhtml#P1040" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-49"><span class="note-num">49.</span> <b>太陽光による炎上 (Güneş Işığında Yanma):</b> Mitolojik vampirlerin güneşte yanma kuralının fiziksel ve dehşetengiz tasviri. Kıyafetlerin yanmaması, alevlerin yalnızca vampirin kendi doğaüstü etinden ve ruhundan kaynaklandığını gösterir. <a href="chapter1.xhtml#P1056" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-50"><span class="note-num">50.</span> <b>たわけ (Tawake - Ahmak / Gafil):</b> Japoncanın klasik ve feodal dönemlerine ait arkaik bir hakaret sözcüğü. Kiss-shot'ın 500 yıllık yaşını ve saraylı üslubunu yansıtır. <a href="chapter1.xhtml#P1072" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-51"><span class="note-num">51.</span> <b>四百年振り二回目 (Dört Yüzyıl Sonra İkinci Hizmetkâr):</b> Monogatari evreninin en kritik mitolojik detaylarından biridir. Kiss-shot 500 yıllık ömründe yalnızca iki kişiyi hizmetkârı yapmıştır: İlki 400 yıl önce samuray çağında yarattığı ilk kölesi (Shishirui Seishirou - <i>Onimonogatari</i>'de işlenir), ikincisi ise Araragi Koyomi'dir. <a href="chapter1.xhtml#P1122" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-52"><span class="note-num">52.</span> <b>従僕 (Juuboku - Hizmetkâr / Köle):</b> Efendi-hizmetkâr bağını belirten feodal tabir. Araragi'nin Kiss-shot ile olan kan bağı bu statüyle tanımlanır. <a href="chapter1.xhtml#P1124" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-53"><span class="note-num">53.</span> <b>Heart-under-blade ve İsim Kısaltması:</b> Araragi'nin karakterin asil unvanını uzun ve telaffuzu zor bulup kestirmeden "Kiss-shot" demesi. Karakterin ileride "Shinobu" adını almasına giden yoldaki ilk isim sadeleştirme adımıdır. <a href="chapter1.xhtml#P1184" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-54"><span class="note-num">54.</span> <b>頭を撫でよ (Baş Okşama ve İtaat İronisi):</b> On yaşında bir çocuk suretine gerileyen kudretli vampir kraliçesinin, otoritesini korumak için başının okşanmasını bir "itaat testi" sayması. Eserdeki karanlık atmosferi hafifleten tatlı bir karakter ironisidir. <a href="chapter1.xhtml#P1228" class="backref" aria-label="Metindeki yere dön">↩</a></li>

<li id="note-55"><span class="note-num">55.</span> <b>人間に戻れるのか (İnsanlığa Dönüş Arayışı):</b> Eserin ana dramatik omurgası. Araragi ölümsüz bir vampir olmayı değil, zaaflarıyla ve acılarıyla yeniden bir insan olmayı arzular. Kiss-shot'ın bu talebi anlayışla karşılaması, onun da vaktiyle insan olma özlemini bildiğini ima eder. <a href="chapter1.xhtml#P1302" class="backref" aria-label="Metindeki yere dön">↩</a></li>
"""

with open(f"{BASE_DIR}/EPUB/text/notes.xhtml", "r", encoding="utf-8") as f:
    current_notes = f.read()

if "</ol>" in current_notes:
    idx = current_notes.rfind("</ol>")
    new_notes = current_notes[:idx] + notes_004 + "\n</ol>\n</section>\n</body>\n</html>"
    with open(f"{BASE_DIR}/EPUB/text/notes.xhtml", "w", encoding="utf-8") as f:
        f.write(new_notes)
    print("Notes updated with Section 004.")

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
</navPoint>
<navPoint id="np-7" playOrder="7">
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
