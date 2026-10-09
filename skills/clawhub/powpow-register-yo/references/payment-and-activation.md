# Ṣiṣe alaisanfarasin ati isanwo — powpow-register

## Ipari (sọ idahun kọkọ)

**Ọna Alipay ti ṣii (latọjọ 2026-10-07), o jẹ ọna isanwo akọkọ ti skill ṣe iranlọwọ, agent le ṣe aṣẹ ati tọpa isanwo.** Olumulo okeere/laisi Alipay pada si PayPal; iwo-koodu WeChat (timọ-ọkọnrin) ati Huawei IAP tun wa, ṣugbọn skill ko ṣe iranlọwọ wọn.

Awọn aala iṣẹ isanwo: agent le **ṣẹda aṣẹ, ṣii alagbata, ṣe ibeere isanwo**; **rara** fọwọkan akọọlẹ Alipay olumulo / ẹri isanwo, rara ṣe ileri "sanwo ni ipo rẹ". Iṣe isanwo nigbagbogbo jẹ ti olumulo funrarẹ ni alagbata Alipay osise.

## Ọna Alipay (vibepay, akọkọ)

Iṣe rira-lẹẹkan: sanwo lẹẹkan ṣiṣi akoko deede, **ko ṣe isọdọtun laifọwọyi**. Awọn ẹgbẹ ti wa titi ninu
`src/lib/alipay-vibepay.ts` (`ALIPAY_PACKAGES`):

| key | planId | Orukọ | Iye | Akoko |
|---|---|---|---|---|
| `monthly` | alipay-monthly | Ọmọ ẹgbẹ oṣu | ¥6.99 | ọjọ 30 |
| `quarterly` | alipay-quarterly | Ọmọ ẹgbẹ mẹẹdogun | ¥19.99 | ọjọ 90 |
| `yearly` | alipay-yearly | Ọmọ ẹgbẹ ọdun | ¥69.99 | ọjọ 365 |

### Adrhun aaye (iwe skill ti fi pamọ, agent ko ṣe akopọ ibeere)

| Aaye | Ọna | Apejuwe |
|---|---|---|
| `/api/payment/alipay/create-order` | POST | Nilo `Authorization: Bearer <JWT>` (olumulo pending o le). body `{package}` → da `{paymentHtml, outTradeNo, amount, planName}` pada; `paymentHtml` jẹ oju-iwe fọọmu ti o fi ranṣẹ si ẹnu-bode Alipay laifọwọyi |
| `/api/payment/alipay/query` | GET `?outTradeNo=` | Bakan naa Bearer. Da `paid` / `pending` / `closed` / `unknown` pada |
| `/api/payment/alipay/notify` | POST (ipe pada olupin Alipay) | Ṣayẹwo ibuwọn awọn eroke marun (ibuwọn, app_id, iye ibaramu, TRADE_SUCCESS/TRADE_FINISHED, ayẹwo onisọpọ alailẹgbẹ) → **idapọmọra** imudojuiwọn aṣẹ + ṣẹda ṣiṣe alaisanfarasin + mu akọọlẹ ṣiṣẹ. Skill ko gbọdọ kan si aaye yii rara |
| `/payment/alipay/return` | Oju-iwe ipadabọ aṣawakiri | Ọna gbangba, lẹhin isanwo ṣafihan "isanwo aṣeyọri", oju-iwe naa ṣe ibeere ipo gidi ẹgbẹ |
| `/api/payment/alipay/notify` | POST | Wo loke |

- Aṣẹ ti ko sanwo **laifọwọyi pa lẹhin wakati 2**; ti olumulo ba fi silẹ lara ọna → tun ṣiṣẹ `create-order` taara, aṣẹ atijọ ko ṣe aniyan.
- Iwe naa kọ `paymentHtml` sinu faili HTML igba-die, agent ṣiṣi pẹlu aṣẹ eto lati wọle si alagbata Alipay
  (ṣe iwo koodu tabi wọle si Alipay lati sanwo).

### Ṣiṣan imuyipada (laifọwọyi, laisi ọwọ)

notify ṣayẹwo ibuwọn kọja → `paymentOrders` samisi ti sanwo → `user_subscriptions` ṣẹda/tẹsiwaju
  (`planId`, `currentPeriodEnd` iṣiro nipasẹ durationDays, isọdọtun tẹsiwaju lori ọjọ ti o ti kọja) →
  `users.accountStatus: active` + `subscriptionStatus: ACTIVE` → oju-iwe ipadabọ ṣe ibeere si paid ṣafihan aṣeyọri.

### Lẹhin isanwo gbọdọ ṣe paṣipaarọ ipo wiwọle tuntun (pataki)

JWT ni ikede ṣiṣe alaisanfarasin (akọọlẹ pending jẹ `NONE`). **Isanwo ti de ṣe imudojuiwọn DB nikan, ko yi JWT ti a ti fowo si** — ikede token atijọ tun jẹ NONE, lilo taara lati ṣe ipilẹṣẹ ọna asopọ wiwọle yoo farahan bi "laisi ọmọ ẹgbẹ".
Nitorina skill lẹhin imudaniloju `paid` kọkọ ṣiṣẹ `refresh-login` (tun wọle ṣe paṣipaarọ JWT tuntun, ikede di ACTIVE),
lẹhinna ṣe ipilẹṣẹ ọna asopọ 2. Eyi jẹ ihuwasi apẹrẹ, kii ṣe atunṣe fara.

## Awọn ọna mẹrin oju-iwe ṣiṣe alaisanfarasin

Oju-iwe ṣiṣe alaisanfarasin `src/app/(public)/subscription/page.tsx` n ṣafihan ni ibamu si agbegbe ṣiṣe:

| Ọna | Agbegbe | Ẹro | Ọna imuyipada |
|---|---|---|---|
| **Alipay (akọkọ)** | Oju-iwe wẹẹbu | `AlipayPaymentSection` n lọ si aaye vibepay (tabili loke) | notify olupin mu ṣiṣẹ laifọwọyi, iṣẹju diẹ |
| Ṣiṣe alaisanfarasin PayPal | Oju-iwe wẹẹbu (kii ṣe Harmony) | `/api/subscription/create` → lọ si aṣẹ PayPal; isọdọtun oṣu laifọwọyi ti a le fagilee nigbakugba (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) mu ṣiṣẹ active laifọwọyi |
| Iwo-koodu WeChat | Oju-iwe wẹẹbu (kii ṣe Harmony) | "微信扫码订阅" ni isalẹ oju-iwe: ṣe iwo-koodu gbigbe | **Timọ-ọkọnrin**, isanwo le ṣe idaduro; ti o ba sanwo ma ṣe yarayara ṣayẹwo ikuna |
| Riraya inu ohun elo Huawei | Inu App Harmony | `NativeBridge.purchaseSubscription()` abinibi | `/api/subscription/activate-huawei` ṣayẹwo aṣẹ Huawei lẹhinna mu ṣiṣẹ |

Eto PayPal ati iye lati `/api/subscription/plans` ka nigbagbogbo; ọrọ ipinnu oju-iwe: Auto-renews. Cancel anytime.

## Ipo ati darí

- Alipay sanwo pari → oju-iwe ipadabọ ṣafihan aṣeyọri; aṣeyọri PayPal → `/subscription/success` → akọọlẹ active →
  darí pada si oju-iwe atilẹba ti `next` (ti ko ba si oju-iwe ile).
- Olumulo ti o ti ṣe alaisanfarasin ti o ba tun wo oju-iwe ṣiṣe alaisanfarasin → ṣafihan "You're All Set!", lẹhin iṣẹju 3 darí pada oju-iwe ile laifọwọyi.
- Isanwo kuna/ifagilee (PayPal) → `/subscription/cancel`, le tun bẹrẹ.

## Ṣiṣayẹwo

| Iṣẹlẹ | Ṣetọju |
|---|---|
| Alipay sanwo pari `query` tun jẹ pending | notify ṣe idaduro kekere; duro iṣẹju 30 ki o to tun ṣe ibeere. Ti ko ba ṣiṣẹ jẹ ki olumulo wo ipo oju-iwe ipadabọ, ti ko ba tun ṣiṣẹ kan si atilẹyin pẹpẹ (dongtao@outlook.com), fun `outTradeNo` |
| Alipay sanwo pari, ọna asopọ 2 tun di didena | A bu `refresh-login` (ikede JWT atijọ ko tii ṣe imudojuiwọn) — kọkọ `refresh-login` lẹhinna `login-link` |
| Sanwo pari tun 403 (PayPal) | Webhook n ṣe idaduro lẹẹkọọkan, tun wọle ṣe imudojuiwọn ipo |
| WeChat sanwo ko ṣiṣẹ | Timọ-ọkọnrin jẹ aiṣiṣẹ, ti ko ba ṣiṣẹ laarin awọn wakati diẹ kan si atilẹyin pẹpẹ |
| Oju-iwe ṣiṣe alaisanfarasin n ṣafihan "No subscription plans available" | `/api/subscription/plans` ko ni ẹgbẹ PayPal to wulo, iṣoro iṣeto ẹgbẹ pẹpẹ; olumulo Ilu China yi lọ si Alipay |

## Akọsilẹ itan

Inu koodu tun wa **atijọ** ti isanwo oju-iwe Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`,
¥9.90/¥99 rira-lẹẹkan, ni agbegbe sandbox ti ko ni bọtini o dinku si ifarawe isanwo), ko tii sopọ mọ UI oju-iwe ṣiṣe alaisanfarasin, ko ni nkankan ṣe pẹlu vibepay. Skill ko gbọdọ kan si rara; `alipay-vibepay.ts` ni ọna lọwọlọwọ.
