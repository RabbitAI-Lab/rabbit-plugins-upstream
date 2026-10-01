# Subscription Activation and Payment — powpow-register

## Conclusion (the answer first)

**Existing payment methods can be reused as-is — the registration assistant skill needs zero payment development.**

Reasons:

1. The registration API (`src/app/api/auth/register/route.ts`) already issues a JWT cookie + pendingUserToken HttpOnly cookie when creating the pending account, so by the time the user lands on `/subscription` they are already logged in — all three payment channels hang off this subscription page, and all of them activate the same pending account.
2. The login API returns 403 + `redirectTo: '/subscription'` for pending accounts and sets the cookies the same way — a user paying late will always be routed back to the same page.
3. Therefore the responsibility boundary of a registration-guidance skill is simply “get the user to /subscription”; no new payment API, no new order model, no backend changes needed.

Also note: the payment step (PayPal JS SDK button, WeChat QR-code manual confirmation, native Huawei IAP) **means it cannot and should not be paid on behalf of the user by a command-line/chat skill**. Don't try to call payment APIs from a script to pay for the user, and don't ask for the user's payment credentials.

## The Three Channels on the Subscription Page

The subscription page `src/app/(public)/subscription/page.tsx` automatically shows the matching channel based on the runtime environment:

| Channel | Environment | Mechanism | Activation |
|---|---|---|---|
| PayPal subscription | Web (non-HarmonyOS) | `/api/subscription/create` creates a PayPal subscription → redirects to PayPal for authorization; auto-renews monthly, cancel anytime (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) automatically sets `accountStatus` to active |
| WeChat QR-code subscription | Web (non-HarmonyOS) | “Scan WeChat to subscribe” section at the bottom of the page: scan to transfer money, **activated after manual confirmation** (`WechatQrPaymentSection`) | Manual confirmation; the funds may arrive with a delay — don't rush to call it a failure right after the user pays |
| Huawei in-app purchase (IAP) | Inside the HarmonyOS App | PayPal/WeChat Pay are unavailable in the HarmonyOS WebView, so the page uses the native `NativeBridge.purchaseSubscription()` instead | `/api/subscription/activate-huawei` verifies the Huawei order and then activates |

Plans and prices are read dynamically from `/api/subscription/plans` (PayPal plans); the page's fixed copy reads: Auto-renews. Cancel anytime.

## Status and Redirects

- Payment success → `/subscription/success` (PayPal callback carries `subscriptionId`) → account active → auto-return to the original page specified by the `next` parameter (home page if none).
- An already-subscribed user visiting the subscription page → shows "You're All Set!", auto-returns to home after 3 seconds.
- Payment failure/cancellation → `/subscription/cancel`, a new attempt can be started.

## Troubleshooting

| Symptom | Handling |
|---|---|
| Still 403 after paying | PayPal: the Webhook is occasionally delayed — log out/in again to refresh the status (login re-checks the latest DB status); WeChat: manual confirmation hasn't finished, wait a bit; Huawei: check whether the in-app payment success page appeared |
| Subscription page shows "No subscription plans available" | No usable PayPal plans on `/api/subscription/plans` — a platform-side configuration issue; ask the user to try again later |
| Paid via WeChat but not activated | Manual confirmation is asynchronous; if it hasn't been activated within a few hours, contact platform support (dongtao@outlook.com) |

## Note: Alipay

The codebase contains a set of Alipay web payment code (`src/lib/alipay.ts`, `/api/payment/create-order`, a one-time purchase model: regular membership ¥9.90 / premium membership ¥99; auto-degrades to mock payment when the sandbox key is unset), **but it is not wired into the subscription page UI** — it's idle/reserved code. If Alipay ever needs to be enabled on the subscription page, wire up this ready-made code — this is unrelated to this skill and is noted here only as reference for platform-side decisions.