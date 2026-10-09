# powpow-register

PowPow Bubble registration helper (OpenClaw version): carry one new user from "e no know wetin Bubble be" go reach "account don activate, one-click login, start to play" — product intro (with interface screenshots), registration wey agent go do (including avatar upload), Alipay subscription order and money-landing tracking, one-click login with two links, error troubleshooting.

**From v2.0.0 na agent-do-am mode**: di main script `scripts/powpow-register.mjs` zero dependency (Node >= 18), di user no dey comot from di chat at all, e only comot two times for small time: go email check di verification code, pay for di Alipay cashier. When Node no dey or di user wan do am by imsef, e go fall back to guide-only mode by imsef.

## Installation

```
openclaw skills install @durenzidu/powpow-register
```

## Features

1. **Product intro**: about 120 words opening + interface screenshots wey dey inside di package (`assets/screenshots/` get 6 pictures under am: map page, post detail page etc., choose 1–3 to send based on di situation; no need external image host, e dey work offline).
2. **Do-am registration**: agent go suggest username/nickname by imsef, password choose one of two (user provide am or agent generate am), send and submit di verification code, avatar direct upload (<=5MB no be SVG), common errors dem dey handle automatic (don dey take/don expire/rate limit).
3. **One-click login (two links)**: registration success give "half-login" link wey land direct on subscription page; after money land, change to new login state then give full member link wey land direct on homepage (e pass through di platform official `me?token=` bridge, e plant HttpOnly cookie automatic).
4. **Subscription payment**: Alipay channel, agent go create order (monthly ¥6.99 / quarterly ¥19.99 / yearly ¥69.99, one-time buy no auto-renew) + poll money landing; overseas users fall back to PayPal; WeChat scan code/Huawei IAP just point di way.
5. **Error troubleshooting**: verification code no dey come, username/email don dey take, 403 no activate, account lock etc. common problems, all of dem come from platform source code with location mark.

## File structure

```
powpow-register/
├── SKILL.md                            # Main guide (trigger conditions, 8-step flow, tone rules, hard rules)
├── README.md
├── .clawhubignore
├── assets/
│   └── screenshots/                    # Product screenshots wey dey inside di package (powpow-01~06.jpg)
├── scripts/
│   └── powpow-register.mjs             # Main script (zero dependency Node>=18, 11 sub-commands)
└── references/
    ├── agent-flow.md                   # Script contract, full sequence, two-link mechanism, security design
    ├── registration-flow.md            # Field rules, rate limit, error troubleshooting table (with source code location)
    ├── payment-and-activation.md       # Alipay vibepay contract, activation chain, channel troubleshooting
    └── screenshots.md                  # Package screenshot list + scenario quick-find
```

## Security

- **Password** only enter di script process through environment variable, never write am inside command line argument, no store am on disk, no put am inside state file; password wey agent generate show once only so di user go save am.
- **Verification code** only dey use for di official registration endpoint, e dey throway once dem use am finish; di state file (email/username/token/order number) dey store for di system temporary directory, when di flow finish `cleanup` go clear am one click.
- **Payment**: agent only create order, open cashier, check money landing; never touch di user Alipay account or payment credential, never pay for am. Payment always happen between di user and di Alipay official cashier.
- All requests dey go only to di official domain `https://global.powpow.online`; e no carry any key inside.

## License

MIT-0 (di unified ClawHub license).

## Links

- Official website: https://global.powpow.online
- Register: https://global.powpow.online/register
- Know Bubble (video): https://www.bilibili.com/video/BV1Wu826UEVz/
