# Cikakken bayanin tsarin rijista — powpow-register

A karanta idan ana binciken matsala. Duk dokuka sun fito daga code ɗin dandalin (tabbatarwa mai jituwa ta Next.js na ɓangaren gaba da baya), an ambaci inda aka samo su. Lokacin da dandalin ya sabunta, a bi halin da gaske na kan layi.

## Shigarwa

- Shafin rijista: https://global.powpow.online/register
- Shafin shiga: https://global.powpow.online/login
- Shafin membanci: https://global.powpow.online/subscription
- Idan an shiga daga mahaɗin rabawa mai `?next=...`, bayan rijista + biya sun kammala za a dawo da kai ga shafin asali.

## Filayen fom da dokuka

| Filin | Wajibi | Dokoki | Inda aka samo |
|---|---|---|---|
| Avatar | Na zaɓi | Hoto ≤5MB, ba ta goyi bayan SVG ba; uwar garwa na rage girma ta kai (idan >100KB a rage zuwa 400×400 / inganci 90) | `src/app/api/auth/register/route.ts` |
| Sunan mai amfani | Wajibi | Haruffa 2~50, bayan yanke sarari ana canza zuwa **kanana** ana ajiye (Tom da tom ana ɗaukarsu sunan mai amfani ɗaya, ɓangaren rijista da ɓangaren shiga ba su son girma-kanana) | iri ɗaya (zod schema) |
| Kalmar sirri | Wajibi | Haruffa 8~100, dole ne ta ɗauke da manyan haruffa, ƙananan haruffa, da lambobi tare | iri ɗaya |
| Tabbatar da kalmar sirri | Wajibi | Ta yi daidai da kalmar sirri (tabbatarwa ta ɓangaren gaba kawai) | `src/app/(public)/register/page.tsx` |
| Laƙabi | Na zaɓi | ≤100 haruffa; idan ba a cika ba tsoho yana ɗaukar sunan mai amfani | register route |
| Imel | **Wajibi** | Fomatin imel mai inganci, ≤255 haruffa; imel ɗaya yana iya rijista asusu ɗaya kawai | register route |
| Lambar tabbatarwa ta imel | **Wajibi** | Lambobi 6; **mai inganci a cikin minti 10**; bayan tabbatarwa ta yi nasara ana soke ta; sake aikawa zai alamta lambar da ta gabata a matsayin an yi amfani da ita | `src/lib/email-verification.ts` |
| Lambar waya | Na zaɓi | Lambar waya ta babban yankin China `1[3-9]` farko jimla lambobi 11; lambar waya ɗaya na iya ɗaura asusu ɗaya kawai | register route |

Shafin yana ba da maɓallan shiga na ɓangare na uku uku kuma: **Google, Watcha, Huawei** (`GoogleSignInButton` /
`WatchaLoginButton` / `HuaweiLoginButton`). Asusun ɓangare na uku ba su da kalmar sirri ta cikin gida, daga baya amfani da kalmar sirri don shiga zai dawo da
「该账号未设置密码，请使用其他方式登录」 (wannan asusun ba a saita masa kalmar sirri ba, ka yi amfani da wata hanya don shiga).

## Iyakancewa da ma'aunin hana fashin ƙoƙari

| Aiki | Iyaka | Inda aka samo |
|---|---|---|
| Ƙaddamar da rijista | **sau 3/minti/IP**, idan ya wuce 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Aikawa da lambar tabbatarwa | IP ɗaya sau 1 a minti **kuma** imel ɗaya sau 1 a minti, idan ya wuce 429; maɓallin ɓangaren gaba na ƙidaya baya daƙiƙa 60 | `src/app/api/auth/register/send-code/route.ts` |
| Tabbatar da lambar tabbatarwa | Kowace imel a cikin minti 10 mafi ƙoƙari **sau 5**, idan aka kai iyaka ko da lambar daidai ce ana ƙin, dole ne a sake aikawa da lambar | `src/lib/email-verification.ts` |
| Aikawa da lambar manta kalmar sirri | Sau 1/minti/IP | `src/app/api/auth/forgot-password/route.ts` |
| Shiga | Sau 5/minti/IP; asusu ɗaya na gaza a jere **sau 5 ana kulle sa'o'i 30** (423), a lokacin sauran ƙoƙarin na raguwa ana nuna wa | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Halin kare keɓaɓɓu**: lokacin aikawa da lambar tabbatarwa / manta kalmar sirri, idan imel an riga an rijista ko ba ya wanzu, tashar na dawo da saƙon nasara iri ɗaya, ba ta fallasa ko imel an riga an rijista ba.

## Daidaiton yanayin agent-yana-taimakawa da rijistar yanar gizo

Script ɗin skill ɗin kira **wannan saitin API na jama'a ɗaya** (`/api/auth/register`, `send-code`, `login`,
`/api/auth/me`), tare da ƙaddamar da fom ɗin shafin rijista na bi tambarin tabbatarwa, iyakancewa da hanyoyin kuskure iri ɗaya — duk
dokukan wannan fayil ɗin dai-dai ne ga hanyoyin biyu. Tsarin lokaci da kwangilar umarnin script ɗin duba `references/agent-flow.md`.

## Canjin hali bayan rijista ta yi nasara

1. Mai amfani ana ajiye shi da `accountStatus: 'pending'`, **badge 3 na farko** (register route).
2. Uwar garwa kuma tana shuka cookie biyu na HttpOnly: JWT (za a iya shiga `/subscription` kai tsaye) da
   pendingUserToken (takaddun shaida na tsarin membanci).
3. Shafin rijista ya gano `pending_payment` → yana turawa `/subscription` (yanayin adana `next` don dawowa);
   a yanayin agent-yana-taimakawa ana amfani da `me?token=…&redirect=/subscription` don samun sakamko ɗaya.
4. Biya ta cika → `accountStatus` ta zama `active` (**Alipay ta hanyar notify uwar garwa ta kunna ta kai**;
   PayPal ta hanyar Webhook ta kunna ta kai; siffanta lambar QR ta WeChat tabbatarwa ce ta hannu; Huawei IAP ta hanyar `activate-huawei`).
   Cikakken bayani duba `payment-and-activation.md`.

Mai amfani da ba a kunna ba (pending) idan ya kira API na asali (kwararar bayanai, taswira, tattaunawa da mutum na dijital, buga halarta da sauransu) yana samun 403 koyaushe; mahaɗin raba sako keɓance (ya kasance a bude ana iya shiga).

## Teburin bincike da gyaran kuskure na kowa

| Alama | Dalili | Me za a yi |
|---|---|---|
| 「用户名已存在」 (sunan mai amfani ya riga ya wanzu) | An yi amfani da sunan mai amfani (ba tare da girma-kanana ba) | Ka canza wani sunan mai amfani |
| 「邮箱已被使用」 (an riga an yi amfani da imel) | An riga an rijista imel | Ka canza imel; ko ka canza zuwa shiga + "manta kalmar sirri" dawo da asusun da ya gabata |
| 「邮箱验证码错误或已过期」 (lambar tabbatarwa ta imel ba ta daidai ko ta ƙare) | An shigar da lambar sosai / ya wuce minti 10 / an gwada fiye da sau 5 an ƙi | Ka danna "aika sake", ka yi amfani da lambar imel **mata ta ƙarshe** |
| Ba a karɓar lambar tabbatarwa | Iyakancewa na daƙiƙa 60; ko ta shiga spam/junk | Ka jira ƙidaya baya ta ƙare sannan ka aika; ka leƙo babban fayil ɗin spam |
| 「手机号已被使用」 (an riga an yi amfani da lambar waya) | An ɗaura lambar waya da wani asusu | Ka cire lambar waya (na zaɓi ce) ko ka canza lamba |
| 「注册请求过于频繁」/ 429 (bukatar rijista sau da yawa / 429) | Rijista sau 3/minti/IP ta kai sama | Ka jira minti kaɗan sannan ka sake gwadawa |
| 409「用户名或邮箱已被注册」 (409 sunan mai amfani ko imel an riga an rijista) | A lokacin ƙaddamarwa ya fada da wani (kariya ta daidaito) | Ka canza sunan mai amfani ko imel sannan ka sake gwadawa |
| 「图片大小不能超过5MB」/「不支持 SVG」 (hoton ba zai wuce 5MB ba / ba a goyi bayan SVG ba) | Avatar ba ta dace ba | Ka canza hoto ko ka tsallake avatar |
| Rijista ta yi nasara amma shiga 403「请完成订阅以激活账户」 (kammala membanci domin kunna asusu) | Asusu har yanzu pending (halin da ake tsammani kafin biya) | Kafin biya: wannan al'ada ce, ka fara kammala membanci; bayan biya har yanzu 403: yana nuna an yi amfani da JWT da ta gabata, a yanayin script ɗin ka fara `refresh-login` ka musanya halin shiga sabuwa |
| Shiga 423「账户已锁定」 (asusu an kulle) | Kalmar sirri ta gaza a jere sau 5 | Ka jira minti 30 |
| Shiga 401「还剩 N 次尝试机会」 (sauran ƙoƙari N suka rage) | Kalmar sirri ba daidai ba, kusa da kullewa | Ka yi tunani sosai sannan ka gwada, ko ka kai tsaye ka bi "manta kalmar sirri" |
| 「该账号未设置密码，请使用其他方式登录」 (wannan asusun ba a saita masa kalmar sirri ba, ka yi amfani da wata hanya don shiga) | Asusu ɓangare na uku (Google/Watcha/Huawei) | Ka yi amfani da maɓallin ɓangare na uku na asali don shiga |
| 「该账号已注销」 (wannan asusun an soke shi) | An deactivate asusun | Buƙatar rijista sabuwa |

## Ƙananan ilimin shiga (don taimakon bincike)

Shiga yana goyi bayan shigarwa guda **sunan mai amfani / imel / lambar waya** (ko ɗaya daga cikin uku za a iya amfani da shi a matsayin sunan asusu).
Manta kalmar sirri: shafin shiga → "manta kalmar sirri" → ka shigar da imel ɗin rijista ka karɓi lambar lambobi 6 → ka saita sake.
