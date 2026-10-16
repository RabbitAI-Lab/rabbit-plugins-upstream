# Registration flow full detail — powpow-register

For when you dey troubleshoot problem. All di rules come from di platform source code (Next.js front-back consistency check), dem mark where dem come from. When di platform update, follow di online actual behavior.

## Entry points

- Register page: https://global.powpow.online/register
- Login page: https://global.powpow.online/login
- Subscription page: https://global.powpow.online/subscription
- If you enter from share link or any link wey carry `?next=...`, after registration + payment finish e go jump back to di original page automatic.

## Form fields and rules

| Field | Required | Rule | Source code location |
|---|---|---|---|
| Avatar | Optional | Image <=5MB, SVG no dey supported; di server compress am automatic (when e pass 100KB e compress am to 400×400 / quality 90) | `src/app/api/auth/register/route.ts` |
| Username | Required | 2~50 characters, after trim e convert to **small letter** to store (Tom and tom dem count as di same username, register side and login side no mind capital or small letter) | Same as above (zod schema) |
| Password | Required | 8~100 characters, e must contain capital letter, small letter and number at di same time | Same as above |
| Confirm password | Required | E must match di password (only front-end check am) | `src/app/(public)/register/page.tsx` |
| Nickname | Optional | <=100 characters; if you no fill am, e take di username by default | register route |
| Email | **Required** | Valid email format, <=255 characters; one email fit register only one account | register route |
| Email verification code | **Required** | 6 digits; **e dey valid for 10 minutes**; once verification succeed e no dey valid again; resend go mark di old code as don use | `src/lib/email-verification.ts` |
| Phone number | Optional | Mainland phone number start with `1[3-9]`, 11 digits total; one phone number fit bind only one account | register route |

Di page still provide three third-party login buttons: **Google, Watcha, Huawei account** (`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Third-party accounts no get local password, if you later use password to login e go give you 该账号未设置密码，请使用其他方式登录 (dis account no set password, please use another way to login).

## Rate limit and anti-bruteforce parameters

| Behavior | Limit | Location |
|---|---|---|
| Registration submit | **3 times/minute/IP**, when e pass am 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Send verification code | Same IP 1 time/minute **and** same email 1 time/minute, when e pass am 429; front-end button 60 seconds countdown | `src/app/api/auth/register/send-code/route.ts` |
| Verification code check | Per email, within 10 minutes maximum try **5 times**, when e reach di limit even if di code correct dem go reject am, you need send new code | `src/lib/email-verification.ts` |
| Forgot password send code | 1 time/minute/IP | `src/app/api/auth/forgot-password/route.ts` |
| Login | 5 times/minute/IP; same account fail straight **5 times e lock for 30 minutes** (423), during dat time di remaining count dey reduce as e show | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Privacy protection behavior**: when you send verification code / forgot password, if di email don register already or e no exist, di endpoint go return success message same way, e no leak whether di email don register.

## Agent do-am mode and web registration equivalence

Di skill script dey call **di same set of public APIs** (`/api/auth/register`, `send-code`, `login`, `/api/auth/me`), e follow di exact same check, rate limit and error path as di registration page form submit — all di rules for dis file apply to di two modes same same. Script sequence and command contract see `references/agent-flow.md`.

## Status flow after registration success

1. Dem store di user with `accountStatus: 'pending'`, initial **3 badges** (register route).
2. Di server plant two HttpOnly cookies at di same time: JWT (fit access `/subscription` direct) and pendingUserToken (di subscription flow identity credential).
3. When di registration page see `pending_payment` → e jump to `/subscription` (e keep di `next` return parameter); for agent do-am mode use `me?token=…&redirect=/subscription` to get di same effect.
4. Payment finish → `accountStatus` change to `active` (**Alipay pass notify, server-side activate automatic**; PayPal pass Webhook activate automatic; WeChat scan code na human confirm; Huawei IAP pass `activate-huawei`). Full detail see `payment-and-activation.md`.

User wey no activate (pending) calling core API (feed, map, digital human chat, check-in etc.) na 403 all di time; except share post link (e stay public and fit access).

## Common error troubleshooting table

| Wetin you see | Why e happen | Wetin to do |
|---|---|---|
| 「用户名已存在」 (username don already exist) | Di username don dey taken (no mind capital or small letter) | Change to another username |
| 「邮箱已被使用」 (email don already dey used) | Di email don register before | Change email; or switch to login + 忘记密码 (forgot password) to recover di old account |
| 「邮箱验证码错误或已过期」 (email verification code wrong or don expire) | Code type wrong / pass 10 minutes / try wrong pass 5 times dem reject am | Click 重新发送 (resend), use di verification code of di **latest** email |
| Verification code no dey come | 60 seconds rate limit; or e enter spam/promotion folder | Wait make di countdown finish then send again; search di spam mail folder |
| 「手机号已被使用」 (phone number don already dey used) | Di phone number don bind another account | Remove di phone number (e optional) or change number |
| 「注册请求过于频繁」 (registration request too many)/ 429 | Registration 3 times/minute/IP reach di top | Wait few minutes then try again |
| 409「用户名或邮箱已被注册」 (409 username or email don already register) | At submit moment e clash with another person (concurrency safety) | Change username or email then retry |
| 「图片大小不能超过5MB」/「不支持 SVG」 (picture size no fit pass 5MB / SVG no dey supported) | Avatar no correct | Change picture or skip di avatar |
| Registration success but login 403「请完成订阅以激活账户」 (please complete subscription to activate account) | Di account still dey pending (di expected state before payment) | Before payment: dis one normal, first finish di subscription; after payment still 403: e mean say di old JWT dey use, for script mode first `refresh-login` change to new login state |
| Login 423「账户已锁定」 (account don lock) | Password wrong 5 times straight | Wait 30 minutes |
| Login 401「还剩 N 次尝试机会」 (N try chance remain) | Password wrong, e near lock | Think well before you try again, or go 忘记密码 (forgot password) direct |
| 「该账号未设置密码，请使用其他方式登录」 (dis account no set password, please use another way to login) | Third-party (Google/Watcha/Huawei) account | Use di original third-party button to login |
| 「该账号已注销」 (dis account don deactivate) | Di account don deactivate | E need register again |

## Login small knowledge (for troubleshooting too)

Login support **username / email / phone number** three-in-one input (any one of di three fit serve as account name). Forgot password: login page → 忘记密码 (forgot password) → enter di register email receive 6-digit verification code → reset.
