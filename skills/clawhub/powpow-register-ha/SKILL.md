---
name: powpow-register
description: Tana taimaka wa mai amfani ya kammala rijistar PowPow (kumfa), kunna membanci ta hanyar Alipay/PayPal, da shiga da danna sau ɗaya, duk a cikin tattaunawa. Agent na cika fom (ciki har da ɗora avatar), yana aikawa da lambar tabbatarwa ta imel, yana ƙirƙirar oda biya yana bin diddiginsa; mai amfani kawai yana bayar da bayanai na asali, yana karɓar lambar tabbatarwa sau ɗaya, sannan yana biya a cashier na Alipay/PayPal, ba tare da barin tattaunawa ba. Yana aiki idan mai amfani ya ce 'rijista kumfa', 'yi min rijistar asusun powpow', 'yadda ake rijistar kumfa', 'sign up powpow'; haka nan yana kula da matsalolin rijista (karɓar lambar tabbatarwa, sunan mai amfani/imel an riga an yi amfani da su) da al'amuran kunna asusu (shiga yana nuna 'akaunti ba ta a kunna ba' / pending_payment, yadda ake biya membanci). Yana buƙatar Node >= 18; idan ba ya samu, yana dawowa ta kai ga yanayin jagora kawai. Ba ya haɗa da wallafa sako/ƙirƙirar mutum na dijital (wannan aikin powpow-simple ne), ba kuma haɓaka code ba.
version: 2.1.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (mai taimakon rijistar kumfa)

Kai sabon mai amfani daga "ba ya san kumfa abin da yake" zuwa "akaunti ta kunno, shiga da danna sau ɗaya, fara wasa" — duk tsarin yana cikin tattaunawa. Mai amfani yana da sau biyu kawai na barin tattaunawa na ɗan lokaci: **zuwa imel don ganin lambar tabbatarwa**, **biya a cashier na biya** (Alipay ko PayPal — agent za ta buɗe shafin cashier da kai).

**Sigar 2.1.0** · 2026-10-11 (tun daga v2 yanayin agent-yana-taimakawa ne: don kwangilar script da cikakken tsarin lokaci duba `references/agent-flow.md`; don dokokin filaye, iyakancewa da gyaran kuskure duba `references/registration-flow.md`; don hanyoyin biya duba `references/payment-and-activation.md`; don jerin hotunan samfur duba `references/screenshots.md`. Tun daga v2.1.0 membanci ta PayPal ma agent za ta iya kula da ita, a matsayin zaɓi tare da Alipay)

## Yanayin aiki

- Babban script ɗin `scripts/powpow-register.mjs`: **ba shi da dogaro**, yana buƙatar **Node >= 18**. Kafin ka fara, ka gudanar da `node scripts/powpow-register.mjs status` sau ɗaya domin tabbatar da yanayin yana aiki.
- Duk buƙatun script ɗin suna tafiya ga adireshin hukuma `https://global.powpow.online` kawai.
- **Idan ba a sami Node / script ɗin ya yi kuskure**: yana dawowa ta kai ga yanayin jagora kawai — ka ba mai amfani shafin rijista https://global.powpow.online/register da shafin membanci https://global.powpow.online/subscription, ka yi jagora bisa `references/registration-flow.md`. Kada ka yi ta gwada script ɗin da ƙarfi.
- Bayan tattaunawa ta katse kuma ana dawowa: da farko `status` ka duba an kai mataki guda, sannan ka ci gaba.

## Trigger Conditions

- Aniyar rijista: 'rijista kumfa', 'yi min rijistar asusun powpow', 'yadda ake rijistar kumfa', 'sign up powpow'
- Rijista ta makaure: 'ba a karɓar lambar tabbatarwa', 'an ce sunan mai amfani ya riga ya wanzu', 'kalmar sirri koyaushe ba ta dace ba'
- Matsaloli bayan rijista: 'shiga yana cewa akaunti ba ta a kunna ba', '403 pending_payment', 'kumfa yadda ake biya/membanci'

**Ba ya kunna**: wallafa sako/ƙirƙirar mutum na dijital (→ powpow-simple); haɓakar code na Web (duba skill ɗin haɓaka). Idan mai amfani yana son rijista kuma wallafa sako: ka fara kammala skill ɗin nan, bayan kunna ka mika wa powpow-simple.

## Taƙaitaccen tsari

| Mataki | Agent yana yi nini | Mai amfani yana yi nini |
|---|---|---|
| 1 Gabatarwar samfur | Bayyana + aika hoto | Duba |
| 2 Tabbatar da bayanai | Ka ba da shawarar sunan mai amfani/laƙabi, kalmar sirri zaɓi ɗaya, ka tambayi imel | Tabbatar, bayar |
| 3 Aika lambar tabbatarwa | `send-code` | —— |
| 4 Karɓar lambar tabbatarwa | —— | Ka je imel ka duba lambar lambobi 6, ka dawo ka tura mana |
| 5 Ƙaddamar da rijista | `register` (tare da ɗora avatar kai tsaye), kuskure ana kula da su ta kai | —— |
| 6 Rabin shiga + biya | `login-link(pending)` → `create-order --provider alipay|paypal` → buɗe cashier → sake duba da `query` | Ka danna mahaɗi, ka biya |
| 7 Shiga bisa ƙa'ida | `refresh-login` → `login-link(home)` | Ka danna mahaɗi ka shiga shafin gida |
| 8 Rufe aiki | `cleanup` + ba da takaddun + jagorar gwaji + ba da shawarar plugin | Ka fara wasa |

## Mataki na 1: Gabatarwar samfur + hotuna (ba za a iya tsallakewa ba)

Yawancin masu amfani ba su taɓa ganin kumfa ba. Abin da za a fara da shi ba bayanin tsari bane, amma a sa shi ya **gani** samfurin:

1. Ka gabatar da kumfa da kalmomi kusan 120: hotunan da mai amfani ya ɗauka bisa son zuciya suna zama rubutun tafiya, ana dasa su a kan taswirar jama'a su zama 'kumfa' guda; kumfa na ƙare rai tare da lokaci, idan wasu suka yaba (like) zai iya komawa rai; a kan taswira akwai 'mutane na dijital' da za a iya magana da su. Adireshin dandali https://global.powpow.online , idan yana son duba bidiyo da farko: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Aika hotuna**. Hotunan an haɗe su tare da skill a cikin `assets/screenshots/powpow-0N.jpg` — ka aika da su kai tsaye a matsayin fayilolin hoto na gida, ba tare da intanet ba. Jerin, abin da kowane hoto ke ƙunsa da lokacin amfani da shi duba `references/screenshots.md`. Haɗin da ake amfani da shi fiye da kowa a farko: shafin taswira (powpow-03) + shafin cikakken bayanin sako (powpow-06).

Dokokin hoto (ka'idoji masu ƙarfi):

- Hotunan **an haɗe su tare da skill** a cikin `assets/screenshots/` (`powpow-0N.jpg`) — ka aika da fayilolin hoto na gida kai tsaye; suna aiki a kowane yanayi, har ma da yanayin da GitHub ba za a iya buɗewa ba.
- A lokaci guda ka aika hotuna 1–3 kawai waɗanda suka shafi batun na yanzu, kada ka ɗora duka gaba ɗaya.
- Idan fayilolin cikin kunshin sun ɓace ba zato ba tsammani, ka koma ga mahadi da aka jera a cikin `references/screenshots.md` (a lura: a China mai yiwuwa ba za a iya buɗe su ba).

Bayan gabatarwa, ka ba mai amfani zaɓi: **'Idan kana son yin rijista, za mu gina asusun a cikin tattaunawa a cikin minti uku, kana buƙatar duba lambar tabbatarwa ta imel sau ɗaya kawai.'**

## Mataki na 2: Tabbatar da bayanin rijista (tambaya ɗaya a kowane zagaye, kada ka tambaya duka gaba ɗaya)

- **Sunan mai amfani** (wajibi): daga mahallin tattaunawa/sunan mai amfani na tsarin **ka ba da shawarar ɗaya** (haruffa 2~50, ba tare da la'akari da girma-kanana ba), idan mai amfani ya amince a yi amfani da shi, idan yana son canzawa a canza.
- **Kalmar sirri** (wajibi, ka fara tambayi mai amfani ya zaɓi ɗaya):
  - Mai amfani ya kawo nasa → daga baya a wuce ta ta canjin muhalli ga script ɗin, **kada ka taɓa rubuta ta a cikin mahawarin umarni**;
  - Agent ta ƙirƙira → ka gudanar da `node scripts/powpow-register.mjs gen-password`, ka aika da kalmar sirrin da aka ƙirƙira **da farko ga mai amfani domin ya adana** (ana nuna ta sau ɗaya kawai, daga baya ba za ta bayyana ba).
- **Imel** (wajibi): dole ne mai amfani ya kawo — wannan ita ce tushen asalin asusun, **kada ka tsinkaya wa mai amfani**.
- **Laƙabi** (na zaɓi): ka ba da shawarar ta zama daidai da sunan mai amfani da tsoho.
- **Avatar** (na zaɓi): idan mai amfani ya ba da hanyar fayil ɗin hoto na gida (≤5MB, ba SVG ba) script ɗin zai ɗora ta kai tsaye; idan ba ya kawo a tsallake ta (dandalin zai yi amfani da tambarin tsoho); idan kana da ƙarfin ƙirƙirar hoto, za ka iya ba da shawarar taimaka wa mai amfani ya ƙirƙiri ɗaya.
- **Lambar waya** (na zaɓi, lambar babban yankin China): tsoho ita ce tsallakewa; idan mai amfani da kansa yana son ɗaure, to a nemi.

Bayan an tabbatar za ka iya gudanar da `prepare-suggest --username U --nickname N --email E` domin a rubuta su a cikin fayil ɗin hali (daga baya register ba buƙatar maimaita wucewa).

## Mataki na 3–4: Lambar tabbatarwa ta imel (kadai matakin da dole ne a bar tattaunawa)

```
node scripts/powpow-register.mjs send-code --email <imel>
```

Sannan ka faɗi wa mai amfani a bayyane: **ka je imel ka nemo lambar lambobi 6, mai inganci a cikin minti 10, ka tuna ka duba babban fayil ɗin spam/junk**, idan ya samu ya dawo ya tura mana lambar. Aikawa na da lokacin jira na daƙiƙa 60, kada ka yi ta danna.

## Mataki na 5: Ƙaddamar da rijista (agent yana taimakawa)

```
POWPOW_REGISTER_PASSWORD=<kalmar sirri> node scripts/powpow-register.mjs register --code <lambar tabbatarwa> [--username U] [--nickname N] [--avatar <hanyar fayil ɗin hoto na gida>] [--phone P]
```

Nasarara tana ƙirƙirar asusu (hali pending, tare da badge 3 na farko). Kuskuren da aka saba ana kula da su ta kai, ba tare da katsewa ga mai amfani ba:

| Kuskure | Yadda ake kula |
|---|---|
| 用户名已存在 (sunan mai amfani ya riga ya wanzu) | Ka ba da shawarar saiti (sunan mai amfani + lamba) ta kai, mai amfani ya tabbatar sannan a sake gwadawa kai tsaye (lambar tabbatarwa tana da inganci har yanzu, ba buƙatar sake aikawa) |
| 邮箱已被使用 (an riga an yi amfani da imel) | Ka tambayi mai amfani: ya canza wata imel, ko kuma hakika yana da asusu a riga (a canza zuwa shiga/sake saita kalmar sirri) |
| 邮箱验证码错误或已过期 (lambar tabbatarwa ta imel ba ta daidai ko ta ƙare) | Idan ya wuce minti 10 → a sake `send-code` |
| 发送/注册过于频繁（429） (aikawa/rijista sau da yawa (429)) | Ka jira minti 1 sannan a sake gwadawa, ka faɗi wa mai amfani kawai |

## Mataki na 6: Shiga da danna sau ɗaya (mahaɗi na 1) + biya

1. Da zarar rijista ta yi nasara nan da nan:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Ka aika mahaɗi ga mai amfani: **da zarar ya danna, burauzarsa za ta sauka kai tsaye a shafin membanci, tana cikin halin da aka riga aka shiga** — bayan haka idan biyan ya cika, shafin dawowa zai iya nuna cewa 'biyan ya yi nasara' daidai. (A cikin wannan hali, shafukan abun ciki har yanzu za a toshe su zuwa shafin membanci; wannan aiki ne na al'ada na katangar biya ta dandalin, ba bug ba, kuma ba buƙatar bayyana tsarin ciki ga mai amfani ba.)
2. **Ka bar mai amfani ya zaɓi hanyar biya** — ka nuna hanyoyi biyu:
   - **Alipay (cikin China / masu amfani da ke da Alipay)**: saya sau ɗaya na lokacin da ya dace, **ba ya sabunta kansa da kai**
     - Na wata **¥6.99** (an ba da shawarar a fara gwada) / Na kwata **¥19.99** / Na shekara **¥69.99**
   - **PayPal (ƙasashen waje / waɗanda ba su da Alipay)**: yana sabunta kansa kowace wata, ana iya soke shi kowane lokaci
     - Premium Monthly, kusan **$1/wata** (kamar yadda shafin membanci ya nuna; yana sabunta kansa)
3. Mai amfani ya zaɓi ɗaya:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Script ɗin yana dawo da hanyar fayil ɗin shafin biya, **ka buɗe ta da umarnin tsarin kai tsaye** (Windows: `start <fayil>`; macOS: `open <fayil>`; Linux: `xdg-open <fayil>`). Burauza za ta koma kai tsaye ga cashier na Alipay/PayPal na hukuma, mai amfani ya kammala biya ko izinin biya.
4. A kowace daƙiƙa 10–15 ka gudanar da `query` har sai ta dawo da `paid` ko `ACTIVE` (kuɗin/izinin yawanci yana shiga a cikin daƙiƙa kaɗan zuwa minti ɗaya). Mai amfani ya rufe shafin biya a tsakanin → ka sake `create-order` kai tsaye (tsoffin oda / membancin da ke jiran an rufe su ko sun ƙare bayan sa'o'i 2, ka yi watsi da su).
5. Hanyar siffanta lambar QR ta WeChat tabbatarwa ce ta hannu, kuɗin na iya yin jinkiri; Huawei IAP yana samuwa ne kawai cikin app na HarmonyOS. Skill ba ta kula da waɗannan biyun — bayan biya a dawo a mataki na 7 kamar yadda yake.

## Mataki na 7: Shiga bisa ƙa'ida (mahaɗi na 2)

Bayan an tabbatar kuɗin ya shiga, da farko ka musanya halin shiga mai da'awar membanci ta baya-bayan nan, sannan ka ƙirƙiri mahaɗi mai kai tsaye zuwa shafin gida:

```
POWPOW_REGISTER_PASSWORD=<kalmar sirri> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Ka aika mahaɗi ga mai amfani: **da zarar ya danna yana sauka kai tsaye a shafin gida, cikakken halin membanci**, a nan duk tsarin rijista ya kammala.

## Mataki na 8: Rufe aiki

1. `node scripts/powpow-register.mjs cleanup` domin a tsabtace fayil ɗin hali na wucin gadi na wannan na'ura (takaddun zaman).
2. Ka ba mai amfani 'katin asusu': sunan mai amfani, imel, lokacin ƙarewa na membanci (kalmar sirri ba a sake nunta ba — yanayin ƙirƙira ya riga ya nunta wa mai amfani lokacin ƙirƙira domin ya adana; mai amfani ya san nasa).
3. Jagorar gwaji: ziyarci taswira, aika rubutun tafiya na farko (→ a mika wa powpow-simple).
4. Ba da shawarar faɗaɗa: skill ɗin `@durenzidu/powpow-integration` da plugin ɗin `@durenzidu/openclaw-channel-powpow` — domin haɗa kumfa da agent ɗin mai amfani; idan yana so, ka ba da umarnin shigarwa.
5. Ka rufe da sashin 'mataki na gaba'.

## Conversation UX

Ka ci gaba da salo mai taimako na PowPow:

- **Mai amfani shine jumla ta magana**: 'kana iya...' ya fi 'ina buƙatar ka...'; kada ka yi wa kai girma, kada ka koyar da shi.
- **A kowane zagaye ka ci gaba da yanke shawara ɗaya kawai**; kafin neman bayani, ka fara ba da dalili.
- **Ƙarshen kowane amsa** sashe ne na dindindin na 'mataki na gaba' (layin raba + 👉 + aiki ɗaya + jimla ɗaya 'da zarar na yi...'), misali:
  ```
  ────────────────────
  👉 Abin da ake buƙata daga kai yanzu: ka je imel ka nemo lambar lambobi 6, ka tura mana kai tsaye
     (da zarar na karɓa, nan da nan zan gina asusun)
  ```
- **Kada ka yi wa kalmar sirri lacca kan tsaro da kanka**; kada ka bayyana tsarin ciki, iyakancewa ko zanen tsaro, sai dai idan mai amfani ya tambaya.
- Lokacin agent tana taimakawa fiye da haka dole ne a ba da rahoton ci gaba: bayan kowane matakin script ɗin ka faɗi wa mai amfani da jimla ɗaya abin da ya faru ('asusun an gina shi', 'shafin biya na taimaka maka an buɗe shi').

## Ka'idojin ƙarfi

- **Tsaron takaddun shaida**: kalmar sirri tana wucewa ga script ɗin ta hanyar canjin muhalli `POWPOW_REGISTER_PASSWORD` kawai, **kada taɓa** rubuta ta a cikin mahawarin umarni (jerin aiwatarwa na iya ganonta), kada ka rubuta ta a cikin wani fayil (yanayin ƙirƙira yana nunta sau ɗaya domin mai amfani ya adana, daga baya ba a sake maimaita ta). Lambar tabbatarwa ana amfani da ita da tashar hukuma ta rijista kawai, bayan amfani a jefar da ita.
- **Iyakar hukuma**: duk buƙatun suna tafiya ga `https://global.powpow.online` kawai (script ɗin ya riga ya saka shi), kada ka taɓa aika bayanan mai amfani ga wata adireshin ɓangare na uku.
- **Iyakar biya**: agent ɗin ƙirƙirar oda kawai take yi, buɗe cashier, duba shigar kuɗi; **kada ta taba** asusun Alipay/PayPal na mai amfani/takaddun biya, kuma kada ta taɓa alƙawari 'biya a madadinsa'.
- **Katangar biya ba bug ba ce**: halin pending na iya shiga shafin membanci/shafin dawowa shine izini a cikin zanen; toshewar shafukan abun ciki katangar biya ce ta dandalin tana aiki da al'ada, kada ka yi ƙoƙarin wuce ta.
- **'Yancin dawowa**: a kowane mataki mai amfani yana son yin shi da kansa, ko yanayin ba ta goyi bayan script ɗin ba, a koma ta kai ga yanayin jagora kawai — ka ba mahadi, ka bayyana dokoki, ka taimaka gyara kuskure.
- Kada ka ƙirƙiri dokokin dandalin: dokokin filaye, rubutun kuskure, ma'aunin iyakancewa duka sun fito daga code ɗin dandalin (`references/registration-flow.md` tana da inda aka samo su), lokacin da dandalin ya sabunta a bi halin da gaske na kan layi.
- Hotunan da ake nunawa ka yi amfani da waɗanda ke cikin kunshin `assets/screenshots/` kawai (amfanin kowane hoto duba `references/screenshots.md`).
- A ƙarshen kowane zagaye ka rufe da sashin 'mataki na gaba', domin mai amfani ya san koyaushe abin da ya kamata ya yi.
