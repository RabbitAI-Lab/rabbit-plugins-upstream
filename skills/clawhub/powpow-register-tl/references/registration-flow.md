# Detalye ng proseso ng rehistro — powpow-register

Para sa pagsangguni kapag nag-troubleshoot. Lahat ng patakaran ay nagmumula sa platform source code (Next.js front-end/back-end consistency validation), kaya may nakalistang pinagmulan. Kapag nag-update ang plataporma, ang aktwal na gawi online ang masusunod.

## Mga Entrada

- Registration page: https://global.powpow.online/register
- Log-in page: https://global.powpow.online/login
- Subscription page: https://global.powpow.online/subscription
- Kung pumasok sa pamamagitan ng share link na may `?next=...`, pagkatapos makumpleto ang rehistro + bayad ay awtomatikong babalik sa orihinal na page.

## Mga field ng form at mga patakaran

| Field | Kinakailangan | Patakaran | Pinagmulan ng source code |
|---|---|---|---|
| Avatar | Opsyonal | Larawan ≤5MB, hindi sumusuporta sa SVG; awtomatikong kinukompres ng server (kapag lumampas ng 100KB, icocompress sa 400×400 / quality 90) | `src/app/api/auth/register/route.ts` |
| Username | Kinakailangan | 2–50 na karakter, pagkatapos ng trim ay iniimbak sa **maliit na titik** (ang Tom at tom ay itinuturing na parehong username; ang registration side at log-in side ay parehong case-insensitive) | pareho (zod schema) |
| Password | Kinakailangan | 8–100 na character, dapat maglaman nang sabay ng malaking titik, maliit na titik, at numero | pareho |
| Confirm password | Kinakailangan | Dapat tugma sa password (front-end validation lang) | `src/app/(public)/register/page.tsx` |
| Palayaw | Opsyonal | ≤100 na karakter; kung walang laman, default ang username | register route |
| Email | **Kinakailangan** | Wastong email format, ≤255 na karakter; isang email ay maaaring magrehistro ng isang account lang | register route |
| Email verification code | **Kinakailangan** | 6 na numero; **bisa sa loob ng 10 minuto**; mawawalan ng bisa pagkatapos ng matagumpay na beripikasyon; ang pagpapadala muli ay mamamarkahan ang lumang code bilang nagamit na | `src/lib/email-verification.ts` |
| Mobile number | Opsyonal | Mainland mobile number na nagsisimula sa `1[3-9]` at may 11 numero sa kabuuan; isang mobile number ay maaaring nakabuklod sa isang account lang | register route |

Mayroon ding tatlong third-party log-in button sa page: **Google, Watcha, Huawei account** (`GoogleSignInButton` /
`WatchaLoginButton` / `HuaweiLoginButton`). Ang mga third-party account ay walang lokal na password, kaya kung mag-log in gamit ang password mamaya ay makakatanggap ng
`该账号未设置密码，请使用其他方式登录` (walang nakatakdang password ang account na ito, gumamit ng ibang paraan ng pag-log in).

## Rate limit at anti-brute-force na mga parameter

| Gawi | Limitasyon | Pinagmulan |
|---|---|---|
| Pagpasa ng rehistro | **3 beses/minuto/IP**, 429 kapag lumampas | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Pagpapadala ng verification code | 1 beses/minuto bawat IP **at** 1 beses/minuto bawat email, 429 kapag lumampas; 60-segundong countdown sa front-end button | `src/app/api/auth/register/send-code/route.ts` |
| Beripikasyon ng code | Bawat email, maximum na **5 pagsubok** sa loob ng 10 minuto; sa pag-abot ng limitasyon, tatanggihan kahit tama ang code, kailangang magpadala muli ng code | `src/lib/email-verification.ts` |
| Pagpapadala ng code sa forgot password | 1 beses/minuto/IP | `src/app/api/auth/forgot-password/route.ts` |
| Log in | 5 beses/minuto/IP; **5 sunud-sunod na kabiguan sa parehong account ay maglilock sa loob ng 30 minuto** (423), na may pababang bilang ng natitirang pagsubok habang naka-lock | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Gawi sa proteksyon ng privacy**: kapag nagpapadala ng verification code / forgot password, kung nakarehistro na o hindi umiiral ang email, magbabalik ang endpoint ng parehong success message nang hindi isiniwalat kung nakarehistro na ang email.

## Katumbas ng agent-assisted mode at web registration

Ang mga script ng skill ay tumatawag sa **parehong hanay ng mga pampublikong API** (`/api/auth/register`, `send-code`, `login`,
`/api/auth/me`) at dumadaan sa eksaktong parehong validation, rate limit, at error path tulad ng form submission sa registration page — lahat ng
patakaran sa file na ito ay pantay para sa parehong mode. Para sa sequence at command contract ng script, tingnan ang `references/agent-flow.md`.

## Pagdaloy ng status pagkatapos ng matagumpay na rehistro

1. Naitatala ang gumagamit na may `accountStatus: 'pending'` at initial na **3 badge** (register route).
2. Sabay na nagtatanim ang server ng dalawang HttpOnly cookie: JWT (maaaring direktang i-access ang `/subscription`) at
   pendingUserToken (identity credential para sa subscription flow).
3. Kapag nadiskubre ng registration page ang `pending_payment` → tumalon sa `/subscription` (pinapanatili ang `next` return parameter);
   sa agent-assisted mode, ginagamit ang `me?token=…&redirect=/subscription` para makamit ang parehong epekto.
4. Pagkatapos ng bayad → nagiging `active` ang `accountStatus` (**ang Alipay ay awtomatikong nag-a-activate sa server-side sa pamamagitan ng notify**;
   ang PayPal ay awtomatiko sa pamamagitan ng Webhook; ang WeChat QR ay manual ang kumpirmasyon; ang Huawei IAP ay sa pamamagitan ng `activate-huawei`).
   Tingnan ang `payment-and-activation.md` para sa detalye.

Ang mga hindi pa naka-activate (pending) na gumagamit na tumatawag sa mga core API (feed, mapa, usapan sa digital na tao, check-in, at iba pa) ay palaging makakatanggap ng 403;
maliban sa mga share link ng post (nananatiling publiko at naa-access).

## Troubleshooting table para sa mga karaniwang error

| Sintomas | Dahilan | Ano ang gagawin |
|---|---|---|
| 「用户名已存在」 (may-ari na ang username) | Ginagamit na ang username (hindi case-sensitive) | Palitan ang username |
| 「邮箱已被使用」 (gamit na ang email) | Nakarehistro na ang email | Palitan ang email; o lumipat sa log in + 「忘记密码」 para mabawi ang lumang account |
| 「邮箱验证码错误或已过期」 (mali o expired na ang email verification code) | Mali ang pagkakatype / lampas 10 minuto / tinanggihan pagkatapos ng higit sa 5 pagsubok | I-click ang 「重新发送」, gamitin ang verification code mula sa **pinakabagong** email |
| Hindi dumating ang verification code | 60-segundong rate limit; o napunta sa spam/promotions | Maghintay hanggang matapos ang countdown bago magpadala muli; siyasatin ang spam folder |
| 「手机号已被使用」 (gamit na ang mobile number) | Nakabuklod na ang mobile number sa ibang account | Alisin ang mobile number (opsyonal) o palitan ang numero |
| 「注册请求过于频繁」 / 429 (sobrang dalas ng registration request / 429) | Nakaabot sa ceiling ang 3 beses/minuto/IP sa rehistro | Maghintay ng ilang minuto bago subukan muli |
| 409「用户名或邮箱已被注册」 (nakarehistro na ang username o email) | Sabay na pagbangga sa ibang tao sa sandali ng pag-submit (concurrency fallback) | Palitan ang username o email at subukan muli |
| 「图片大小不能超过5MB」/「不支持 SVG」 (hindi dapat lampas 5MB ang laki ng larawan / hindi suportado ang SVG) | Hindi angkop ang avatar | Palitan ang larawan o laktawan ang avatar |
| Matagumpay ang rehistro ngunit 403 sa log in 「请完成订阅以激活账户」 (kumpletuhin ang subscription para i-activate ang account) | Pending pa rin ang account (inaasahang status bago magbayad) | Bago magbayad: normal ito, kumpletuhin muna ang subscription; pagkatapos magbayad ay 403 pa rin: ibig sabihin lumang JWT ang ginamit; sa script mode, patakbuhin muna ang `refresh-login` para palitan ang log-in status ng bago |
| Log in 423「账户已锁定」 (naka-lock ang account) | 5 beses na mali ang password | Maghintay ng 30 minuto |
| Log in 401「还剩 N 次尝试机会」 (may natitira pang N na pagsubok) | Mali ang password, malapit nang ma-lock | Pag-isipang mabuti bago subukan muli, o diretso sa 「忘记密码」 |
| 「该账号未设置密码，请使用其他方式登录」 (walang nakatakdang password ang account na ito, gumamit ng ibang paraan ng pag-log in) | Third-party (Google/Watcha/Huawei) account | Mag-log in gamit ang orihinal na third-party button |
| 「该账号已注销」 (deactivated na ang account) | Na-deactivate ang account | Kailangang magrehistro muli |

## Mga tip sa log in (para sa pag-troubleshoot)

Sinusuportahan ng log in ang **username / email / mobile number** na tatlong-sa-isa na input (alinman sa tatlo ay maaaring gamitin bilang account name).
Forgot password: log-in page → 「忘记密码」 → i-enter ang registered email para tumanggap ng 6 na numerong verification code → i-reset.
