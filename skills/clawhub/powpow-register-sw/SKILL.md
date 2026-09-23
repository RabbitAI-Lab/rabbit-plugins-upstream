---
name: powpow-register
description: Husaidia mtumiaji kujiandikisha akaunti ya PowPow (Bubble) na kukamilisha uanzishaji wa usajili. Hutekelezwa mtumiaji anaposema «Nijiandikishe Bubble», «Nijiandikishe akaunti ya powpow», «Bubble inajiandikishwaje», «Nisaidie kujiandikisha akaunti ya powpow», «sign up powpow»; pia hushughulikia matatizo ya mchakato wa kujiandikisha (kutopokea msimbo wa uthibitisho, jina la mtumiaji/barua pepe kuwa limechukuliwa, umbizo la neno la siri lisilo sahihi) na matatizo ya uanzishaji baada ya kujiandikisha (kuingia kukiwa na ujumbe «akaunti haijaanzishwa» / pending_payment, jinsi ya kusajili/kulipa). Skill ya mwongozo tu: utambulisho wa bidhaa (pamoja na picha za skrini) → mwongozo wa hatua kwa hatua wa kujiandikisha → utatuzi wa makosa → uanzishaji wa usajili. Haitoi uchapishaji wa machapisho/kuunda watu wa kidijitali (hilo ni la powpow-simple), wala maendeleo ya msimbo.
version: 1.0.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Msaidizi wa Kujiandikisha Bubble)

Mongoze mtumiaji mpya kutoka «kutojua Bubble ni nini» hadi «akaunti imeamilishwa, inaweza kutumika kikamilifu».

**Toleo 1.0.0** · 2026-09-23 (maelezo ya kina ya mchakato wa kujiandikisha na utatuzi wa makosa yamo `references/registration-flow.md`; uanzishaji wa usajili na njia za malipo zimo `references/payment-and-activation.md`; orodha ya picha za skrini za bidhaa iko `references/screenshots.md`)

## Mazingira ya Uendeshaji

Skill hii ni **ya mwongozo pekee (pure guidance)**: haina skripti yoyote, haihitaji Node wala tegemezi lingine. Vitendo vyote (kujaza fomu, kupokea msimbo wa uthibitisho, malipo) hufanywa na mtumiaji ndani ya kivinjari/App; wewe ndiye unayeanzisha utambulisho, kuongoza na kutatua matatizo.

## Masharti ya Kutekelezwa (Trigger Conditions)

- Kusudio la kujiandikisha: «Nijiandikishe Bubble», «Nijiandikishe akaunti ya powpow», «Bubble inajiandikishwaje», «sign up powpow»
- Kujiandikisha kukwama: «Sipokei msimbo wa uthibitisho», «jina la mtumiaji linasemekana kuwa limechukuliwa», «neno la siri halipitishi kila mara»
- Matatizo baada ya kujiandikisha: «kuingia kunaonyesha akaunti haijaanzishwa», «403 pending_payment», «Bubble inalipwaje/ninawezaje kusajili»

**Haitekelezwi kwa**: kuchapisha machapisho/kuunda watu wa kidijitali (→ powpow-simple); maendeleo ya msimbo wa wavuti (tazama skill za maendeleo ya msimbo).
Mtumiaji anapotaka kujiandikisha na pia kuchapisha: kamilisha skill hii kwanza, kisha baada ya kujiandikisha na kuamilishwa mkabidhi powpow-simple.

## Utambulisho wa Bidhaa + Kuonyesha Picha za Skrini (Hatua ya Kwanza, Usiiruke)

Watumiaji wengi hawajawahi kuona Bubble. Jambo la kwanza si kuelezea mchakato, bali kumfanya mtumiaji **aone** bidhaa:

1. Tumia maneno ~120 kumtambulisha Bubble: picha uliyopiga kwa bahati inageuzwa kuwa kumbukumbu ya safari (travelogue), inapachikwa kwenye ramani ya umma ikawa «kiputo»; kiputo hupitwa na wakati, lakini kupendwa na watu wengine kunakiwezesha kurudi hai; ramani pia ina «watu wa kidijitali» ambao unaweza kuongea nao. Anwani ya jukwaa: https://global.powpow.online ; ukitaka kuona video kwanza: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Tuma viungo vya picha za skrini** (picha ya Markdown au kiungo tupu — vyote vinafaa). Orodha kamili, maudhui ya kila picha na wakati wa kuitumia yamo `references/screenshots.md`. Mchanganyiko unaotumika sana wakati wa ufunguzi: ukurasa wa ramani (powpow-03) + ukurasa wa maelezo ya chapisho (powpow-06).

Kanuni za picha za skrini (kanuni ngumu):

- Picha za skrini zimehifadhiwa kwenye hazina ya umma `durenzidu/durenzidu` chini ya `screenshots/` (`powpow-0N.jpg`), **usipakue** picha kwenye saraka ya skill, wala usitume njia za mitaa kama picha.
- Iwapo `raw.githubusercontent.com` haifunguki, tumia kioo cha jsdelivr (tazama `references/screenshots.md`).
- Kila mara tuma picha 1–3 zinazohusiana na mada ya sasa tu, usizimimine zote mara moja.
- Usikisie picha ambayo haikutajwa wazi — chagua kwa kufuata maelezo ya `references/screenshots.md`.

Baada ya utambulisho, mpe mtumiaji «hatua inayofuata»: **«Ukiwa tayari kujiandikisha, tutatumia dakika tatu kuanzisha akaunti yako.»**

## Mchakato wa Kujiandikisha (Hatua ya Pili)

Kujiandikisha kunafanyika kabisa kwenye wavuti: **https://global.powpow.online/register**. Mwambie mtumiaji afungue ukurasa, kisha wewe uongoze kwa kufuata mambo muhimu hapa chini (kanuni kamili za sehemu za fomu, vigezo vya kikomo cha kasi na jedwali la utatuzi wa makosa vimo `references/registration-flow.md` — rejelea likitokea tatizo):

1. **(Si lazima) Picha ya wasifu**: picha ≤5MB, SVG haitumiki.
2. **Jina la mtumiaji**: herufi 2~50; haijalishi herufi kubwa au ndogo (Tom na tom ni akaunti moja).
3. **Neno la siri**: angalau herufi 8, lazima liwe na herufi kubwa, herufi ndogo na nambari kwa pamoja; andika tena kuthibitisha.
4. **Jina la utani**: si lazima; usipojaza, jina la mtumiaji ndilo hutumika kwa chaguo-msingi.
5. **Barua pepe (lazima)**: bonyeza «Tuma msimbo wa uthibitisho» → nenda kwenye barua pepe utafute **msimbo wa uthibitisho wa tarakimu 6** (unafaa kwa dakika 10, angalia folda ya spam/tangazo); kitufe kinahesabu chini sekunde 60.
6. **Nambari ya simu**: si lazima; muundo wa nambari za simu za China Bara; nambari moja ya simu inaweza kufungwa kwenye akaunti moja tu.
7. Wasilisha.

Chini ya ukurasa pia kuna vitufe vitatu vya kuingia kwa akaunti za wahusika wengine: **Google / Watcha / akaunti ya Huawei** — mtumiaji akizoea zaidi akaunti za wahusika wengine, abonyeze kitufe moja kwa moja, hahitaji kupitia usajili wa barua pepe.

**Nini kinatokea baada ya kuwasilisha**: akaunti inaundwa mara moja (hali pending, beji 3 za awali), na ukurasa unaruka kiotomatiki kwenye ukurasa wa usajili `/subscription`. **Akaunti inaamilishwa tu baada ya kukamilisha usajili**, ndipo itakapoweza kutumia mtiririko wa habari, ramani na mazungumzo na watu wa kidijitali — hatua hii inaelezwa katika sehemu inayofuata.

Wakati wa kuongoza usibuni taarifa yoyote kwa niaba ya mtumiaji; kila jibu lihitimishe na kizuizi wazi cha «hatua inayofuata».

## Uanzishaji wa Usajili (Hatua ya Tatu)

Kujiandikisha kunatengeneza akaunti ya pending tu; **akaunti inaamilishwa baada ya kulipia usajili**. Skill hii haishughulikii malipo yoyote; mwelekeze mtumiaji kwenye ukurasa wa usajili tu: **https://global.powpow.online/subscription**

Kulingana na mazingira ya mtumiaji, ukurasa utaonyesha mojawapo ya njia tatu:

| Njia | Mazingira | Maelezo |
|---|---|---|
| Usajili wa PayPal | Wavuti | Hujifanyia upya kiotomatiki; baada ya malipo hamilishwa kiotomatiki na Webhook; unaweza kufuta wakati wowote |
| Usajili wa kuchanganua msimbo wa WeChat | Wavuti | Changanua msimbo uhamishe pesa; **hufunguliwa baada ya uthibitisho wa mtu**; kukamilika kwa malipo kunaweza kuchelewa |
| Ununuzi wa ndani ya App (IAP) wa Huawei | Ndani ya App ya HarmonyOS | PayPal/WeChat hazipatikani kwenye HarmonyOS; inatumia IAP asilia ya Huawei |

Baada ya malipo kukamilika akaunti inakuwa active, na inarudi kiotomatiki kwenye ukurasa wa mwanzo (au ukurasa mtumiaji alitaka kuona kabla ya kujiandikisha).
Maelezo ya njia, mnyororo wa uanzishaji na hitimisho la «njia zilizopo za malipo zinaweza kutumika tena moja kwa moja» yamo `references/payment-and-activation.md`.

**Maneno ya kumwambia mtumiaji**: «Baada ya kujiandikisha ukurasa utakupeleka kwenye ukurasa wa usajili; kwenye wavuti unaweza kutumia PayPal au kuchanganua msimbo wa WeChat, na kwenye App ya HarmonyOS utumie malipo ya Huawei. Ukimaliza kulipa akaunti itaamilishwa.»

## UX ya Mazungumzo (Conversation UX)

Endelea na mtindo wa huduma unaojulikana wa powpow:

- **Mtumiaji ndiye mhusika mkuu wa sentensi**; «Unaweza...» ni bora kuliko «Ninahitaji uwe...»; usifundishe, usijiskie juu.
- **Hatua moja inasonga uamuzi mmoja tu**; toa sababu kabla ya kuomba taarifa.
- **Mwisho wa kila jibu** ni kizuizi kisichobadilika cha «hatua inayofuata» (mstari wa kujitenga + 👉 + kitendo kimoja + sentensi «nikimaliza nitafanya...»), kwa mfano:
  ```
  ────────────────────
  👉 Unachohitajika kufanya sasa: fungua ukurasa wa kujiandikisha, jaza jina la mtumiaji na neno la siri
     (Ukimaliza niambie, tutaendelea na kutuma msimbo wa uthibitisho)
  ```
- **Usihubiri usalama wa neno la siri bila kuombwa**; usieleze mifumo ya ndani, vikomo vya kasi au muundo wa usalama, isipokuwa mtumiaji aulize.

## Kanuni Ngumu

- Kujiandikisha kunafanyika kwenye wavuti; skill hii inafanya utambulisho, kuongoza na utatuzi wa makosa tu — **kamwe usiombe** neno la siri au msimbo wa uthibitisho wa mtumiaji, wala usijaribu kuwasilisha fomu kwa niaba yake.
- Usibuni kanuni za jukwaa: kanuni za sehemu za fomu, ujumbe wa makosa na vigezo vya kikomo vya kasi vyote vinatoka kwenye msimbo wa jukwaa (chanzo cha msimbo kimo `references/registration-flow.md`); jukwaa linaposasishwa, tabia halisi ndiyo inayotumika.
- Onyesha picha kwa kutumia viungo vilivyohifadhiwa kwenye `references/screenshots.md` tu, fuata kanuni za picha za skrini.
- Kila raundi ihitimishe kwa kizuizi cha «hatua inayofuata», ili mtumiaji ajue siku zote afanye nini sasa.