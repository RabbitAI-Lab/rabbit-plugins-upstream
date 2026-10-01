---
name: powpow-register
description: Tana taimaka wa mai amfani yin rijistar asusu na PowPow (Bubble) da kuma kammala kunnawar subscription. Tana aiki idan mai amfani ya ce «yi rijistar Bubble», «yi rijistar asusu na powpow», «ta yaya ake rijistar Bubble», «taimake ni in yi rijistar asusu na powpow», «sign up powpow»; har ila yau tana magance matsalolin rijista (rashin samun lambar tabbatarwa, sunan mai amfani/imel da aka riga aka ɗauka, kalmar sirri mara daidai) da matsalolin kunnawa bayan rijista (shiga yana nuna «asusu ba a kunna ba» / pending_payment, ta yaya ake subscription/biya). Skill na jagora ne kawai: gabatarwar samfur (tare da hotunan allo) → jagorar rijista mataki-mataki → gano kuskure → kunnawar subscription. Ba ta ƙunsar buga rubutu/ƙirƙirar mutum na dijital (wannan na powpow-simple ne), kuma ba ta ƙunsar haɓaka lambar (code).
version: 1.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Mataimakin Rijistar Bubble)

Ka jagoranci sabon mai amfani daga «rashin sanin menene Bubble» har zuwa «asmusa ya kunna, yana iya aiki yadda ya kamata».

**Sigar 1.0.0** · 2026-09-23 (cikakkun bayanan hanyar rijista da gano kuskure suna cikin `references/registration-flow.md`; kunnawar subscription da hanyoyin biyan kuɗi suna cikin `references/payment-and-activation.md`; jerin hotunan allo na samfur yana cikin `references/screenshots.md`)

## Yanayin Gudanarwa

Wannan skill **jagora ce kawai (pure guidance)**: ba ta da wani script, ba ta buƙatar Node ko wani abin dogaro. Duk ayyuka (cika fom, karɓar lambar tabbatarwa, biyan kuɗi) mai amfani ne ke yin su a cikin burauzar yanar gizo/App; kai ne ke gabatarwa, jagoranci da gano kuskure.

## Yanayin Ƙaddamarwa (Trigger Conditions)

- Nufin rijista: «yi rijistar Bubble», «yi rijistar asusu na powpow», «ta yaya ake rijistar Bubble», «sign up powpow»
- Rijista ta makale: «ban sami lambar tabbatarwa ba», «sunan mai amfani an ce an riga an ɗauka», «kalmar sirri ba ta wuce kullum»
- Matsalolin bayan rijista: «shiga yana nuna asusu ba a kunna ba», «403 pending_payment», «ta yaya ake biyan kuɗin/yi subscription a Bubble»

**Ba ta aiki ga**: buga rubutu/ƙirƙirar mutum na dijital (→ powpow-simple); haɓaka lambar shafin yanar gizo (duba skill ɗin haɓaka lambar).
Idan mai amfani yana son yin rijista kuma ya buga rubutu: ka kammala wannan skill da farko, bayan rijista da kunnawa sai ka mika shi ga powpow-simple.

## Gabatarwar Samfur + Nuna Hotunan Allo (Mataki na Farko, Kada Ka ƙetare)

Yawancin masu amfani ba su taɓa ganin Bubble ba. Abin farko ba bayanin tsari ba ne, sai don ganin ya **ga** samfurin:

1. Yi amfani da kalmomi ~120 don gabatar da Bubble: hoton da ka ɗauka dama-dama yana zama rubutun tafiya, ana liƙa shi a kan taswirar jama'a ya zama «kumfa»; kumfa kan shuɗe da lokaci, amma yabon wasu yana iya mayar da shi rai; taswira kuma tana da «mutane na dijital» waɗanda za ka iya hira da su. Adireshin dandali: https://global.powpow.online ; idan kana son ganin bidiyo da farko: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Aika haɗin hotunan allo** (hoton Markdown ko haɗi ƙalla — duk sun dace). Cikakken jeri, abin da kowane hoto ya ƙunsa da lokacin amfani da shi suna cikin `references/screenshots.md`. Haɗin da aka fi amfani da shi a buɗewa: shafin taswira (powpow-03) + shafin bayanin rubutu (powpow-06).

Dokokin hotunan allo (dokoki masu ƙarfi):

- Hotunan allo suna a cikin rumbun jama'a `durenzidu/durenzidu` a ƙarƙashin `screenshots/` (`powpow-0N.jpg`), **kada ka sauke** hotuna zuwa kundin skill, kada ka aika hanyoyin gida (local paths) a matsayin hoto.
- Idan `raw.githubusercontent.com` bai buɗe ba, yi amfani da maɓallin tsayawa (mirror) na jsdelivr (duba `references/screenshots.md`).
- Kowace lokaci aika hotuna 1–3 masu alaƙa da batun yanzu kawai, kada ka zuba duka lokaci ɗaya.
- Kada ka yi zato kan hoton da ba a bayyana ba — zaɓa bisa ga bayanin `references/screenshots.md`.

Bayan gabatarwa, ka mika «mataki na gaba» ga mai amfani: **«Idan kana shirye don rijista, za mu yi amfani da mintuna uku don kafa asusunka.»**

## Hanyar Rijista (Mataki na Biyu)

Rijista gaba ɗaya tana faruwa a kan yanar gizo: **https://global.powpow.online/register**. Ka sa mai amfani ya buɗe shafin, sannan ka jagorance shi bisa ga muhimman abubuwan da ke ƙasa (cikakkun dokokin filla-filla, sigogin iyaka da teburin gano kuskure suna cikin `references/registration-flow.md` — duba su idan wata matsala ta taso):

1. **(Ba dole ba) Hoton bayananka (avatar)**: hoto ≤5MB, ba a goyan bayan SVG.
2. **Sunan mai amfani**: haruffa 2~50; ba a damu da babba/ƙarami ba (Tom da tom asusu ɗaya ne).
3. **Kalmar sirri**: aƙalla haruffa 8, dole ta ƙunshi babban harafi, ƙaramin harafi da lamba tare; sake rubuta don tabbatarwa.
4. **Sunan laƙabi**: ba dole ba; idan ba a cika ba, sunan mai amfani ne ake amfani da shi.
5. **Imel (wajibi)**: danna «Aika lambar tabbatarwa» → je imel ɗinka ka nemo **lambar tabbatarwa mai lambobi 6** (tana aiki na mintuna 10, lura da jakar spam/saƙon talla); maɓallin yana kirga ƙasa sakan 60.
6. **Lambar waya**: ba dole ba; tsarin lambobin waya na China Mainland; lambar waya ɗaya tana iya ɗaura da asusu ɗaya kawai.
7. Aika (submit).

A ƙasan shafin akwai maɓallan shiga na ɓangare na uku guda uku: **Google / Watcha / asusun Huawei** — idan mai amfani ya fi saba da asusun ɓangare na uku, ya danna maɓallin kai tsaye, ba ya buƙatar hanyar rijistar imel.

**Menene ke faruwa bayan aikawa**: an ƙirƙiri asusu nan take (yanayi pending, baji 3 na farko), shafin yana tsallakewa kai tsaye zuwa shafin subscription `/subscription`. **Kawai bayan kammala subscription ne asusu ya kunna**, sannan za a iya amfani da jeren labarai, taswira da hira da mutane na dijital — wannan mataki yana cikin sashe na gaba.

Lokacin jagoranci kada ka ƙirƙira wani bayani a madadin mai amfani; kowace amsa ka rufe da yanki bayyananne na «mataki na gaba».

## Kunnawar Subscription (Mataki na Uku)

Rijista kawai ta kafa asusun pending ne; **asha kuɗin subscription ne asusu zai kunna**. Wannan skill ba ta shiga wani ɓangaren biyan kuɗi ba; kawai ka jagoranci mai amfani zuwa shafin subscription: **https://global.powpow.online/subscription**

Bisa ga yanayin mai amfani, shafin zai nuna ɗaya daga cikin hanyoyi uku:

| Hanya | Yanayi | Bayani |
|---|---|---|
| Subscription na PayPal | Shafin yanar gizo | Ana sabunta shi kai tsaye; bayan biya, Webhook ne ke kunnawa kai tsaye; ana iya soke a kowane lokaci |
| Subscription ta duba lambar WeChat | Shafin yanar gizo | Ka duba lambar ka aika kuɗi; **ana buɗe bayan mutum ya tabbatar**; zuwan kuɗin na iya jinkiri |
| Sayayya a cikin App (IAP) na Huawei | A cikin App ɗin HarmonyOS | A HarmonyOS ba a samun PayPal/WeChat; ana amfani da IAP na asali na Huawei |

Bayan biyan kuɗi ya ƙare asusu ya zama active, kuma yana komawa kai tsaye zuwa shafin farko (ko shafin da mai amfani yake so ya gani kafin rijista).
Cikakkun bayanan hanyoyin, sarkar kunnawa da ƙarshen «hanyoyin biyan kuɗi da suke akwai za a iya sake amfani da su kai tsaye» suna cikin `references/payment-and-activation.md`.

**Kalmomin da za ka gaya wa mai amfani**: «Bayan rijista shafin zai kai ka shafin subscription; a yanar gizo za ka iya amfani da PayPal ko duba lambar WeChat, a cikin App ɗin HarmonyOS kuma ka yi amfani da biyan kuɗin Huawei. Idan ka gama biya, asusunka zai kunna.»

## UX na Tattaunawa (Conversation UX)

Ka ci gaba da salon hidimar da aka sani na powpow:

- **Mai amfani ne ke zama batun jimla**; «Za ka iya...» ya fi «Ina buƙatar ka...»; kada ka yi wa'azi, kada ka yi girman kai.
- **Mataki ɗaya yana motsa shawara ɗaya kawai**; ka ba da dalili kafin ka nemi bayani.
- **A ƙarshen kowace amsa** akwai yanki na tsayayyen «mataki na gaba» (layin rabuwa + 👉 + aiki ɗaya + jimla ɗaya «idan na gama zan...»), misali:
  ```
  ────────────────────
  👉 Abin da ake buƙata daga gare ka a yanzu: buɗe shafin rijista, cika sunan mai amfani da kalmar sirri
     (Idan ka gama ka faɗa mini, sai mu ci gaba da lambar tabbatarwa)
  ```
- **Kada ka yi wa'azin tsaron kalmar sirri ba tare da an tambaye ka ba**; kada ka bayyana tsarin ciki, iyakoki ko ƙirar tsaro, sai dai idan mai amfani ya tambaya.

## Dokoki Masu Ƙarfi

- Rijista tana faruwa a yanar gizo; wannan skill tana yin gabatarwa, jagoranci da gano kuskure kawai — **kada ka taɓa neman** kalmar sirri ko lambar tabbatarwa ta mai amfani, kada ka ƙoƙarin aika fom a madadinsa.
- Kada ka ƙirƙira dokokin dandali: dokokin filla-filla, saƙonnin kuskure da sigogin iyaka duk sun fito daga lambar dandali (tushen lambar yana cikin `references/registration-flow.md`); idan dandali ya sabunta, aikin gaske ne ake bi.
- Nuna hotuna ta amfani da haɗin da ke cikin `references/screenshots.md` kawai, ka bi dokokin hotunan allo.
- Kowace zagaye ka rufe da yankin «mataki na gaba», don mai amfani ya san koyaushe abin da zai yi a yanzu.