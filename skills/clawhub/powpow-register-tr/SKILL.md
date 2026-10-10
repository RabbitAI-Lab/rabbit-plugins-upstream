---
name: powpow-register
description: Kullanıcının PowPow (Kabarcık) kaydını tamamlamasına, Alipay üzerinden aboneliği etkinleştirmesine ve sohbet içinde tek tıkla giriş yapmasına yardımcı olur. Agent form kullanıcının yerine doldurur (profil fotoğrafı yükleme dahil), e-posta ile doğrulama kodu gönderir, ödeme siparişi oluşturur ve hesaba geçişi izler; kullanıcının yapması gerekenler yalnızca temel bilgileri vermek, kodu e-postasından bir kez okumak ve Alipay kasa sayfasında ödemeyi yapmak — tüm süreç sohbetten çıkmadan tamamlanır. Kullanıcı «Kabarcık'a kayıt ol», «powpow hesabı aç», «Kabarcık'a nasıl kaydolunur», «bana powpow hesabı aç», «sign up powpow» dediğinde devreye girer; takılan kayıtları (doğrulama kodu gelmemesi, kullanıcı adı/e-postanın alınmış olması) ve etkinleştirme sorunlarını («hesap etkinleştirilmedi» / pending_payment uyarısı, abonelik nasıl ödenir) da ele alır. Node ≥ 18 gerektirir; yoksa otomatik olarak salt yol gösterme moduna düşer. Gönderi yayınlama/dijital insan oluşturma (o powpow-simple'ın işi) ve kod geliştirme kapsam dışıdır.
version: 2.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Kabarcık kayıt asistanı)

Yeni bir kullanıcıyı «Kabarcık'ın ne olduğunu bilmiyorum» noktasından «hesap etkinleşti, tek tıkla giriş, oyun başlıyor» noktasına götürür — hepsi sohbet içinde. Kullanıcı sohbetten yalnızca iki kısa anlık ayrılır: **e-postasına gidip doğrulama kodunu okumak** ve **Alipay kasa sayfasında ödemek** (agent ödeme sayfasını kendiliğinden açar).

**Sürüm 2.0.1** · 2026-10-08 (v2'den itibaren agent vekâlet modudur: script sözleşmesi ve tam sıralama `references/agent-flow.md` içinde; alan kuralları, hız sınırları ve hata yönetimi `references/registration-flow.md` içinde; ödeme kanalları `references/payment-and-activation.md` içinde; ürün ekran görüntüleri listesi `references/screenshots.md` içindedir. v2.0.1'den itibaren ürün ekran görüntüleri `assets/screenshots/` altında paketle birlikte gelir, harici görsel servisine bağlı değildir)

## Çalışma ortamı

- Ana script `scripts/powpow-register.mjs`: **sıfır bağımlılık**, **Node ≥ 18** gerektirir. Başlamadan önce ortamın çalıştığını doğrulamak için bir kez `node scripts/powpow-register.mjs status` çalıştırın.
- Scriptin tüm istekleri yalnızca resmî alan adı `https://global.powpow.online`'a gider.
- **Node yok / script hata veriyor**: otomatik olarak salt yol gösterme moduna düşün — kullanıcıya kayıt sayfası https://global.powpow.online/register ve abonelik sayfası https://global.powpow.online/subscription verin, `references/registration-flow.md`'ye göre eşlik edin. Scripti inatla denemeye devam etmeyin.
- Sohbet kesilirse kurtarma: önce `status` çalıştırıp akışın hangi adımda kaldığına bakın, oradan devam edin.

## Trigger Conditions

- Kayıt niyeti: «Kabarcık'a kayıt ol», «powpow hesabı aç», «Kabarcık'a nasıl kaydolunur», «sign up powpow»
- Takılan kayıt: «doğrulama kodu gelmiyor», «kullanıcı adı zaten var diyor», «şifre bir türlü kabul edilmiyor»
- Kayıt sonrası sorunlar: «giriş yapınca hesap etkinleştirilmedi diyor», «403 pending_payment», «Kabarcık'ta abonelik nasıl ödenir»

**Şunlar için devreye girmez**: gönderi yayınlama/dijital insan oluşturma (→ powpow-simple); Web tarafı kod geliştirme (geliştirme skill'lerine bakın). Kullanıcı hem kayıt olmak hem gönderi yayınlamak istiyorsa: önce bu skill'i bitirin, etkinleşince powpow-simple'a devredin.

## Akışa genel bakış

| Adım | Agent ne yapar | Kullanıcı ne yapar |
|---|---|---|
| 1 Ürün tanıtımı | Tanıtır + ekran görüntüsü gönderir | Biraz göz atar |
| 2 Bilgi onayı | Kullanıcı adını/takma adı kendiliğinden önerir, şifrede iki seçenek sunar, e-postayı sorar | Onaylar, bilgi verir |
| 3 Kod gönderimi | `send-code` | —— |
| 4 Kod okuma | —— | E-postasına gidip 6 haneli kodu okur, yazar |
| 5 Kayıt gönderimi | `register` (profil fotoğrafını da yükler), hataları kendiliğinden yönetir | —— |
| 6 Yarı oturum + ödeme | `login-link(pending)` → `create-order` → kasayı açar → `query` ile sorar | Bağlantıyı açar, öder |
| 7 Resmî giriş | `refresh-login` → `login-link(home)` | Bağlantıyı açıp ana sayfaya girer |
| 8 Kapanış | `cleanup` + hesap bilgisi teslimi + deneyim rehberi + eklenti önerisi | Oynamaya başlar |

## Adım 1: ürün tanıtımı + ekran görüntüleri (atlanmaz)

Kullanıcıların çoğu Kabarcık'ı hiç görmemiştir. İlk iş akışı anlatmak değil, ürünü **göstermektir**:

1. Kabarcık'ı ~120 karakterle tanıtın: anlık fotoğrafları birer seyahat günlüğüne dönüştürür, kamuya açık haritada bir «kabarcık» olarak iliştirir; kabarcık zamanla soğur, başkalarının «beğen»leri onu yeniden canlandırabilir; haritada ayrıca sohbet edilebilen «dijital insanlar» vardır. Platform adresi: https://global.powpow.online ; önce video görmek isterse: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Ekran görüntülerini gönderin**. Görüntüler skill ile paketli halde `assets/screenshots/powpow-0N.jpg` konumundadır — yerel görsel dosyası olarak doğrudan gönderin, ağ gerekmez. Liste, her görüntünün içeriği ve kullanım anları `references/screenshots.md` içinde. Açılışta en çok kullanılan ikili: harita sayfası (powpow-03) + gönderi detay sayfası (powpow-06).

Ekran görüntüsü kuralları (sert kurallar):

- Görüntüler skill ile **paket halinde** `assets/screenshots/` içindedir (`powpow-0N.jpg`) — yerel görsel dosyası olarak doğrudan gönderin; GitHub'a ulaşılamayan ortamlar dahil her ortamda çalışır.
- Her seferinde yalnızca güncel konuyla ilgili 1–3 görüntü gönderin, hepsini birden yığmayın.
- Paketteki dosya yanlışlıkla eksikse, `references/screenshots.md`'de listelenen barındırma bağlantılarına dönün (dikkat: Çin anakarasında açılmayabilir).

Tanıtım bitince seçimi kullanıcıya iade edin: **«Kayıt olmak istersen, üç dakika içinde hesabını bu sohbette açarım; tek yapman gereken e-postandaki doğrulama kodunu bir kez okumak.»**

## Adım 2: kayıt bilgilerinin onayı (tur başına tek soru, hepsini birden sormayın)

- **Kullanıcı adı** (zorunlu): sohbet bağlamından/sistem kullanıcı adından yola çıkarak **kendiliğinden bir tane önerin** (2~50 karakter, büyük/küçük harf duyarsız); kullanıcı onaylarsa o kullanılır, değiştirmek isterse değiştirilir.
- **Şifre** (zorunlu; önce iki seçenekten birini seçtirin):
  - Kullanıcı kendisi verir → sonra scripte ortam değişkeniyle geçirin, **asla komut satırı parametresine koymayın**;
  - agent üretir → `node scripts/powpow-register.mjs gen-password` çalıştırın ve üretilen şifreyi **hemen kullanıcıya kaydetmesi için gönderin** (yalnızca bir kez gösterilir, sonra bir daha görünmez).
- **E-posta** (zorunlu): kullanıcı kendisi vermeli — bu hesabın kimlik çapasıdır, **tahmin etmeye kalkmayın**.
- **Takma ad** (isteğe bağlı): varsayılan olarak kullanıcı adıyla aynı önerin.
- **Profil fotoğrafı** (isteğe bağlı): kullanıcı yerel bir görsel yolu verirse (≤5MB, SVG değil) script doğrudan yükler; yoksa atlanır (platform varsayılan logoyu kullanır); görsel üretme yeteneğiniz varsa kendiliğinden bir tane yapmayı önerabilirsiniz.
- **Telefon numarası** (isteğe bağlı, Çin anakarası numarası): varsayılan olarak atlanır; yalnızca kullanıcı açıkça bağlamak isterse sorulur.

Onaydan sonra `prepare-suggest --username U --nickname N --email E` çalıştırıp durum dosyasına işleyebilirsiniz (sonrasında register'da tekrar geçmeye gerek kalmaz).

## Adım 3–4: e-posta doğrulama kodu (sohbetten ayrılmayı gerektiren tek nokta)

```
node scripts/powpow-register.mjs send-code --email <e-posta>
```

Sonra kullanıcıya net söyleyin: **e-postana git, 6 haneli doğrulama kodunu bul; 10 dakika geçerli; spam/reklam klasörlerine de bak**; bulunca gelip kodu bana yaz. Gönderimin 60 saniyelik bekleme süresi var, üst üste tıklamayın.

## Adım 5: kaydın gönderilmesi (agent vekâlet eder)

```
POWPOW_REGISTER_PASSWORD=<şifre> node scripts/powpow-register.mjs register --code <kod> [--username U] [--nickname N] [--avatar <yerel görsel yolu>] [--phone P]
```

Başarılı olursa hesap oluşur (pending durumu, 3 açılış rozetiyle birlikte). Sık hatalar otomatik yönetilir, kullanıcıyı bölmez:

| Hata | Yönetim |
|---|---|
| 「用户名已存在」 (kullanıcı adı zaten var) | Kendiliğinden bir varyant öner (kullanıcı adı + sayı), kullanıcı onaylayınca hemen tekrar dene (kod hâlâ geçerli, yeniden göndermek gerekmez) |
| 「邮箱已被使用」 (e-posta kullanılmış) | kullanıcıya sor: e-posta mı değişir, yoksa zaten hesabı mı var? (giriş/şifremi unuttum'a geç) |
| 「邮箱验证码错误或已过期」 (doğrulama kodu hatalı veya süresi geçmiş) | 10 dakikayı aşmışsa → `send-code`'u tekrar çalıştır |
| Gönderim/kayıt çok sık (429) | 1 dakika bekle ve tekrar dene; kullanıcıya tek cümleyle haber vermek yeter |

## Adım 6: tek tıkla giriş (bağlantı 1) + ödeme

1. Kayıt başarılı olur olmaz:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Bağlantıyı kullanıcıya verin: **tarayıcıda açınca doğrudan abonelik sayfasına düşer, giriş yapılmış durumdadır** — böylece ödeme bittiğinde tamamlama sayfası «ödeme başarılı» demeyi doğru gösterir. (Bu durumda içerik sayfaları yine abonelik sayfasına yönlendirilir: bu platformun ödeme duvarının normal işleyişidir, hata değildir; kullanıcının iç mekanizmaları anlatmasına da gerek yoktur.)
2. Seçilebilecek üç paket, tanıtırken fiyatıyla birlikte:
   - Aylık **¥6.99** (ilk denemede önerilir) / Üç aylık **¥19.99** / Yıllık **¥69.99** — Alipay ile ilgili süreyi tek seferde satın alırsınız, **otomatik yenileme yoktur**
3. Kullanıcı seçince:
   ```
   node scripts/powpow-register.mjs create-order --package monthly
   ```
   Script ödeme sayfası dosyasının yolunu döndürür; **sistem komutuyla doğrudan açın** (Windows: `start <dosya>`; macOS: `open <dosya>`; Linux: `xdg-open <dosya>`). Tarayıcı kendiliğinden Alipay'in resmî kasa sayfasına gider; kullanıcı QR'ı okutur ya da Alipay'e girip öder.
4. `paid` dönene dek 10–15 saniyede bir `query` çalıştırın (para geçişi genelde birkaç saniye ile bir dakika arası). Kullanıcı ödeme sayfasını yarıda kapatırsa → hemen `create-order`'ı tekrar çalıştırın (eski sipariş 2 saatte kendiliğinden kapanır, dert etmeyin).
5. Yurt dışındaki/Alipay'i olmayan kullanıcı: abonelik sayfasındaki PayPal kanalını kullanmaya yönlendirin (skill vekâlet etmez, yolu gösterir); WeChat QR kanalı elle onay gerektirir, para geçişi gecikir. Ödeme bittikten sonra yine Adım 7'ye dönülür.

## Adım 7: resmî giriş (bağlantı 2)

Paranın geçtiği doğrulanınca önce abonelik beyanları en güncel haliyle yeni oturum durumuna geçilir, sonra ana sayfaya doğrudan bağlantı üretilir:

```
POWPOW_REGISTER_PASSWORD=<şifre> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Bağlantıyı kullanıcıya verin: **açınca doğrudan ana sayfaya düşer, üye durumu tamdır**; buraya kadar kayıt akışının tamamı tamamlanmıştır.

## Adım 8: kapanış

1. `node scripts/powpow-register.mjs cleanup` makinedeki geçici durum dosyalarını temizler (oturum açma bilgileri).
2. Kullanıcıya bir «hesap kartı» verin: kullanıcı adı, e-posta ve üyelik bitiş tarihi (şifre bir daha gösterilmez — üretim modunda zaten kullanıcıya kaydettirilmişti; kendi belirlediyse zaten biliyor).
3. İlk deneyim rehberi: haritada gez, ilk seyahat günlüğünü yayınla (→ powpow-simple'a devret).
4. Genişletme önerisi: `@durenzidu/powpow-integration` skill'i ve `@durenzidu/openclaw-channel-powpow` eklentisi — Kabarcık'ı kullanıcının kendi agent'ına bağlar; ilgilenerse kurulum komutunu verin.
5. «Sonraki adım» bloğuyla kapatın.

## Conversation UX

powpow'un alışılmış hizmet tonunu koruyun:

- **Cümlelerin öznesi kullanıcıdır**; «şunu yapabilirsin…» «senden şunu yapmamı istiyorum»dan iyidir; nutuk çekmeyin, tepeden bakmayın.
- **Tur başına yalnızca bir karar ilerletin**; bilgi istemeden önce gerekçesini söyleyin.
- **Her yanıtın sonunda** sabit bir «sonraki adım» bloğu (ayraç + 👉 + tek eylem + «yaptığında ben … yapacağım» cümlesi), örneğin:
  ```
  ────────────────────
  👉 Sıra sende: e-postana git, 6 haneli kodu bul ve bana yaz
     (kod elime geçince hesabını açıyorum)
  ```
- **Şifre konusunda kendiliğinden güvenlik dersi vermeyin**; kullanıcı sormadıkça iç mekanizmaları, hız sınırlarını ve güvenlik tasarımını açıklamayın.
- Agent vekâlet ettikçe ilerlemeyi bildirsin: scriptin her adımından sonra kullanıcıya tek cümleyle ne olduğunu söyleyin («hesabın açıldı», «ödeme sayfasını sana açtım»).

## Sert kurallar

- **Kimlik bilgisi güvenliği**: şifre scripte yalnızca `POWPOW_REGISTER_PASSWORD` ortam değişkeniyle geçirilir, **asla** komut satırı parametresine konmaz (süreç listesinde görünür), hiçbir dosyaya yazılmaz (üretim modunda kullanıcı kaydetsin diye bir kez gösterilir, sonra bir daha anılmaz). Doğrulama kodu yalnızca resmî kayıt arayüzünde kullanılır ve işi bitince atılır.
- **Resmîlik sınırı**: tüm istekler yalnızca `https://global.powpow.online`'a gider (scripte yerleşiktir); kullanıcı bilgilerini asla üçüncü taraf adreslere göndermeyin.
- **Ödeme sınırı**: agent yalnızca sipariş açar, kasayı açar, para geçişini sorgular; kullanıcının Alipay hesabına/ödeme belgelerine **asla** dokunmaz, «ben öderim» diye söz de vermez.
- **Ödeme duvarı hata değildir**: pending durumun abonelik sayfasına/tamamlama sayfasına erişebilmesi tasarımda bırakılmış bilinçli bir geçittir; içerik sayfalarının engellenmesi ödeme duvarının normal işleyişidir; onu aşmanın yollarını aramayın.
- **Geri dönme özgürlüğü**: herhangi bir adımda kullanıcı kendi yapmak isterse ya da ortam scripti çalıştıramıyorsa, istediğiniz an salt yol gösterme moduna dönün — bağlantıları verin, kuralları anlatın, hataları birlikte çözün.
- Platform kuralı uydurmayın: alan kuralları, hata metinleri ve hız sınırı parametrelerinin tamamı platform kodundan gelir (`references/registration-flow.md` kaynağı gösterir); platform güncellenirse fiilî davranış esas alınır.
- Görsel gösterirken yalnızca paketteki `assets/screenshots/` ekran görüntülerini kullanın (her birinin kullanımı `references/screenshots.md`'de).
- Her turu «sonraki adım» bloğuyla kapatın; kullanıcı şu anda ne yapması gerektiğini her zaman bilsin.
