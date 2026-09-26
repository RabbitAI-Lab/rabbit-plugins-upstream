# powpow-register

PowPow Bubble sign-up helper (OpenClaw version): e dey carry new user from "I no know wetin Bubble be" go reach
"account don activate, e fit use am normal" — product introduction (with interface screenshots), step-by-step registration guide,
error checking, subscription activation explanation.

Na pure guide skill, no script, no dependency; all registration actions na the user go do am inside browser/App.

## Installation

```
openclaw skills install @durenzidu/powpow-register
```

## Features

1. **Product introduction**: ~120 words opening + interface screenshot links wey dey hosted for public GitHub repo
   (map page, post detail page, etc. 6 pictures, pick 1–3 according to situation).
2. **Registration guide**: field rules (username/password/email verification code/phone number/profile picture), third-party login
   (Google/Watcha/Huawei), rate limit parameters, all of dem come from platform source code and dem note source.
3. **Error checking**: verification code no dey come, username/email don dey use, 403 never activate, account don lock, etc.
   13 common problems.
4. **Subscription activation**: explanation and checking for three channels PayPal (web) / WeChat scan QR (manual confirm) / Huawei IAP (HarmonyOS);
   the payment chain wey dey now fit use am direct, the skill only dey show road.

## File Structure

```
powpow-register/
├── SKILL.md                            # Main guide (trigger conditions, process, tone standard)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Field rules, rate limit, error checking table (with source citation)
    ├── payment-and-activation.md       # Subscription activation, payment channels, reuse conclusion
    └── screenshots.md                  # Hosted screenshot list + quick check according to situation
```

## Security

- E no get any key; no script, e no dey touch user credentials.
- **Never ask** for the user password, verification code, or payment credentials; registration and payment dey happen complete for platform page.

## License

MIT-0 (ClawHub unified license).

## Links

- Official site: https://global.powpow.online
- Registration: https://global.powpow.online/register
- Know Bubble (video): https://www.bilibili.com/video/BV1Wu826UEVz/