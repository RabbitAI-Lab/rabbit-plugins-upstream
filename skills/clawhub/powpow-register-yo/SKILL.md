---
name: powpow-register
description: Ran olumulo lati pari iforukosile PowPow (Bubble), imuyipada ṣiṣẹ ti Alipay/PayPal ati wiwọle ọkan-tẹ ninu ibaraẹnisọrọ. Agent ṣe fọọmu (pẹlu ikojade aworan profaili), firanṣẹ koodu ijẹrisi imeeli, ṣẹda aṣẹ isanwo ati tọpa isanwo dide; olumulo nilo lati pese alaye ipilẹ, gba koodu ijẹrisi lẹẹkan, sanwo ni alagbata Alipay/PayPal, laisi jijade ninu ibaraẹnisọrọ. A ṣe iṣẹ nigbati olumulo sọ 'foruko Bubble', 'foruko akọọlẹ powpow', 'bawo ni a ṣe foruko powpow', 'sign up powpow'. A tun ṣetọju awọn iṣoro iforukosile (gbigba koodu ijẹrisi, oruko olumulo/imeeli ti a ti lo) ati awọn ọran imuyipada (wiwọle nfihan 'akọọlẹ ko tii mu ṣiṣẹ' / pending_payment, bawo ni a ṣe sanwo). O nilo Node >= 18; ti ko ba si ni adaṣe pada si ipo itọsọna lasan. Ko ni gbigbe ifiweranṣẹ/ẹda eniyan oni-nọmba (iyẹn jẹ iṣẹ powpow-simple), ko si idagbasoke koodu.
version: 2.1.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (oluranlọwọ iforukosile Bubble)

Mu olumulo tuntun lati "ko mọ ohun ti Bubble jẹ" de "akọọlẹ ti mu ṣiṣẹ, wiwọle ọkan-tẹ, bẹrẹ ere" — gbogbo ilana naa waye ninu ibaraẹnisọrọ. Olumulo ni akoko meji nikan lati jade ninu ibaraẹnisọrọ fun igba diẹ: **lọ si imeeli wo nọmba ijẹrisi**, **sanwo ni alagbata isanwo** (Alipay tabi PayPal — agent yoo ṣii oju-iwe alagbata naa laifọwọyi).

**Ẹ̀dà 2.1.0** · 2026-10-11 (lati v2 jẹ ipo agent-oluranlọwọ: adehun iwe ati ṣiṣan akoko ni kikun wo `references/agent-flow.md`; awọn ofin aaye, ihamọ, ati ṣiṣayẹwo aṣiṣe wo `references/registration-flow.md`; ọna isanwo wo `references/payment-and-activation.md`; atokọ awọn aworan ọja wo `references/screenshots.md`. Lati v2.1.0 ṣiṣe alaisanfarasin PayPal tun le ṣe itọsọna nipasẹ agent, gẹgẹ bi yiyan lẹgbẹẹ Alipay)

## Agbegbe ṣiṣe

- Iwe pataki `scripts/powpow-register.mjs`: **laisi awọn igbẹkẹle**, o nilo **Node >= 18**. Ṣaaju ki o to bẹrẹ, ṣiṣẹ lẹẹkan `node scripts/powpow-register.mjs status` lati ni idaniloju agbegbe ṣiṣe.
- Gbogbo awọn ibeere iwe n lọ si ibugbe osise nikan `https://global.powpow.online`.
- **Ti ko si Node / iwe naa nfihan aṣiṣe**: pada laifọwọyi si ipo itọsọna lasan — fun olumulo oju-iwe iforukosile https://global.powpow.online/register ati oju-iwe ṣiṣe alaisanfarasin https://global.powpow.online/subscription, ṣe itọsọna ni ibamu si `references/registration-flow.md`. Maṣe gbiyanju iwe naa ni agbara leralera.
- Ipadabọ lẹhin ti ibaraẹnisọrọ naa ti ge: kọkọ `status` lati wo iru ipe ti ilana naa ti de, lẹhinna tẹsiwaju.

## Trigger Conditions

- Ète iforukosile: "foruko Bubble", "foruko akọọlẹ powpow kan", "bawo ni a ṣe foruko powpow", "sign up powpow"
- Iforukosile ti di duro: "gbigba nọmba ijẹrisi imeeli", "oruko olumulo ni a sọ pe o ti wa tẹlẹ", "ọrọ igbaniwọle ko dara nigbagbogbo"
- Awọn ọran lẹhin iforukosile: "wiwọle nfihan akọọlẹ ko tii mu ṣiṣẹ", "403 pending_payment", "bawo ni a ṣe sanwo/fowole PowPow"

**Ko ṣe nkan**: gbigbe ifiweranṣẹ/ẹda eniyan oni-nọmba (→ powpow-simple); idagbasoke koodu oju opo wẹẹbu (wo skill idagbasoke). Nigbati olumulo ba fẹ iforukosile ati tun fẹ gbe ifiweranṣẹ: kọkọ pari skill yii, lẹhin imuyipada fi si ọwọ powpow-simple.

## Akopọ ṣiṣan

| Ipe | Ohun ti agent ṣe | Ohun ti olumulo ṣe |
|---|---|---|
| 1 Ifihan ọja | Ṣalaye + firanṣẹ aworan | Wo |
| 2 Imudaniloju alaye | Dabanọ oruko olumulo/oruko ọrẹ, yan ọrọ igbaniwọle, beere imeeli | Imudaniloju, pese |
| 3 Firanṣẹ koodu ijẹrisi | `send-code` | —— |
| 4 Ka nọmba ijẹrisi | —— | Lọ si imeeli wo nọmba oni-nọmba 6, pada fi ranṣẹ |
| 5 Fi iforukosile silẹ | `register` (pẹlu ikojade aworan profaili taara), ṣetọju aṣiṣe laifọwọyi | —— |
| 6 Idaji-wiwọle + isanwo | `login-link(pending)` → `create-order --provider alipay|paypal` → ṣii alagbata → ṣe ibeere `query` | Tẹ ọna asopọ, sanwo |
| 7 Wiwọle deede | `refresh-login` → `login-link(home)` | Tẹ ọna asopọ wọ oju-iwe ile |
| 8 Ipari | `cleanup` + fi iwe-ẹri fun + ṣe itọsọna iriri + daba afikun | Bẹrẹ ere |

## Ipe 1: Ifihan ọja + aworan (maṣe fo)

Ọpọlọpọ awọn olumulo ko tii ri Bubble rara. Ohun akọkọ kii ṣe alaye ilana, ṣugbọn jẹ ki wọn **ri** ọja naa:

1. Lo ọrọ bii 120 lati ṣalaye Bubble: awọn aworan ti o ya ni irọrun yipada si irin-ajo irin-ajo, wọn fi si maapu gbangba bi "bebula" kan; bebula naa n rẹwẹsi pẹlu akoko, awọn miiran ti o ba fẹran a o sọji; lori maapu tun wa awọn "eniyan oni-nọmba" ti o le ba sọrọ. Adirẹsi pẹpẹ https://global.powpow.online, ti o ba fẹ wo fidio kọkọ: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Firanṣẹ aworan**. Awọn aworan ti dahun pọ pẹlu skill ninu `assets/screenshots/powpow-0N.jpg` — fi ranṣẹ taara bi faili aworan agbegbe, ko nilo nẹtiwọọki. Atokọ, ohun ti o wa ninu aworan kọọkan ati igba lati lo wọn wo `references/screenshots.md`. Apapọ ti a lo julọ ni ibẹrẹ: oju-iwe maapu (powpow-03) + oju-iwe alaye ifiweranṣẹ (powpow-06).

Awọn ofin aworan (ofin lile):

- Aworan **ti dahun pọ pẹlu skill** ninu `assets/screenshots/` (`powpow-0N.jpg`) — fi ranṣẹ faili aworan agbegbe nikan; o ṣiṣẹ ni gbogbo agbegbe, pẹlu awọn agbegbe nibiti GitHub ko ṣii.
- Firanṣẹ awọn aworan 1–3 ti o jọmọ koko-ọrọ lọwọlọwọ nikan ni igba kan, maṣe fi gbogbo wọn ranṣẹ ni ẹẹkan.
- Ti awọn faili inu ba padanu lairotẹlẹ, pada si awọn ọna asopọ ibi ipamọ ti a ṣe akojọ ninu `references/screenshots.md` (akiyesi: o le ma ṣii ni Ilu China).

Lẹhin alaye, fi yiyan fun olumulo: **"Ti o ba fẹ foruko, a o kọ akọọlẹ sinu ibaraẹnisọrọ ni iṣẹju mẹta, o nilo nikan lati wo nọmba ijẹrisi imeeli lẹẹkan."**

## Ipe 2: Imudaniloju alaye iforukosile (beere ibeere kan fun ipe kan, maṣe beere gbogbo wọn ni ẹẹkan)

- **Oruko olumulo** (dandan): lati agbegbe ibaraẹnisọrọ/oruko olumulo eto **daba ọkan** (awọn ohun kikọ 2~50, laibikita nla-kekere), ti olumulo ba fọwọsi lo, ti o ba fẹ yi padà yipada.
- **Ọrọ igbaniwọle** (dandan, kọkọ beere olumulo yan ọkan):
  - Olumulo funra rẹ pese → lẹhinna fi via oniyipada ayika si iwe, **maṣe kọ sinu awọn ariyanjiyan aṣẹ rara**;
  - agent ṣe ipilẹṣẹ → ṣiṣẹ `node scripts/powpow-register.mjs gen-password`, fi ọrọ igbaniwọle ti a ṣipilẹṣẹ **ranṣẹ si olumulo lẹẹkan ki o tọju** (a fi han lẹẹkan nikan, ko tun farahan lẹhinna).
- **Imeeli** (dandan): olumulo gbọdọ pese — eyi ni oran idanimọ ti akọọlẹ, **maṣe gboju boya fun olumulo**.
- **Oruko ọrẹ** (iyanjiyan): daba aiyipada kanna bi oruko olumulo.
- **Aworan profaili** (iyanjiyan): olumulo fun ọna faili aworan agbegbe kan (<=5MB, kii ṣe SVG) jẹ ki iwe gbe taara; ti ko ba si fo (pẹpẹ lo aami aiyipada); ti o ba ni agbara ṣiṣẹda aworan, o le daba lati ran olumulo lọwọ ṣe ọkan.
- **Nọmba foonu** (iyanjiyan, nọmba oluile): aiyipada fo, ti olumulo ba fẹ dipọ beere.

Lẹhin imudaniloju o le ṣiṣẹ `prepare-suggest --username U --nickname N --email E` lati kọ si faili ipo (lẹhinna register ko nilo tun ranṣẹ).

## Ipe 3–4: Nọmba ijẹrisi imeeli (ipin kan ṣoṣo ti o nilo jade kuro ninu ibaraẹnisọrọ)

```
node scripts/powpow-register.mjs send-code --email <imeeli>
```

Lẹhinna sọ fun olumulo ni gbangba: **lọ si imeeli wa nọmba oni-nọmba 6, wulo fun iṣẹju 10, ranti wo folda idọti/ifilọle**, ti o ba ri pada fi ranṣẹ. Firanṣẹ ni ihamọ iṣẹju 60, maṣe tẹ leralera.

## Ipe 5: Fi iforukosile silẹ (agent n ṣe iranlọwọ)

```
POWPOW_REGISTER_PASSWORD=<ọrọigbaniwọle> node scripts/powpow-register.mjs register --code <nọmba ijẹrisi> [--username U] [--nickname N] [--avatar <ọna faili aworan agbegbe>] [--phone P]
```

Aṣeyọri ṣẹda akọọlẹ (ipo pending, pẹlu baaji 3 ibẹrẹ). Awọn aṣiṣe ti o wọpọ ni a ṣetọju laifọwọyi, laisi idilọwọ olumulo:

| Aṣiṣe | Ṣetọju |
|---|---|
| 用户名已存在 (oruko olumulo ti wa tẹlẹ) | Daba iyatọ laifọwọyi (oruko olumulo + nọmba), olumulo fọwọsi lẹhinna tun gbiyanju taara (koodu ijẹrisi tun wulo, ko nilo atunfiranṣẹ) |
| 邮箱已被使用 (imeeli ti a ti lo) | Beere olumulo: paṣẹ imeeli miiran, tabi boya o ti ni akọọlẹ (yi lọ si wiwọle/iranti ọrọ igbaniwọle) |
| 邮箱验证码错误或已过期 (koodu ijẹrisi imeeli jẹ aṣiṣe tabi ti di ofo) | Ti o ba kọja iṣẹju 10 → tun `send-code` |
| 发送/注册过于频繁（429） (firanṣẹ/iforukosile pupọ ju (429)) | Duro iṣẹju 1 lẹhinna tun gbiyanju, sọ fun olumulo nikan |

## Ipe 6: Wiwọle ọkan-tẹ (ọna asopọ 1) + isanwo

1. Lẹhin iforukosile aṣeyọri lẹṣẹkan:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Firanṣẹ ọna asopọ si olumulo: **lẹhin tite, aṣawakiri rẹ de oju-iwe ṣiṣe alaisanfarasin taara, ti wa ni ipo ti a ti wọle** — lẹhinna nigbati isanwo ba pari oju-iwe ipadabọ le ṣafihan 'isanwo aṣeyọri' deede. (Ninu ipo yii awọn oju-iwe akoonu tun di didena si oju-iwe ṣiṣe alaisanfarasin, eyi jẹ iṣẹ deede ti odi isanwo pẹpẹ, kii ṣe bug, maṣe ṣalaye ero inu fun olumulo.)
2. **Jẹ ki olumulo yan ọna isanwo**, ṣafihan awọn ọna meji:
   - **Alipay (Ilu China / olumulo ti o ni Alipay)**: rira-lẹẹkan fun akoko deede, **ko ṣe isọdọtun laifọwọyi**
     - Oṣu **¥6.99** (daba lati gbiyanju kọkọ) / mẹẹdogun **¥19.99** / ọdun **¥69.99**
   - **PayPal (okeere / olumulo laisi Alipay)**: isọdọtun oṣu laifọwọyi, a le fagilee nigbakugba
     - Premium Monthly, bii **$1/oṣu** (gẹgẹbi oju-iwe ṣiṣe alaisanfarasin ṣe fihan, isọdọtun laifọwọyi)
3. Nigbati olumulo ba yan:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Iwe naa da ọna faili oju-iwe isanwo pada, **ṣii taara pẹlu aṣẹ eto** (Windows: `start <faili>`; macOS: `open <faili>`; Linux: `xdg-open <faili>`). Aṣawakiri yoo lọ taara si alagbata Alipay/PayPal osise, olumulo ṣe isanwo tabi fowo si aṣẹ.
4. Ṣiṣẹ `query` ni iṣẹmu 10–15 kọọkan titi yoo fi da `paid` tabi `ACTIVE` pada (owo/ifọwọsi deede laarin iṣẹmu diẹ si iṣẹmu kan). Ti olumulo ba ti pa oju-iwe isanwo ni aarin → tun ṣiṣẹ `create-order` taara (aṣẹ atijọ / ṣiṣe alaisanfarasin PENDING ti pa laifọwọyi lẹhin wakati 2, maṣe yọnu).
5. Ọna iwo-koodu WeChat jẹ timo-ọkọnrin, isanwo n ṣe idaduro; Huawei IAP wa nikan ninu App HarmonyOS. Skill ko ṣe iranlọwọ awọn mejeeji — lẹhin isanwo pada si Ipe 7.

## Ipe 7: Wiwọle deede (ọna asopọ 2)

Lẹhin imudaniloju isanwo, kọkọ ṣe paṣipaarọ ipo wiwọle ti o ni ikede ṣiṣe alaisanfarasin tuntun, lẹhinna ṣe ipilẹṣẹ ọna asopọ taara si oju-iwe ile:

```
POWPOW_REGISTER_PASSWORD=<ọrọigbaniwọle> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Firanṣẹ ọna asopọ si olumulo: **lẹhin tite o de oju-iwe ile taara, ipo ọmọ ẹgbẹ ni kikun**, titi iforukosile gbogbo ti pari.

## Ipe 8: Ipari

1. `node scripts/powpow-register.mjs cleanup` nu faili ipo igba-die ti ẹrọ yii kuro (ẹri igba-iṣẹ).
2. Fun olumulo "kaadi akọọlẹ" kan: oruko olumulo, imeeli, akoko ipari ọmọ ẹgbẹ (ọrọ igbaniwọle ko tun ṣafihan — ipo ipilẹṣẹ ti han lẹẹkan ki olumulo to tọju; ti ara rẹ mọ ti o ṣe).
3. Ṣe itọsọna iriri: rin maapu, fi irin-ajo akọkọ rẹ ranṣẹ (→ fi si ọwọ powpow-simple).
4. Daba imugboroosi: skill `@durenzidu/powpow-integration` ati afikun `@durenzidu/openclaw-channel-powpow` — so Bubble pọ si agent ti ara rẹ; ti o ba fẹ ṣafikun fun aṣẹ fifi sori ẹrọ.
5. Pari pẹlu apa "igbesẹ ti nbọ".

## Conversation UX

Tẹle ohun orin iṣẹ ti PowPow:

- **Olumulo ni koko-ọrọ gbolohun**, "o le..." dara ju "mo nilo ki o..."; maṣe kọni, maṣe ga ju.
- **Ṣe ilosiwaju ipinnu kan fun iyipo kan**; ṣaaju ki o to beere alaye fun idi.
- **Ni ipari idahun kọọkan** jẹ apa "igbesẹ ti nbọ" ti o duro (ila ipinya + 👉 + iṣe kan + gbolohun kan "nigbati mo ba pari emi yoo..."), fun apẹẹrẹ:
  ```
  ────────────────────
  👉 Ohun ti o nilo lati ṣe ni bayi: lọ si imeeli wo nọmba oni-nọmba 6, fi ranṣẹ taara
     (nigbati mo ba gba emi yoo kọ akọọlẹ naa lẹṣẹkan)
  ```
- **Maṣe ṣe ẹkọ aabo lori ọrọ igbaniwọle funrarẹ**; maṣe ṣalaye ero inu, ihamọ, tabi apẹrẹ aabo, ayafi ti olumulo ba beere.
- Nigbati agent ba n ṣe iranlọwọ, sọ ilọsiwaju siwaju: lẹhin igbesẹ iwe kọọkan sọ fun olumulo ohun ti o ṣẹlẹ ní gbolohun kan ("akọọlẹ ti ṣẹda", "a ti ṣii oju-iwe isanwo fun ọ").

## Awọn ofin lile

- **Aabo ẹri**: ọrọ igbaniwọle n lọ nipasẹ oniyipada ayika `POWPOW_REGISTER_PASSWORD` si iwe nikan, **rara** kọ sinu awọn ariyanjiyan aṣẹ (atipe akojọ ilana han), rara kọ sinu eyikeyi faili (ipo ipilẹṣẹ fihan lẹẹkan ki olumulo to tọju, ko tun sọ). Koodu ijẹrisi n lo fun akojọpọ iforukosile osise nikan, lẹhin lilo jẹ abojuto.
- **Ààlà osise**: gbogbo awọn ibeere n lọ si `https://global.powpow.online` nikan (iwe ti fi sii tẹlẹ), rara maṣe fi alaye olumulo ranṣẹ si eyikeyi adirẹsi ẹnikẹta.
- **Ààlà isanwo**: agent n ṣẹda aṣẹ, ṣii alagbata, ṣe ibeere isanwo; **rara** fọwọkan akọọlẹ Alipay/PayPal olumulo / ẹri isanwo, rara ṣe ileri "sanwo ni ipo rẹ".
- **Odi isanwo kii ṣe bug**: ipo pending ni anfani lati wọ oju-iwe ṣiṣe alaisanfarasin / oju-iwe ipadabọ jẹ igbanilaaye inu apẹrẹ; awọn oju-iwe akoonu ti a dena jẹ odi isanwo pẹpẹ ti n ṣiṣẹ deede, maṣe gbiyanju lati fọ.
- **Ominira ipadabọ**: nigbati olumulo ba fẹ ṣe ọwọ funrarẹ ni eyikeyi ipe, tabi agbegbe ko ṣe atilẹyin iwe, pada si ipo itọsọna lasan nigbakugba — fun awọn ọna asopọ, ṣalaye awọn ofin, ṣe iranlọwọ ṣiṣayẹwo aṣiṣe.
- Maṣe ṣe ipilẹṣẹ awọn ofin pẹpẹ: awọn ofin aaye, ọrọ aṣiṣe, awọn ariyanjiyan ihamọ gbogbo wa lati inu koodu pẹpẹ (`references/registration-flow.md` ni orisun koodu), imudojuiwọn pẹpẹ tẹle ihuwasi gangan.
- Awọn aworan ifihan lo awọn ti o wa ninu `assets/screenshots/` ti a dahun pọ pẹlu skill nikan (lilo aworan kọọkan wo `references/screenshots.md`).
- Iyipo kọọkan pari pẹlu apa "igbesẹ ti nbọ", ki olumulo maa mọ ohun ti o yẹ ki o ṣe nigbagbogbo.
