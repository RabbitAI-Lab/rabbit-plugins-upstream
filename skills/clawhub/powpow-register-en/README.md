# powpow-register

The PowPow Bubble registration assistant (OpenClaw edition): takes a new user from “I don't know what Bubble is” to “account activated and ready to use” — product intro (with UI screenshots), step-by-step registration walkthrough, error troubleshooting, and subscription activation explained.

A pure guidance skill: no scripts, no dependencies; all registration actions are completed by the user in the browser/App.

## Installation

```
openclaw skills install @durenzidu/powpow-register
```

## Features

1. **Product intro**: ~120-character opening + UI screenshot links hosted in a public GitHub repo (6 images: map page, post detail page, etc.; send 1–3 depending on the scenario).
2. **Registration walkthrough**: field rules (username/password/email verification code/phone/avatar), third-party login (Google/Watcha/Huawei), rate-limit parameters — all taken from the platform source code with citations.
3. **Error troubleshooting**: 13 common issues, including verification code not received, username/email already taken, 403 not activated, account locked.
4. **Subscription activation**: three channels — PayPal (web) / WeChat QR code (manual confirmation) / Huawei IAP (HarmonyOS) — with explanations and troubleshooting; the existing payment chain is reused as-is, the skill only shows the way.

## File Structure

```
powpow-register/
├── SKILL.md                            # Main guidance (triggers, flow, tone rules)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Field rules, rate limits, error lookup table (with source citations)
    ├── payment-and-activation.md       # Subscription activation, payment channels, reuse conclusion
    └── screenshots.md                  # Hosted screenshot list + scenario quick reference
```

## Security

- Contains no secrets; no scripts, never touches user credentials.
- **Never ask for** the user's password, verification code or payment credentials; registration and payment all happen on the platform pages.

## License

MIT-0 (unified ClawHub license).

## Links

- Official site: https://global.powpow.online
- Registration: https://global.powpow.online/register
- Learn about Bubble (video): https://www.bilibili.com/video/BV1Wu826UEVz/