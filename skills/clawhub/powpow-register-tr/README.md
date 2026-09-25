# powpow-register

PowPow kayıt asistanı (OpenClaw sürümü): yeni bir kullanıcıyı «PowPow'un ne olduğunu bilmiyorum» noktasından «hesap aktif, normal şekilde kullanabiliyorum» noktasına taşır — ürün tanıtımı (arayüz ekran görüntüleri dahil), adım adım kayıt yönlendirmesi, hata giderme, abonelik aktivasyonu açıklaması.

Tamamen rehber amaçlı skill: betik yok, bağımlılık yok; tüm kayıt işlemlerini kullanıcı tarayıcıda / uygulamada yapar.

## Kurulum

```
openclaw skills install @durenzidu/powpow-register
```

## Özellikler

1. **Ürün tanıtımı**: ~120 karakterlik açılış + GitHub genel deposunda barındırılan arayüz ekran görüntüsü bağlantıları (harita sayfası, gönderi detay sayfası vb. — 6 görsel, duruma göre 1–3 tane gönderilir).
2. **Kayıt yönlendirmesi**: alan kuralları (kullanıcı adı / şifre / e-posta doğrulama kodu / telefon / avatar), üçüncü taraf girişi (Google / Watcha / Huawei), limit parametreleri — hepsi platform kaynak kodundan, kaynağı belirtilerek alınmıştır.
3. **Hata giderme**: doğrulama kodu gelmemesi, dolu kullanıcı adı / e-posta, aktivasyon öncesi 403, kilitli hesap vb. — 13 yaygın sorun.
4. **Abonelik aktivasyonu**: üç kanalın açıklaması ve arıza gidermesi — PayPal (web) / WeChat QR (manuel onay) / Huawei IAP (HarmonyOS); mevcut ödeme kanalları doğrudan kullanılabilir, skill yalnızca yol gösterir.

## Dosya yapısı

```
powpow-register/
├── SKILL.md                            # Ana rehber (tetikleyiciler, süreç, üslup kuralları)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Alan kuralları, limitler, hata tablosu (kaynaklarıyla)
    ├── payment-and-activation.md       # Abonelik aktivasyonu, ödeme kanalları, yeniden kullanım sonucu
    └── screenshots.md                  # Barındırılan ekran görüntüleri listesi + durum hızlı bakışı
```

## Güvenlik

- Hiçbir anahtar içermez; betik yok, kullanıcı kimlik bilgilerine dokunmaz.
- Kullanıcıdan **asla** şifre, doğrulama kodu veya ödeme bilgisi istemeyin; kayıt ve ödeme tamamen platform sayfalarında gerçekleşir.

## Lisans

MIT-0 (ClawHub ortak lisansı).

## Bağlantılar

- Resmi site: https://global.powpow.online
- Kayıt: https://global.powpow.online/register
- PowPow'u tanıyın (video): https://www.bilibili.com/video/BV1Wu826UEVz/