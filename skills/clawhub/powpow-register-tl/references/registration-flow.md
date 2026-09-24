# Detalye ng Proseso ng Pagrehistro — powpow-register

Ginagamit kapag may kailangang i-check na problema. Ang lahat ng panuntunan ay mula sa platform source code (Next.js frontend/backend consistency validation), may nakasaad na pinagmulan.
Kapag nag-update ang platform, sundin ang aktwal na ugali online.

## Mga Entry Point

- Pahina ng pagrehistro: https://global.powpow.online/register
- Pahina ng login: https://global.powpow.online/login
- Pahina ng subscription: https://global.powpow.online/subscription
- Kung pumasok mula sa shared link na may `?next=...`, awtomatikong babalik sa orihinal na pahina pagkatapos matapos ang pagrehistro + pagbabayad.

## Mga Field ng Form at Panuntunan

| Field | Kailangan | Panuntunan | Pinagmulan ng Code |
|---|---|---|---|
| Profile photo | Opsyonal | larawan ≤5MB, hindi sumusuporta ng SVG; awtomatikong nag-co-compress ang server (>100KB, i-compress sa 400×400 / quality 90) | `src/app/api/auth/register/route.ts` |
| Username | Kailangan | 2~50 character, pagkatapos i-trim ay **naka-lowercase** ang itatago (magkapareho ang Tom at tom, parehong insensitive sa malaki/maliit ang registration at login) | Pareho (zod schema) |
| Password | Kailangan | 8~100 character, dapat may malaking letra, maliit na letra, at numero | Pareho |
| Kumpirmahin ang password | Kailangan | dapat kapareho ng password (frontend check lang) | `src/app/(public)/register/page.tsx` |
| Palayaw | Opsyonal | ≤100 character; kapag walang laman, username ang default | register route |
| Email | **Kailangan** | valid na email format, ≤255 character; isang email ay isang account lang ang kayang i-register | register route |
| Email verification code | **Kailangan** | 6 na numero; **may bisa sa 10 minuto**; pagkatapos ma-verify ay hindi na magagamit; ang pagpapadala muli ay mamarkahan ang lumang code bilang nagamit na | `src/lib/email-verification.ts` |
| Numero ng telepono | Opsyonal | mainland China phone number na nagsisimula sa `1[3-9]` total 11 digit; isang numero ay isang account lang ang kayang ibind | register route |

Nagbibigay pa ang pahina ng tatlong third-party login button: **Google, Watcha, Huawei account** (`GoogleSignInButton` /
`WatchaLoginButton` / `HuaweiLoginButton`). Walang local password ang third-party account, at kapag gumamit ng password sa login ay makukuha ang
"该账号未设置密码，请使用其他方式登录" (hindi pa naka-set ng password ang account na ito, mangyaring gumamit ng ibang paraan para mag-login).

## Rate Limit at Anti-Bruteforce Parameters

| Ugali | Limitasyon | Pinagmulan |
|---|---|---|
| Pagsumite ng pagrehistro | **3 beses/minuto/IP**, sobra ay 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Pagpapadala ng verification code | parehong IP 1 beses/minuto **at** parehong email 1 beses/minuto, sobra ay 429; may 60-segundong countdown ang frontend button | `src/app/api/auth/register/send-code/route.ts` |
| Pag-check ng verification code | bawat email sa loob ng 10 minuto ay max **5 tries**, pagdating sa limit kahit tama ang code ay tatanggihan, kailangang magpadala muli | `src/lib/email-verification.ts` |
| Pagpapadala ng forgot-password code | 1 beses/minuto/IP | `src/app/api/auth/forgot-password/route.ts` |
| Login | 5 beses/minuto/IP; parehong account na sunod-sunod na mali **5 beses ay mai-lock ng 30 minuto** (423), habang ganoon ay may paalala na bumababa ang natitirang tries | `src/app/api/auth/login/route.ts`、`rate-limit.ts` |

**Privacy protection behavior**: kapag nagpapadala ng verification code / forgot password, hindi man naka-register o wala ang email, pareho lang ang ibinabalik ng API
na success text, hindi nabubunyag kung naka-register na ang email.

## Pagbabago ng Status Pagkatapos Magtagumpay ang Pagrehistro

1. Ini-save ang user na may `accountStatus: 'pending'`, unang **3 badge** (register route).
2. Sabay na itinatanim ng server ang dalawang HttpOnly cookie: JWT (direktang maa-access ang `/subscription`) at
   pendingUserToken (identity credential ng subscription process).
3. Nakikita ng registration page ang `pending_payment` → lumulukso sa `/subscription` (iniingatan ang `next` return parameter).
4. Tapos na ang pagbabayad → nagiging `active` ang `accountStatus` (ang PayPal ay awtomatikong nag-a-activate sa pamamagitan ng Webhook; ang WeChat QR scan ay
   manual confirmation; ang Huawei IAP ay sa pamamagitan ng `activate-huawei`). Detalye, tingnan ang `payment-and-activation.md`.

Ang hindi pa aktibo (pending) na user na tumatawag sa core API (feed, mapa, pakikipag-usap sa digital na tao, check-in, atbp.) ay 403 lahat;
maliban sa shared post links (nananatiling publicly accessible).

## Talahanayan ng Karaniwang Error Checking

| Sintomas (orihinal na error text sa Mandarin) | Dahilan | Paano Aayusin |
|---|---|---|
| 「用户名已存在」 (Mayroon nang username) | ginamit na ang username (insensitive sa malaki/maliit) | magpalit ng username |
| 「邮箱已被使用」 (Ginamit na ang email) | naka-register na ang email | magpalit ng email; o dumaan sa login + "forgot password" para mabawi ang lumang account |
| 「邮箱验证码错误或已过期」 (Mali o expired na ang email verification code) | maling na-type na code / lumampas sa 10 minuto / higit 5 maling tries ay tinanggihan | i-click ang "Ipadala muli", gamitin ang code mula sa **pinakabagong email** |
| Hindi dumating ang verification code | na-rate limit sa 60 segundo; o napunta sa spam/ads | hintaying matapos ang countdown bago magpadala muli; buksan ang spam folder |
| 「手机号已被使用」 (Ginamit na ang numero ng telepono) | naibind na ang numero sa ibang account | tanggalin ang numero (opsyonal) o magpalit ng numero |
| 「注册请求过于频繁」/ 429 (Masyadong madalas ang request sa pagrehistro) | naabot ang limit na 3 beses/minuto/IP sa pagrehistro | maghintay ng ilang minuto bago subukang muli |
| 409「用户名或邮箱已被注册」 (Naka-register na ang username o email) | nakasabay ng iba ang pangalan sa mismong pagsumite (concurrency fallback) | magpalit ng username o email at subukang muli |
| 「图片大小不能超过5MB」/「不支持 SVG」 (Hindi dapat lumampas sa 5MB ang larawan / Hindi sumusuporta ng SVG) | hindi sumusunod sa panuntunan ang profile photo | magpalit ng larawan o laktawan ang profile photo |
| Nagtagumpay ang rehistro ngunit 403 sa login「请完成订阅以激活账户」 (Mangyaring kumpletuhin ang subscription para i-activate ang account) | pending pa ang account | pagkatapos mag-login, sundan ang paalala sa pahina papunta sa `/subscription` at kumpletuhin ang subscription |
| Login 423「账户已锁定」 (Naka-lock na ang account) | 5 beses na sunod-sunod na maling password | maghintay ng 30 minuto |
| Login 401「还剩 N 次尝试机会」 (N natitirang tries) | maling password, malapit nang ma-lock | mag-isip muna bago subukan, o dumiretso sa "forgot password" |
| 「该账号未设置密码，请使用其他方式登录」 (Hindi pa naka-set ng password ang account na ito, mangyaring gumamit ng ibang paraan para mag-login) | third-party account (Google/Watcha/Huawei) | gamitin ang orihinal na third-party button para mag-login |
| 「该账号已注销」 (Na-deactivate na ang account na ito) | na-deactivate na ang account | kailangang magrehistro muli |

## Maliit na Kaalaman sa Login (pambackup na pagtingin sa error)

Sumusuporta ang login ng three-in-one input na**username / email / numero ng telepono** (kahit alin sa mga ito ay maaaring gamiting account name).
Forgot password: pahina ng login → "forgot password" → ilagay ang registered email para makatanggap ng 6-digit verification code → i-reset.