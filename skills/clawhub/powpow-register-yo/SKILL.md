---
name: powpow-register
description: Ní ìrànlọ́wọ́ fún olùmúlò láti forúkọ àkọọlẹ̀ PowPow (Bubble) sílẹ̀ àti láti parí ìmúṣiṣẹ́ ìforúkọsílẹ̀. Ó máa ń bẹ̀rẹ̀ nígbà tí olùmúlò bá sọ «Forúkọ Bubble sílẹ̀», «Forúkọ àkọọlẹ̀ powpow sílẹ̀», «Báwo ni a ṣe ń forúkọ Bubble sílẹ̀», «Ran mi lọ́wọ́ láti forúkọ àkọọlẹ̀ powpow sílẹ̀», «sign up powpow»; ó sì ń bójú tó àwọn ìṣòro tó máa ń yọjú nínú ìforúkọsílẹ̀ (kò tíì gba kódì ìmúdarí, orúkọ olùmúlò/ìmélì ti wà tẹ́lẹ̀, ọ̀rọ̀ àsìrí kò bá ìlànà mu) àti àwọn ìṣòro ìmúṣiṣẹ́ lẹ́yìn ìforúkọsílẹ̀ (ìwọlé tó ń wí pé «a kò tíì mú àkọọlẹ̀ ṣiṣẹ́» / pending_payment, báwo ni a ṣe ń sanwó ìforúkọsílẹ̀). Skill ìtọ́sọ́nà (guidance) péré: ìfihàn ọjà (pẹ̀lú àwọn àwòrán ojú-ìwé) → ìtọ́sọ́nà ìforúkọsílẹ̀ lẹ́sẹ̀-kẹ̀tẹ́kẹ̀tẹ́ → ìṣàwárí ìṣòro → ìmúṣiṣẹ́ ìforúkọsílẹ̀. Kò ní í ṣe pẹ̀lú kíkọ àwọn ìkọ̀wé/ṣíṣẹ̀dá ènìyàn dídijitá (èyí jẹ́ ti powpow-simple), kò sì ní í ṣe pẹ̀lú ìdàgbàsókè kóòdù.
version: 1.0.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Olùrànlọ́wọ́ Ìforúkọsílẹ̀ Bubble)

Máa ṣe amọ̀nà olùmúlò tuntun láti «mọ ohun tí Bubble jẹ́» dé «ìmúṣiṣẹ́ àkọọlẹ̀ àti lílò rẹ̀ dáradára».

**Ìwé 1.0.0** · 2026-09-23 (Àwọn ìlànà fọ́ọ̀mù àti ìṣàwárí ìṣòro wà ní `references/registration-flow.md`; ìmúṣiṣẹ́ ìforúkọsílẹ̀ àti àwọn ọ̀nà ìsanwó wà ní `references/payment-and-activation.md`; àkójọpọ̀ àwọn àwòrán ojú-ìwé ọjà wà ní `references/screenshots.md`)

## Àyíká Ìṣiṣẹ́

Skill yìí **ìtọ́sọ́nà péré (pure guidance)** ni: kò ní ìkọ̀wé-ètò (script) kankan, kò béèrè Node tàbí ìgbẹ́kẹ̀lé (dependency) mìíràn. Gbogbo ìgbésẹ̀ (kíkún fọ́ọ̀mù, gbígba kódì ìmúdarí, ìsanwó) ni olùmúlò ṣe lórí browser/app; iṣẹ́ rẹ ni ìfihàn, ìtọ́sọ́nà àti ìṣàwárí ìṣòro nìkan.

## Àwọn Ipò Ìmúbẹ̀rẹ̀ (Trigger Conditions)

- Ìfẹ́ ìforúkọsílẹ̀: «Forúkọ Bubble sílẹ̀», «Forúkọ àkọọlẹ̀ powpow sílẹ̀», «Báwo ni a ṣe ń forúkọ Bubble sílẹ̀», «sign up powpow»
- Ìforúkọsílẹ̀ ṣẹ́kun: «Kò tíì gba kódì ìmúdarí», «Ó ní orúkọ olùmúlò ti wà tẹ́lẹ̀», «Ọ̀rọ̀ àsìrí kì í gbà nígbà gbogbo»
- Àwọn ìṣòro lẹ́yìn ìforúkọsílẹ̀: «Ìwọlé ń wí pé àkọọlẹ̀ kò tíì ṣiṣẹ́», «403 pending_payment», «Báwo ni a ṣe ń sanwó/forúkọ sílẹ̀ fún Bubble»

**Àwọn tí kò yẹ kó máa ń mú un bẹ̀rẹ̀**: kíkọ àwọn ìkọ̀wé/ṣíṣẹ̀dá ènìyàn dídijitá (→ powpow-simple); ìdàgbàsókè kóòdù ojú-ìwé (wo àwọn skill ìdàgbàsókè).
Tí olùmúlò bá fẹ́ forúkọ sílẹ̀ àti kọ̀wé lápapọ̀: kọ́kọ́ parí skill yìí, lẹ́yìn ìforúkọsílẹ̀ àti ìmúṣiṣẹ́, kó o sì ṣàkóso sí powpow-simple.

## Ìfihàn Ọjà + Ìfihàn Àwòrán Ojú-Ìwé (Ìgbésẹ̀ Kìíní, má ṣe fo ó)

Ọ̀pọ̀lọpọ̀ olùmúlò ò tíì rí Bubble rí. Ohun àkọ́kọ́ kì í ṣe láti ṣàlàyé ìlànà, ṣùgbọ́n láti jẹ́ kí wọ́n **rí ọjà náà**:

1. Fi ọ̀rọ̀ ~120 láfẹ̀ẹ́sí hàn Bubble: àwòrán tí a yá pẹ̀lú àyànmọ́ di ìránṣẹ́ ìrìn-àjò, tí a so mọ́ máàpù gbogbogbò tí ó di «Bubble» (àmì àtẹ́gùn); Bubble náà ń ṣánlẹ̀ pẹ̀lú àkókò, ṣùgbọ́n àwọn ìfẹ́ràn ènìyàn lè mú un sòjí; lórí máàpù náà, àwọn «ènìyàn dídijitá» wà tí o lè bá sọ̀rọ̀. Adirẹ́sì pẹ̀pẹ̀ náà ni https://global.powpow.online, tí o bá fẹ́ wo fídíò ṣáájú: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Rán àwọn ọ̀rọ̀ asopọ̀ àwòrán ojú-ìwé sí i** (àwòrán Markdown tàbí ọ̀rọ̀ asopọ̀ òfo — méjèèjì á ṣiṣẹ́). Àkójọpọ̀ kíkún, àwọn àkóónú àwòrán kọ̀ọ̀kan àti àkókò lílò wà ní `references/screenshots.md`; àkópọ̀ tó wúlò jù lọ fún ibẹ̀rẹ̀: ojú-ìwé máàpù (powpow-03) + ojú-ìwé àkójọ àwọn ìkọ̀wé (powpow-06).

Àwọn òfin àwòrán ojú-ìwé (àwọn òfin líle):

- Àwọn àwòrán ojú-ìwé wà ní ìpamọ́ gbogbogbò `durenzidu/durenzidu` lábẹ́ `Screenshots/` (`powpow-0N.jpg`), **má ṣe gbà wọ́n sílẹ̀** sínú àkójọpọ̀ skill, má sì fi àwọn ọ̀nà àdúgbò rán gẹ́gẹ́ bí àwòrán.
- Tí `raw.githubusercontent.com` ò bá ṣí, lo ẹ̀dà-ojú (mirror) jsdelivr (wo `references/screenshots.md`).
- Rán àwòrán 1–3 tí ó bá ọ̀rọ̀ lọ́wọ́ lọ́wọ́ nìkan, má ṣe da gbogbo wọ́n ní ẹ̀ẹ̀kan.
- Tí kò bá ṣe kedere èyí tá a ń sọ, má ṣe gbọ̀ọ́rọ̀ — yàn ní ìbámu pẹ̀lú àpèjúwe `references/screenshots.md`.

Lẹ́yìn ìfihàn, fi «ìgbésẹ̀ tó kàn» hàn fún olùmúlò: **«Bí o bá fẹ́ forúkọ sílẹ̀, a ó fi ìṣẹ́jú mẹ́ta ṣètò àkọọlẹ̀ rẹ.»**

## Ìlànà Ìforúkọsílẹ̀ (Ìgbésẹ̀ Kejì)

Ìforúkọsílẹ̀ náà ń ṣẹlẹ̀ pátápátá lórí ayélujára: **https://global.powpow.online/register**. Sọ fún olùmúlò kí ó ṣí ojú-ìwé náà, ìwọ sì máa ṣe amọ̀nà rẹ̀ ní ìbámu pẹ̀lú àwọn kókó tó wà nísàlẹ̀. (Àwọn ìlànà pípé fún gbogbo pápá fọ́ọ̀mù, àwọn ṣíṣètò ìdíwọ̀n àti tábìlì ìṣàwárí ìṣòro wà ní `references/registration-flow.md` — wo ó nígbà tí ìṣòro bá yọjú):

1. **(Ìyàn)** Àwòrán ìdánimọ̀: àwòrán ≤5MB, SVG kò ṣiṣẹ́.
2. **Orúkọ olùmúlò**: 2~50 lẹ́tà; kò já sí pàtàkì lẹ́tà ńlá àti kékeré (Tom àti tom jẹ́ àkọọlẹ̀ kan).
3. **Ọ̀rọ̀ àsìrí**: ó gbọ́dọ̀ ní ó kéré tán 8 lẹ́tà, lẹ́tà ńlá kan, lẹ́tà kékeré kan àti nọ́ḿbà kan; kọ̀ ọ́ lẹ́ẹ̀mejì láti fi dá a mọ́.
4. **Orúkọ ìpè**: ìyàn ní; tí a kò bá kún un, orúkọ olùmúlò náà ni a ó lò.
5. **Ìmélì (dánilójú)**: tẹ «Rán kódì ìmúdarí» → lọ sí àpótí ìmélì rẹ kí o wá **kódì oní nọ́ḿbà mẹ́fà** (ó máa ń ṣiṣẹ́ fún wákàtí fún ìṣẹ́jú mẹ́wàá, wo ìpín spam/ìpolówó) → kó o sì fi un sílẹ̀; bọ̀tìnì náà ní kààntì àìkà ọgọ́ta ìṣẹ́jú-àáyá.
6. **Nọ́ḿbà fóónù**: ìyàn ní; ọ̀nà nọ́ḿbà fóónù orílẹ̀-èdè Ṣáínà; nọ́ḿbà fóónù kan ṣoṣo ni ó lè so mọ́ àkọọlẹ̀ kan.
7. Fi sílẹ̀ (Submit).

Nísàlẹ̀ ojú-ìwé náà, àwọn bọ̀tìnì ìwọlé onígbà-mẹ́ta wà: **Google / Watcha / Àkọọlẹ̀ Huawei** — bí olùmúlò bá ṣeun láti lo àkọọlẹ̀ onígbà-mẹ́ta, kí ó tẹ bọ̀tìnì náà taara, kò sí láti forúkọ ìmélì sílẹ̀.

**Ohun tí ó ń ṣẹlẹ̀ lẹ́yìn fífilẹ̀**: àkọọlẹ̀ náà máa ń dá sílẹ̀ lẹ́sẹ̀kẹsẹ̀ (ipò pending, àmì-ẹ̀yẹ mẹ́ta àkọ́kọ́), ojú-ìwé náà á sì lọ sí ojú-ìwé ìforúkọsílẹ̀ `/subscription` fúnrarẹ̀. **Àkọọlẹ̀ náà á máa ṣiṣẹ́ nígbà tí o bá parí ìforúkọsílẹ̀ nìkan**, nígbà náà ni o lè wo ìtàn ìkọ̀wé, máàpù àti bá àwọn ènìyàn dídijitá sọ̀rọ̀ — a ṣàlàyé ìgbésẹ̀ yìí nínú apá tó kàn.

Nígbà ìtọ́sọ́nà, má ṣe dá àkọọlẹ̀ kankan sílẹ̀ ní orúkọ olùmúlò; parí ìdáhùn kọ̀ọ̀kan pẹ̀lù apá «ìgbésẹ̀ tó kàn» tí ó ṣe kedere.

## Ìmúṣiṣẹ́ Ìforúkọsílẹ̀ (Ìgbésẹ̀ Kẹta)

Ìforúkọsílẹ̀ kì í ṣe ju ṣíṣẹ̀dá àkọọlẹ̀ pending; **àkọọlẹ̀ náà á máa ṣiṣẹ́ nígbà tí ìsanwó ìforúkọsílẹ̀ bá parí**. Skill yìí kò kópa nínú ìlànà ìsanwó kankan; ó máa ń darí olùmúlò sí ojú-ìwé ìforúkọsílẹ̀: **https://global.powpow.online/subscription**

Ní ìbámu pẹ̀lú àyíká olùmúlò, ojú-ìwé náà á fi ọ̀kan nínú àwọn ọ̀nà mẹ́ta hàn:

| Ọ̀nà | Àyíká | Àlàyé |
|---|---|---|
| Ìforúkọsílẹ̀ PayPal | Ayélujára | Ó máa ń tún ara rẹ̀ ṣe fúnrarẹ̀; lẹ́yìn ìsanwó, ó máa ń ṣiṣẹ́ fúnrarẹ̀ nípasẹ̀ Webhook; ó ṣeé ṣe láti fagilé nígbàkúgbà |
| Ìforúkọsílẹ̀ QR WeChat | Ayélujára | A kà kódì QR tán, a sanwó; **a máa ń ṣiṣẹ́ lẹ́yìn ìfọwọ́sowọ́pọ̀ ènìyàn**; ìsanwó lè sún ọ̀wọ́n |
| Rírà inú-app Huawei (IAP) | Nínú app HarmonyOS | Ní HarmonyOS, ìsanwó PayPal/WeChat kò sí; a lo IAP Huawei ẹlẹ́yà (native) |

Lẹ́yìn tí ìsanwó bá parí, àkọọlẹ̀ náà di active, á sì tún padà sí ojú-ìwé àkọ́kọ́ fúnrarẹ̀ (tàbí sí ojú-ìwé tí ó wà ṣáájú ìforúkọsílẹ̀).
Àwọn ìsọkún ọ̀nà, ìwọ̀n ìmúṣiṣẹ́ àti ìpinnu «a lè lo àwọn ọ̀nà ìsanwó tó wà lọ́wọ́ taara» wà ní `references/payment-and-activation.md`.

**Ọ̀rọ̀ tí o máa sọ fún olùmúlò**: «Lẹ́yìn ìforúkọsílẹ̀, ojú-ìwé náà á gbé ọ lọ sí ojú-ìwé ìforúkọsílẹ̀; lórí ayélujára o lè lo PayPal tàbí QR WeChat, nínú app HarmonyOS o á lo ìsanwó Huawei. Tí o bá parí ìsanwó, àkọọlẹ̀ rẹ á ṣiṣẹ́.»

## Àwọn Ilé-ìṣe Ìbánisọ̀rọ̀ (Conversation UX)

Máa tẹ̀síwájú nínú ìwà ìsìn powpow tí a mọ̀:

- **Olùmúlò ni kókó gbólóhùn náà**: «o lè...» dára ju «mo fẹ́ kí o...»; má ṣe kọ́ni lẹ́kọ̀ọ́, má ṣe wáyà.
- **Ìpinnu kan ṣoṣo ní ìyípo kan**: fún ìdí ní ṣáájú kí o tó béèrè ìsọfúnni.
- **Ní ìparí ìdáhùn kọ̀ọ̀kan**, apá «ìgbésẹ̀ tó kàn» wà tí ó dúró ṣinṣin (ìlà-ìyapa + 👉 + ìgbésẹ̀ kan + gbólóhùn «nígbà tí...»; àpẹẹrẹ):
  ```
  ────────────────────
  👉 Ìgbésẹ̀ tí o gbọ́dọ̀ ṣe nísinsìnyí: ṣí ojú-ìwé ìforúkọsílẹ̀ kí o kún orúkọ olùmúlò àti ọ̀rọ̀ àsìrí
     (nígbà tí o bá kún un, sọ fún mi, a ó tẹ̀síwájú sí kódì ìmúdarí)
  ```
- **Má ṣe béèrè ìsọfúnni ìsọkẹ́rẹ́ ti ọ̀rọ̀ àsìrí tí wọn kò béèrè**: má ṣe ṣàlàyé àwọn ìlànà inú, ìdíwọ̀n tàbí ẹ̀rọ ààbò, àyàfi tí olùmúlò bá béèrè.

## Àwọn Òfin Líle

- Ìforúkọsílẹ̀ ń ṣẹlẹ̀ lórí ayélujára; skill yìí ń ṣe ìfihàn, ìtọ́sọ́nà àti ìṣàwárí ìṣòro nìkan — **má ṣe béèrè** ọ̀rọ̀ àsìrí tàbí kódì ìmúdarí olùmúlò, má sì gbìyànjú láti fi fọ́ọ̀mù sílẹ̀ lórúkọ rẹ̀.
- Má ṣe dá àwọn òfin pẹ̀pẹ̀: àwọn ìlànà pápá fọ́ọ̀mù, àwọn ìránṣẹ́ àṣìṣe àti àwọn ṣíṣètò ìdíwọ̀n gbogbo wá láti inú kóòdù pẹ̀pẹ̀ (ìdídí kóòdù wà ní `references/registration-flow.md`); nigbà tí pẹ̀pẹ̀ bá ṣe àtúnyẹ̀wò, tẹ̀lé ìwà gidi tó wà lórí ayélujára.
- Fún àwọn àwòrán, lo àwọn ọ̀rọ̀ asopọ̀ tí a tọ́jú nínú `references/screenshots.md` nìkan, kí o sì tẹ̀lé àwọn òfin àwòrán ojú-ìwé.
- Parí ìyípo kọ̀ọ̀kan pẹ̀lú apá «ìgbésẹ̀ tó kàn», kí olùmúlò lè mọ ohun tí ó ṣe nísinsìnyí nígbà gbogbo.