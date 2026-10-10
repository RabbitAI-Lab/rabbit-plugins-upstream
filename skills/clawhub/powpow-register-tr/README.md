# powpow-register

PowPow Kabarcık kayıt asistanı (OpenClaw sürümü): yeni bir kullanıcıyı «Kabarcık'ın ne olduğunu bilmiyorum»dan
«hesap etkinleşti, tek tıkla giriş, oyun başlıyor» noktasına götürür — ürün tanıtımı (arayüz ekran
görüntüleriyle), agent vekâletiyle kayıt (profil fotoğrafı yükleme dahil), Alipay abonelik siparişi ve hesaba
geçiş takibi, çift bağlantıyla tek tıkla giriş, hata giderme.

**v2.0.0'dan itibaren agent vekâlet modudur**: ana script `scripts/powpow-register.mjs` sıfır bağımlılıktır
(Node ≥ 18), kullanıcı sürecin tamamında sohbetten ayrılmaz; yalnızca iki kısa ayrılık yaşar: e-postaya gidip
doğrulama kodunu okumak ve Alipay kasasında ödemek. Node yoksa ya da kullanıcı kendi yapmak isterse otomatik
olarak salt yol gösterme moduna dönülür.

## Kurulum

```
openclaw skills install @durenzidu/powpow-register
```

## Özellikler

1. **Ürün tanıtımı**: ~120 karakterlik açılış + paketle birlikte gelen arayüz ekran görüntüleri
   (`assets/screenshots/` altında 6 adet: harita sayfası, gönderi detay sayfası vb.; senaryoya göre 1–3 adet
   seçilip gönderilir; harici görsel servisi gerekmez, çevrimdışı çalışır).
2. **Vekâleten kayıt**: agent kullanıcı adını/takma adı kendiliğinden önerir, şifre iki seçeneklidir (kullanıcı
   verir ya da agent üretir), doğrulama kodunun gönderilip girilmesi, profil fotoğrafının doğrudan yüklenmesi
   (≤5MB, SVG değil), sık hataların otomatik yönetimi (alınmış/süresi geçmiş/hız sınırı).
3. **Tek tıkla giriş (çift bağlantı)**: kayıt başarılı olur olmaz «yarı oturum» bağlantısı abonelik sayfasına
   götürür; ödeme hesaba geçtikten sonra yeni oturum durumu alınır ve tam üye bağlantısı ana sayfaya götürür
   (platformun resmî `me?token=` köprüsünden geçer, HttpOnly cookie'yi kendiliğinden yerleştirir).
4. **Abonelik ödemesi**: Alipay kanalında agent siparişi vekâleten açar (aylık ¥6.99 / üç aylık ¥19.99 / yıllık
   ¥69.99, tek seferlik satın alma, otomatik yenileme yok) + hesaba geçiş yoklaması; yurt dışındaki kullanıcılar
   PayPal'e döner; WeChat QR/Huawei IAP için yol gösterilir.
5. **Hata giderme**: doğrulama kodunun gelmemesi, kullanıcı adı/e-postanın alınmış olması, 403 etkinleşmemiş,
   hesap kilitlenmesi gibi sık sorunlar — tamamı platform kaynak kodundan gelir ve kaynağı belirtilir.

## Dosya yapısı

```
powpow-register/
├── SKILL.md                            # Ana kılavuz (tetik koşulları, 8 adımlı akış, ton kuralları, sert kurallar)
├── README.md
├── .clawhubignore
├── assets/
│   └── screenshots/                    # Paketle gelen ürün ekran görüntüleri (powpow-01~06.jpg)
├── scripts/
│   └── powpow-register.mjs             # Ana script (sıfır bağımlılık, Node≥18, 11 alt komut)
└── references/
    ├── agent-flow.md                   # Script sözleşmesi, tam sıralama, çift bağlantı mekanizması, güvenlik tasarımı
    ├── registration-flow.md            # Alan kuralları, hız sınırları, hata giderme tablosu (kaynak kodlu)
    ├── payment-and-activation.md       # Alipay vibepay sözleşmesi, etkinleştirme zinciri, kanal teşhisi
    └── screenshots.md                  # Paket görüntü listesi + senaryoya hızlı bakış
```

## Güvenlik

- **Şifre** script sürecine yalnızca ortam değişkeniyle girer; komut satırı parametresine asla konmaz, diske
  yazılmaz, durum dosyasına girmez; agent'ın ürettiği şifre kullanıcıya kaydettirilmek için yalnızca bir kez
  gösterilir.
- **Doğrulama kodu** yalnızca resmî kayıt arayüzünde kullanılır, işi bitince atılır; durum dosyası
  (e-posta/kullanıcı adı/token/sipariş numarası) sistem geçici dizininde tutulur, akış sonunda `cleanup` tek
  komutla siler.
- **Ödeme**: agent yalnızca sipariş açar, kasayı açar, hesaba geçişi sorgular; kullanıcının Alipay hesabına ya
  da ödeme belgelerine asla dokunmaz, asla vekâleten ödeme yapmaz. Ödeme her zaman kullanıcı ile Alipay'in resmî
  kasası arasında gerçekleşir.
- Tüm istekler yalnızca resmî alan adı `https://global.powpow.online`'a gider; hiçbir anahtar içermez.

## Lisans

MIT-0 (ClawHub birleşik lisansı).

## Bağlantılar

- Resmî site: https://global.powpow.online
- Kayıt: https://global.powpow.online/register
- Kabarcık'ı tanıyın (video): https://www.bilibili.com/video/BV1Wu826UEVz/
