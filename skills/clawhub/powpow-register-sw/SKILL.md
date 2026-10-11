---
name: powpow-register
description: Kusaidia mtumiaji kukamilisha usajili wa PowPow (Povu), uwezeshaji wa usajili kupitia Alipay, na ingia kwa kubofya mara moja ndani ya mazungumzo. Agent hujaza fomu (pamoja na picha ya wasifu), hutuma nambari ya uthibitisho ya barua pepe, huunda agizo la malipo na kufuatilia malipo, mtumiaji hutoa tu maelezo ya msingi, kupokea nambari ya uthibitisho mara moja, na kulipa kwenye cashier ya Alipay, bila kuondoka mazungumzoni. Inafanya kazi wakati mtumiaji anaposema 'sajili Povu', 'sajili akaunti ya powpow', 'jinsi ya kusajili powpow', 'sign up powpow'. Pia inashughulikia matatizo ya usajili (kutopokea nambari ya uthibitisho, jina la mtumiaji/barua pepe imeshachukuliwa) na masuala ya uwezeshaji (ingia inashow 'akaunti haijawa hiyari' / pending_payment, jinsi ya kusajili kulipa). Inahitaji Node >= 18; ikipatikana haipatikani inarudi kiotomatiki kwenye mtindo wa mwongozo mtupu. Haijumuishi kutuma chapisho/kutengeneza mtu wa kidijitali (hicho ni kazi ya powpow-simple), wala haijumuishi maendeleo ya msimbo.
version: 2.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (msaidizi wa usajili wa Povu)

Kuleta mtumiaji mpya kutoka "hajui Povu ni nini" hadi "akaunti imewezeshwa, ingia kwa kubofya mara moja, anze kucheza" — mchakato mzima unafanyika ndani ya mazungumzo. Mtumiaji ana mara mbili tu za kutoka mazungumzoni kwa muda: **kwenda kwenye barua pepe kuona nambari ya uthibitisho**, **kulipa kwenye cashier ya Alipay** (agent itafungua ukurasa wa cashier kiotomatiki).

**Toleo 2.0.1** · 2026-10-08 (tangu v2 ni mtindo wa agent-kusaidia: mkataba wa hati na mlolongo kamili angalia `references/agent-flow.md`; sheria za sehemu, vizuizi, na utatuzi wa makosa angalia `references/registration-flow.md`; njia za malipo angalia `references/payment-and-activation.md`; orodha ya picha za bidhaa angalia `references/screenshots.md`. Tangu v2.0.1 picha za bidhaa zimefungwa pamoja na skill katika `assets/screenshots/`, hazitegemei tena hifadhi ya picha ya nje)

## Mazingira ya kukimbia

- Hati kuu `scripts/powpow-register.mjs`: **haina tegemezi**, inahitaji **Node >= 18**. Kabla ya kuanza endesha mara moja `node scripts/powpow-register.mjs status` kuwa na uhakika mazingira yanafaa.
- Maombi yote ya hati yanaenda tu kwenye kikoa rasmi `https://global.powpow.online`.
- **Usipokuwa na Node / hati inapoleta hitilafu**: inarudi kiotomatiki kwenye mtindo wa mwongozo mtupu — upe ukurasa wa usajili https://global.powpow.online/register na ukurasa wa usajili wa malipo https://global.powpow.online/subscription kwa mtumiaji, uongoze kwa kufuata `references/registration-flow.md`. Usijaribu hati mara kwa mara kwa nguvu.
- Baada ya mazungumzo kukatika na kurudisha: kwanza `status` kuona mchakato umefika hatua gani, kisha endelea.

## Trigger Conditions

- Nia ya usajili: "sajili Povu", "sajili akaunti ya powpow", "jinsi ya kusajili powpow", "sign up powpow"
- Usajili umekwama: "hauskii nambari ya uthibitisho", "jina la mtumiaji limesemwa kuwa limeshakuwepo", "nenosiri haifai kila wakati"
- Matatizo baada ya usajili: "ingia inashow akaunti haijawa hiyari", "403 pending_payment", "jinsi ya kulipa/kusajili PowPow"

**Haifanyi trigger**: kutuma chapisho/kuunda mtu wa kidijitali (→ powpow-simple); maendeleo ya msimbo wa wavuti (tazama skill ya maendeleo). Mtumiaji anapotaka kusajili na pia kutuma chapisho: kwanza maliza skill hii, baada ya uwezeshaji peleka kwa powpow-simple.

## Muhtasari wa mtiririko

| Hatua | Agent anafanya nini | Mtumiaji anafanya nini |
|---|---|---|
| 1 Utangulizi wa bidhaa | Eleza + tuma picha | Tazama |
| 2 Uthibitisho wa maelezo | Pendekeza jina la mtumiaji/jina la kirafiki, nenosiri uchague moja, uliza barua pepe | Thibitisha, toa |
| 3 Tuma nambari ya uthibitisho | `send-code` | —— |
| 4 Soma nambari ya uthibitisho | —— | Nenda barua pepe tazama nambari ya tarakimu 6, rudi uitume |
| 5 Wasilisha usajili | `register` (pamoja na picha ya wasifu moja kwa moja), shughulikia makosa kiotomatiki | —— |
| 6 Nusu-login + malipo | `login-link(pending)` → `create-order` → fungua cashier → hoji `query` | Bofya kiungo, lipa |
| 7 Ingia rasmi | `refresh-login` → `login-link(home)` | Bofya kiungo uingie ukurasa wa nyumbani |
| 8 Kumalizia | `cleanup` + toa utambulisho + ongoza uzoefu + pendekeza programu-jalizi | Anza kucheza |

## Hatua ya 1: Utangulizi wa bidhaa + picha (haipitiwi)

Watumiaji wengi hawajawahi kuona Povu. Jambo la kwanza si kueleza mtiririko, bali kumfanya **aone** bidhaa:

1. Eleza Povu kwa maneno ya takriban 120: picha ulizoipiga kirahisi zinageuka kuwa safari ya kusafiri, zimepachikwa kwenye ramani ya wazi kuwa "povu" moja; povu huzidi kupoa kwa wakati, watu wengine wakipenda huufufua; kwenye ramani pia kuna "watu wa kidijitali" unaweza kuongea nao. Anwani ya jukwaa https://global.powpow.online, ukiwa unataka kutazama video kwanza: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Tuma picha**. Picha zimefungwa pamoja na skill katika `assets/screenshots/powpow-0N.jpg` — tuma moja kwa moja kama faili ya picha ya ndani, huhitaji mtandao. Orodha, yaliyomo ya kila picha na wakati wa kuzitumia angalia `references/screenshots.md`. Mchanganyiko unaotumika zaidi kwa mwanzo: ukurasa wa ramani (powpow-03) + ukurasa wa maelezo ya chapisho (powpow-06).

Sheria za picha (kanuni ngumu):

- Picha **zimefungwa pamoja na skill** katika `assets/screenshots/` (`powpow-0N.jpg`) — tuma tu faili ya picha ya ndani; inafaa katika mazingira yoyote, hata mazingira ambayo GitHub haifunguliwi.
- Tuma mara moja tu picha 1–3 zinazohusiana na mada ya sasa, usizipake zote mara moja.
- Ikiwa faili za ndani zinakosekana kwa bahati mbaya, rudi kwenye viungo vya hifadhi vilivyoorodheshwa katika `references/screenshots.md` (tahadhari: nchini China vinaweza kutofunguliwa).

Baada ya kueleza, mruhusu mtumiaji achague: **"Ukitaka kusajili, tutajenga akaunti mazungumzoni kwa dakika tatu, unahitaji tu kutazama nambari ya uthibitisho ya barua pepe mara moja."**

## Hatua ya 2: Thibitisha maelezo ya usajili (uliza swali moja kwa wakati, usziulize zote mara moja)

- **Jina la mtumiaji** (inahitajika): kutoka muktadha wa mazungumzo/jina la mtumiaji wa mfumo **pendekeza moja** (herufi 2~50, bila kujali herufi kubwa ndogo), mtumiaji akipiga kuni atumie, akitaka kubadilisha abadilishe.
- **Nenosiri** (inahitajika, uliza mtumiaji uchague moja):
  - Mtumiaji mwenyewe atoe → baadaye litumie kupitia kigezo cha mazingira kwa hati, **kamwe usiiandike kwenye vigezo vya amri**;
  - Agent itengeneze → endesha `node scripts/powpow-register.mjs gen-password`, utume nenosiri lililotengenezwa **mara moja kwa mtumiaji aliweke** (inaonyeshwa mara moja tu, baadaye haitatokea tena).
- **Barua pepe** (inahitajika): lazima mtumiaji atoe — hii ndiyo nanga ya utambulisho wa akaunti, **usimwaghani mtumiaji**.
- **Jina la kirafiki** (hiari): pendekeza chaguo-msingi sawa na jina la mtumiaji.
- **Picha ya wasifu** (hiari): mtumiaji akitoa njia ya faili ya picha ya ndani (<=5MB, sio SVG) hati itaipakia moja kwa moja; usipotoa aache (jukwaa litumie nembo ya chaguo-msingi); ukiwa na uwezo wa kutengeneza picha, unaweza kupendekeza kumsaidia mtumiaji kutengeneza moja.
- **Nambari ya simu** (hiari, nambari ya bara): chaguo-msingi ache, mtumiaji akipenda kufunga atoe.

Baada ya kuthibitisha unaweza kuendesha `prepare-suggest --username U --nickname N --email E` kuandika kwenye faili ya hali (baadaye register haitaki kurudia kutuma).

## Hatua ya 3–4: Nambari ya uthibitisho ya barua pepe (sehemu pekee inayohitaji kuondoka mazungumzoni)

```
node scripts/powpow-register.mjs send-code --email <barua pepe>
```

Kisha mwambie wazi mtumiaji: **nenda barua pepe tafuta nambari ya tarakimu 6, inayofaa kwa dakika 10, kumbuka kuangalia folda ya barua taka/utangazaji**, ukipata rudi uitume. Kutuma kuna muda wa kupoeza sekunde 60, usibofye mara kwa mara.

## Hatua ya 5: Wasilisha usajili (agent husaidia)

```
POWPOW_REGISTER_PASSWORD=<nenosiri> node scripts/powpow-register.mjs register --code <nambari ya uthibitisho> [--username U] [--nickname N] [--avatar <njia ya faili ya picha ya ndani>] [--phone P]
```

Mafanikio yaunda akaunti (hali ya pending, pamoja na beji 3 za mwanzo). Makosa ya kawaida yashughulikiwa kiotomatiki, hayakatishi mtumiaji:

| Kosa | Shughulikia |
|---|---|
| 用户名已存在 (jina la mtumiaji limeshakuwepo) | Pendekeza toleo (jina la mtumiaji + nambari) kiotomatiki, mtumiaji athibitisha halafu jaribu tena moja kwa moja (nambari ya uthibitisho bado inafaa, hahitaji kutuma tena) |
| 邮箱已被使用 (barua pepe imeshatumiwa) | Uliza mtumiaji: badilisha barua pepe nyingine, au labda tayari ana akaunti (badili kwenda kuingia/urejeshaji nenosiri) |
| 邮箱验证码错误或已过期 (nambari ya uthibitisho ya barua pepe ni mbaya au imeisha muda) | Ikipita dakika 10 → tuma tena `send-code` |
| 发送/注册过于频繁（429） (kutuma/usajili mara nyingi mno (429)) | Subiri dakika 1 kisha jaribu tena, mwambie mtumiaji tu |

## Hatua ya 6: Ingia kwa kubofya mara moja (kiungo 1) + malipo

1. Baada ya usajili kufanikiwa mara moja:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Tuma kiungo kwa mtumiaji: **baada ya kubofya, kivinjari chako kinaingia moja kwa moja kwenye ukurasa wa usajili wa malipo, tayari iko hali ya imeingia** — baadaye malipo yanapofanikiwa ukurasa wa kurudi unaweza kuonyesha kwa usahihi "malipo yamefanikiwa". (Katika hali hii kurasa za maudhui bado zitazuiliwa hadi ukurasa wa usajili wa malipo, hii ni kazi ya kawaida ya ukuta wa malipo wa jukwaa, sio bug, wala hujaelezei mtumiaji utaratibu wa ndani.)
2. Chagua mpango mmoja kati ya tatu, uonyeshe bei:
   - Mwezi **¥6.99** (pendekeza ujaribu kwanza) / Robo mwaka **¥19.99** / Mwaka **¥69.99** —— Alipay ununuzi wa mara moja wa muda unaolingana, **haushamiri otomatiki**
3. Mtumiaji amepochagua:
   ```
   node scripts/powpow-register.mjs create-order --package monthly
   ```
   Hati inarudisha njia ya faili ya ukurasa wa malipo, **ifungue kwa amri ya mfumo moja kwa moja** (Windows: `start <faili>`; macOS: `open <faili>`; Linux: `xdg-open <faili>`). Kivinjari kitaelekea moja kwa moja kwenye cashier rasmi ya Alipay, mtumiaji asome msimbo au ingia kwenye Alipay kulipa.
4. Kila sekunde 10–15 endesha `query` hadi irudishe `paid` (malipo hufika kwa kawaida katika sekunde chache hadi dakika moja). Mtumiaji akifunga ukurasa wa malipo katikati → endesha tu tena `create-order` (agizo la zamani hufungwa kiotomatiki baada ya saa 2, usijali).
5. Mtumiaji wa nje/asiyekuwa na Alipay: ongoza kutumia njia ya PayPal kwenye ukurasa wa usajili wa malipo (skill haiwasiliani, toa tu mwongozo); njia ya usome msimbo wa WeChat ni ya uthibitisho wa mtu, malipo hufika kwa kuchelewa. Baada ya kulipa rudi hatua ya 7 vile vile.

## Hatua ya 7: Ingia rasmi (kiungo 2)

Baada ya malipo kuthibitishwa, kwanza badilisha hali ya ingia iliyo na tamko jipya la usajili, kisha tengeneza kiungo cha moja kwa moja cha ukurasa wa nyumbani:

```
POWPOW_REGISTER_PASSWORD=<nenosiri> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Tuma kiungo kwa mtumiaji: **baada ya kubofya inaingia moja kwa moja kwenye ukurasa wa nyumbani, hali kamili ya mwanachama**, hapa usajili mzima umemalizika.

## Hatua ya 8: Kumalizia

1. `node scripts/powpow-register.mjs cleanup` kusafisha faili ya hali ya muda ya mashine hii (kitambulisho cha kikao).
2. Mpe mtumiaji "kadi ya akaunti": jina la mtumiaji, barua pepe, muda wa mwanachama kuisha (nenosiri haionyeshwi tena — mtindo wa kutengeneza ulimwonyesha mtumiaji alihifadhi wakati wa kutengeneza; mtumiaji mwenyewe anajua ile aliyoiweka).
3. Ongoza uzoefu: tembea ramani, tuma safari yako ya kwanza ya kusafiri (→ peleka kwa powpow-simple).
4. Pendekeza kupanua: skill `@durenzidu/powpow-integration` na programu-jalizi `@durenzidu/openclaw-channel-powpow` — kuunganisha Povu kwenye agent yako mwenyewe; ukitaka ongeza tu amri ya usakinishaji.
5. Malizia kwa sehemu ya "hatua inayofuata".

## Conversation UX

Endeleza sauti ya huduma ya PowPow:

- **Mtumiaji ndiye mada ya sentensi**, "unaweza..." ni bora kuliko "ninahitaji wewe..."; usifundishe, usijinyanyue.
- **Songa mbele kwa uamuzi mmoja kwa raundi**; kabla ya kuomba maelezo toa sababu.
- **Mwisho wa kila jibu** ni sehemu ya kudumu ya "hatua inayofuata" (mlalo wa kutenganisha + 👉 + kitendo kimoja + sentensi moja ya "nitakapofanya..."), kwa mfano:
  ```
  ────────────────────
  👉 Unachohitaji sasa: nenda barua pepe tafuta nambari ya tarakimu 6, uitume moja kwa moja
     (nitakapopokea nitajenga akaunti mara moja)
  ```
- **Usifanye mafunzo ya usalama kwa nenosiri kwa nafsi yako**; usieleze utaratibu wa ndani, vizuizi, au muundo wa usalama, isipokuwa mtumiaji aulize.
- Wakati agent inaposaidia, toa taarifa za maendeleo zaidi: baada ya kila hatua ya hati mwambie kwa sentensi moja kilichoendelea (akaunti imejengwa, ukurasa wa malipo umefunguliwa kwa ajili yako).

## Kanuni ngumu

- **Usalama wa kitambulisho**: nenosiri hutumiwa tu kupitia kigezo cha mazingira `POWPOW_REGISTER_PASSWORD` kwa hati, **kamwe** usiiandike kwenye vigezo vya amri (orodha ya mchakato inaonekana), usiiandike kwenye faili yoyote (mtindo wa kutengeneza unaonyesha mara moja ili mtumiaji ahifadhi, baadaye haitajwi tena). Nambari ya uthibitisho hutumiwa tu kwa kiolesura rasmi cha usajili, inapotumika inaachwa.
- **Mpaka rasmi**: maombi yote yanaenda tu kwenye `https://global.powpow.online` (hati imejumuisha tayari), kamwe usitume maelezo ya mtumiaji kwa anwani yoyote ya mtu wa tatu.
- **Mpaka wa malipo**: agent huunda agizo, hufungua cashier, hufuatilia malipo; **kamwe** haigusi akaunti ya Alipay ya mtumiaji / kitambulisho cha malipo, wala haiahidi "kulipa badala yake".
- **Ukuta wa malipo sio bug**: hali ya pending inaweza kuingia ukurasa wa usajili wa malipo / ukurasa wa kurudi ni ruhusa ndani ya muundo; kurasa za maudhui kuzuiliwa ni ukuta wa malipo wa jukwaa unao fanya kazi kwa kawaida, usijaribu kuuzuia.
- **Uhuru wa kurudi nyuma**: hatua yoyote mtumiaji anapotaka kufanya mwenyewe, au mazingira hayasaidii hati, anaweza kurudi wakati wowote kwenye mtindo wa mwongozo mtupu — toa viungo, eleza sheria, saidia kutatua makosa.
- Usitengeneze sheria za jukwaa: sheria za sehemu, maandishi ya makosa, vigezo vya vizuizi vyote vinatoka kwenye msimbo wa jukwaa (`references/registration-flow.md` ina chanzo cha msimbo), sasisho la jukwaa hufuata tabia halisi ya mtandaoni.
- Picha uonyesho tumia tu zile za `assets/screenshots/` zilizofungwa pamoja na skill (matumizi ya kila picha angalia `references/screenshots.md`).
- Kila raundi malizia kwa sehemu ya "hatua inayofuata", ili mtumiaji ajuu kila wakati anachopaswa kufanya.
