# Subscription Activation and Payment — powpow-register

## Conclusion (talk the answer first)

**The payment method wey dey now fit use am direct, the registration helper skill na zero payment development.**

Reasons:

1. The registration endpoint (`src/app/api/auth/register/route.ts`) when e dey create pending account, e don already issue
   JWT cookie + pendingUserToken HttpOnly cookie, when user land for `/subscription`, e don already
   dey login status — the three payment channels all dey hang on this subscription page, and wetin dem dey activate na the same pending account.
2. The login endpoint for pending account dey return 403 + `redirectTo: '/subscription'`, e still plant the
   same cookie — no matter when the user later complete payment, dem go guide am back to the same page.
3. So the responsibility boundary of registration guide skill na "carry the user go /subscription"; e no need new
   payment endpoint, e no need new order model, e no need any backend change.

At the same time, make you know: the payment stage (PayPal JS SDK button, WeChat scan QR manual confirm, native Huawei IAP)
**na how e dey make e impossible and e no suppose be paid by command-line/chat skill**. No try to use script to call payment
endpoint to pay for the user, and no ask for the user payment credentials.

## Three Channels on the Subscription Page

The subscription page `src/app/(public)/subscription/page.tsx` dey show am automatic according to the running environment:

| Channel | Environment | Mechanism | Activation Method |
|---|---|---|---|
| PayPal subscription | Web (no be HarmonyOS) | `/api/subscription/create` dey create PayPal subscription → go jump to PayPal authorization; e dey renew automatic every month, you fit cancel any time (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) dey set `accountStatus` to active automatic |
| WeChat scan QR subscription | Web (no be HarmonyOS) | "WeChat scan QR subscription" block for down the page: scan QR transfer, **e go open after manual confirm** (`WechatQrPaymentSection`) | manual confirm, the money fit delay; after user pay, no rush to say e fail |
| Huawei in-app purchase (IAP) | Inside HarmonyOS App | for HarmonyOS WebView, PayPal/WeChat payment no fit use, the page go change to native `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` dey verify Huawei order before e activate |

The plans and prices dey read from `/api/subscription/plans` dynamic (PayPal plans); the fixed text on the page:
Auto-renews. Cancel anytime.

## Status and Page Jumps

- Payment success → `/subscription/success` (PayPal callback dey carry `subscriptionId`) → account
  active → e go jump back to the original page wey `next` specify (if no get, na home page).
- User wey don subscribe wey dey visit subscription page again → e go show "You're All Set!", after 3 seconds e go go back home automatic.
- Payment fail/cancel → `/subscription/cancel`, you fit start am again.

## Error Checking

| Symptom | Handling |
|---|---|
| You don pay but still 403 | PayPal: Webhook dey delay sometimes, login again to refresh status (when you login, e go check the latest status from DB again); WeChat: manual confirm never finish, wait small; Huawei: check whether the in-app payment success page don show |
| Subscription page dey show "No subscription plans available" | `/api/subscription/plans` no get available PayPal plan, na platform-side configuration issue, make the user try again later |
| You pay WeChat but e never open | the manual confirm na async, if hours don pass and e still never open, then contact platform support (dongtao@outlook.com) |

## Note: Alipay

Inside the code, there be one set of Alipay web payment (`src/lib/alipay.ts`, `/api/payment/create-order`,
one-time buy model wey regular member na ¥9.90 / premium member na ¥99, if sandbox never configure key, e go down automatic
to simulated payment), **but e never connect to the subscription page UI**, na idle/reserved code. If one day you wan
enable Alipay for the subscription page, just wire this existing code set — this one no dey relate to this skill,
e just dey for platform-side decision reference.