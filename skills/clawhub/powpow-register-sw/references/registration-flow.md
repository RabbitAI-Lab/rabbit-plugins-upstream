# Mchakato wa Kujiandikisha kwa Kina — powpow-register

Rejea hati hii unapotatua matatizo. Kanuni zote zinatokana na msimbo chanzi wa jukwaa (uthibitishaji wa mwendo sawa kati ya mbele na nyuma kwa Next.js), vyanzo vimetajwa. Jukwaa linaposasishwa, tabia halisi mtandaoni ndiyo inayotumika.

## Njia za Kuingia

- Ukurasa wa kujiandikisha: https://global.powpow.online/register
- Ukurasa wa kuingia: https://global.powpow.online/login
- Ukurasa wa usajili: https://global.powpow.online/subscription
- Iwapo mtumiaji anaingia kupitia kiungo cha kushiriki chenye `?next=...`, baada ya kujiandikisha + malipo kukamilika atarudishwa kiotomatiki kwenye ukurasa wa awali.

## Sehemu za Fomu na Kanuni

| Sehemu | Lazima | Kanuni | Chanzo cha msimbo |
|---|---|---|---|
| Picha ya wasifu | Si lazima | Picha ≤5MB, SVG haitumiki; seva inabana kiotomatiki (>100KB inabanwa hadi 400×400 / ubora 90) | `src/app/api/auth/register/route.ts` |
| Jina la mtumiaji | Lazima | Herufi 2~50, baada ya trim huhifadhiwa kwa **herufi ndogo** (Tom na tom huhesabiwa kuwa jina moja; upande wa kujiandikisha na wa kuingia vyote havivutii herufi kubwa/ndogo) | Hapo juu (zod schema) |
| Neno la siri | Lazima | Herufi 8~100, lazima liwe na herufi kubwa, herufi ndogo na nambari kwa pamoja | Hapo juu |
| Thibitisha neno la siri | Lazima | Lifanane na neno la siri (uthibitishaji wa mbele tu) | `src/app/(public)/register/page.tsx` |
| Jina la utani | Si lazima | ≤herufi 100; usipojaza, huchukua jina la mtumiaji | register route |
| Barua pepe | **Lazima** | Muundo halali wa barua pepe, ≤herufi 255; barua pepe moja inaweza kujiandikisha akaunti moja tu | register route |
| Msimbo wa uthibitisho wa barua pepe | **Lazima** | Tarakimu 6; **unafaa kwa dakika 10**; unapothibitishwa kwa ufanisi unabatilika; kutuma tena kunatiaga alama kuwa msimbo wa zamani umetumika | `src/lib/email-verification.ts` |
| Nambari ya simu | Si lazima | Nambari za simu za China Bara zinaanza `1[3-9]` na jumla tarakimu 11; nambari moja ya simu inaweza kufungwa kwenye akaunti moja tu | register route |

Ukurasa pia hutoa vitufe vitatu vya kuingia kwa wahusika wengine: **Google, Watcha, akaunti ya Huawei** (`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Akaunti za wahusika wengine hazina neno la siri la ndani; baadaye ukijaribu kuingia kwa neno la siri utapata «该账号未设置密码，请使用其他方式登录» (akaunti hii haikuwekewa neno la siri, tafadhali ingia kwa njia nyingine).

## Vigezo vya Kikomo cha Kasi na Ulinzi dhidi ya Mashambulizi

| Kitendo | Kikomo | Chanzo |
|---|---|---|
| Kuwasilisha kujiandikisha | **Mara 3 kwa dakika/IP**, kupita kikomo 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Kutuma msimbo wa uthibitisho | IP moja mara 1 kwa dakika **na** barua pepe moja mara 1 kwa dakika, kupita kikomo 429; kitufe cha mbele kinahesabu chini sekunde 60 | `src/app/api/auth/register/send-code/route.ts` |
| Uthibitishaji wa msimbo | Kila barua pepe inaweza kujaribu **mara 5** zaidi ndani ya dakika 10; kufikia kikomo hukataliwa hata msimbo ukiwa sahihi, inahitaji kutuma msimbo mpya | `src/lib/email-verification.ts` |
| Kutuma msimbo wa kusahau neno la siri | Mara 1 kwa dakika/IP | `src/app/api/auth/forgot-password/route.ts` |
| Kuingia | Mara 5 kwa dakika/IP; akaunti moja ikishindikana **mara 5 mfululizo inafungwa kwa dakika 30** (423), wakati huo kunaonyeshwa idadi inayopungua ya majaribio yaliyobaki | `src/app/api/auth/login/route.ts`、`rate-limit.ts` |

**Tabia ya kulinda faragha**: wakati wa kutuma msimbo wa uthibitisho / kusahau neno la siri, iwapo barua pepe tayari imejiandikisha au haipo, interface inarudisha ujumbe wa mafanikio unaofanana, bila kufichua kama barua pepe imejiandikisha au la.

## Mabadiliko ya Hali baada ya Kujiandikisha Kwa Ufanisi

1. Mtumiaji huhifadhiwa kwenye hifadhidata akiwa na `accountStatus: 'pending'`, na **beji 3** za awali (register route).
2. Seva wakati huo huo huweka cookie mbili za HttpOnly: JWT (inaruhusu kufikia `/subscription` moja kwa moja) na pendingUserToken (kitambulisho cha mchakato wa usajili).
3. Ukurasa wa kujiandikisha ukigundua `pending_payment` → inaruka kwenda `/subscription` (inahifadhi parameta ya kurudi `next`).
4. Malipo yakikamilika → `accountStatus` inakuwa `active` (PayPal inaamilishwa kiotomatiki kupitia Webhook; msimbo wa WeChat unathibitishwa na mtu; Huawei IAP inapitia `activate-huawei`). Tazama `payment-and-activation.md`.

Mtumiaji ambaye hajaamilishwa (pending) anapotumia API za msingi (mtiririko wa habari, ramani, mazungumzo na watu wa kidijitali, ukaguzi n.k.) atapata 403; isipokuwa viungo vya machapisho yaliyoshirikiwa (vinabaki kupatikana kwa umma).

## Jedwali la Utatuzi wa Makosa ya Kawaida

| Dalili (ujumbe wa mfumo) | Sababu | Nini cha kufanya |
|---|---|---|
| 「用户名已存在」 (jina la mtumiaji tayari lipo) | Jina la mtumiaji limechukuliwa (haijalishi herufi kubwa/ndogo) | Badilisha jina la mtumiaji |
| 「邮箱已被使用」 (barua pepe tayari imetumika) | Barua pepe tayari imejiandikisha | Badilisha barua pepe; au nenda kupitia kuingia + «Nimesahau neno la siri» kurejesha akaunti ya zamani |
| 「邮箱验证码错误或已过期」 (msimbo wa uthibitisho wa barua pepe si sahihi au umeisha muda) | Msimbo umeandikwa vibaya / zaidi ya dakika 10 / majaribio makosa zaidi ya 5 yamekataliwa | Bonyeza «Tuma tena», tumia msimbo wa uthibitisho wa **barua pepe ya hivi punde zaidi** |
| Sipokei msimbo wa uthibitisho | Kikomo cha sekunde 60; au kimeingia kwenye spam/tangazo | Subiri hesabu ya chini imalizike kisha tuma tena; angalia folda ya spam |
| 「手机号已被使用」 (nambari ya simu tayari imetumika) | Nambari ya simu imefungwa kwenye akaunti nyingine | Ondoa nambari ya simu (hiari) au badilisha nambari |
| 「注册请求过于频繁」/ 429 (ombi la kujiandikisha ni la mara kwa mara sana) | Kujiandikisha kumefikia kikomo cha mara 3 kwa dakika/IP | Subiri dakika chache kisha jaribu tena |
| 409「用户名或邮箱已被注册」 (jina la mtumiaji au barua pepe tayari imejiandikisha) | Kuwasilisha kukutana na jina la mtu mwingine kwa wakati mmoja (hifadhi ya dharura ya ushindani) | Badilisha jina la mtumiaji au barua pepe kisha jaribu tena |
| 「图片大小不能超过5MB」/「不支持 SVG」 (picha haiwezi kuzidi 5MB / SVG haitumiki) | Picha ya wasifu haifai | Badilisha picha au ruka picha ya wasifu |
| Kujiandikisha kumefanikiwa lakini kuingia kunatoa 403「请完成订阅以激活账户」 (tafadhali kamilisha usajili kuamilisha akaunti) | Akaunti bado iko pending | Baada ya kuingia fuata maelezo ya ukurasa nenda `/subscription` ukamilishe usajili |
| Kuingia 423「账户已锁定」 (akaunti imefungwa) | Neno la siri limekosewa mara 5 mfululizo | Subiri dakika 30 |
| Kuingia 401「还剩 N 次尝试机会」 (zimesalia majaribio N) | Neno la siri si sahihi, karibu kufungwa | Fikiri vizuri kabla ya kujaribu, au nenda moja kwa moja kwenye «Nimesahau neno la siri» |
| 「该账号未设置密码，请使用其他方式登录」 (akaunti hii haikuwekewa neno la siri, tafadhali ingia kwa njia nyingine) | Akaunti ya wahusika wengine (Google/Watcha/Huawei) | Ingia ukitumia kitufe cha awali cha akaunti ya wahusika wengine |
| 「该账号已注销」 (akaunti imefutwa) | Akaunti imedeactivate | Inahitaji kujiandikisha upya |

## Ujuzi Mdogo wa Kuingia (kwa utatuzi wa matatizo)

Kuingia kunasaidia **jina la mtumiaji / barua pepe / nambari ya simu** kwa pamoja (yoyote kati ya hizo tatu inaweza kuwa jina la akaunti). Nimesahau neno la siri: ukurasa wa kuingia → «Nimesahau neno la siri» → weka barua pepe ya kujiandikisha upokee msimbo wa tarakimu 6 → weka upya.