# Subscription activation and payment — powpow-register

## Conclusion (di answer first)

**Di Alipay channel don go live (from 2026-10-07), na di main payment method wey dis skill dey push, agent fit do order and money-landing tracking for di user.**
Overseas/user wey no get Alipay dem fall back to PayPal; WeChat scan code (human confirm) and Huawei IAP still dey, but skill no dey do dem for di user.

Di duty boundary for di payment part: agent fit **create order, open cashier, check money landing**; **never** touch di user Alipay account/payment credential, never promise say "e go pay for am". Di payment action always na di user imsef go do am for di Alipay official cashier.

## Alipay channel (vibepay, main push)

One-time buy system: pay once to open di corresponding time, **e no dey auto-renew**. Di packages dey fixed inside `src/lib/alipay-vibepay.ts` (`ALIPAY_PACKAGES`):

| key | planId | Name | Price | Duration |
|---|---|---|---|---|
| `monthly` | alipay-monthly | Monthly member | ¥6.99 | 30 days |
| `quarterly` | alipay-quarterly | Quarterly member | ¥19.99 | 90 days |
| `yearly` | alipay-yearly | Yearly member | ¥69.99 | 365 days |

### Endpoint contract (di skill script don wrap dem already, agent no dey build request direct)

| Endpoint | Method | Explanation |
|---|---|---|
| `/api/payment/alipay/create-order` | POST | E need `Authorization: Bearer <JWT>` (pending user dey okay). body `{package}` → e return `{paymentHtml, outTradeNo, amount, planName}`; `paymentHtml` na di form page wey dey submit to di Alipay gateway automatic |
| `/api/payment/alipay/query` | GET `?outTradeNo=` | Same Bearer authentication. E return `paid` / `pending` / `closed` / `unknown` |
| `/api/payment/alipay/notify` | POST (Alipay server callback) | Check signature five elements (signature, app_id, amount match, TRADE_SUCCESS/TRADE_FINISHED, merchant uniqueness) → **idempotent** update order + build subscription + activate account. Skill never touch dis endpoint |
| `/payment/alipay/return` | Browser return page | Public path, after payment e show 支付成功 (payment success) confirmation, inside di page e dey poll di backend real status |

- Order wey no pay **go close automatic after 2 hours**; if user give up for middle → just run `create-order` again, no mind di old order.
- Di script write `paymentHtml` into temporary HTML file, agent use system command open am to enter di Alipay cashier (scan code or login inside Alipay to pay).

### Activation chain (automatic, no need human)

notify signature check pass → `paymentOrders` mark as paid → `user_subscriptions` build/extend (`planId`, `currentPeriodEnd` dem calculate am based on durationDays, renewal dey extend on top di original expiry date) → `users.accountStatus: active` + `subscriptionStatus: ACTIVE` → di return page poll until paid then e show success.

### After payment you must change to new login state (important)

Di JWT carry subscription claim inside (pending account na `NONE`). **When payment land e only update di database, e no go change di JWT wey dem don already issue** — di old token claim still be NONE, if you use am direct to generate login link e go behave like "no member". So di skill after e confirm `paid` first run `refresh-login` (login again to change to new JWT, claim change to ACTIVE), then generate link 2. Na design behavior be dis, e no be vulnerability fix.

## Subscription page four channels

Di subscription page `src/app/(public)/subscription/page.tsx` dey show based on di running environment:

| Channel | Environment | Mechanism | How e activate |
|---|---|---|---|
| **Alipay (main push)** | Web side | `AlipayPaymentSection` pass through vibepay endpoint (di table above) | notify server-side activate automatic, seconds level |
| PayPal subscription | Web side (no be Harmony) | `/api/subscription/create` → jump to PayPal authorization; monthly auto-renew fit cancel anytime (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) set active automatic |
| 微信扫码订阅 (WeChat scan code subscribe) | Web side (no be Harmony) | Page bottom 微信扫码订阅 (WeChat scan code subscribe): scan code transfer money | **Human confirm**, money fit land late; after payment no rush judge say e fail |
| Huawei in-app purchase | Inside Harmony App | Native `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` verify di Huawei order then activate |

PayPal plans and prices dey read from `/api/subscription/plans` dynamic; di page fixed text: Auto-renews. Cancel anytime.

## Status and redirect

- Alipay payment finish → di return page show success; PayPal success → `/subscription/success` → account active → e jump back to di original page wey di `next` parameter point (if no dey, homepage).
- User wey don subscribe visit di subscription page again → e show "You're All Set!", after 3 seconds e go back to homepage automatic.
- Payment fail/cancel (PayPal) → `/subscription/cancel`, you fit start am again.

## Troubleshooting

| Wetin you see | How to handle am |
|---|---|
| Alipay pay finish `query` still pending | notify delay rare rare; wait 30 seconds then check again. If e still no work, make di user go back to browser check di return page status; if e still no work contact platform support (dongtao@outlook.com), report `outTradeNo` |
| Alipay pay finish, link 2 enter still dey block | You miss run `refresh-login` (old JWT claim no update) — first `refresh-login` then `login-link` |
| Pay finish still 403 (PayPal) | Webhook sometimes get delay, login again to refresh di status |
| WeChat pay but e no activate | Human confirmation na asynchronous, if e no activate within few hours then contact platform support |
| Subscription page show "No subscription plans available" | `/api/subscription/plans` no get available PayPal plan, na platform side configuration problem; China users just switch to Alipay |

## History note

Inside di code still get one **old** Alipay web payment (`src/lib/alipay.ts`, `/api/payment/create-order`, ¥9.90/¥99 one-time buy, when sandbox no configure key e degrade to mock payment), dem never connect am to di subscription page UI at all, e no relate to vibepay. Skill no dey touch am at all; `alipay-vibepay.ts` na di current channel.
