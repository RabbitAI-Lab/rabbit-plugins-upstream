# Agent do-am flow and script contract — powpow-register

Execution details for each step of SKILL.md. All commands na `node scripts/powpow-register.mjs <sub-command> [parameters]`, di script **zero dependency**, e need **Node >= 18**, all requests dey go only `https://global.powpow.online`.

## Security design (why dem design am like dis)

| Design | Reason |
|---|---|
| Password only pass in through di environment variable `POWPOW_REGISTER_PASSWORD` | Di command line arguments of a process fit dey visible to other processes on di same machine (argv leak surface), di environment variable inside di script dem read am and use am sharp sharp |
| Password **never write into state file**, never show inside log | Di state file fit remain on disk; inside di chat, di generate mode show am once only so di user go save am |
| Di state file dey store for di system temporary directory (`os.tmpdir()/powpow-register-state.json`, 0600) | E only contain five fields: email / username / nickname / token / outTradeNo, `cleanup` go clear am one click |
| Di JWT wey agent collect, dem exchange am for browser cookie through di official `me?token=` endpoint | Na di official bridge wey di platform build for Harmony WebView; di signature check only check signature + validity period, e no bind device fingerprint, di user browser fit use am |
| Payment only do create-order / query / open cashier | Di payment action and payment credential always dey between di user and di Alipay official cashier, agent no dey pass through am |

## Command reference

| Command | Key parameters | Work / when |
|---|---|---|
| `status` | —— | Check di flow progress (read di state file); after chat break, run dis one first |
| `gen-password` | —— | Generate 24-character strong password (contain capital + small letter and number), e show for stdout **only dis one time** |
| `prepare-suggest` | `--username --nickname --email` | Write di confirmed info into di state file (after dat register no need pass dem again) |
| `send-code` | `--email` | Trigger di platform to send 6-digit verification code (e dey valid 10 minutes, 60s cooldown) |
| `register` | `--code` (required); `--username --nickname --avatar --phone` (optional, if di state file get dem, no need pass am) | Build pending account; password pass through `POWPOW_REGISTER_PASSWORD` environment variable; after success di JWT go save into di state file automatic |
| `login-link` | `--target pending` or `--target home` | Generate one-click login link (two-link design, see below) |
| `create-order` | `--package monthly\|quarterly\|yearly` | Create Alipay order; e return payment page file path + outTradeNo (e dey write into di state file automatic) |
| `query` | —— | Check di order status `paid / pending / closed / unknown` (outTradeNo dey come from di state file), poll every 10–15s |
| `refresh-login` | Password pass through environment variable | Login again to change to **new JWT** (di subscription claim change from NONE to ACTIVE), you must run am after money land |
| `whoami` | —— | Use di token inside di state file to check di account and subscription status (verify whether di activation don work) |
| `cleanup` | —— | Delete di state file (you must run am at di end) |

**Environment variable passing** (password never enter command line):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<password>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<password>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<password> && node scripts/powpow-register.mjs register --code 123456
```

## Two-link mechanism (core design)

Di platform login state na HttpOnly cookie, agent no fit plant cookie for di browser direct; di bridge na di official `/api/auth/me?token=<JWT>&redirect=<inside-site path>` endpoint: check signature → for pending user e build session for am automatic → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 days) → check redirect (e must start with single slash only, `//` and backslash dey banned, after parsing e must be same origin) → 307 temporary redirect to di target page.

- **Link 1 (give am sharp sharp after registration success)**: `--target pending` → e land on `/subscription`.
  Di user browser enter "half-login" state: subscription page and Alipay return page dey visible and fit use; content pages still dey block back to di subscription page by di paywall (three layers of protection: JWT claims gateway check → DB check again → core API check, na normal behavior).
- **Link 2 (give am after you confirm paid)**: first `refresh-login` change to new JWT (payment only update DB, e no change di claims of di JWT wey dem don already issue; if you no change am e go behave like "you pay but you no get member"), then `--target home` → e land on homepage, full member state.

## Full sequence (normal path)

```
1.  status                          # environment self-check
2.  (Step 2 chat confirm di info, password choose one of two; generate mode: gen-password → make di user save am sharp sharp)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → user go email check di code (di only part to comot from chat ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → link 1 send to di user
7.  (di user choose package) create-order --package monthly
8.  start <payment page file>       # Windows; macOS use open, Linux use xdg-open
    # → di user pay for Alipay cashier (comot from chat part ②)
9.  query (every 10–15s) until paid
10. refresh-login                   # change to new JWT wey carry ACTIVE claim
11. login-link --target home        # → link 2 send to di user
12. whoami                          # confirm subscriptionStatus: ACTIVE (optional)
13. cleanup                         # clear di state file
```

## Command → platform API mapping

| Script command | Platform endpoint |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, avatar direct upload) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (na di link itself, e work when di browser click am) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Where di rules come from: registration fields and rate limit see `registration-flow.md`; packages and activation chain see `payment-and-activation.md` (dem all mark di platform source code file).

## Script-level error handling

| Wetin you see | How to handle am |
|---|---|
| `Node 版本过低` (Node version too low) | Fall back to guide-only mode, no force try |
| Network error / timeout | Retry one time; if e still fail, make di user check di network then continue (di state file still dey, run `status` from di start to recover) |
| register report business error (用户名已存在 etc.) | Handle am with di table for SKILL.md Step 5, **no need resend di verification code** (e still dey valid within 10 minutes) |
| register report 邮箱验证码错误或已过期 | If e timeout → run `send-code` again |
| After `create-order` di user close di payment page | Just run `create-order` again (old order go close automatic after 2h) |
| `query` dey pending anyhow | Di user fit be say e no pay yet; ask am one question. If e truly pay → follow di troubleshooting table for payment-and-activation.md |
| `refresh-login` 403 `pending_payment` | Payment no land yet, go back to Step 9 continue polling |
| Di state file lost (hand slip delete am / change machine) | `whoami`/`refresh-login` no fit work; make di user for di browser wey don open link 1 before, refresh di subscription page direct to confirm di status, or login again (web mode) |

## Fall back mode (guide only)

For any of di following situations, fall back to v1-style guide-only sharp sharp, no dey disturb di script again:

- No get Node >= 18 or di script fail two times straight with di same kind of failure;
- Di user talk am clear say "I go do am myself for di web";
- Company/device policy no allow di script to connect internet.

After fall back: give di register page https://global.powpow.online/register and di subscription page https://global.powpow.online/subscription, follow di rules for `registration-flow.md` to follow am troubleshoot, di tone no change, every round still end with "next step" block.
