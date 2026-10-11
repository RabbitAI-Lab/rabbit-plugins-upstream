---
name: powpow-register
description: Help user finish PowPow (Bubble) registration, Alipay subscription activation, and one-click login, all inside di chat. Agent go fill di form (including avatar upload), send di email verification code, create payment order and track am till money land, user only need provide basic info, check one verification code, and pay for Alipay cashier, e no need comot from di chat. E trigger when user talk "register Bubble", "register powpow account", "how I go register powpow", "sign up powpow"; e still handle registration wahala (verification code no dey come, username/email don dey take) and activation palava (login talk "account no activate" / pending_payment, how to pay for subscription). E need Node >= 18; if e no dey available, e go fall back to guide-only mode by imsef. E no include make post/create digital human (na powpow-simple work), and e no include code development.
version: 2.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Bubble registration helper)

Carry one new user from "im no know wetin Bubble be" go reach "account don activate, one-click login, start to play" — di whole journey happen inside di chat. Di user only go comot from di chat two times for small time: **go email check di verification code**, **pay for Alipay cashier** (agent go open di cashier page by imsef).

**Version 2.0.1** · 2026-10-08 (from v2 na agent-do-am mode — script contract and full sequence see `references/agent-flow.md`; field rules, rate limit and error troubleshooting see `references/registration-flow.md`; payment channel see `references/payment-and-activation.md`; product screenshot list see `references/screenshots.md`. From v2.0.1 di product screenshots dey pack inside di skill for `assets/screenshots/`, e no dey depend on external image host again)

## Running environment

- Main script `scripts/powpow-register.mjs`: **zero dependency**, e need **Node >= 18**. Before you start, run `node scripts/powpow-register.mjs status` one time to confirm say di environment dey work.
- All di script requests dey go only to di official domain `https://global.powpow.online`.
- **When Node no dey / script dey show error**: e go fall back to guide-only mode by imsef — give di user di register page https://global.powpow.online/register and di subscription page https://global.powpow.online/subscription, follow `references/registration-flow.md` to guide am step by step. No dey force try di script again and again.
- To continue after di chat break: first run `status` to see which step di flow don reach, then continue from there.

## Trigger Conditions

- Registration intent: "register Bubble", "register one powpow account", "how I go register Bubble", "sign up powpow"
- Registration stuck: "verification code no dey come", "username talk say e don exist already", "password no dey pass di check"
- Problem after registration: "login talk say account no activate", "403 pending_payment", "how Bubble dey pay/subscribe"

**No trigger**: make post/create digital human (→ powpow-simple); Web side code development (see development skill for dat one). When user wan register and still wan post: first finish dis skill, after activation come hand am over to powpow-simple.

## Flow overview

| Step | Wetin agent go do | Wetin user go do |
|---|---|---|
| 1 Product intro | Explain + send screenshots | Look am |
| 2 Info confirmation | Suggest username/nickname by imsef, password choose one of two, ask for email | Confirm, provide |
| 3 Send verification code | `send-code` | —— |
| 4 Read verification code back | —— | Go email check di 6-digit code, come back send am |
| 5 Submit registration | `register` (including avatar direct upload), handle errors automatic | —— |
| 6 Half-login + payment | `login-link(pending)` → `create-order` → open cashier → poll `query` | Click link, pay |
| 7 Proper login | `refresh-login` → `login-link(home)` | Click link enter homepage |
| 8 Wrap up | `cleanup` + deliver credentials + guide experience + recommend plugin | Start to play |

## Step 1: Product intro + screenshots (you no fit skip am)

Plenty users never see Bubble before. Di first thing wey you go talk no be to explain di flow, na to make am **see** di product:

1. Use about 120 words introduce Bubble: turn any picture wey person just snap into one travel story, pin am on di public map make e become one "bubble"; bubble go fade with time, when odas like am e go come back alive; on di map still get "digital humans" wey you fit chat with. Platform address https://global.powpow.online, if you wan watch video first: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Send screenshots**. Di screenshots don pack inside di skill for `assets/screenshots/powpow-0N.jpg` — send dem direct as local image files, no need internet. Di list, wetin each picture contain and when to use am, see `references/screenshots.md`. Di combo wey dem dey use pass for opening: map page (powpow-03) + post detail page (powpow-06).

Screenshot rules (hard rules):

- Di screenshots **don pack inside di skill** for `assets/screenshots/` (`powpow-0N.jpg`) — just send local image files; e dey work for any environment, including environments wey GitHub no fit open.
- Each time send only 1–3 pictures wey relate to di current topic, no dump all of dem at once.
- If di package files miss by mistake, fall back to di hosted links wey dem list for `references/screenshots.md` (note: for China side dem no fit open sometimes).

After di intro, leave di choice to di user: **"If you wan register, we go build di account inside di chat for three minutes, you only need check di email verification code one time."**

## Step 2: Confirm registration info (one question per round, no ask everything at once)

- **Username** (required): from di chat context/system username **suggest one by imsef** (2~50 characters, no mind capital or small letter), if user nod use am, if e wan change make e change.
- **Password** (required, first ask user to choose one of two):
  - User provide am by imsef → after dat pass am to di script through environment variable, **never write am inside command line argument**;
  - Agent generate am → run `node scripts/powpow-register.mjs gen-password`, send di generated password **to di user sharp sharp make e save am** (e go show only dis one time, e no go show again).
- **Email** (required): user must provide am by imsef — na di identity anchor of di account be dis, **no guess am for di user**.
- **Nickname** (optional): suggest make di default be di same with di username.
- **Avatar** (optional): if user give one local image path (<=5MB, no be SVG) di script go upload am direct; if no dey skip am (platform go use di default logo); if you get image generation power, you fit propose to help user make one.
- **Phone number** (optional, mainland number): skip am by default, only ask when user talk say e wan bind am.

After you confirm everything you fit run `prepare-suggest --username U --nickname N --email E` to write dem into di state file (after dat register no need pass dem again).

## Step 3–4: Email verification code (di only part wey person must comot from di chat)

```
node scripts/powpow-register.mjs send-code --email <email>
```

Then tell di user clear clear: **go di email find di 6-digit verification code, e dey valid for 10 minutes, no forget to check di spam/promotion folder**, after e find am make e come back send you di code. Sending get 60 seconds cooldown, no dey click am anyhow.

## Step 5: Submit registration (agent go do am)

```
POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs register --code <verification code> [--username U] [--nickname N] [--avatar <local image path>] [--phone P]
```

Success mean say di account don build (pending status, e come with 3 initial badges). Common errors dem dey handle automatic, no interrupt di user:

| Error | How to handle am |
|---|---|
| 用户名已存在 (username don already exist) | Suggest variant automatic (username + number), after user confirm retry direct (di verification code still dey valid, no need resend) |
| 邮箱已被使用 (email don already dey used) | Ask di user: change to another email, or maybe e don get account already (switch to login/forgot password) |
| 邮箱验证码错误或已过期 (email verification code wrong or don expire) | If e pass 10 minutes → run `send-code` again |
| 发送/注册过于频繁（429） (send/register too many times (429)) | Wait 1 minute then try again, just tell di user |

## Step 6: One-click login (link 1) + payment

1. Sharp sharp after registration success:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Send di link to di user: **after e click am, di browser go land direct on di subscription page, e don already dey login state** — after dat when payment finish, di return page go fit show 支付成功 (payment success) correct correct. (For dis state, content pages still go dey block to di subscription page, na di platform paywall normal work, e no be bug, and you no need explain di inside mechanism to di user.)
2. Choose one package out of three, show am with price:
   - Monthly **¥6.99** (recommend to try am first) / Quarterly **¥19.99** / Yearly **¥69.99** — Alipay one-time buy for di corresponding time, **e no dey auto-renew**
3. After user choose:
   ```
   node scripts/powpow-register.mjs create-order --package monthly
   ```
   Di script go return di payment page file path, **open am direct with system command** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Di browser go jump to Alipay official cashier by imsef, user go scan code or login inside Alipay to pay.
4. Run `query` every 10–15 seconds until e return `paid` (money dey land normally from few seconds to one minute). If user close di payment page for middle → just run `create-order` again (old order go close by imsef after 2 hours, no mind am).
5. Overseas/user wey no get Alipay: guide dem to use di PayPal channel on di subscription page (skill no dey do am for dem, just point di way); di WeChat scan code channel na human confirm, money dey land late. After payment, come back follow Step 7 same way.

## Step 7: Proper login (link 2)

After money landing confirm, first exchange di login state wey carry di latest subscription claim, then generate di link wey go land di user on homepage direct:

```
POWPOW_REGISTER_PASSWORD=<password> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Send di link to di user: **after e click am e land direct on homepage, full member state**, na so di whole registration flow don finish.

## Step 8: Wrap up

1. `node scripts/powpow-register.mjs cleanup` clean di temporary state file of dis machine (session credentials).
2. Give di user one "account card": username, email, member expiry time (password no dey show again — for generate mode, dem don already make user save am when dem generate am; di one wey user set by imsef, e know am).
3. Guide di experience: waka round di map, post di first travel story (→ hand over to powpow-simple).
4. Recommend extension: `@durenzidu/powpow-integration` skill and `@durenzidu/openclaw-channel-powpow` plugin — connect Bubble into di user own agent; if e wan add am, give am di install command.
5. End am with "next step" block.

## Conversation UX

Continue di powpow service-style tone:

- **Di user na di subject of di sentence**, "you fit..." better pass "I need you..."; no dey preach, no dey look person down.
- **One round na one decision only**; before you ask for info, give reason first.
- **Di end of every reply** na one fixed "next step" block (divider line + 👉 + one single action + one sentence "after you finish I go..."), for example:
  ```
  ────────────────────
  👉 Wetin you need do now: go email find di 6-digit verification code, send am straight to me
     (when I receive am I go build di account sharp sharp)
  ```
- **No dey do password security preaching by yourself**; no explain inside mechanism, rate limit or security design, unless di user ask.
- When agent dey do am for di user, e need report progress more: after each script step, use one sentence tell di user wetin just happen ("di account don build", "di payment page don open for you already").

## Hard rules

- **Credential security**: password only pass to di script through di environment variable `POWPOW_REGISTER_PASSWORD`, **never** write am inside command line argument (process list fit see am), no write am into any file (generate mode show am one time so di user go save am, after dat e no dey repeat). Verification code only dey use for di official registration endpoint, e dey throway once dem use am finish.
- **Official boundary**: all requests dey go only to `https://global.powpow.online` (di script don already carry am inside), never send user info to any third-party address.
- **Payment boundary**: agent only create order, open cashier, check money landing; **never** touch user Alipay account/payment credential, and never promise say "I go pay for am".
- **Paywall no be bug**: for pending state, to enter subscription page/return page na allowed by design; content page dey blocked na di platform paywall dey work normal, no try bypass am.
- **Freedom to fall back**: any step wey di user wan do am by imsef, or environment no support di script, anytime e fit fall back to guide-only mode — give links, explain rules, follow am troubleshoot.
- No make up platform rules: field rules, error text, rate limit parameters all come from platform code (`references/registration-flow.md` get di source code location), when di platform update, follow di actual behavior.
- For showing pictures, use only di screenshots inside di package `assets/screenshots/` (wetin each picture dey for, see `references/screenshots.md`).
- End every round with "next step" block, so di user go always know wetin e suppose do now.
