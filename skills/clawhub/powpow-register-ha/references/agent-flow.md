# Tsarin agent-yana-taimakawa da kwangilar script — powpow-register

Cikakkun bayanai na aiwatar da matakai a SKILL.md. Duk umarni suke `node scripts/powpow-register.mjs <umarnin-ciki> [mahawari]`, script ɗin **ba shi da dogaro**, yana buƙatar **Node >= 18**, duk buƙatun suna tafiya ga `https://global.powpow.online` kawai.

## Zanen tsaro (me yasa aka zane haka)

| Zane | Dalili |
|---|---|
| Kalmar sirri tana wucewa ta canjin muhalli `POWPOW_REGISTER_PASSWORD` kawai | Mahawarin umarnin aiwatarwa na iya ganuwa ta wasu aiwatarwa na wannan na'ura (fafutukar argv), canjin muhalli a cikin script ɗin ana karantewa ana amfani da shi nan take |
| Kalmar sirri **kada ta rubuta a cikin fayil ɗin hali**, kada ta bayyana a cikin rajistan ayyukan | Fayil ɗin hali na iya zama a kan diski; yanayin ƙirƙira yana nunta sau ɗaya domin mai amfani ya adana |
| Fayil ɗin hali yana cikin babban fayil ɗin wucin gadi na tsarin (`os.tmpdir()/powpow-register-state.json`, 0600) | Yana ɗauke da filaye biyar kawai: email / username / nickname / token / outTradeNo, `cleanup` yana sharewa da danna ɗaya |
| JWT ɗin da agent ta samu ana musanya shi zuwa cookie ɗin burauza ta hanyar gada ta hukuma `me?token=` | Gada ce ta hukuma da dandalin ya zana wa Harmony WebView; tabbatarwa tana duba saitti + lokacin inganci kawai, ba ta ɗaura da sawun na'ura ba, burauzar mai amfani za ta iya amfani da ita |
| Biya yana yin create-order / query / buɗe cashier kawai | Aikin biya da takaddun biya koyaushe suna tsakanin mai amfani da cashier na Alipay na hukuma, agent ba ta shiga ba |

## Jagoran umarni

| Umarni | Mahawari masu mahimmanci | Aiki / lokaci |
|---|---|---|
| `status` | —— | Duba ci gaban tsari (karanta fayil ɗin hali); bayan tattaunawa ta katse ka fara da wannan |
| `gen-password` | —— | Ƙirƙiri kalmar sirri mai ƙarfi ta haruffa 24 (girma-kanana + lambobi), ana nunta a stdout **sau ɗaya kawai** |
| `prepare-suggest` | `--username --nickname --email` | Ka rubuta bayanan da aka tabbatar a cikin fayil ɗin hali (daga baya register ba buƙatar maimaita wucewa) |
| `send-code` | `--email` | Ka haddasa dandalin ya aika lambar lambobi 6 (mai inganci a cikin minti 10, lokacin jira daƙiƙa 60) |
| `register` | `--code` (wajibi); `--username --nickname --avatar --phone` (na zaɓi, idan fayil ɗin hali yana da su ba buƙatar wucewa) | Ka gina asusun pending; kalmar sirri ta `POWPOW_REGISTER_PASSWORD`; bayan nasara JWT ana adanawa cikin fayil ɗin hali ta kai |
| `login-link` | `--target pending` ko `--target home` | Ka ƙirƙiri mahaɗin shiga da danna sau ɗaya (zane mahadi biyu, duba ƙasa) |
| `create-order` | `--package monthly\|quarterly\|yearly` | Ka ƙirƙiri oda Alipay; yana dawo da hanyar fayil ɗin shafin biya + outTradeNo (ana adanawa cikin fayil ɗin hali ta kai) |
| `query` | —— | Duba halin oda `paid / pending / closed / unknown` (outTradeNo ana ɗaukarsa daga fayil ɗin hali), sake duba kowace daƙiƙa 10–15 |
| `refresh-login` | Kalmar sirri ta canjin muhalli | Ka sake shiga ka musanya **JWT sabuwa** (da'awar membanci na canzawa daga NONE zuwa ACTIVE), dole ne a gudanar da ita bayan kuɗin ya shiga |
| `whoami` | —— | Ka yi amfani da token ɗin fayil ɗin hali ka duba halin asusu da membanci (tabbatar da kunna ta yi aiki) |
| `cleanup` | —— | Ka share fayil ɗin hali (dole ne a gudanar da ita a ƙarshe) |

**Wucewa ta canjin muhalli** (kalmar sirri kada ta taɓa umarni):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<kalmar sirri>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<kalmar sirri>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<kalmar sirri> && node scripts/powpow-register.mjs register --code 123456
```

## Tsarin mahadi biyu (zane na asali)

Halin shiga na dandalin cookie ce ta HttpOnly, agent ba za ta iya shuka wa burauza cookie kai tsaye ba; gada ita ce tashar hukuma
`/api/auth/me?token=<JWT>&redirect=<hanyar-ciki>`: tabbatarwa da saitti → mai amfani na pending ana gina masa
session ta kai → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / kwana 7) → tabbatar da
redirect (yana farawa da sanda guda kawai, an hana `//` da backslash, bayan fassara dole ne ya zama asali guda) → turawa ta ɗan lokaci 307 zuwa shafin da aka nufa.

- **Mahaɗi na 1 (ana ba da shi nan da nan bayan rijista ta yi nasara)**: `--target pending` → yana sauka a `/subscription`.
  Burauzar mai amfani tana shiga halin "rabin shiga": shafin membanci, shafin dawowa na Alipay ana gani ana iya amfani da su; shafukan abun ciki har yanzu ana tosuwa zuwa shafin membanci (tsaro uku: duba ƙofar da'awar JWT → sake duba DB → duba API na asali, halin al'ada ne).
- **Mahaɗi na 2 (ana ba da shi bayan an tabbatar paid)**: da farko `refresh-login` ka musanya JWT sabuwa (biya na canza DB kawai, ba ta canza da'awar JWT da aka riga aka bayar ba, idan ba ka canza za ta bayyana 'ya biya amba ba memba ba'), sannan `--target home` → yana sauka a shafin gida,
  cikakken halin membanci.

## Cikakken tsarin lokaci (hanya ta al'ada)

```
1.  status                          # tabbatar da yanayin aiki
2.  (Mataki na 2 tattaunawa tabbatar da bayanai, kalmar sirri zaɓi ɗaya; yanayin ƙirƙira: gen-password → ka tambayi mai amfani ya adana nan take)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → mai amfani ya je imel ya duba lambar (kadai matakin barin tattaunawa ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → mahaɗi na 1 ga mai amfani
7.  (Mai amfani ya zaɓi shiri) create-order --package monthly
8.  start <fayil ɗin shafin biya>              # Windows; macOS tana amfani da open, Linux tana amfani da xdg-open
    # → mai amfani ya biya a cashier na Alipay (matakin barin tattaunawa na ②)
9.  query (kowace daƙiƙa 10–15) har sai paid
10. refresh-login                   # musanya JWT sabuwa mai da'awar ACTIVE
11. login-link --target home        # → mahaɗi na 2 ga mai amfani
12. whoami                          # tabbatar da subscriptionStatus: ACTIVE (na zaɓi)
13. cleanup                         # share fayil ɗin hali
```

## Taswirar umarni → API na dandalin

| Umarnin script | Tashar dandalin |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, ana ɗora avatar kai tsaye) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (mahaɗi ɗaya ne, yana aiki lokacin da burauza ta danna) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Inda dokuka suka samo: dokokin filaye da iyakancewa na rijista duba `registration-flow.md`; shiri da hanyar kunnawa duba
`payment-and-activation.md` (duka sun ambaci fayilolin code na dandalin).

## Kula da kuskure a matakin script

| Alama | Yadda ake kula |
|---|---|
| `Node 版本过低` (Node tana da ƙananan siga) | Ka koma yanayin jagora kawai, kada ka yi ta gwadawa da ƙarfi |
| Kuskuren hanyar sadarwa / lokaci ya wuce | Ka sake gwadawa sau ɗaya; har yanzu ya gaza, ka tambayi mai amfani ya duba hanyar sadarwa sannan ya ci gaba (fayil ɗin hali yana nan, ka gudanar da `status` daga farko domin dawowa) |
| register ta kawo kuskuren kasuwanci (用户名已存在 da sauransu) | Ka kula bisa teburin Mataki na 5 na SKILL.md, **lambar tabbatarwa ba buƙatar sake aikawa** (tana da inganci a cikin minti 10) |
| register ta kawo `邮箱验证码错误或已过期` (lambar tabbatarwa ta imel ba ta daidai ko ta ƙare) | Ya wuce lokaci → a sake `send-code` |
| Bayan `create-order` mai amfani ya rufe shafin biya | Ka sake `create-order` kai tsaye (tsohon oda yana rufewa da kai bayan sa'o'i 2) |
| `query` na ci gaba da pending | Mai amfani mai yiwuwa ba ya biya; ka tambaya. Hakika ya biya → ka bi teburin bincike na payment-and-activation.md |
| `refresh-login` 403 `pending_payment` | Kuɗin ba shiga tukuna ba, ka koma mataki na 9 ka ci gaba da sake dubawa |
| Fayil ɗin hali ya ɓace (an share shi ba zato ba tsammani / an canza na'ura) | `whoami`/`refresh-login` ba za a iya amfani da su ba; ka tambayi mai amfani a cikin burauzar da ta taɓa buɗe mahaɗi na 1 ya sabunta shafin membanci ya tabbatar da hali, ko ya sake shiga (yanayin yanar gizo) |

## Yanayin dawowa (jagora kawai)

A kowane ɗayan waɗannan hali, ka koma nan take ga yanayin jagora kawai na salon v1, kada ka ƙara damuwa da script ɗin:

- Ba a sami Node >= 18 ko script ɗin ta gaza sau biyu a jere iri ɗaya;
- Mai amfani ya faɗi a bayyane 'na da kansa zai yi aiki a yanar gizo';
- Manufofin kamfani/na'ura sun hana script ɗin haɗawa da intanet.

Bayan dawowa: ka ba shafin rijista https://global.powpow.online/register da shafin membanci
https://global.powpow.online/subscription , ka bi dokokin `registration-flow.md` ka taimaka gyara kuskure, salo
ba ya canzawa, kowane zagaye har yanzu yana rufewa da sashin 'mataki na gaba'.
