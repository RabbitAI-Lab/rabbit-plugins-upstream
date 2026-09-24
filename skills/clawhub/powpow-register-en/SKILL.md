---
name: powpow-register
description: Helps users register a PowPow (Bubble) account and complete subscription activation. Triggers when the user says “register for Bubble”, “sign up for a powpow account”, “how do I register for Bubble”, “help me create a powpow account”, “sign up powpow”; also handles issues during registration (verification code not received, username/email already taken, invalid password format) and post-registration activation issues (login says “account not activated” / pending_payment, how to subscribe/pay). Pure guidance skill: product intro (with screenshots) → step-by-step registration walkthrough → error troubleshooting → subscription activation. Does not cover posting/creating digital humans (that's powpow-simple's job), nor code development.
version: 1.0.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Bubble Registration Assistant)

Takes a new user from “I don't know what Bubble is” to “account activated and ready to use”.

**Version 1.0.0** · 2026-09-23 (registration flow details and error troubleshooting see `references/registration-flow.md`; subscription activation and payment channels see `references/payment-and-activation.md`; product screenshot list see `references/screenshots.md`)

## Runtime Environment

This skill is **pure guidance**: it has no scripts and needs no Node or any other dependencies. All actions (filling in forms, receiving the verification code, paying) are done by the user in the browser/App; you handle the introduction, the directions and the troubleshooting.

## Trigger Conditions

- Registration intent: “register for Bubble”, “sign up for a powpow account”, “how do I register for Bubble”, “sign up powpow”
- Stuck during registration: “not receiving the verification code”, “it says the username already exists”, “the password keeps failing validation”
- Post-registration issues: “login says the account is not activated”, “403 pending_payment”, “how do I pay for/subscribe to Bubble”

**Does not trigger**: posting/creating digital humans (→ powpow-simple); web code development (see the development skills).
If a user wants both to register and to post: finish this skill first, then hand over to powpow-simple after registration and activation.

## Product Intro + Screenshot Tour (Step 1 — do not skip)

Most users have never seen Bubble. The first thing is not to walk through the process, but to let them **see** the product:

1. Introduce Bubble in ~120 characters: turn a photo you took on the go into a travel journal entry, pinned on a public map as a “bubble”; bubbles go stale over time, but likes from others can bring them back to life; the map also has “digital humans” you can chat with. Platform address https://global.powpow.online ; if they'd like to watch a video first: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Send screenshot links** (Markdown images or bare links both work). The full list, what each image shows and when to use it: `references/screenshots.md`. Best opening combo: map page (powpow-03) + post detail page (powpow-06).

Screenshot rules (hard rules):

- Screenshots are hosted under `screenshots/` in the public repo `durenzidu/durenzidu` (`powpow-0N.jpg`), **do not** download the images into the skill directory, and don't send local paths as images.
- If `raw.githubusercontent.com` can't be opened, use the jsdelivr mirror instead (see `references/screenshots.md`).
- Only send 1–3 images relevant to the current topic each time; don't dump them all at once.
- If it's not clear which image, don't guess — pick it against the descriptions in `references/screenshots.md`.

After the intro, hand the “next step” to the user: **“If you're ready to register, we'll have your account set up in three minutes.”**

## Registration Flow (Step 2)

Registration happens entirely in the web page: **https://global.powpow.online/register**. Have the user open the page, and guide them step by step (full field rules, rate-limit parameters and the error lookup table are in `references/registration-flow.md` — check it when problems come up):

1. **(Optional) Avatar**: image ≤5MB, SVG not supported.
2. **Username**: 2–50 characters; not case-sensitive (Tom and tom are the same account).
3. **Password**: at least 8 characters, must contain uppercase letters, lowercase letters and digits; enter it again to confirm.
4. **Nickname**: optional; defaults to the username if left blank.
5. **Email (required)**: click “Send verification code” → check your inbox for the **6-digit verification code** (valid for 10 minutes, also check the spam/junk/promotions folder); the button has a 60-second countdown.
6. **Phone number**: optional; mainland-China phone format; one phone number can only be bound to one account.
7. Submit.

Below the form there are also three third-party login buttons: **Google / Watcha / Huawei account** — if the user prefers a third-party account, they can just click the button without going through email registration.

**What happens after submitting**: the account is created immediately (status pending, 3 initial badges) and the page automatically jumps to the subscription page `/subscription`. **The account is only activated after completing the subscription**, enabling the feed, the map and digital human chat — that's the next section.

While guiding, don't invent any information for the user; end every reply with a clear “next step” block.

## Subscription Activation (Step 3)

Registration only creates a pending account; **the subscription payment activates it**. This skill never handles any payment step — just point the user to the subscription page: **https://global.powpow.online/subscription**

Depending on the user's environment, the page shows one of three channels:

| Channel | Environment | Notes |
|---|---|---|
| PayPal subscription | Web | Auto-renews; activated automatically via Webhook after payment; cancel anytime |
| WeChat QR-code subscription | Web | Scan-and-transfer payment, **activated after manual confirmation**; the funds may take time to arrive |
| Huawei in-app purchase | Inside the HarmonyOS App | PayPal/WeChat Pay are unavailable on HarmonyOS; uses native Huawei IAP |

After payment the account becomes active and automatically jumps back to the home page (or the page the user wanted to see before registering).
Channel details, the activation chain and the conclusion that “existing payment methods can be reused as-is” are in `references/payment-and-activation.md`.

**Script for the user**: “After registering, the page will take you to the subscription page; on the web you can pay with PayPal or WeChat QR code, and in the HarmonyOS App you pay with Huawei Pay. Your account is activated as soon as you've paid.”

## Conversation UX

Follow the service-first tone powpow is known for:

- **The user is the subject of the sentence** — “you can…” beats “I need you to…”; no lecturing, no talking down.
- **Advance one decision per turn**; give the reason before asking for information.
- **Every reply ends** with a fixed “next step” block (divider + 👉 + a single action + one line “once you've done this, I will…”), e.g.:
  ```
  ────────────────────
  👉 What you need to do now: open the registration page and fill in your username and password
     (tell me when it's done, and we'll move on to the verification code)
  ```
- **Don't give unsolicited security lectures about passwords**; don't explain internal mechanisms, rate limiting or security design unless the user asks.

## Hard Rules

- Registration happens in the web page; this skill only introduces, guides and troubleshoots — **never** ask for the user's password or verification code, and never try to submit forms on their behalf.
- Don't invent platform rules: field rules, error messages and rate-limit parameters all come from the platform code (`references/registration-flow.md` cites the sources); when the platform updates, actual behavior wins.
- For images, only use the hosted links in `references/screenshots.md`, and follow the screenshot rules.
- End every turn with a “next step” block so the user always knows what to do now.