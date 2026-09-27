# Abonelik aktivasyonu ve ödeme — powpow-register

## Sonuç (önce cevap)

**Mevcut ödeme yöntemleri doğrudan kullanılabilir — kayıt asistanı skill'i için sıfır ödeme geliştirmesi gerekir.**

Nedenleri:

1. Kayıt arayüzü (`src/app/api/auth/register/route.ts`), pending hesap oluştururken zaten JWT cookie + pendingUserToken HttpOnly cookie verir — kullanıcı `/subscription`'a giriş yapmış hâlde iner; üç ödeme kanalı da bu abonelik sayfasına bağlıdır ve aynı pending hesabı aktifleştirir.
2. Giriş arayüzü pending hesap için 403 + `redirectTo: '/subscription'` döndürür (cookie'yi de koyar) — kullanıcı ne zaman ödeme tamamlarsa aynı sayfaya yönlendirilir.
3. Dolayısıyla kayıt rehberi skill'inin sorumluluk sınırı yalnızca «kullanıcıyı /subscription'a yönlendirmek»tir; yeni ödeme arayüzüne, yeni sipariş modeline veya herhangi bir arka uç değişikliğine gerek yoktur.

Ayrıca dikkat: ödeme aşaması (PayPal JS SDK butonları, WeChat QR manuel onayı, Huawei yerel IAP) **doğası gereği komut satırı / sohbet skill'i tarafından kullanıcı adına ödenemez ve ödenmemelidir**. Betikle ödeme arayüzünü kullanıcı adına çağırmaya çalışmayın, kullanıcıdan ödeme bilgisi de istemeyin.

## Abonelik sayfasındaki üç kanal

Abonelik sayfası `src/app/(public)/subscription/page.tsx`, çalışma ortamına göre kanalı otomatik gösterir:

| Kanal | Ortam | Mekanizma | Aktifleşme yöntemi |
|---|---|---|---|
| PayPal aboneliği | Web (HarmonyOS değil) | `/api/subscription/create` PayPal aboneliği oluşturur → PayPal onayına geçer; aylık otomatik yenileme, dilediğiniz an iptal (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) `accountStatus`'u otomatik active yapar |
| WeChat QR ile abonelik | Web (HarmonyOS değil) | Sayfa altı «WeChat QR ile abone ol» bölümü: QR okutup havale, **manuel onay sonrası açılır** (`WechatQrPaymentSection`) | Manuel onay; yansıma gecikebilir; kullanıcı ödeme yaptıktan sonra hemen başarısız saymayın |
| Huawei uygulama içi satın alma (IAP) | HarmonyOS uygulaması | HarmonyOS WebView'da PayPal / WeChat Pay çalışmaz, sayfa yerel `NativeBridge.purchaseSubscription()` kullanır | `/api/subscription/activate-huawei` Huawei siparişini doğrulayıp aktifleştirir |

Plan ve fiyatlar `/api/subscription/plans` adresinden dinamik okunur (PayPal planları); sayfadaki sabit metin: Auto-renews. Cancel anytime.

## Durumlar ve yönlendirmeler

- Ödeme başarılı → `/subscription/success` (PayPal geri çağrısı `subscriptionId` getirir) → hesap active → `next` parametresindeki orijinal sayfaya otomatik dönüş (yoksa ana sayfa).
- Abone olmuş kullanıcı abonelik sayfasını tekrar açarsa → "You're All Set!" görünür, 3 saniye sonra otomatik ana sayfaya döner.
- Ödeme başarısız / iptal → `/subscription/cancel` sayfası, yeniden başlatılabilir.

## Arıza giderme

| Belirti | Yapılacak |
|---|---|
| Ödendi ama hâlâ 403 | PayPal: Webhook bazen gecikir — durumu yenilemek için tekrar giriş yapın (giriş DB'deki güncel durumu kontrol eder); WeChat: manuel onay henüz tamamlanmadı, bekleyin; Huawei: uygulama içinde ödeme başarı sayfasının çıkıp çıkmadığını kontrol edin |
| Abonelik sayfası "No subscription plans available" gösteriyor | `/api/subscription/plans` içinde kullanılabilir PayPal planı yok — platform tarafı yapılandırma sorunu; kullanıcıya sonra tekrar denemesini söyleyin |
| WeChat ile ödendi ama açılmadı | Manuel onay eşzamansızdır; birkaç saat içinde açılmazsa platform desteğiyle iletişime geçin (dongtao@outlook.com) |

## Not: Alipay

Kodda bir Alipay web ödeme seti mevcut (`src/lib/alipay.ts`, `/api/payment/create-order`, normal üyelik ¥9.90 / premium üyelik ¥99 tek seferlik satın alma modeli; sandbox anahtarı yoksa otomatik olarak simüle ödemeye düşer), **ancak abonelik sayfası UI'ına bağlanmamıştır** — atıl / rezerve kod niteliğindedir. Gelecekte abonelik sayfasında Alipay etkinleştirmek isterseniz bu hazır kodu bağlamak yeterlidir — bu skill'le ilgisi yoktur, yalnızca platform tarafı kararları için referanstır.