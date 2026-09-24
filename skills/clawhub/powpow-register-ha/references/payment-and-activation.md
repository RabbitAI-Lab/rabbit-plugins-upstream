# Subscription, Kunnawa da Biyan Kuɗi — powpow-register

## Ƙarshe (Amsa da farko)

**Hanyoyin biyan kuɗi da ke akwai za a iya sake amfani da su kai tsaye; skill ɗin mataimakin rijista ba ta buƙatar kowane haɓakar biyan kuɗi ba.**

Dalilai:

1. Interface ɗin rijista (`src/app/api/auth/register/route.ts`) lokacin ƙirƙirar asusun pending an riga an ba da JWT cookie + pendingUserToken HttpOnly cookie, don haka idan mai amfani ya isa `/subscription` ya riga ya kasance cikin yanayin shiga (logged-in) — hanyoyin biyan kuɗi guda uku duk sun rataye a wannan shafin subscription, kuma duk suna kunnawa asusu ɗaya na pending.
2. Interface ɗin shiga tana mayar da 403 + `redirectTo: '/subscription'` ga asusun pending, kuma tana sanya cookie iri ɗaya — mai amfani ko da yaushe idan ya biya kari za a mayar da shi wannan shafi.
3. Don haka iyakar aikin skill ɗin jagorar rijista shi ne «kai mai amfani zuwa /subscription»; ba a buƙatar sabuwar interface ta biyan kuɗi, ba a buƙatar sabon model na oda, ba a buƙatar kowane canji a ƙarshen baya (backend).

A lokaci ɗaya ka lura: ɓangaren biyan kuɗi (maɓallin PayPal JS SDK, tabbatarwar mutum na lambar WeChat, IAP na asali na Huawei) **ya nuna cewa ba zai yiwu ba kuma bai kamata a biya shi daga skill ɗin layin umarni/tattaunawa ba**. Kada ka ƙoƙarin amfani da script don kiran interface ɗin biyan kuɗi a madadin mai amfani, kada ka nemi tantanar biyan kuɗi na mai amfani.

## Hanyoyi Uku na Shafin Subscription

Shafin subscription `src/app/(public)/subscription/page.tsx` yana nunawa kai tsaye bisa ga yanayin gudanarwa:

| Hanya | Yanayi | Tsari | Hanyar kunnawa |
|---|---|---|---|
| Subscription na PayPal | Shafin yanar gizo (ba HarmonyOS ba) | `/api/subscription/create` tana ƙirƙirar subscription na PayPal → tsallakewa zuwa izinin PayPal; ana sabunta shi kai tsaye kowane wata, ana iya soke kowane lokaci (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) tana saita `accountStatus` zuwa active kai tsaye |
| Subscription ta duba lambar WeChat | Shafin yanar gizo (ba HarmonyOS ba) | Yankin ƙasan shafin «Subscription ta duba lambar WeChat»: ka duba lambar ka aika kuɗi, **ana buɗe bayan mutum ya tabbatar** (`WechatQrPaymentSection`) | Tabbatarwar mutum; zuwan kuɗin na iya jinkiri; bayan mai amfani ya biya kada ka yi gaggawar yanke hukuncin cewa ya gaza |
| Sayayya a cikin App (IAP) na Huawei | A cikin App ɗin HarmonyOS | A cikin WebView ɗin HarmonyOS ba a samun PayPal/WeChat; shafin yana amfani da `NativeBridge.purchaseSubscription()` na asali | `/api/subscription/activate-huawei` tana tabbatar da odar Huawei sannan ta kunna |

Shirye-shirye da farashi ana karanta su kai tsaye (dynamically) daga `/api/subscription/plans` (shirye-shiryen PayPal); rubutun da ba ya canzawa a shafin: Auto-renews. Cancel anytime.

## Yanayi da Juyawa na Shafi

- Biyan kuɗi ya yi nasara → `/subscription/success` (komawar PayPal tana ɗauke da `subscriptionId`) → asusu active → yana komawa kai tsaye zuwa shafin asali da sigar `next` ta nuna (idan babu, shafin farko).
- Mai amfani da ya riga ya yi subscription idan ya sake zuwa shafin subscription → yana nuna "You're All Set!", bayan sakan 3 yana komawa shafin farko kai tsaye.
- Biyan kuɗi ya gaza/an soke shi → `/subscription/cancel`, ana iya sake ƙaddamarwa.

## Gano Kuskure

| Alama | Abin da za a yi |
|---|---|
| Har yanzu 403 bayan biya | PayPal: Webhook na iya jinkiri; sake shiga don sabunta yanayi (a shiga ana duba sabon yanayi a ma'ajiyar bayanai); WeChat: tabbatarwar mutum ba ta gama ba, jira; Huawei: tabbatar ko shafin nasarar biyan kuɗi a cikin App ya bayyana |
| Shafin subscription yana nuna "No subscription plans available" | `/api/subscription/plans` ba ta da shirin PayPal da ke akwai; matsala ce ta saitawa a ɓangaren dandali, ka sa mai amfani ya jira sannan ya sake gwadawa |
| Ya biya ta WeChat amma ba a buɗe ba | Tabbatarwar mutum aiki ce na lokaci (asynchronous); idan ba a buɗe ba a cikin sa'o'i kaɗan ka tuntuɓi tallafin dandali (dongtao@outlook.com) |

## Bayani: Alipay

A cikin lambar akwai tsarin biyan kuɗi na yanar gizo na Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`, model ɗin sayan har abada na memba na yau da kullun ¥9.90 / memba na ƙwararru ¥99, kuma idan sandbox ba ta da maɓallai ana sauka ta atomatik zuwa biyan kuɗi na kwaikwayo), **amma ba a haɗa shi da UI ɗin shafin subscription ba** — lambar da ba a yi amfani da ita/tsayayyiyar lamba ce. Idan a nan gaba za a kunna Alipay a shafin subscription, ka haɗa ta amfani da wannan lambar da ke akwai — wannan bai shafi wannan skill ba, kawai don yanke shawara a ɓangaren dandali ne.