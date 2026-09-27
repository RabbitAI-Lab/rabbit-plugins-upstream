# Subscription Activation at Pagbabayad — powpow-register

## Konklusyon (unahin ang sagot)

**Maaaring direktang gamitin muli ang kasalukuyang paraan ng pagbabayad, zero payment development ang registration assistant skill.**

Mga dahilan:

1. Ang registration endpoint (`src/app/api/auth/register/route.ts`) sa paggawa ng pending account ay nagbigay na ng
   JWT cookie + pendingUserToken HttpOnly cookie, ang user na dumating sa `/subscription` ay
   naka-login na — lahat ng tatlong payment channel ay nakakabit sa subscription page na ito, at ang ina-activate ay ang parehong pending account.
2. Ang login endpoint para sa pending account ay nagbabalik ng 403 + `redirectTo: '/subscription'`, itinatanim din nito ang
   parehong cookie — kahit kailan magbayad ang user ay maidadala pabalik sa parehong pahina.
3. Kaya ang hangganan ng responsibilidad ng registration guidance skill ay "idadala ang user sa /subscription"; hindi kailangan ng bagong
   payment endpoint, hindi kailangan ng bagong order model, hindi kailangan ng anumang backend change.

Dapat ding pansinin: ang payment stage (PayPal JS SDK button, WeChat QR scan manual confirmation, native na Huawei IAP)
**ay nagtatakda na hindi ito maaari at hindi dapat bayaran ng command-line/chat skill**. Huwag subukang gumamit ng script na tumatawag sa payment
endpoint para magbayad para sa user, at huwag humingi ng payment credentials ng user.

## Tatlong Channel sa Subscription Page

Awtomatikong ipinapakita ng subscription page na `src/app/(public)/subscription/page.tsx` ayon sa kapaligiran:

| Channel | Kapaligiran | Mekanismo | Paraan ng Pag-activate |
|---|---|---|---|
| PayPal subscription | Web (hindi HarmonyOS) | gumagawa ang `/api/subscription/create` ng PayPal subscription → lulukso sa PayPal authorization; awtomatikong nagre-renew kada buwan, maaaring i-cancel anumang oras (`/api/subscription/manage`) | awtomatikong iginagawang active ng PayPal Webhook (`BILLING.SUBSCRIPTION.*`) ang `accountStatus` |
| WeChat QR scan subscription | Web (hindi HarmonyOS) | "WeChat QR scan subscription" block sa ibaba ng page: scan QR para maglipat, **bubuksan pagkatapos ng manual confirmation** (`WechatQrPaymentSection`) | manual confirmation, maaaring ma-delay ang pagdating ng pera; huwag agad husgahang nabigo kapag nakapagbayad na ang user |
| Huawei in-app purchase (IAP) | Sa loob ng HarmonyOS App | sa HarmonyOS WebView ay hindi magagamit ang PayPal/WeChat payment, lumilipat ang page sa native na `NativeBridge.purchaseSubscription()` | sine-verify ng `/api/subscription/activate-huawei` ang Huawei order bago i-activate |

Ang mga plano at presyo ay dinamikong binabasa mula sa `/api/subscription/plans` (PayPal plans); fixed text sa page:
Auto-renews. Cancel anytime.

## Status at Paglipat ng Pahina

- Tagumpay ang pagbabayad → `/subscription/success` (ang PayPal callback ay may kasamang `subscriptionId`) → active ang
  account → awtomatikong babalik sa orihinal na pahinang itinakda ng `next` (kung wala, home page).
- Ang user na naka-subscribe na ay bumisitang muli sa subscription page → magpapakita ng "You're All Set!", pagkatapos ng 3 segundo ay awtomatikong babalik sa home.
- Nabigo/naka-cancel ang pagbabayad → `/subscription/cancel`, maaaring magsimula muli.

## Pagtingin sa Error

| Sintomas | Pag-aayos |
|---|---|
| Nakabayad na pero 403 pa rin | PayPal: minsan naaantala ang Webhook, mag-login muli para i-refresh ang status (nagre-reexamine sa pinakabagong status mula sa DB kapag nag-login); WeChat: hindi pa tapos ang manual confirmation, maghintay sandali; Huawei: tingnan kung lumitaw ang success page ng in-app payment |
| Nagpapakita ang subscription page ng "No subscription plans available" | walang available na PayPal plan sa `/api/subscription/plans`, configuration issue ito sa panig ng platform, patingnan muli sa user mamaya |
| Nakabayad na sa WeChat pero hindi pa binuksan | asynchronous ang manual confirmation, kung ilang oras na at hindi pa nabubuksan saka makipag-ugnayan sa platform support (dongtao@outlook.com) |

## Tandaan: Alipay

May nakahandang set ng Alipay web payment sa code (`src/lib/alipay.ts`, `/api/payment/create-order`,
one-time purchase model na regular member ¥9.90 / premium member ¥99, kapag walang naka-configure na key ang sandbox ay
awtomatikong magde-degrade sa simulated payment), **ngunit hindi pa nakakabit sa subscription page UI**, idle/reserved code ito. Kung balang araw
gustong paganahin ang Alipay sa subscription page, i-wire lang ang kasalukuyang code set na ito — hindi ito nauugnay sa skill na ito,
para lamang sa reference ng desisyon sa panig ng platform.