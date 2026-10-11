# Agent-assisted na daloy at script contract — powpow-register

Mga detalye ng pagpapatupad ng bawat hakbang sa SKILL.md. Lahat ng command ay `node scripts/powpow-register.mjs <subcommand> [mga argumento]`; ang script ay **zero dependency**, nangangailangan ng **Node >= 18**, at lahat ng request ay ipinapadala lang sa `https://global.powpow.online`.

## Disenyo ng seguridad (bakit ganito ang disenyo)

| Disenyo | Dahilan |
|---|---|
| Ang password ay ipinapasa lang sa pamamagitan ng environment variable `POWPOW_REGISTER_PASSWORD` | Ang command line arguments ng process ay nakikita ng iba pang process sa parehong makina (argv leak surface); ang environment variable ay binabasa at ginagamit agad sa loob ng script |
| Ang password ay **huwag kailanman isulat sa state file**, huwag lalabas sa mga log | Maaaring manatili sa disk ang state file; sa generate mode sa usapan, isang beses lang ito ipinapakita para i-save ng gumagamit |
| Ang state file ay nakaimbak sa system temp directory (`os.tmpdir()/powpow-register-state.json`, 0600) | Naglalaman lang ito ng limang field: email / username / nickname / token / outTradeNo, binubura nang isang `cleanup` lang |
| Ang JWT na nakuha ng agent ay pinalilitan sa browser cookie sa pamamagitan ng opisyal na `me?token=` endpoint | Opisyal na bridge na dinisenyo para sa HarmonyOS WebView; ang beripikasyon ay nag-beripika lang ng signature + validity period, hindi nakatali sa device fingerprint, kaya magagamit sa browser ng gumagamit |
| Ang bayad ay gumagawa lang ng create-order / query / pagbukas ng cashier | Ang pagbabayad at payment credentials ay palaging nasa pagitan ng gumagamit at ng opisyal na Alipay cashier, hindi dumadaan sa agent |

## Sanggunian ng mga Command

| Command | Mga pangunahing argumento | Gamit / kailan |
|---|---|---|
| `status` | —— | Tingnan ang progreso ng daloy (binabasa ang state file); patakbuhin ito muna pagkatapos maantala ang usapan |
| `gen-password` | —— | Gumawa ng 24-character na malakas na password (may maliliit/malalaking titik + mga numero), ipapakita sa stdout **nang isang beses lang** |
| `prepare-suggest` | `--username --nickname --email` | Itala ang kumpirmadong impormasyon sa state file (pagkatapos, hindi na kailangang ipasa muli sa register) |
| `send-code` | `--email` | Pagsabihan ang plataporma na magpadala ng 6 na numerong verification code (bisa 10 minuto, 60s cooldown) |
| `register` | `--code` (kinakailangan); `--username --nickname --avatar --phone` (opsyonal, hindi na kailangang ipasa kung nasa state file na) | Gumawa ng pending account; ang password ay sa `POWPOW_REGISTER_PASSWORD` environment variable; sa tagumpay, awtomatikong mase-save ang JWT sa state file |
| `login-link` | `--target pending` o `--target home` | Gumawa ng one-click log-in link (two-link design, tingnan sa ibaba) |
| `create-order` | `--package monthly\|quarterly\|yearly` | Gumawa ng Alipay order; nagbabalik ng payment page file path + outTradeNo (awtomatikong naitatala sa state file) |
| `query` | —— | Tingnan ang status ng order na `paid / pending / closed / unknown` (ang outTradeNo ay kinukuha sa state file), mag-poll kada 10–15s |
| `refresh-login` | ang password ay sa environment variable | Mag-log in muli para sa **bagong JWT** (ang subscription claim ay nagiging ACTIVE mula NONE), kailangang patakbuhin pagkatapos dumating ang bayad |
| `whoami` | —— | Gamitin ang token sa state file para tingnan ang status ng account at subscription (beripikahin na gumana ang activation) |
| `cleanup` | —— | Burahin ang state file (kailangang patakbuhin sa dulo) |

**Pagpasa sa pamamagitan ng environment variable** (ang password ay hindi kailanman dumadaan sa command line):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<password>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<password>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<password> && node scripts/powpow-register.mjs register --code 123456
```

## Two-link mechanism (pangunahing disenyo)

Ang log-in status ng plataporma ay HttpOnly cookie, kaya hindi direktang maitatanim ng agent ang cookie sa browser; ang tulay ay ang opisyal na
`/api/auth/me?token=<JWT>&redirect=<path sa loob ng site>` endpoint: beripikasyon ng signature → awtomatikong gagawa ng
session para sa pending user → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 araw) → beripikasyon ng
redirect (dapat magsimula sa isang slash, ipinagbabawal ang `//` at backslash, pagkatapos i-resolve ay dapat same-origin) → 307 temporary redirect sa target page.

- **Link 1 (ibinibigay agad pagkatapos ng matagumpay na rehistro)**: `--target pending` → papunta sa `/subscription`.
  Pumapasok ang browser ng gumagamit sa "half log in" state: ang subscription page at Alipay return page ay nakikita at magagamit; ang mga content page ay pipigilin pa rin at ibabalik sa subscription page (tatlong suson ng proteksyon: JWT claims gateway check → DB recheck → core API check, normal na gawi).
- **Link 2 (ibinibigay pagkatapos makumpirma ang paid)**: patakbuhin muna ang `refresh-login` para sa bagong JWT (ang bayad ay nag-a-update lang sa DB, hindi nagbabago ng claims ng JWT na naibigay na; kapag hindi napalitan, magiging "nagbayad pero walang membership" ang dating), pagkatapos ay `--target home` → papunta sa home page
  na may kumpletong membership state.

## Kumpletong sequence (normal na daan)

```
1.  status                          # Self-check ng kapaligiran
2.  (Hakbang 2: kumpirmahin ang impormasyon sa usapan, password na piliin ang isa; generate mode: gen-password → sabihin agad na i-save ng gumagamit)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → puntahan ng gumagamit ang email para sa code (tanging pag-alis sa usapan ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → ipasa ang Link 1 sa gumagamit
7.  (Pumili ang gumagamit ng package) create-order --package monthly
8.  start <payment page file>       # Windows; sa macOS gumamit ng open, sa Linux gumamit ng xdg-open
    # → magbayad ang gumagamit sa Alipay cashier (pag-alis sa usapan ②)
9.  query (kada 10–15s) hanggang paid
10. refresh-login                   # palitan ng bagong JWT na may ACTIVE claim
11. login-link --target home        # → ipasa ang Link 2 sa gumagamit
12. whoami                          # kumpirmahin ang subscriptionStatus: ACTIVE (opsyonal)
13. cleanup                         # burahin ang state file
```

## Command → platform API mapping

| Command ng script | Platform endpoint |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, direct na pag-upload ng avatar) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (ang link mismo, gumagana kapag na-click sa browser) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Pinagmulan ng mga patakaran: para sa mga field rule at rate limit sa rehistro, tingnan ang `registration-flow.md`; para sa mga package at activation chain, tingnan ang
`payment-and-activation.md` (pareho may nakalistang platform source file).

## Script-level error handling

| Sintomas | Paghawak |
|---|---|
| `Node 版本过低` (masyadong lumang bersyon ng Node) | Bumalik sa pure guidance mode, huwag pilitin |
| Error sa network / timeout | Subukan muli nang isang beses; kung tatagal pa, sabihan ang gumagamit na i-check ang network at magpatuloy (nasaan pa rin ang state file, patakbuhin ang `status` mula simula para ipagpatuloy) |
| Nagbalik ng business error ang register (用户名已存在 at iba pa) | I-handle ayon sa table sa Hakbang 5 ng SKILL.md, **hindi na kailangang ipadala muli ang verification code** (may bisa pa ito sa loob ng 10 minuto) |
| Nagbalik ang register ng `邮箱验证码错误或已过期` (mali o expired na ang email verification code) | Kung nag-expire → muling `send-code` |
| Pagkatapos ng `create-order`, isinara ng gumagamit ang payment page | Muling patakbuhin lang ang `create-order` (awtomatikong magsasara ang lumang order pagkatapos ng 2 oras) |
| `query` ay laging pending | Maaaring hindi pa nagbayad ang gumagamit; magtanong. Kung talagang nagbayad → sundan ang troubleshooting table ng payment-and-activation.md |
| `refresh-login` 403 `pending_payment` | Hindi pa dumarating ang bayad, bumalik sa Hakbang 9 at mag-poll muli |
| Nawala ang state file (nabura nang aksidente / lumipat ng makina) | Hindi na magagamit ang `whoami`/`refresh-login`; sabihan ang gumagamit na i-refresh ang subscription page mismo sa browser kung saan nabuksan ang Link 1 para kumpirmahin ang status, o mag-log in muli (web mode) |

## Fallback mode (pure guidance)

Sa alinmang sumusunod na sitwasyon, agad na bumalik sa v1-style na pure guidance at hindi na mag-eksperimento sa script:

- Walang Node >= 18, o ang script ay nabigo nang dalawang beses magkasunod sa parehong uri;
- Malinaw na sinabi ng gumagamit na "ako mismo ang gagawa sa web page";
- Pinaghihigpitan ng patakaran ng kumpanya/device ang pagkakakonekta ng script sa internet.

Matapos bumalik: ibigay ang registration page https://global.powpow.online/register at subscription page
https://global.powpow.online/subscription , gabayan ang pag-troubleshoot ayon sa mga patakaran sa `registration-flow.md`, hindi nagbabago ang tono, at ang bawat round pa rin ay nagtatapos sa "susunod na hakbang" block.
