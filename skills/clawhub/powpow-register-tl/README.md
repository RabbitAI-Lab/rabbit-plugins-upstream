# powpow-register

Katulong sa pagrehistro ng PowPow Bubble (bersyon OpenClaw): dalhin ang bagong user mula sa "hindi alam kung ano ang Bubble" papunta sa
"na-activate ang account, magagamit nang normal" — pagpapakilala ng produkto (may kasamang screenshots), sunud-sunod na gabay sa pagrehistro,
pagtingin sa error, pagpapaliwanag ng subscription activation.

Skill na puro gabay, walang script, walang dependency; lahat ng aksyon sa pagrehistro ay ginagawa ng user sa browser/App.

## Pag-install

```
openclaw skills install @durenzidu/powpow-register
```

## Mga Kakayahan

1. **Pagpapakilala ng produkto**: ~120 salita na pagbubukas + mga screenshot link na naka-host sa pampublikong GitHub repo
   (pahina ng mapa, pahina ng post details, atbp. 6 na larawan, pumili ng 1–3 ayon sa sitwasyon).
2. **Gabay sa pagrehistro**: field rules (username/password/email verification code/numero ng telepono/profile photo), third-party login
   (Google/Watcha/Huawei), rate limit parameters, lahat mula sa platform source code at may citation.
3. **Pagtingin sa error**: hindi dumating ang verification code, ginamit na ang username/email, 403 hindi pa aktibo, naka-lock ang account, atbp.
   13 karaniwang problema.
4. **Subscription activation**: paliwanag at pagtingin sa tatlong channel na PayPal (web) / WeChat QR scan (manual confirmation) / Huawei IAP (HarmonyOS);
   ang kasalukuyang payment chain ay puwedeng direktang gamitin muli, gabay lang ang skill.

## Istruktura ng File

```
powpow-register/
├── SKILL.md                            # Pangunahing gabay (trigger conditions, proseso, pamantayan ng tone)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Field rules, rate limit, error checking table (may source citation)
    ├── payment-and-activation.md       # Subscription activation, payment channel, konklusyon sa paggamit muli
    └── screenshots.md                  # Listahan ng hosted screenshots + mabilisang pagtingin ayon sa sitwasyon
```

## Seguridad

- Walang anumang susi; walang script, hindi nagkakalapit sa user credentials.
- **Huwag kailanman humingi** ng password, verification code, o payment credentials ng user; ganap na sa platform page ang pagrehistro at pagbabayad.

## Lisensya

MIT-0 (unified na lisensya ng ClawHub).

## Mga Link

- Opisyal na site: https://global.powpow.online
- Pagrehistro: https://global.powpow.online/register
- Kilalanin ang Bubble (video): https://www.bilibili.com/video/BV1Wu826UEVz/