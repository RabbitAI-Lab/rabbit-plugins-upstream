# Kunna membanci da biya — powpow-register

## Ƙarshe (amsa da farko)

**Hanyar Alipay ta fara aiki (tun 2026-10-07), ita ce babbar hanyar biya ta skill ɗin nan, agent za ta iya taimakawa ƙirƙirar oda da bin diddigin shigar kuɗi.**
Mai amfani na ƙasashen waje/ba shi da Alipay ya koma PayPal; siffanta lambar QR ta WeChat (tabbatarwa ta hannu) da Huawei IAP har yanzu suna nan, amma skill ba ta aikatawa ba.

Iyakar aiki na ɓangaren biya: agent za ta iya **ƙirƙirar oda, buɗe cashier, duba shigar kuɗi**; **kada ta taba** asusun Alipay na mai amfani/takaddun biya, kada ta taɓa alkawari 'biya a madadinsa'. Aikin biya koyaushe mai amfani da kansa yana yi a cashier na Alipay na hukuma.

## Hanyar Alipay (vibepay, babbar)

Tsarin biya sau ɗaya: ka biya sau ɗaya ka kunna lokacin da ya dace, **ba ya sabunta kansa da kai**. Shirye-shirye an ƙuntata su a
`src/lib/alipay-vibepay.ts` (`ALIPAY_PACKAGES`):

| key | planId | Suna | Farashi | Lokaci |
|---|---|---|---|---|
| `monthly` | alipay-monthly | Membanci na wata | ¥6.99 | kwanaki 30 |
| `quarterly` | alipay-quarterly | Membanci na kwata | ¥19.99 | kwanaki 90 |
| `yearly` | alipay-yearly | Membanci na shekara | ¥69.99 | kwanaki 365 |

### Kwangilar tashoshi (script ɗin skill ya riga ya ƙunsa, agent ba ta gina buƙata kai tsaye ba)

| Tasha | Hanya | Bayani |
|---|---|---|
| `/api/payment/alipay/create-order` | POST | Tana buƙatar `Authorization: Bearer <JWT>` (mai amfani na pending ya isa). jiki `{package}` → tana dawo da `{paymentHtml, outTradeNo, amount, planName}`; `paymentHtml` shafi ne na fom mai tura kai tsaye ga ƙofar Alipay |
| `/api/payment/alipay/query` | GET `?outTradeNo=` | Hakika tabbatarwa ta Bearer. Tana dawo da `paid` / `pending` / `closed` / `unknown` |
| `/api/payment/alipay/notify` | POST (kiran uwar garwa ta Alipay) | Tabbatar da saitti na abubuwa biyar (saitti, app_id, adadin kuɗin yayi daidai, TRADE_SUCCESS/TRADE_FINISHED, keɓaɓɓun ma'aikaci) → **idempotent** sabunta oda + gina membanci + kunna asusu. Skill kada ta taba wannan tasha |
| `/payment/alipay/return` | Shafin dawowa na burauza | Hanya ce ta jama'a, bayan biya tana nuna tabbacin "支付成功" (biyan ya yi nasara), shafin yana sake duba halin gaske na ɓangaren baya |

- Oda da ba a biya ba **tana rufewa da kai bayan sa'o'i 2**; mai amfani ya bar a tsakanin → ka sake `create-order` kai tsaye, tsohon oda ba buƙatar damuwa.
- Script ɗin yana rubuta `paymentHtml` a cikin fayil ɗin HTML na wucin gadi, agent ta yi amfani da umarnin tsarin ta buɗe shi ta shiga cashier na Alipay
  (siffanta lambar QR ko shiga cikin Alipay ya biya).

### Hanyar kunnawa (ta kai, ba buƙatar hannu)

notify tabbatar da saitti ta wuce → `paymentOrders` alamta an biya → `user_subscriptions` gina/cigaba
(`planId`, `currentPeriodEnd` ana ƙidaya bisa durationDays, sabunta membanci na cigabawa a kan ranar ƙarewa ta asali) →
`users.accountStatus: active` + `subscriptionStatus: ACTIVE` → shafin dawowa yana sake duba har paid yana nuna nasara.

### Bayan biya dole ne a musanya halin shiga sabuwa (mai mahimmanci)

JWT na ɗauke da da'awar membanci (asusun pending `NONE`). **Shigar kuɗin kawai na sabunta ma'ajiyar bayanai, ba ta canza JWT da aka riga aka bayar ba** — da'awar token ɗin da ya gabata har yanzu NONE, idan ka yi amfani da ita kai tsaye ka ƙirƙiri mahaɗin shiga zai bayyana "ba memba ba".
Saboda haka skill bayan tabbatar da `paid` da farko na gudanar da `refresh-login` (sake shiga musanya JWT sabuwa, da'awar na canzawa zuwa ACTIVE),
sannan ta ƙirƙiri mahaɗi na 2. Wannan halin zane ne, ba gyaran rami ba.

## Hanyoyi huɗu na shafin membanci

Shafin membanci `src/app/(public)/subscription/page.tsx` yana nuna bisa yanayin aiki:

| Hanya | Yanayi | Tsari | Hanyar kunnawa |
|---|---|---|---|
| **Alipay (babbar)** | ɓangaren yanar gizo | `AlipayPaymentSection` tana bi ta tashar vibepay (teburin sama) | notify uwar garwa tana kunna ta kai, daƙiƙa kaɗan |
| Membancin PayPal | ɓangaren yanar gizo (ba Harmony ba) | `/api/subscription/create` → turawa izinin PayPal; biyan kowane wata na sabunta kansa za a iya soke a kowane lokaci (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) tana saka active ta kai |
| Membancin siffanta lambar QR ta WeChat | ɓangaren yanar gizo (ba Harmony ba) | ƙarshen shafi "微信扫码订阅" (membancin siffanta lambar QR ta WeChat): siffanta lambar turawa kuɗi | **tabbatarwa ta hannu**, kuɗi na iya yin jinkiri; bayan biya kada ka yanke hukunci da wuri |
| Siye na ciki na Huawei | a cikin manhaja ta Harmony | na asali `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` tabbatar da oda Huawei sannan ta kunna |

Shirye-shirye da farashin PayPal ana karanta su daga `/api/subscription/plans` bisa canji; rubutun dauri na shafi: Auto-renews. Cancel anytime.

## Hali da turawa

- Alipay bayan biya → shafin dawowa yana nuna nasara; PayPal ta yi nasara → `/subscription/success` → asusu active →
  turawa ta kai ga shafin asali da `next` ya nuna (babu shi to shafin gida).
- Mai amfani da ya riga ya yi membanci idan ya koma shafin membanci → yana nuna "You're All Set!", bayan daƙiƙa 3 yana dawowa shafin gida ta kai.
- Biya ta gaza/an soke (PayPal) → `/subscription/cancel`, za a iya farawa sake.

## Bincike

| Alama | Yadda ake kula |
|---|---|
| Alipay bayan biya `query` har yanzu pending | notify na yin jinkiri kaɗan ne; ka jira daƙiƙa 30 sannan ka sake duba. Har yanzu bai yi ka tambayi mai amfani ya koma burauza ya duba halin shafin dawowa, har yanzu bai yi ka tuntubi taimakon dandalin (dongtao@outlook.com), ka ba da `outTradeNo` |
| Alipay ta biya, mahaɗi na 2 ya shiga har yanzu ana toshi | An tsallake `refresh-login` (da'awar JWT ta da ba a sabunta ba) — ka fara `refresh-login` sannan `login-link` |
| Bayan biya har yanzu 403 (PayPal) | Webhook wani lokaci na yin jinkiri, ka sake shiga ka sabunta hali |
| WeChat ta biya ba a kunna ba | Tabbatarwa ta hannu ce asynchronous, a cikin sa'o'i kaɗan idan ba a kunna ba sai ka tuntubi taimakon dandalin |
| Shafin membanci yana nuna "No subscription plans available" | `/api/subscription/plans` ba shi da shirin PayPal mai samuwa, matsala ce ta saitin ɓangaren dandalin; masu amfani na China su canza su bi Alipay kawai |

## Rubutun tarihi

A cikin code akwai wata tsarin **tsohuwar** biya ta yanar gizo ta Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`,
¥9.90/¥99 biya sau ɗaya, lokacin sandbox ba a saita makullai ba tana faduwa zuwa biyar da ƙarya), ba ta taɓa haɗawa da UI ɗin shafin membanci ba, ba ta da alaƙa da vibepay.
Skill kada ta taba shi; `alipay-vibepay.ts` ne hanyar da ake amfani da ita a yanzu.
