# Registration Process Full Detail — powpow-register

Na for error checking you go open this one. All the rules come from platform source code (Next.js frontend/backend consistency check), dem note source.
If platform update, use the real online behavior as standard.

## Entrances

- Registration page: https://global.powpow.online/register
- Login page: https://global.powpow.online/login
- Subscription page: https://global.powpow.online/subscription
- If you enter from share link wey get `?next=...`, after registration + payment finish, e go jump back to the original page automatic.

## Form Fields and Rules

| Field | Compulsory | Rule | Source |
|---|---|---|---|
| Profile picture | Optional | picture ≤5MB, e no support SVG; server dey compress am automatic (>100KB e go compress am to 400×400 / quality 90) | `src/app/api/auth/register/route.ts` |
| Username | Compulsory | 2~50 characters, after trim dem save am **small letter** (Tom and tom na same username, both registration and login side no dey care big/small letter) | Same as above (zod schema) |
| Password | Compulsory | 8~100 characters, e must get big letter, small letter, number | Same as above |
| Confirm password | Compulsory | e must match the password (frontend check only) | `src/app/(public)/register/page.tsx` |
| Nickname | Optional | ≤100 characters; if no fill, default na username | register route |
| Email | **Compulsory** | valid email format, ≤255 characters; one email fit register only one account | register route |
| Email verification code | **Compulsory** | 6 numbers; **e dey valid for 10 minutes**; once e don verify, e don finish; if you resend am, dem go mark old code as don use | `src/lib/email-verification.ts` |
| Phone number | Optional | mainland China phone number wey start with `1[3-9]`, total 11 digits; one number fit tie only one account | register route |

The page still get three third-party login buttons: **Google, Watcha, Huawei account** (`GoogleSignInButton` /
`WatchaLoginButton` / `HuaweiLoginButton`). Third-party account no get local password, if you later use password to login, you go get
"该账号未设置密码，请使用其他方式登录" (this account never set password, make you use other method to login).

## Rate Limit and Anti-Bruteforce Parameters

| Behavior | Limit | Source |
|---|---|---|
| Registration submit | **3 times/minute/IP**, if you pass am na 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Send verification code | same IP 1 time/minute **and** same email 1 time/minute, if you pass am na 429; frontend button get 60-second countdown | `src/app/api/auth/register/send-code/route.ts` |
| Verification code check | each email within 10 minutes max **5 tries**, if you reach the limit even the code correct dem go reject am, you need resend code | `src/lib/email-verification.ts` |
| Forgot-password code send | 1 time/minute/IP | `src/app/api/auth/forgot-password/route.ts` |
| Login | 5 times/minute/IP; same account wey fail consecutively **5 times go lock 30 minutes** (423), during that time e go show remaining tries wey dey go down | `src/app/api/auth/login/route.ts`、`rate-limit.ts` |

**Privacy protection behavior**: when you send verification code / forgot password, whether the email don register or e no dey, the API go return the
same success text, e no go leak whether email don register or not.

## Status Change After Registration Success

1. Dem save the user with `accountStatus: 'pending'`, first **3 badges** (register route).
2. Server dey plant two HttpOnly cookies at the same time: JWT (e fit access `/subscription` direct) and
   pendingUserToken (identity credential for subscription process).
3. Registration page dey detect `pending_payment` → e go jump `/subscription` (e dey keep the `next` return parameter).
4. Payment don finish → `accountStatus` go become `active` (PayPal dey activate am automatic through Webhook; WeChat scan QR na
   manual confirm; Huawei IAP go through `activate-huawei`). Full detail see `payment-and-activation.md`.

User wey never activate (pending) wey dey call core API (feed, map, digital pesin talk, check-in, etc.) go get 403 all of dem;
except shared post links (dem keep am public, anybody fit open am).

## Common Error Checking Table

| Symptom (original Chinese error text) | Cause | Wetin to Do |
|---|---|---|
| 「用户名已存在」 (Username don already dey) | username don dey use (e no dey care big/small letter) | change to another username |
| 「邮箱已被使用」 (Email don already dey use) | email don already register | change email; or go through login + "forgot password" to recover old account |
| 「邮箱验证码错误或已过期」 (Email verification code wrong or don expire) | code type am wrong / pass 10 minutes / try wrong pass 5 times dem reject am | click "Resend", use the code from the **latest email** |
| Verification code no dey come | e don hit 60-second rate limit; or e enter spam/ads folder | wait countdown finish before you send again; open the spam folder |
| 「手机号已被使用」 (Phone number don already dey use) | phone number don tie to another account | remove the phone number (optional) or change number |
| 「注册请求过于频繁」/ 429 (Registration request too frequent) | you don reach registration limit 3 times/minute/IP | wait some minutes then try again |
| 409「用户名或邮箱已被注册」 (Username or email don already register) | the name jam another person at the exact time you submit (concurrency fallback) | change username or email then try again |
| 「图片大小不能超过5MB」/「不支持 SVG」 (Picture size no fit pass 5MB / No support SVG) | profile picture no follow the rule | change picture or skip profile picture |
| Registration success but login 403「请完成订阅以激活账户」 (Make you finish subscription to activate account) | account still dey pending | after login follow the hint for the page go `/subscription` finish the subscription |
| Login 423「账户已锁定」 (Account don lock) | password wrong 5 times consecutively | wait 30 minutes |
| Login 401「还剩 N 次尝试机会」 (N tries remain) | password wrong, e dey close to lock | think well before you try, or go "forgot password" direct |
| 「该账号未设置密码，请使用其他方式登录」 (This account never set password, make you use other method to login) | third-party account (Google/Watcha/Huawei) | use the original third-party button to login |
| 「该账号已注销」 (This account don deactivate) | the account don deactivate | you need to register again |

## Small Login Knowledge (for error checking too)

Login dey support three-in-one input **username / email / phone number** (any one of dem fit be account name).
Forgot password: login page → "forgot password" → enter the registered email to receive 6-digit verification code → reset am.