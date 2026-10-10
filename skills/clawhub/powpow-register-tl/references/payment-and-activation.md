# Activation ng subscription at bayad — powpow-register

## Konklusyon (sagot muna)

**Naka-live na ang Alipay channel (mula 2026-10-07), ito ang pangunahing inirerekomendang paraan ng bayad ng skill na ito, at ang agent ay maaaring gumawa ng order at subaybayan ang pagdating ng bayad.**
Para sa mga gumagamit sa ibang bansa/walang Alipay, bumabalik sa PayPal; nananatili ang WeChat QR (manual na kumpirmasyon) at Huawei IAP, ngunit hindi ina-asikaso ng skill.

Hangganan ng responsibilidad sa bahagi ng bayad: ang agent ay maaaring **gumawa ng order, buksan ang cashier, tingnan ang pagdating ng bayad**; **huwag kailanman** hawakan ang Alipay
account/payment credentials ng gumagamit, huwag kailanman mangako ng "pagbabayad para sa kanya". Ang pagbabayad ay palaging ginagawa mismo ng gumagamit sa opisyal na Alipay cashier.

## Alipay channel (vibepay, pangunahi)

One-time purchase system: magbayad nang isang beses para sa kaukulang tagal, **hindi auto-renew**. Naka-hardcode ang mga package sa
`src/lib/alipay-vibepay.ts` (`ALIPAY_PACKAGES`):

| key | planId | Pangalan | Presyo | Tagal |
|---|---|---|---|---|
| `monthly` | alipay-monthly | Buwanang membership | ¥6.99 | 30 araw |
| `quarterly` | alipay-quarterly | Tatlong-buwang membership | ¥19.99 | 90 araw |
| `yearly` | alipay-yearly | Taunang membership | ¥69.99 | 365 araw |

### API contract (naka-encapsulate na sa skill script, hindi direktang nagbubuo ng request ang agent)

| Endpoint | Method | Paglalarawan |
|---|---|---|
| `/api/payment/alipay/create-order` | POST | Nangangailangan ng `Authorization: Bearer <JWT>` (sapat na ang pending user). body `{package}` → nagbabalik ng `{paymentHtml, outTradeNo, amount, planName}`; ang `paymentHtml` ay form page na awtomatikong nagse-submit sa Alipay gateway |
| `/api/payment/alipay/query` | GET `?outTradeNo=` | Bearer auth din. Nagbabalik ng `paid` / `pending` / `closed` / `unknown` |
| `/api/payment/alipay/notify` | POST (callback mula sa Alipay server) | Beripikasyon ng limang elemento ng signature (signature, app_id, katumbas na halaga, TRADE_SUCCESS/TRADE_FINISHED, uniqueness ng merchant) → **idempotent** na pag-update ng order + paggawa ng subscription + pag-activate ng account. Hindi kailanman gagalawin ng skill ang endpoint na ito |
| `/payment/alipay/return` | Browser return page | Pampublikong path; pagkatapos ng bayad ay ipinapakita ang 「支付成功」 (matagumpay na bayad) na kumpirmasyon, at nagpo-poll ang page sa totoong status ng back-end |

- Ang mga hindi pa nababayarang order ay **awtomatikong magsasara pagkatapos ng 2 oras**; kung tumigil ang gumagamit sa gitna → muling patakbuhin lang ang `create-order`, hindi na intindihin ang lumang order.
- Isinusulat ng script ang `paymentHtml` sa pansamantalang HTML file, at binubuksan ng agent gamit ang system command para makapasok sa Alipay cashier
  (mag-scan ng QR code o mag-log in sa Alipay para magbayad).

### Activation chain (awtomatiko, walang manual na gawain)

Matapos pumasa ang beripikasyon ng signature ng notify → mamamarkahang nabayaran ang `paymentOrders` → gagawa/magpapatuloy ang `user_subscriptions`
(`planId`, kinukwenta ang `currentPeriodEnd` ayon sa durationDays; sa pag-renew ay ipagpapatuloy mula sa orihinal na petsa ng pag-expire) →
`users.accountStatus: active` + `subscriptionStatus: ACTIVE` → kapag nakita ng return page ang paid, ipapakita ang success.

### Pagkatapos magbayad, kailangang palitan ang log-in status ng bago (mahalaga)

Nagdadala ang JWT ng subscription claim (para sa pending account ito ay `NONE`). **Ang pagdating ng bayad ay nag-a-update lang sa database, hindi nagbabago ng naibigay nang
JWT** — ang claim ng lumang token ay NONE pa rin; kung gagamitin ito nang direkta para gumawa ng log-in link, magiging "walang membership" ang dating.
Kaya ang skill, pagkatapos makumpirma ang `paid`, ay patakbuhin muna ang `refresh-login` (mag-log in muli para sa bagong JWT, magiging ACTIVE ang claim),
bago gawin ang Link 2. Ito ay sadyang disenyo, hindi bug fix.

## Apat na channel sa subscription page

Ipinapakita ng subscription page na `src/app/(public)/subscription/page.tsx` ayon sa running environment:

| Channel | Kapaligiran | Mekanismo | Paraan ng activation |
|---|---|---|---|
| **Alipay (pangunahi)** | Web | Ang `AlipayPaymentSection` ay gumagamit ng vibepay endpoint (talahanayan sa itaas) | Awtomatikong server-side activation sa pamamagitan ng notify, ilang segundo |
| PayPal subscription | Web (hindi Harmony) | `/api/subscription/create` → tumatalon sa PayPal authorization; buwanang auto-renew na maaaring kanselahin anumang oras (`/api/subscription/manage`) | Awtomatikong gagawing active ng PayPal Webhook (`BILLING.SUBSCRIPTION.*`) |
| 「微信扫码订阅」 (WeChat QR subscription) | Web (hindi Harmony) | 「微信扫码订阅」 sa ibaba ng page: mag-scan ng QR code para mag-transfer | **Manual na kumpirmasyon**, maaaring ma-delay ang pagdating ng bayad; huwag magmadaling maghukom na nabigo |
| Huawei in-app purchase | Sa loob ng Harmony app | Native `NativeBridge.purchaseSubscription()` | Bineripika ng `/api/subscription/activate-huawei` ang Huawei order bago i-activate |

Ang mga PayPal plan at presyo ay dinamikong binabasa mula sa `/api/subscription/plans`; nakatakdang text sa page: Auto-renews. Cancel anytime.

## Status at pag-redirect

- Pagkatapos magbayad sa Alipay → ipapakita ng return page ang success; kapag tagumpay sa PayPal → `/subscription/success` → magiging active ang account →
  awtomatikong babalik sa orihinal na page na tinutukoy ng `next` parameter (kung wala, home page).
- Kapag pumunta sa subscription page ang naka-subscribe na nang gumagamit → magpapakita ng "You're All Set!", at pagkatapos ng 3 segundo ay awtomatikong babalik sa home page.
- Nabigo/kanselado ang bayad (PayPal) → `/subscription/cancel`, maaaring muling simulan.

## Troubleshooting

| Sintomas | Paghawak |
|---|---|
| Pagkatapos magbayad sa Alipay, pending pa rin ang `query` | Bihirang ma-delay ang notify; maghintay ng 30 segundo at mag-query muli. Kung hindi pa rin, sabihan ang gumagamit na bumalik sa browser at tingnan ang status sa return page; kung hindi pa rin, kontakin ang platform support (dongtao@outlook.com) at ibigay ang `outTradeNo` |
| Pagkatapos magbayad sa Alipay, hinarang pa rin ng Link 2 | May nakaligtaang `refresh-login` (hindi na-update ang claim ng lumang JWT) — patakbuhin muna ang `refresh-login` bago ang `login-link` |
| 403 pa rin pagkatapos magbayad (PayPal) | Minsan ma-delay ang Webhook; mag-log in muli para i-refresh ang status |
| Nagbayad sa WeChat ngunit hindi na-activate | Manual ang kumpirmasyon at asynchronous; kung hindi pa na-activate sa loob ng ilang oras, kontakin ang platform support |
| Nagpapakita ang subscription page ng "No subscription plans available" | Walang available na PayPal plan sa `/api/subscription/plans`, problema sa configuration sa gilid ng plataporma; para sa mga gumagamit sa China, lumipat lang sa Alipay |

## Makasaysayang tala

May isa pang **lumang** Alipay web payment sa code (`src/lib/alipay.ts`, `/api/payment/create-order`,
¥9.90/¥99 one-time purchase, bumabagsak sa simulated payment kapag walang naka-configure na sandbox key), ngunit hindi kailanman ikinonekta sa subscription page UI at walang kaugnayan sa vibepay.
Hindi ito gagalawin ng skill; ang `alipay-vibepay.ts` ang kasalukuyang gumaganang channel.
