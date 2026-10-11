# Abonelik etkinleştirme ve ödeme — powpow-register

## Sonuç (önce cevap)

**Alipay kanalı yayında (2026-10-07'den beri), bu skill'in ana ödeme yöntemidir ve agent sipariş açma ile hesaba
geçiş takibini vekâleten yürütür.** Yurt dışındaki/Alipay'i olmayan kullanıcılar PayPal'e döner; WeChat QR (elle
onay) ve Huawei IAP da mevcuttur ama skill bunlarda vekâlet etmez.

Ödemede sorumluluk sınırı: agent **sipariş açar, kasayı açar, hesaba geçişi sorgular**; kullanıcının Alipay
hesabına/ödeme belgelerine **asla dokunmaz**, «ben öderim» vaadinde **asla** bulunmaz. Ödeme eylemi her zaman
kullanıcı tarafından Alipay'in resmî kasasında yapılır.

## Alipay kanalı (vibepay, ana kanal)

Tek seferlik satın alma modeli: bir kez ödenir, ilgili süre açılır, **otomatik yenileme yoktur**. Paketler
`src/lib/alipay-vibepay.ts` içinde tanımlıdır (`ALIPAY_PACKAGES`):

| key | planId | Ad | Fiyat | Süre |
|---|---|---|---|---|
| `monthly` | alipay-monthly | Aylık üyelik | ¥6.99 | 30 gün |
| `quarterly` | alipay-quarterly | Üç aylık üyelik | ¥19.99 | 90 gün |
| `yearly` | alipay-yearly | Yıllık üyelik | ¥69.99 | 365 gün |

### Arayüz sözleşmesi (skill scriptine önceden sarmalanmıştır, agent isteği kendisi kurmaz)

| Arayüz | Yöntem | Açıklama |
|---|---|---|
| `/api/payment/alipay/create-order` | POST | `Authorization: Bearer <JWT>` gerektirir (pending kullanıcı da olur). body `{package}` → `{paymentHtml, outTradeNo, amount, planName}` döner; `paymentHtml`, Alipay ağ geçidine kendiliğinden gönderilen form sayfasıdır |
| `/api/payment/alipay/query` | GET `?outTradeNo=` | Aynı Bearer. `paid` / `pending` / `closed` / `unknown` döner |
| `/api/payment/alipay/notify` | POST (Alipay sunucusundan geri çağrı) | Beş yönlü imza denetimi (imza, app_id, tutar eşleşmesi, TRADE_SUCCESS/TRADE_FINISHED, satıcı sipariş benzersizliği) → **idempotent** sipariş güncelleme + abonelik oluşturma + hesap etkinleştirme. Skill bu arayüze asla dokunmaz |
| `/payment/alipay/return` | Tarayıcı geri dönüş sayfası | Herkese açık yol; ödeme sonrası 「支付成功」 gösterir, sayfa arka uçtaki gerçek durumu yoklar |

- Ödenmemiş siparişler **2 saatte otomatik kapanır**; kullanıcı yarıda bıraktıysa → doğrudan yeniden
  `create-order`, eski siparişle ilgilenmeyin.
- Script `paymentHtml`'i geçici bir HTML dosyasına yazar; agent bir sistem komutuyla açar ve Alipay kasasına
  doğrudan gidilir (QR okutulur ya da Alipay'e girilip ödenir).

### Etkinleştirme zinciri (otomatik, elle iş yok)

notify'un imza denetimi geçer → `paymentOrders` kaydı ödendi olarak işaretlenir → `user_subscriptions` oluşturulur/
uzatılır (`planId`, `currentPeriodEnd` durationDays'ten hesaplanır; yenileme yalnızca orijinal bitiş tarihine eklenir) →
`users.accountStatus: active` + `subscriptionStatus: ACTIVE` → geri dönüş sayfası paid'yı yakalayıp başarıyı gösterir.

## Ödedikten sonra yeni oturum durumu almak şart (önemli)

JWT'nin içinde abonelik beyanı gömülüdür (pending hesapta `NONE`). **Ödemede hesaba geçiş yalnızca veritabanını
günceller, verilmiş JWT değişmez** — eski tokenın beyanı NONE olarak kalır; onunla giriş bağlantısı üretilirse
«üye değil» gibi görünür. Bu yüzden skill `paid` doğrulandıktan sonra önce `refresh-login` çalıştırır (yeniden
giriş, yeni JWT, beyanı ACTIVE), sonra bağlantı 2'yi üretir. Bu tasarımın davranışıdır, düzeltilmesi gereken bir
hata değildir.

## Abonelik sayfasındaki dört kanal

Abonelik sayfası `src/app/(public)/subscription/page.tsx` çalışma ortamına göre gösterir:

| Kanal | Ortam | Mekanizma | Etkinleşme yöntemi |
|---|---|---|---|
| **Alipay (ana)** | Web | `AlipayPaymentSection` vibepay arayüllerine bağlıdır (yukarıdaki tablo) | notify ile sunucu tarafında otomatik etkinleşme, saniyeler içinde |
| PayPal aboneliği | Web (HarmonyOS'ta yok) | `/api/subscription/create` → PayPal yetkilendirmesi; aylık otomatik yenilenir, istenildiği an iptal edilir (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) otomatik active yapar |
| WeChat QR aboneliği | Web (HarmonyOS'ta yok) | Sayfanın altında 「微信扫码订阅」: QR okutularak havale | **Elle onay**, para geçişi gecikebilir; ödemenin hemen ardından başarısız saymayın |
| Huawei uygulama içi satın alma | HarmonyOS uygulaması içinde | Yerel `NativeBridge.purchaseSubscription()` çağrısı | `/api/subscription/activate-huawei` Huawei siparişini doğrulayıp etkinleştirir |

PayPal paketleri ve fiyatları `/api/subscription/plans`'tan dinamik gelir; sayfadaki sabit metin:
Auto-renews. Cancel anytime.

## Durumlar ve yönlendirmeler

- Alipay tamam → geri dönüş sayfası başarıyı gösterir; PayPal başarılı → `/subscription/success` → hesap active →
  `next` parametresine göre orijinal sayfaya otomatik dönüş (yoksa ana sayfa).
- Zaten üye olan kullanıcı abonelik sayfasını açarsa → "You're All Set!" görür, 3 saniyede kendiliğinden ana sayfaya döner.
- Ödeme başarısız/iptal (PayPal) → `/subscription/cancel`, tekrar denenebilir.

## Teşhis

| Belirti | Çare |
|---|---|
| Alipay ödemesinden sonra `query` hâlâ pending | notify gecikmesi nadirdir; 30 saniye bekleyip tekrar bakın. Yine olmazsa kullanıcı tarayıcıdaki geri dönüş sayfasının durumuna baksın; o da çözmezse platform desteğiyle (dongtao@outlook.com) `outTradeNo`'yu vererek iletişime geçsin |
| Alipay ücreti kesti ama bağlantı 2 ile girince yine engelleniyor | `refresh-login` atlandı (eski JWT'nin beyanı güncellenmemiş) — önce `refresh-login`, sonra `login-link` |
| Ödedikten sonra yine 403 (PayPal) | Webhook bazen gecikir; yeniden giriş yapıp durum yenilensin |
| WeChat ile ödendi, abonelik açılmadı | Elle onay eşzamansızdır; birkaç saat içinde açılmazsa platform desteğiyle iletişime geçilsin |
| Abonelik sayfasında "No subscription plans available" | `/api/subscription/plans` PayPal paketi döndürmüyor; platform tarafındaki yapılandırma arızasıdır; Çin anakarasındaki kullanıcılar arada Alipay'i kullanabilir |

## Tarihsel not

Kodda **eski** bir Alipay web ödeme seti daha vardır (`src/lib/alipay.ts`, `/api/payment/create-order`,
¥9.90/¥99 tek seferlik; sandbox anahtarı yoksa sahte ödeme yapar); bu set hiçbir zaman abonelik sayfası
arayüzüne bağlanmadı ve vibepay'le ilgisizdir. Skill oraya asla dokunmaz; yürürlükteki kanal
`alipay-vibepay.ts`'dir.
