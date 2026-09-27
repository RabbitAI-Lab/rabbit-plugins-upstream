# Cikakken Bayanin Hanyar Rijista — powpow-register

Ka duba wannan takarda lokacin gano kuskure. Duk dokoki sun fito daga lambar tushe ta dandali (tabbatarwar daidaito tsakanin gaba da baya ta Next.js), an bayyana tushensu. Idan dandali ya sabunta, aikin gaske a kan layi ne ake bi.

## Hanyoyin Shiga

- Shafin rijista: https://global.powpow.online/register
- Shafin shiga: https://global.powpow.online/login
- Shafin subscription: https://global.powpow.online/subscription
- Idan mai amfani ya shigo ta haɗin rabawa mai ɗauke da `?next=...`, bayan kammala rijista + biyan kuɗi zai koma kai tsaye zuwa shafin na asali.

## Filla-filla na Fom da Dokoki

| Filla-filla | Wajibi | Doka | Tushen lambar |
|---|---|---|---|
| Hoton bayananka (avatar) | Ba dole ba | Hoto ≤5MB, ba a tallafawa SVG; uwar garken tana matsewa kai tsaye (>100KB ana matse shi zuwa 400×400 / inganci 90) | `src/app/api/auth/register/route.ts` |
| Sunan mai amfani | Wajibi | Haruffa 2~50, bayan trim ana adana shi da **ƙaramin harafi** (Tom da tom ana ɗaukar su suna ɗaya; ɓangaren rijista da shiga duk ba sa bambanta babba/ƙarami) | A sama (zod schema) |
| Kalmar sirri | Wajibi | Haruffa 8~100, dole ta ƙunshi babban harafi, ƙaramin harafi da lamba tare | A sama |
| Tabbatar da kalmar sirri | Wajibi | Dole ta yi daidai da kalmar sirri (tabbatarwa ta ɓangaren gaba kawai) | `src/app/(public)/register/page.tsx` |
| Sunan laƙabi | Ba dole ba | ≤haruffa 100; idan ba a cika ba, ana ɗaukar sunan mai amfani | register route |
| Imel | **Wajibi** | Tsarin imel mai inganci, ≤haruffa 255; imel ɗaya tana iya yin rijistar asusu ɗaya kawai | register route |
| Lambar tabbatarwar imel | **Wajibi** | Lambobi 6; **tana aiki na mintuna 10**; idan ta yi nasara ana soke ta; sake aikawa yana yi wa tsohuwar lambar alamar an yi amfani da ita | `src/lib/email-verification.ts` |
| Lambar waya | Ba dole ba | Lambobin waya na China Mainland suna farawa da `1[3-9]` jimla lambobi 11; lambar waya ɗaya tana iya ɗaura da asusu ɗaya kawai | register route |

Shafin kuma yana ba da maɓallan shiga na ɓangare na uku guda uku: **Google, Watcha, asusun Huawei** (`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Asusun ɓangare na uku ba su da kalmar sirri ta ciki; daga baya idan ka yi ƙoƙarin shiga da kalmar sirri za ka samu «该账号未设置密码，请使用其他方式登录» (wannan asusu ba a saita masa kalmar sirri ba, don Allah yi amfani da wata hanyar shiga).

## Sigogin Iyaka da Kariya daga Hare-hare

| Aiki | Iyaka | Tushen |
|---|---|---|
| Aika rijista | **Sau 3 a minti/IP**, wuce iyaka 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Aika lambar tabbatarwa | IP ɗaya sau 1 a minti **kuma** imel ɗaya sau 1 a minti, wuce iyaka 429; maɓallin ɓangaren gaba yana kirga ƙasa sakan 60 | `src/app/api/auth/register/send-code/route.ts` |
| Tabbatar da lambar | Kowace imel tana iya ƙoƙari **sau 5** a cikin mintuna 10; idan an kai iyaka ana ƙi ko da lambar tayi daidai, ana buƙatar aika lambar sabuwa | `src/lib/email-verification.ts` |
| Aika lambar manta kalmar sirri | Sau 1 a minti/IP | `src/app/api/auth/forgot-password/route.ts` |
| Shiga | Sau 5 a minti/IP; asusu ɗaya idan ya kasa **sau 5 a jere ana kulle shi na mintuna 30** (423), a lokacin ana nuna raguwar adadin ƙoƙarin da ya rage | `src/app/api/auth/login/route.ts`、`rate-limit.ts` |

**Halin kare sirri (privacy)**: lokacin aika lambar tabbatarwa / manta kalmar sirri, idan imel ɗin an riga an yi rijista ko ba ya wanzu ba, interface ɗin tana mayar da saƙon nasara ɗaya, ba ta fallasa ko imel ɗin an yi rijista ba.

## Sarrafa Yanayi bayan Nasarar Rijista

1. Ana adana mai amfani a cikin ma'ajiyar bayanai da `accountStatus: 'pending'`, tare da **baji 3** na farko (register route).
2. Uwar garken lokaci ɗaya tana sanya cookie biyu na HttpOnly: JWT (wanda ke ba da izinin shiga `/subscription` kai tsaye) da pendingUserToken (shaida ta hanyar subscription).
3. Shafin rijista idan ya gano `pending_payment` → yana tsallakewa zuwa `/subscription` (yana riƙe sigar dawowa `next`).
4. Biyan kuɗi ya ƙare → `accountStatus` ya zama `active` (PayPal ana kunnawa kai tsaye ta Webhook; lambar WeChat mutum ne ke tabbatarwa; Huawei IAP tana bi ta `activate-huawei`). Duba `payment-and-activation.md`.

Mai amfani da bai yi kunnawa ba (pending) idan ya kira API na muhimmanci (jeren labarai, taswira, hira da mutane na dijital, checking-in da sauransu) duk ya kai 403; banda haɗin rubutun da aka raba (suna kasancewa a buɗe ga jama'a).

## Teburin Gano Kuskuren Gama-gari

| Alamar (saƙon tsarin) | Dalili | Abin da za a yi |
|---|---|---|
| 「用户名已存在」 (sunan mai amfani ya riga ya wanzu) | An riga an ɗauki sunan mai amfani (ba a bambanta babba/ƙarami ba) | Canza sunan mai amfani |
| 「邮箱已被使用」 (imel an riga an yi amfani da ita) | Imel ɗin an riga an yi rijista | Canza imel; ko kuma bi ta shiga + «Manta kalmar sirri» don dawo da tsohon asusu |
| 「邮箱验证码错误或已过期」 (lambar tabbatarwar imel ba daidai ba ko ta ƙare) | An rubuta lambar ba daidai ba / fiye da mintuna 10 / ƙoƙarin kuskure fiye da 5 an ƙi | Danna «Aika sake», yi amfani da lambar tabbatarwa ta **sabuwar imel ɗin ƙarshe** |
| Ba a sami lambar tabbatarwa ba | Iyaka na sakan 60; ko kuma ta shiga jakar spam/talla | Jira kirgar ƙasa ta gama sannan ka sake aikawa; duba jakar spam |
| 「手机号已被使用」 (lambar waya an riga an yi amfani da ita) | Lambar waya tana ɗaure da wani asusu | Cire lambar waya (ba dole ba) ko canza lambar |
| 「注册请求过于频繁」/ 429 (buƙatar rijista tana da yawan gaske) | Rijista ta kai iyakar sau 3 a minti/IP | Jira mintuna kaɗan sannan ka sake gwadawa |
| 409「用户名或邮箱已被注册」 (sunan mai amfani ko imel an riga an yi rijista) | Aikawa ya ci karo da sunan wani a daidai lokacin (kariyar gasa) | Canza sunan mai amfani ko imel sannan ka sake gwadawa |
| 「图片大小不能超过5MB」/「不支持 SVG」 (hoto bai kamata ya wuce 5MB ba / ba a tallafawa SVG ba) | Hoton bayananka bai dace ba | Canza hoton ko tsallake hoton bayananka |
| Rijista ta yi nasara amma shiga ya ba 403「请完成订阅以激活账户」 (don Allah ka kammala subscription don kunna asusu) | Asusu har yanzu pending ne | Bayan shiga ka bi umarnin shafin ka je `/subscription` ka kammala subscription |
| Shiga 423「账户已锁定」 (an kulle asusu) | Kalmar sirri ta yi kuskure sau 5 a jere | Jira mintuna 30 |
| Shiga 401「还剩 N 次尝试机会」 (sauran ƙoƙari N ne) | Kalmar sirri ba daidai ba, kusa da kullewa | Ka yi tunani da kyau kafin ka gwada, ko kai tsaye je «Manta kalmar sirri» |
| 「该账号未设置密码，请使用其他方式登录」 (wannan asusu ba a saita masa kalmar sirri ba, don Allah yi amfani da wata hanyar shiga) | Asusun ɓangare na uku (Google/Watcha/Huawei) ne | Shiga ta amfani da maɓallin ɓangare na uku na asali |
| 「该账号已注销」 (an soke wannan asusu) | Asusun an deactivate shi | Ana buƙatar yin rijista sabuwa |

## Ƙaramin Ilimi na Shiga (don gano kuskure)

Shiga yana tallafawa **sunan mai amfani / imel / lambar waya** a haɗe (kowanne daga cikin ukun zai iya zama sunan asusu). Manta kalmar sirri: shafin shiga → «Manta kalmar sirri» → shigar da imel ɗin rijista don karɓar lambobi 6 → sake saitawa.