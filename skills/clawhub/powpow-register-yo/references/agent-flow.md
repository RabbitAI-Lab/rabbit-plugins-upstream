# Ṣiṣan agent-oluranlọwọ ati adehun iwe — powpow-register

Awọn alaye ṣiṣe ti awọn ipe SKILL.md. Gbogbo awọn aṣẹ jẹ `node scripts/powpow-register.mjs <subcommand> [awọn ariyanjiyan]`, iwe naa **laisi awọn igbẹkẹle**, nilo **Node >= 18**, gbogbo awọn ibeere n lọ si `https://global.powpow.online` nikan.

## Apẹrẹ aabo (ki a fi le ṣe bẹ)

| Apẹrẹ | Idi |
|---|---|
| Ọrọ igbaniwọle n lọ nipasẹ oniyipada ayika `POWPOW_REGISTER_PASSWORD` nikan | Awọn ariyanjiyan aṣẹ aṣẹ han si awọn ilana miiran lori ẹrọ kanna (ipa ṣiṣafihan argv), oniyipada ayika a ka ninu iwe ki o lo lẹṣẹkan |
| Ọrọ igbaniwọle **ko kọ sinu faili ipo rara**, ko han ninu akọọlẹ | Faili ipo le duro lori disk; ipo ipilẹṣẹ ninu ibaraẹnisọrọ fihan lẹẹkan nikan ki olumulo to tọju |
| Faili ipo wa ninu folda igba-die eto (`os.tmpdir()/powpow-register-state.json`, 0600) | O ni awọn aaye marun nikan `email / username / nickname / token / outTradeNo`, `cleanup` nu laifọwọyi |
| JWT ti agent gba n lọ nipasẹ aaye osise `me?token=` ṣe cookie aṣawakiri | Afara osise ti a ṣe apẹrẹ fun Harmony WebView; ayẹwo ibuwọn ṣayẹwo ibuwọn + akoko nikan, ko so mọ ika ẹrọ, aṣawakiri olumulo le lo |
| Isanwo n ṣe create-order / query / ṣiṣi alagbata nikan | Iṣe isanwo ati ẹri isanwo nigbagbogbo wa laarin olumulo ati alagbata Alipay osise, agent ko ṣe afọwọṣe |

## Itọkasi aṣẹ

| Aṣẹ | Awọn ariyanjiyan bọtini | Iṣe / akoko |
|---|---|---|
| `status` | —— | Wo ilọsiwaju ilana (ka faili ipo); lẹhin ti ibaraẹnisọrọ ti ge kọkọ ṣiṣẹ eyi |
| `gen-password` | —— | Ṣe ipilẹṣẹ ọrọ igbaniwọle to lagbara oni-nọmba 24 (pẹlu nla-kekere + nọmba), stdout fihan **lẹẹkan nikan** |
| `prepare-suggest` | `--username --nickname --email` | Kọ alaye ti a ti damiloju sinu faili ipo (lẹhinna register ko nilu tun ranṣẹ) |
| `send-code` | `--email` | Nṣe okunfa pẹpẹ lati fi nọmba oni-nọmba 6 ranṣẹ (wulo fun iṣẹju 10, ihamọ iṣẹju 60) |
| `register` | `--code` (dandan); `--username --nickname --avatar --phone` (iyanjiyan, ti faili ipo ba ni ko nilo tun ranṣẹ) | Ṣẹda akọọlẹ pending; ọrọ igbaniwọle nipasẹ oniyipada ayika `POWPOW_REGISTER_PASSWORD`; lẹhin aṣeyọri JWT fi sinu faili ipo laifọwọyi |
| `login-link` | `--target pending` tabi `--target home` | Ṣe ipilẹṣẹ ọna asopọ wiwọle ọkan-tẹ (ero ọna asopọ meji, wo isalẹ) |
| `create-order` | `--package monthly\|quarterly\|yearly` | Ṣẹda aṣẹ Alipay; da ọna faili oju-iwe isanwo pada + outTradeNo (fi sinu faili ipo laifọwọyi) |
| `query` | —— | Ṣe ibeere ipo aṣẹ `paid / pending / closed / unknown` (outTradeNo lati faili ipo), ṣe ibeere ni iṣẹju 10–15 |
| `refresh-login` | Ọrọ igbaniwọle nipasẹ oniyipada ayika | Tun wọle lati ṣe paṣipaarọ JWT tuntun (ikede ṣiṣe alaisanfarasin lati NONE di ACTIVE), ṣiṣe lẹhin isanwo de |
| `whoami` | —— | Lo token ninu faili ipo lati ṣe ibeere akọọlẹ ati ipo ṣiṣe alaisanfarasin (jẹrisi boya imuyipada ti ṣiṣẹ) |
| `cleanup` | —— | Nu faili ipo kuro (ṣiṣe ni ipari) |

**Gbigbe oniyipada ayika** (ọrọ igbaniwọle ko gun aṣẹ rara):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<ọrọigbaniwọle>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<ọrọigbaniwọle>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<ọrọigbaniwọle> && node scripts/powpow-register.mjs register --code 123456
```

## Ero ọna asopọ meji (apẹrẹ pataki)

Ipo wiwọle pẹpẹ jẹ cookie HttpOnly, agent ko le fi cookie fun aṣawakiri taara; afara naa jẹ aaye osise
`/api/auth/me?token=<JWT>&redirect=<ipari aaye inu>` : ayẹwo ibuwọn → olumulo pending ni a ṣe igbese session → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / ọjọ 7) → ṣayẹwo
redirect (bẹrẹ pẹlu slash kan nikan, fi `//` ati slash-pada le, lẹhin itupalẹ gbọdọ jẹ ibugbe kanna) → atunṣe 307 si oju-iwe ibi-afẹde.

- **Ọna asopọ 1 (fun olumulo lẹṣẹkan lẹhin iforukosile)** : `--target pending` → de `/subscription`.
  Aṣawakiri olumulo wọ ipo "idaji-wiwọle": oju-iwe ṣiṣe alaisanfarasin, oju-iwe ipadabọ Alipay han ati ṣiṣẹ; awọn oju-iwe akoonu tun di didena si oju-iwe ṣiṣe alaisanfarasin (aabo awọn ipe mẹta: ayẹwo ẹnu-bode JWT → atunwo DB → ayẹwo API pataki, ihuwasi deede).
- **Ọna asopọ 2 (fun lẹhin imudaniloju paid)** : kọkọ `refresh-login` ṣe paṣipaarọ JWT tuntun (isanwo n ṣe imudojuiwọn DB nikan, ko yi awọn ikede JWT ti a ti fowo si, ti ko ba ṣe paṣipaarọ yoo farahan bi "isanwo laisi ọmọ ẹgbẹ"), lẹhinna `--target home` → de oju-iwe ile, ipo ọmọ ẹgbẹ pipe.

## Ṣiṣan akoko pipe (ọna deede)

```
1.  status                          # Ayẹwo ayika
2.  (Ipe 2 ibaraẹnisọrọ damiloju alaye, yan ọrọ igbaniwọle; ipo ipilẹṣẹ: gen-password → jẹ ki olumulo tọju lẹṣẹkan)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → olumulo lọ si imeeli wo koodu (ipin kan ṣoṣo ti o jade kuro ninu ibaraẹnisọrọ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → ọna asopọ 1 ranṣẹ si olumulo
7.  (olumulo yan ẹgbẹ) create-order --package monthly
8.  start <faili oju-iwe isanwo>              # Windows; macOS lo open, Linux lo xdg-open
    # → olumulo sanwo ni alagbata Alipay (ipin ti o jade kuro ninu ibaraẹnisọrọ②)
9.  query (ni iṣẹmu 10–15) titi yoo fi paid
10. refresh-login                   # Ṣe paṣipaarọ JWT tuntun oni ACTIVE
11. login-link --target home        # → ọna asopọ 2 ranṣẹ si olumulo
12. whoami                          # Jẹrisi subscriptionStatus: ACTIVE (iyanjiyan)
13. cleanup                         # Nu faili ipo
```

## Maapu aṣẹ → API pẹpẹ

| Aṣẹ iwe | Aaye pẹpẹ |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, ikojade aworan taara) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (ọna asopọ funrarẹ, ni imuṣẹ nigbati a ba tẹ) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Orisun ofin: awọn aaye iforukosile ati ihamọ wo `registration-flow.md`; awọn ẹgbẹ ati ṣiṣan imuyipada wo
`payment-and-activation.md` (awọn mejeeji ni orisun koodu pẹpẹ).

## Ṣiṣayẹwo aṣiṣe ipe iwe

| Iṣẹlẹ | Ṣetọju |
|---|---|
| `Node ẹ̀dà rẹ̀ kẹ́gàn` (Node version too low) | Pada si ipo itọsọna lasan, maṣe gbiyanju ni agbara |
| Aṣiṣe nẹtiwọọki / akoko tu | Tun gbiyanju lẹẹkan; ti ko ba ṣaṣeyọri jẹ ki olumulo ṣayẹwo nẹtiwọọki ki o tẹsiwaju (faili ipo tun wa, tun ṣiṣẹ `status` lati bọsipọ) |
| register n ṣafihan aṣiṣe iṣowo (oruko olumulo ti wa tẹlẹ, ati bẹbẹ) | Ṣetọju gẹgẹbi tabili Ipe 5 SKILL.md, **maṣe tun ranṣẹ koodu ijẹrisi** (wulo laarin iṣẹju 10) |
| register n ṣafihan "邮箱验证码错误或已过期" | Ti o ba kọja akoko → tun `send-code` |
| Lẹhin `create-order` olumulo ti pa oju-iwe isanwo | Tun ṣiṣẹ `create-order` taara (aṣẹ atijọ laipẹ pa laifọwọyi ni wakati 2) |
| `query` wa pending nigbagbogbo | Olumulo le ma sanwo; beere ọrọ kan. Ti o ba sanwo gangan → tẹle tabili ṣiṣayẹwo `payment-and-activation.md` |
| `refresh-login` 403 `pending_payment` | Isanwo ko tii de, pada si Ipe 9 tẹsiwaju ibeere |
| Faili ipo sọnù (aṣiṣe nu / pa ẹrọ) | `whoami`/`refresh-login` ko le lo; jẹ ki olumulo ṣe awọn atunto ninu aṣawakiri nibiti o ti ṣii ọna asopọ 1 lati ṣayẹwo ipo, tabi tun wọle (ipo oju-iwe) |

## Ipo ipadabọ (itọsọna lasan)

Eyikeyi ninu awọn ipo wọnyi pada lẹṣẹkan si ipo itọsọna lasan v1, maṣe tun yan iwe:

- Ko si Node >= 18 tabi iwe naa kuna iru aṣiṣe meji ni itẹlera;
- Olumulo sọ ni gbangba "ema ṣe lori oju-iwe funrarẹ";
- Ilana ile/ẹrọ fi iwe de idiwọ nẹtiwọọki.

Lẹhin ipadabọ: fun oju-iwe iforukosile https://global.powpow.online/register ati oju-iwe ṣiṣe alaisanfarasin
https://global.powpow.online/subscription , tẹle awọn ofin `registration-flow.md` lati ṣe ibaṣepọ ṣiṣayẹwo aṣiṣe,
ohun orin ko yipada, iyipo kọọkan tun pari pẹlu apa "igbesẹ ti nbọ".
