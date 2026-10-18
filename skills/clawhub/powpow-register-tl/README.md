# powpow-register

Katulong sa pagrehistro ng PowPow Bula (OpenClaw version): samahan ang bagong gumagamit mula sa "hindi alam kung ano ang Bula" hanggang sa "naka-activate na ang account, one-click log in, maaari nang maglaro" — pagpapakilala ng produkto (kasama ang mga screenshot ng interface), agent-assisted na rehistro (kasama ang pag-upload ng avatar), Alipay/PayPal subscription ordering at pagsubaybay sa pagdating ng bayad, two-link one-click log in, at pag-troubleshoot ng mga error.

**Mula v2.0.0 ay agent-assisted mode, at mula v2.1.0 ang PayPal ay kayang hawakan din**: ang pangunahing script `scripts/powpow-register.mjs` ay zero dependency (Node >= 18), hindi umaalis ang gumagamit sa usapan, at dalawang beses lang siyang pansamantalang aalis: puntahan ang email para makita ang verification code, at magbayad sa Alipay/PayPal cashier. Kapag walang Node o gusto mismo ng gumagamit na gumawa nang mag-isa, automatic na bumabalik sa pure guidance mode.

## Pag-install

```
openclaw skills install @durenzidu/powpow-register
```

## Mga Tampok

1. **Pagpapakilala ng produkto**: ~120 salitang intro + mga screenshot ng interface na nakapaketeng kasama ng pakete (6 na larawan sa ilalim ng `assets/screenshots/`: mapa page, post detail page, at iba pa, pumili ng 1–3 ayon sa sitwasyon; walang kailangang external image host, gumagana offline).
2. **Agent-assisted na rehistro**: aktibong imumungkahi ng agent ang username/palayaw, password na piliin ang isa (ibibigay ng gumagamit o gagawin ng agent), pagpapadala at pagpasa ng verification code, direct na pag-upload ng avatar (≤5MB, hindi SVG), awtomatikong paghawak ng mga karaniwang error (ginagamit na/expired/rate-limited).
3. **One-click log in (dalawang link)**: sa tagumpay ng rehistro agad na may "half log in" link na diretso sa subscription page; pagkatapos dumating ang bayad, papalitan ang log-in status at bibigyan ng kumpletong membership link na diretso sa home page (dumadaan sa opisyal na `me?token=` bridge ng plataporma, awtomatikong nagtatanim ng HttpOnly cookie).
4. **Subscription payment**: ang Alipay (buwanan ¥6.99 / tatlong buwan ¥19.99 / taunan ¥69.99, one-time na bayad na hindi auto-renew) at PayPal (Premium Monthly, humigit-kumulang $1/buwan, auto-renew, maaaring kanselahin anumang oras) ay parehong hinahawakan ng agent sa paggawa ng order + pagsubaybay sa pagdating ng bayad; para sa mga gumagamit sa ibang bansa, bumabalik sa PayPal; itinuturo ang daan para sa WeChat QR/Huawei IAP.
5. **Pag-troubleshoot ng mga error**: hindi dumating na verification code, may-ari nang username/email, 403 hindi activated, naka-lock na account, at iba pang karaniwang problema — lahat nagmumula sa platform source code na may nakalistang pinagmulan.

## Istruktura ng mga File

```
powpow-register/
├── SKILL.md                            # Pangunahing gabay (trigger conditions, 8-hakbang na daloy, gabay sa tono, hard na mga patakaran)
├── README.md
├── .clawhubignore
├── assets/
│   └── screenshots/                    # Product screenshots na kasama ng pakete (powpow-01~06.jpg)
├── scripts/
│   └── powpow-register.mjs             # Pangunahing script (zero dependency Node>=18, 11 subcommand)
└── references/
    ├── agent-flow.md                   # Script contract, kumpletong sequence, two-link mechanism, security design
    ├── registration-flow.md            # Mga field rule, rate limit, error troubleshooting table (may source citations)
    ├── payment-and-activation.md       # Alipay vibepay contract, activation chain, channel troubleshooting
    └── screenshots.md                  # Listahan ng mga kasamang screenshot + mabilisang sanggunian sa sitwasyon
```

## Seguridad

- **Password** ipinapasa sa script process lang sa pamamagitan ng environment variable; huwag kailanman isulat sa command line argument, sa disk, o sa state file; ang password na ginawa ng agent ay ipinapakita nang isang beses lang para i-save ng gumagamit.
- **Verification code** para lang sa opisyal na registration endpoint, itinatapon pagkatapos gamitin; ang state file (email/username/token/order number) ay nakaimbak sa system temp directory, at sa dulo ng proseso ay isang `cleanup` lang ang nagbubura nito.
- **Bayad**: ang agent ay gumagawa lang ng order, nagbubukas ng cashier, nagtatanong ng pagdating ng bayad; huwag kailanman hahawakan ang Alipay/PayPal account o payment credentials ng gumagamit, huwag kailanman magbabayad para sa kanya. Ang pagbabayad ay palaging nagaganap sa pagitan ng gumagamit at ng opisyal na cashier.
- Lahat ng request ay ipinapadala lang sa opisyal na domain `https://global.powpow.online`; walang kasamang anumang key.

## Lisensya

MIT-0 (pinag-isang lisensya ng ClawHub).

## Mga Link

- Opisyal na website: https://global.powpow.online
- Rehistro: https://global.powpow.online/register
- Kilalanin ang Bula (video): https://www.bilibili.com/video/BV1Wu826UEVz/
