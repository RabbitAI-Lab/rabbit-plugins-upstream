# Mkato wa agent-kusaidia na mkataba wa hati — powpow-register

Maelezo ya utekelezaji wa hatua za SKILL.md. Amri zote ni `node scripts/powpow-register.mjs <amri-ndogo> [vigezo]`, hati **haina tegemezi**, inahitaji **Node >= 18**, maombi yote yanaenda tu `https://global.powpow.online`.

## Muundo wa usalama (kwa nini imeundwa hivi)

| Muundo | Sababu |
|---|---|
| Nenosiri hutumiwa tu kupitia kigezo cha mazingira `POWPOW_REGISTER_PASSWORD` | vigezo vya amri ya mchakato vinaonekana kwa michakato mingine ya mashine hii (usemi wa uvujaji wa argv), kigezo cha mazingira ndani ya hati kinasomwa kikitumika mara moja |
| Nenosiri **kamwe haiiandikwi kwenye faili ya hali**, kamwe haionekani kwenye logi | faili ya hali inaweza kubaki kwenye diski; mtindo wa kutengeneza unaoonyesha mara moja ni ili mtumiaji ahifadhi |
| Faili ya hali imehifadhiwa katika saraka ya muda ya mfumo (`os.tmpdir()/powpow-register-state.json`, 0600) | inayo sehemu tano tu: email / username / nickname / token / outTradeNo, `cleanup` hufuta kiotomatiki |
| JWT anayopata agent hubadilishwa kuwa cookie ya kivinjari kupitia kiolesura rasmi `me?token=` | daraja rasmi jukwaa lililounda kwa Harmony WebView; uthibitisho wa saini huchunguza tu saini + muda wa ufanisi, haifungi kwenye alama ya kifaa, kivinjari cha mtumiaji kinaweza kutumia |
| Malipo yanafanya tu create-order / query / kufungua cashier | kitendo cha kulipa na kitambulisho cha malipo kila wakati kiko kati ya mtumiaji na cashier rasmi ya Alipay, agent haipiti |

## Marejeleo ya amri

| Amri | Vigezo vya msingi | Kazi / wakati |
|---|---|---|
| `status` | —— | Tazama maendeleo ya mtiririko (soma faili ya hali); baada ya mazungumzo kukatika endesha hii kwanza |
| `gen-password` | —— | Tengeneza nenosiri dhabiti ya herufi 24 (mchanganyiko wa herufi kubwa ndogo + tarakimu), inaonyeshwa **mara moja tu** kwenye stdout |
| `prepare-suggest` | `--username --nickname --email` | Andika maelezo yaliyothibitishwa kwenye faili ya hali (baadaye register haitaki kurudia kutuma) |
| `send-code` | `--email` | Chasema jukwaa litume nambari ya tarakimu 6 (inayofaa kwa dakika 10, muda wa kupoeza sekunde 60) |
| `register` | `--code` (inahitajika); `--username --nickname --avatar --phone` (hiari, kama faili ya hali inavo hahitaji kutuma) | Unda akaunti ya pending; nenosiri kupitia `POWPOW_REGISTER_PASSWORD`; baada ya mafanikio JWT huhifadhiwa kiotomatiki kwenye faili ya hali |
| `login-link` | `--target pending` au `--target home` | Tengeneza kiungo cha ingia kwa kubofya mara moja (muundo wa viungo viwili, tazama chini) |
| `create-order` | `--package monthly\|quarterly\|yearly` | Unda agizo la Alipay; inarudisha njia ya faili ya ukurasa wa malipo + outTradeNo (huhifadhiwa kiotomatiki kwenye faili ya hali) |
| `query` | —— | Angalia hali ya agizo `paid / pending / closed / unknown` (outTradeNo inachukuliwa kutoka faili ya hali), hoji kila sekunde 10–15 |
| `refresh-login` | Nenosiri kupitia kigezo cha mazingira | Ingia tena kubadilisha **JWT mpya** (tamko la usajili hubadilika kutoka NONE kuwa ACTIVE), lazima iendeshwe baada ya malipo kufika |
| `whoami` | —— | Tumia token ya faili ya hali kuangalia hali ya akaunti na usajili (thibitisha uwezeshaji umefanya kazi) |
| `cleanup` | —— | Futa faili ya hali (lazima iendeshwe mwishoni) |

**Upitishaji wa kigezo cha mazingira** (nenosiri kamwe haingii kwenye amri):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<nenosiri>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<nenosiri>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<nenosiri> && node scripts/powpow-register.mjs register --code 123456
```

## Utaratibu wa viungo viwili (muundo msingi)

Hali ya ingia ya jukwaa ni cookie ya HttpOnly, agent haiwezi kuipandia kivinjari moja kwa moja; daraja ni kiolesura rasmi
`/api/auth/me?token=<JWT>&redirect=<njia-ya-kati-ya-tovuti>` : uthibitisho wa saini → mtumiaji wa pending hubuniwa
session moja kwa moja → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / siku 7) → uthibitisho wa
redirect (inaanza tu na mslaski mmoja, inazuia `//` na backslash, baada ya kutatua inapaswa kuwa asili moja) → uelekezaji wa muda 307 kwenye ukurasa unaolengwa.

- **Kiungo 1 (toleo baada ya usajili kufanikiwa mara moja)**: `--target pending` → inaingia `/subscription`.
  Kivinjari cha mtumiaji kinaingia hali ya "nusu-login": ukurasa wa usajili wa malipo, ukurasa wa kurudi wa Alipay unaonekana na unaweza kutumika; kurasa za maudhui bado zinazuiliwa hadi ukurasa wa usajili wa malipo (nguzo tatu za ulinzi: uchunguzi wa malango ya madai ya JWT → ukaguzi wa DB → uchunguzi wa API kuu, ni tabia ya kawaida).
- **Kiungo 2 (baada ya kuthibitisha paid)**: kwanza `refresh-login` kubadilisha JWT mpya (malipo hubadilisha tu DB, haibadilishi madai ya JWT iliyotolewa tayari, usipobadilisha utaonekana "umelipa bila ya kuwa mwanachama"), kisha `--target home` → inaingia ukurasa wa nyumbani,
  hali kamili ya mwanachama.

## Mlolongo kamili (njia ya kawaida)

```
1.  status                          # Uchunguzi wa mazingira
2.  (Hatua ya 2 mazungumzo kuthibitisha maelezo, nenosiri uchague moja; mtindo wa kutengeneza: gen-password → mruhusu mtumiaji ahifadhi mara moja)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → mtumiaji nenda barua pepe tazama nambari (sehemu pekee ya kuondoka mazungumzoni①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → kiungo 1 kwa mtumiaji
7.  (Mtumiaji achagua mpango) create-order --package monthly
8.  start <faili ya ukurasa wa malipo>              # Windows; macOS hutumia open, Linux hutumia xdg-open
    # → mtumiaji alipe kwenye cashier ya Alipay (sehemu ya kuondoka mazungumzoni②)
9.  query (kila sekunde 10–15) hadi paid
10. refresh-login                   # badilisha JWT mpya yenye tamko la ACTIVE
11. login-link --target home        # → kiungo 2 kwa mtumiaji
12. whoami                          # thibitisha subscriptionStatus: ACTIVE (hiari)
13. cleanup                         # futa faili ya hali
```

## Ramani ya amri → API ya jukwaa

| Amri ya hati | Kiolesura cha jukwaa |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, picha ya wasifu hupakia moja kwa moja) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (kiungo yenyewe, kinatoa madhumuni wakati mtumiaji abofya) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Chanzo cha sheria: sheria za sehemu na vizuizi za usajili angalia `registration-flow.md`; mpango na mlolongo wa uwezeshaji angalia
`payment-and-activation.md` (yote yana chanzo la faili ya msimbo wa jukwaa kilichotajwa).

## Utatuzi wa makosa ya kiwango cha hati

| Tukio | Shughulikia |
|---|---|
| `Node 版本过低` (Node imekuwa toleo la chini) | Rudi kwenye mtindo wa mwongozo mtupu, usijaribu kwa nguvu |
| Kosa la mtandao / muda uliopita | Jaribu tena mara moja; bado ikishindwa mwambie mtumiaji achunguze mtandao kisha aendelee (faili ya hali bado ipo, endesha `status` mwanzo ili urudie) |
| register inaporoja kosa la biashara (jina la mtumiaji limeshakuwepo, n.k.) | Shughulikia kulingana na jedwali la Hatua ya 5 la SKILL.md, **nenosiri haihitaji kutumiwa tena** (bado inafaa ndani ya dakika 10) |
| register inaporoja `邮箱验证码错误或已过期` (nambari ya uthibitisho ya barua pepe ni mbaya au imeisha muda) | Ikipita muda → tuma tena `send-code` |
| Baada ya `create-order` mtumiaji amefunga ukurasa wa malipo | Endesha tu tena `create-order` (agizo la zamani hufungwa kiotomatiki baada ya saa 2) |
| `query` inabaki pending | Labda mtumiaji hajali; uliza. Amekweli kulipa → fuata jedwali la utatuzi wa payment-and-activation.md |
| `refresh-login` 403 `pending_payment` | Malipo bado hayajafika, rudi Hatua ya 9 endelea kuhoji |
| Faili ya hali imepotea (ilifutwa kwa bahati mbaya / kuhamia mashine nyingine) | `whoami`/`refresh-login` haviwezi kutumika; mruhusu mtumiaji kwenye kivinjari alichofungua kiungo 1 aburudge ukurasa wa usajili wa malipo ili athibitishe hali, au ingia tena (mtindo wa wavuti) |

## Mtindo wa kurudi nyuma (mwongozo mtupu)

Hali yoyote ifuatayo, rudi mara moja kwenye mtindo wa mwongozo mtupu wa v1, usisumbue tena hati:

- Hakuna Node >= 18 au hati inashindwa mara mbili mfululizo kwa aina ile ile;
- Mtumiaji anasema wazi "mimi mwenyewe nitafanya kwenye wavuti";
- Sera ya kampuni/kifaa inazuia hati kuunganisha mtandao.

Baada ya kurudi: toa ukurasa wa usajili https://global.powpow.online/register na ukurasa wa usajili wa malipo
https://global.powpow.online/subscription, fuata sheria za `registration-flow.md` kumsaidia kutatua, sauti
hubadilika, kila raundi bado malizia kwa sehemu ya "hatua inayofuata".
