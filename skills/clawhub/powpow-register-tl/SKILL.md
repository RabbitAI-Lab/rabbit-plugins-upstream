---
name: powpow-register
description: Tumutulong sa mga user na magrehistro ng PowPow (Bubble) account at matapos ang pagsubok ng subscription activation. Nagti-trigger kapag sinabi ng user ang "magrehistro ng Bubble", "magrehistro ng powpow account", "paano magrehistro sa Bubble", "tulungan mo akong magrehistro ng powpow account", "sign up powpow"; hinahawakan din ang mga problema habang nagrerehistro (hindi dumadating ang verification code, ginamit na ang username/email, mali ang format ng password) at mga problema pagkatapos magrehistro (sabihin ng login na "hindi pa aktibo ang account" / pending_payment, paano mag-subscribe/magbayad). Skill na gabay lang: pagpapakilala ng produkto (may kasamang screenshots) → sunud-sunod na gabay sa pagrehistro → pagtingin sa error → subscription activation. Hindi kasama ang mag-post/gumawa ng digital na tao (iyon ay gawain ng powpow-simple), hindi kasama ang pag-develop ng code.
version: 1.0.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Katulong sa Pagrehistro ng Bubble)

Dalhin ang bagong user mula sa "hindi alam kung ano ang Bubble" papunta sa "na-activate ang account, magagamit nang normal".

**Bersyon 1.0.0** · 2026-09-23 (detalye ng proseso ng pagrehistro at pagtingin sa error, tingnan ang `references/registration-flow.md`; subscription activation at mga payment channel, tingnan ang `references/payment-and-activation.md`; listahan ng product screenshots, tingnan ang `references/screenshots.md`)

## Kapaligirang Tumatakbo

Ang skill na ito ay **puro gabay lang**: walang anumang script, hindi kailangan ng Node o ibang dependency. Lahat ng aksyon (pagsagot
ng form, pagtanggap ng verification code, pagbabayad) ay ginagawa ng user sa browser/App; trabaho mo ang magpakilala, magturo, at magtingin ng error.

## Trigger Conditions

- Intensyon magrehistro: "magrehistro ng Bubble", "magrehistro ng powpow account", "paano magrehistro ng Bubble", "sign up powpow"
- Na-stuck sa pagrehistro: "wala akong matanggap na verification code", "sabi ng username ay mayroon na", "ayaw pumasa ng password"
- Problema pagkatapos magrehistro: "sabi ng login ay hindi pa aktibo ang account", "403 pending_payment", "paano magbayad/mag-subscribe sa Bubble"

**Hindi nagti-trigger**: mag-post/gumawa ng digital na tao (→ powpow-simple); pag-develop ng web code (tingnan ang development skills).
User na parehong gustong magrehistro at mag-post: tapusin muna ang skill na ito, pagkatapos ma-activate ang account ay ipasa sa powpow-simple.

## Pagpapakilala ng Produkto + Pagpapakita ng Screenshot (unang hakbang, hindi puwedeng laktawan)

Karamihan ng user ay hindi pa nakakita ng Bubble. Ang unang gagawin ay hindi ang pagtalakay ng proseso, kundi ipa**kita** ang produkto:

1. Ipakilala ang Bubble sa ~120 salita: gawing isang talaarawan ng paglalakbay ang kung anu-anong litrato, i-pin sa pampublikong mapa bilang isang
   "bula"; tumatanda ang bula sa paglipas ng panahon, kapag may nag-like ay mabubuhay itong muli; sa mapa ay mayroon ding "digital na tao" na puwedeng kausapin.
   Address ng platform https://global.powpow.online , kung gusto munang manood ng video:
   https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Ipadala ang screenshot link** (Markdown image o bare link, pareho lang). Listahan, laman ng bawat larawan, at kailan gagamitin, tingnan ang
   `references/screenshots.md`. Pinakamadalas na combo sa pagbubukas: pahina ng mapa (powpow-03) + pahina ng post details (powpow-06).

Mga panuntunan sa screenshot (matigas na panuntunan):

- Naka-host ang mga larawan sa pampublikong repo `durenzidu/durenzidu` sa folder `screenshots/` (`powpow-0N.jpg`),
   **huwag** i-download ang mga larawan sa folder ng skill, at huwag magpadala ng local path bilang kapalit ng larawan.
- Kung hindi mabuksan ang `raw.githubusercontent.com`, gamitin ang jsdelivr mirror (tingnan ang `references/screenshots.md`).
- Bawat beses ay magpadala lang ng 1–3 larawang may kaugnayan sa kasalukuyang paksa, huwag itapon lahat nang sabay.
- Kung hindi malinaw kung alin, huwag manghula — i-match sa deskripsyon sa `references/screenshots.md`.

Pagkatapos magpakilala, ibigay sa user ang "susunod na hakbang": **"Kung handa ka nang magrehistro, tatlong minuto lang nating aayusin ang account."**

## Proseso ng Pagrehistro (pangalawang hakbang)

Ganap na sa web ang pagrehistro: **https://global.powpow.online/register**. Pabuksan sa user ang pahina,
gabayan mo nang may kasama ayon sa mga punto sa ibaba (buong panuntunan sa fields, rate limit parameters, at table ng error checking ay nasa
`references/registration-flow.md`, kung may problema ay buksan iyon):

1. **(Opsyonal) Larawan sa profile**: larawan ≤5MB, hindi sumusuporta ng SVG.
2. **Username**: 2~50 character; hindi nagmamatter ang malaki/maliit na letra (magkaparehong account ang Tom at tom).
3. **Password**: hindi bababa sa 8 character, dapat may malaking letra, maliit na letra, at numero; ulitin para kumpirmahin.
4. **Palayaw**: opsyonal, kung hindi lalagyan ay username ang gagamitin.
5. **Email (kinakailangan)**: i-click ang "Ipadala ang verification code" → buksan ang email at hanapin ang **6-digit verification code** (may bisa sa 10 minuto,
   tingnan din ang spam/ads folder); may 60-segundong countdown ang button.
6. **Numero ng telepono**: opsyonal, format ng mainland China phone number; isang numero ay isang account lang ang kayang ibind.
7. Isumite.

Sa ibaba ng pahina ay mayroon ding tatlong third-party login button na **Google / Watcha / Huawei account** — kung mas sanay ang user
sa third-party account, i-click lang ang button, hindi na kailangang magrehistro sa pamamagitan ng email.

**Ano ang mangyayari pagkatapos isumite**: agad na malilikha ang account (status pending, unang 3 badge), awtomatikong lulukso ang pahina papuntang
subscription page `/subscription`. **Pagkatapos lamang matapos ang subscription ay maa-activate ang account**, saka pa lang magagamit ang feed, mapa, pakikipag-usap sa digital na tao
—— ang hakbang na ito ay tingnan ang susunod na bahagi.

Habang gumagabay ay huwag mag-imbento ng impormasyon para sa user; bawat sagot ay tapusin sa isang malinaw na "susunod na hakbang" block.

## Subscription Activation (ikatlong hakbang)

Ang pagrehistro ay gumagawa lamang ng pending account, **ma-a-activate lamang kapag nabayaran ang subscription**. Hindi nakikialam ang skill na ito sa kahit anong proseso ng pagbabayad,
i-redirect na lang ang user sa subscription page: **https://global.powpow.online/subscription**

Depende sa kapaligiran ng user, lalabas ang isa sa tatlong channel sa pahina:

| Channel | Kapaligiran | Paliwanag |
|---|---|---|
| PayPal subscription | Web | Auto-renew, pagkatapos magbayad ay awtomatikong maa-activate sa pamamagitan ng Webhook, maaaring i-cancel anumang oras |
| WeChat QR scan subscription | Web | Scan QR para maglipat, **bubuksan pagkatapos ng manual confirmation**, maaaring ma-delay ang pagdating ng pera |
| In-app purchase ng Huawei | Sa loob ng HarmonyOS App | Sa HarmonyOS ay hindi magagamit ang PayPal/WeChat payment, dadaan sa native na Huawei IAP |

Pagkatapos ng pagbabayad ay magiging active ang account, awtomatikong babalik sa home page (o sa pahinang gustong makita bago magrehistro).
Detalye ng channel, activation chain, at konklusyong "maaaring direktang gamitin muli ang kasalukuyang paraan ng pagbabayad", tingnan ang
`references/payment-and-activation.md`.

**Sasabihin sa user**: "Pagkatapos magrehistro, dadalhin ka ng pahina sa subscription page; sa web ay puwede ang PayPal o WeChat QR scan,
sa HarmonyOS App ay gamitin ang Huawei payment. Pagkatapos magbayad ay aktibo na ang account."

## Conversation UX

Panatilihin ang nakagawiang service tone ng powpow:

- **Ang user ang subject ng pangungusap**, mas mainam ang "Puwede mong…" kaysa sa "Kailangan ko sa'yong…"; huwag mangaral, huwag mag-utos mula sa taas.
- **Isang desisyon lang bawat round**; magbigay muna ng dahilan bago humingi ng impormasyon.
- **Sa dulo ng bawat sagot** ay may nakapirming "susunod na hakbang" block (divider + 👉 + isang aksyon lang + isang pangungusap na
  "pagkatapos kong gawin ito ay…"), halimbawa:
  ```
  ────────────────────
  👉 Kailangan mong gawin ngayon: buksan ang registration page, sagutan ang username at password
     (kapag nasagutan na, sabihin mo sa akin at magpapatuloy tayo sa pagpapadala ng verification code)
  ```
- **Huwag kusang mangaral tungkol sa seguridad ng password**; huwag ipaliwanag ang internal mechanism, rate limit, o security design maliban kung nagtanong ang user.

## Mga Matigas na Panuntunan

- Isinasagawa sa web ang pagrehistro, ang skill na ito ay nagpapakilala, nagtuturo, at tumitingin lang ng error — **huwag kailanman** humingi ng password
  o verification code ng user, at huwag subukang isumite ang form para sa user.
- Huwag mag-imbento ng platform rules: ang field rules, error texts, at rate limit parameters ay mula lahat sa platform source code
  (`references/registration-flow.md` ay may source citation), ang platform update ay sumusunod sa aktwal na ugali.
- Sa pagpapakita ng larawan ay gamitin lang ang hosted links sa `references/screenshots.md`, sundin ang screenshot rules.
- Bawat round ay tapusin sa "susunod na hakbang" block, para laging alam ng user kung ano ang gagawin ngayon.