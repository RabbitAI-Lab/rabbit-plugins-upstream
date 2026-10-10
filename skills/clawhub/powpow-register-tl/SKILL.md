---
name: powpow-register
description: Sakop ng agent ang pagrehistro ng PowPow (Bula), pag-activate ng subscription sa Alipay, at one-click log in sa loob ng usapan. Ang agent ang nagpupuno ng form (kasama ang pag-upload ng avatar), nagpapadala ng email verification code, gumagawa ng order ng bayad at sinusubaybayan ang pagdating nito; ang gumagamit ay nagbibigay lang ng basic na impormasyon, tumatanggap nang isang beses ng verification code, at nagbabayad sa Alipay cashier nang hindi umaalis sa usapan. Nagti-trigger kapag sinabi ng gumagamit na 'magrehistro ng Bula', 'paano magrehistro ng powpow account', 'gumawa ng powpow account', 'sign up powpow'; pinoproseso rin ang natigil na rehistro (hindi dumating ang verification code, may-ari na ang username/email) at mga problema sa activation (sinasabi sa log in na hindi pa activated ang account / pending_payment, paano mag-subscribe nang bayaran). Nangangailangan ng Node >= 18; kapag hindi available, automatic na bumabalik sa pure guidance mode. Hindi kasama ang pag-post/paglikha ng digital na tao (gawain iyon ng powpow-simple) at hindi rin kasama ang code development.
version: 2.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (katulong sa pagrehistro ng Bula)

Samahan ang bagong gumagamit mula sa "hindi alam kung ano ang Bula" hanggang sa "naka-activate na ang account, one-click log in, maaari nang maglaro" — natatapos ang buong proseso sa loob ng usapan. Dalawang beses lang kailangang pansamantalang iwan ng gumagamit ang usapan: **puntahan ang email para makita ang verification code**, **magbayad sa Alipay cashier** (awtomatikong bubuksan ng agent ang cashier page).

**Bersyon 2.0.1** · 2026-10-08 (mula v2 ay agent-assisted mode: para sa script contract at kumpletong sequence, tingnan ang `references/agent-flow.md`; para sa mga field rule, rate limit, at pag-troubleshoot ng mga error, tingnan ang `references/registration-flow.md`; para sa mga payment channel, tingnan ang `references/payment-and-activation.md`; para sa listahan ng product screenshots, tingnan ang `references/screenshots.md`. Mula v2.0.1, ang mga product screenshot ay nakapaketeng kasama ng skill sa `assets/screenshots/`, hindi na umaasa sa external image host)

## Kapaligiran ng Pagtakbo

- Pangunahing script `scripts/powpow-register.mjs`: **zero dependency**, nangangailangan ng **Node >= 18**. Bago magsimula, patakbuhin nang isang beses ang `node scripts/powpow-register.mjs status` para kumpirmahing gumagana ang kapaligiran.
- Lahat ng request ng script ay ipinapadala lang sa opisyal na domain `https://global.powpow.online`.
- **Kapag walang Node / nag-error ang script**: automatic na bumabalik sa pure guidance mode — ibigay ang registration page https://global.powpow.online/register at subscription page https://global.powpow.online/subscription sa gumagamit, at gabayan nang sunud-sunod ayon sa `references/registration-flow.md`. Huwag paulit-ulit na pilitin ang script.
- Para ipagpatuloy pagkatapos maantala ang usapan: unahin ang `status` para makita kung saang hakbang na ang daloy, tapos ituloy.

## Trigger Conditions

- Intensyon ng pagrehistro: "magrehistro ng Bula", "magrehistro ng powpow account", "paano magrehistro sa Bula", "sign up powpow"
- Nahihirapan sa rehistro: "hindi dumarating ang verification code", "sinasabing may-ari na ang username", "laging hindi tanggap ang password"
- Mga problema pagkatapos ng rehistro: "sinasabi sa log in na hindi pa activated ang account", "403 pending_payment", "paano magbayad/mag-subscribe sa Bula"

**Hindi nagti-trigger**: pag-post/paglikha ng digital na tao (→ powpow-simple); Web-side code development (tingnan ang development skill). Kapag gusto ng gumagamit na magrehistro at mag-post nang sabay: tapusin muna ang skill na ito, at pagkatapos i-activate ay ipasa sa powpow-simple.

## Pangkalahatang-ideya ng Daloy

| Hakbang | Ano ang ginagawa ng agent | Ano ang ginagawa ng gumagamit |
|---|---|---|
| 1 Pagpapakilala ng produkto | Magpaliwanag + magpadala ng screenshots | Tumingin |
| 2 Pagkumpirma ng impormasyon | Aktibong magmungkahi ng username/palayaw, password na piliin ang isa, tanungin ang email | Kumpirmahin, ibigay |
| 3 Pagpapadala ng verification code | `send-code` | —— |
| 4 Pagbabalik ng verification code | —— | Puntahan ang email para sa 6 na numero, balikan at ipasa |
| 5 Pagpasa ng rehistro | `register` (kasama ang direct na pag-upload ng avatar), awtomatikong paghawak ng mga error | —— |
| 6 Half log in + bayad | `login-link(pending)` → `create-order` → buksan ang cashier → paulit-ulit na `query` | I-click ang link, magbayad |
| 7 Opisyal na log in | `refresh-login` → `login-link(home)` | I-click ang link para pumasok sa home page |
| 8 Pagtatapos | `cleanup` + ibigay ang mga kredensyal + gabayan sa karanasan + magmungkahi ng plugins | Magsimulang maglaro |

## Hakbang 1: Pagpapakilala ng produkto + screenshots (hindi maaaring laktawan)

Karamihan sa mga gumagamit ay hindi pa nakakakita ng Bula. Ang unang gawain ay hindi ang pagpapaliwanag ng daloy, kundi pagpapahintulot sa kanya na **makita** ang produkto:

1. Ipakilala ang Bula sa humigit-kumulang 120 salita: ang mga larawang kinuha mo lang nang pasadya ay nagiging isang tala ng paglalakbay, nakapin sa pampublikong mapa bilang isang "bula"; ang mga bula ay nawawalan ng gana sa paglipas ng panahon, at mabubuhay muli kapag may nag-like; sa mapa ay may mga "digital na tao" na puwedeng makipag-usapan. Ang address ng plataporma ay https://global.powpow.online , at kung gusto munang manood ng video: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Magpadala ng screenshots**. Ang mga screenshot ay nakapaketeng kasama ng skill sa `assets/screenshots/powpow-0N.jpg` — ipadala nang direkta bilang lokal na image file, hindi na kailangan ng internet. Para sa listahan, nilalaman ng bawat larawan, at kailan gagamitin, tingnan ang `references/screenshots.md`. Pinakakaraniwang kombinasyon sa simula: mapa page (powpow-03) + post detail page (powpow-06).

Mga patakaran sa screenshots (hard na patakaran):

- Ang mga screenshot ay **nakapaketeng kasama ng skill** sa `assets/screenshots/` (`powpow-0N.jpg`) — magpadala lang ng lokal na image file; gumagana sa anumang kapaligiran, kasama ang mga kapaligirang hindi mabuksan ang GitHub.
- Isang beses lang magpadala ng 1–3 larawan na nauugnay sa kasalukuyang paksa, huwag ipagsabay lahat.
- Kapag aksidenteng nawala ang mga file sa pakete, bumalik sa mga hosted link na nakalista sa `references/screenshots.md` (tandaan: posibleng hindi mabuksan sa mainland China).

Matapos magpakilala, ibigay ang pagpipilian sa gumagamit: **"Kung gusto mong magrehistro, mabubuo natin ang account sa loob ng tatlong minuto dito sa usapan; kailanganin mo lang tingnan nang isang beses ang email verification code."**

## Hakbang 2: Kumpirmahin ang impormasyon ng rehistro (isang tanong kada round, huwag tanungin lahat nang sabay)

- **Username** (kinakailangan): mula sa konteksto ng usapan/system username, **aktibong magmungkahi ng isa** (2–50 na karakter, hindi case-sensitive), kung pumayag ang gumagamit ay gamitin iyon, kung gusto niyang palitan ay palitan.
- **Password** (kinakailangan, tanungin muna ang gumagamit na pumili ng isa):
  - Kung ibibigay mismo ng gumagamit → ipasa sa script sa pamamagitan ng environment variable, **huwag kailanman isulat sa command line argument**;
  - Kung gagawa ang agent → patakbuhin ang `node scripts/powpow-register.mjs gen-password`, at **agad na ipasa ang ginawang password sa gumagamit para i-save** (ipapakita lang nang isang beses, hindi na lalabas muli).
- **Email** (kinakailangan): dapat ibigay mismo ng gumagamit — ito ang identity anchor ng account, **huwag hulaan para sa gumagamit**.
- **Palayaw** (opsyonal): imungkahi bilang default na kapareho ng username.
- **Avatar** (opsyonal): kung magbibigay ang gumagamit ng lokal na image path (≤5MB, hindi SVG), ida-direct upload ng script; kung wala, laktawan (gagamit ang plataporma ng default logo); kung may kakayahan ka sa image generation, maaari kang aktibong mag-alok na gumawa ng isa para sa gumagamit.
- **Mobile number** (opsyonal, mainland number): default na laktawan, hingin lang kung gusto mismo ng gumagamit mag-bind.

Matapos makumpirma, puwedeng patakbuhin ang `prepare-suggest --username U --nickname N --email E` para itala sa state file (pagkatapos, hindi na kailangang ipasa muli sa register).

## Hakbang 3–4: Email verification code (tanging bahagi na kailangang lumabas ng usapan)

```
node scripts/powpow-register.mjs send-code --email <email>
```

Pagkatapos, sabihin nang malinaw sa gumagamit: **puntahan ang email para hanapin ang 6 na numerong verification code, may bisa sa loob ng 10 minuto, at tandaang tingnan ang spam/promotions folder**, kapag nakuha na ay bumalik at ipasa ang code. May 60-segundong cooldown ang pagpapadala, huwag pindutin nang paulit-ulit.

## Hakbang 5: Ipasa ang rehistro (ginagawa ng agent)

```
POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs register --code <verification code> [--username U] [--nickname N] [--avatar <lokal na image path>] [--phone P]
```

Kapag matagumpay, nabubuo ang account (pending status, may kasamang 3 initial badge). Awtomatikong hinihawak ang mga karaniwang error nang hindi inaabala ang gumagamit:

| Error | Paghawak |
|---|---|
| 用户名已存在 (may-ari na ang username) | Awtomatikong magmungkahi ng variant (username + numero), pagkatapos kumpirmahin ng gumagamit ay subukan muli nang direkta (may bisa pa ang verification code, hindi na kailangang ipadala muli) |
| 邮箱已被使用 (gamit na ang email) | Tanungin ang gumagamit: palitan ang email, o baka may account na pala siya (lumipat sa log in / password recovery) |
| 邮箱验证码错误或已过期 (mali o expired na ang email verification code) | Kapag lumampas ng 10 minuto → muling `send-code` |
| 发送/注册过于频繁（429） (sobrang dalas ng pagpapadala/pagrehistro (429)) | Maghintay ng 1 minuto bago subukan muli, sabihin lang sa gumagamit |

## Hakbang 6: One-click log in (Link 1) + bayad

1. Pagkatapos maging matagumpay ang rehistro, agad na:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Ipadala ang link sa gumagamit: **kapag na-click, diretso ang browser sa subscription page at naka-log in na ang status** — sa gayon, kapag natapos ang bayad, tama ang ipapakita ng return page na 「支付成功」 (matagumpay na bayad). (Sa status na ito, ang content page ay pipigilin pa rin at ideredeblekta sa subscription page — ito ay normal na paggana ng platform paywall, hindi bug, at hindi na kailangang ipaliwanag sa gumagamit ang panloob na mekanismo.)
2. Piliin ang isa sa tatlong package, ipakita kasama ang presyo:
   - Buwanan **¥6.99** (imungkahing subukan muna) / Tatlong-buwan **¥19.99** / Taunang **¥69.99** — isang beses na bayad sa Alipay para sa kaukulang tagal, **hindi auto-renew**
3. Matapos piliin ng gumagamit:
   ```
   node scripts/powpow-register.mjs create-order --package monthly
   ```
   Nagbabalik ang script ng file path ng payment page, **buksan nang direkta gamit ang system command** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Awtomatikong dadako ang browser sa opisyal na Alipay cashier, kung saan magre-scan ang gumagamit ng QR code o mag-log in sa Alipay para magbayad.
4. Patakbuhin ang `query` kada 10–15 segundo hanggang magbalik ng `paid` (karaniwang ilang segundo hanggang isang minuto ang pagdating ng bayad). Kung isinara ng gumagamit ang payment page sa gitna → muling patakbuhin lang ang `create-order` (awtomatikong magsasara ang lumang order pagkatapos ng 2 oras, huwag intindihin).
5. Para sa mga gumagamit sa ibang bansa/walang Alipay: gabayan silang gamitin ang PayPal channel sa subscription page (hindi ito ina-asikaso ng skill, ituro lang ang daan); ang WeChat QR channel ay may manual na kumpirmasyon at maaaring ma-delay ang pagdating ng bayad. Pagkatapos magbayad, magpatuloy pa rin sa Hakbang 7.

## Hakbang 7: Opisyal na log in (Link 2)

Matapos makumpirma ang pagdating ng bayad, palitan muna ang log-in status ng pinakabagong subscription claim, pagkatapos ay gawin ang link na diretso sa home page:

```
POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Ipadala ang link sa gumagamit: **kapag na-click, diretso sa home page na may kumpletong membership status**, sa puntong ito natapos na ang buong proseso ng rehistro.

## Hakbang 8: Pagtatapos

1. `node scripts/powpow-register.mjs cleanup` para linisin ang pansamantalang state file ng makinang ito (mga session credential).
2. Ibigay sa gumagamit ang "account card": username, email, petsa ng pag-expire ng membership (hindi na ipapakita muli ang password — sa generate mode, pinasabi nang i-save ng gumagamit noong ginawa ito; kung sarili niyang itinakda, alam niya iyon).
3. Gabayan sa karanasan: mag-ikot sa mapa, magpost ng unang tala ng paglalakbay (→ ipasa sa powpow-simple).
4. Magmungkahi ng mga extension: ang `@durenzidu/powpow-integration` skill at ang `@durenzidu/openclaw-channel-powpow` plugin — para iugnay ang Bula sa agent mismo ng gumagamit; kung gusto niya, bigyan ng install command.
5. Wakasan gamit ang "susunod na hakbang" block.

## Conversation UX

Manatili sa pamilyar na service tone ng PowPow:

- **Ang gumagamit ang paksa ng pangungusap**, mas mainam ang "Puwede kang..." kaysa sa "Kailangan mong..."; huwag mangaral, huwag mamatas.
- **Isang desisyon lang ang isulong kada round**; magbigay muna ng dahilan bago humingi ng impormasyon.
- **Ang dulo ng bawat sagot** ay isang nakatakdang "susunod na hakbang" block (separator + 👉 + iisang aksyon + isang pangungusap na "kapag natapos mo, gagawin ko ang..."), halimbawa:
  ```
  ────────────────────
  👉 Ang kailangan mong gawin ngayon: puntahan ang email, hanapin ang 6 na numerong verification code, ipasa nang direkta sa akin
     (sa oras na matanggap ko, agad kong bubuuin ang account)
  ```
- **Huwag kusang mag-lecture tungkol sa seguridad ng password**; huwag ipaliwanag ang panloob na mekanismo, rate limit, o security design maliban kung itanong ng gumagamit.
- Lalo nang iulat ang progreso habang ginagawa ng agent ang lahat: pagkatapos ng bawat script step, sabihin sa gumagamit sa isang pangungusap kung ano ang nangyari ("nabuo na ang account", "nabuksan na para sa iyo ang payment page").

## Mga Hard na Patakaran

- **Seguridad ng kredensyal**: ang password ay ipinapasa sa script lang sa pamamagitan ng environment variable `POWPOW_REGISTER_PASSWORD`, **huwag kailanman** isulat sa command line argument (nakikita ito sa process list), huwag isulat sa anumang file (sa generate mode, ipinapakita nang isang beses para i-save ng gumagamit, pagkatapos ay hindi na uulitin). Ang verification code ay para lang sa opisyal na registration endpoint, itinatapon pagkatapos gamitin.
- **Opisyal na hangganan**: lahat ng request ay ipinapadala lang sa `https://global.powpow.online` (naka-embed na ito sa script), huwag kailanman ipapadala ang impormasyon ng gumagamit sa kahit anong third-party na address.
- **Hangganan ng bayad**: ang agent ay gumagawa lang ng order, nagbubukas ng cashier, nagtatanong ng pagdating ng bayad; **huwag kailanman** hawakan ang Alipay account/payment credentials ng gumagamit, at huwag kailanman mangako ng "pagbabayad para sa kanya".
- **Ang paywall ay hindi bug**: sa pending status, ang pag-access sa subscription page/return page ay sadyang pinapayagan; ang paghaharang sa content page ay normal na paggana ng platform paywall, huwag tangkang lumusot dito.
- **Kalayaang bumalik sa manual**: kung sa anumang hakbang gustong gawin mismo ng gumagamit, o hindi sinusuportahan ng kapaligiran ang script, anumang oras ay maaaring bumalik sa pure guidance mode — bigyan ng link, ipaliwanag ang mga patakaran, samahan sa pag-troubleshoot.
- Huwag gumawa ng mga patakaran ng plataporma: lahat ng field rule, error text, at rate limit parameter ay nagmumula sa platform code (may mga source citation sa `references/registration-flow.md`); kapag nag-update ang plataporma, ang aktwal na gawi online ang masusunod.
- Para sa mga ipinapakitang larawan, gamitin lang ang mga screenshot sa `assets/screenshots/` sa pakete (tingnan ang `references/screenshots.md` para sa gamit ng bawat larawan).
- Wakasan ang bawat round gamit ang "susunod na hakbang" block, para laging alam ng gumagamit ang kanyang susunod na gagawin.
