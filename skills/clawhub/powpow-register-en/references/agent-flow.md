# Agent-Assisted Flow and Script Contract — powpow-register

Execution details for each step of SKILL.md. All commands are `node scripts/powpow-register.mjs <subcommand> [args]`,
the script is **zero-dependency** and requires **Node ≥ 18**, and all requests go to `https://global.powpow.online` only.

## Security Design (why it's built this way)

| Design | Reason |
|---|---|
| The password is passed only via the `POWPOW_REGISTER_PASSWORD` environment variable | Process command-line arguments are visible to other processes on the same machine (argv leak surface); the environment variable is read inside the script and used immediately |
| The password is **never written to the state file** and never appears in logs | The state file may persist on disk; in generated mode it's shown once in the conversation only so the user can save it |
| The state file lives in the system temp directory (`os.tmpdir()/powpow-register-state.json`, 0600) | Contains only five fields — email / username / nickname / token / outTradeNo; `cleanup` removes it in one shot |
| The JWT obtained by the agent is exchanged for browser cookies via the official `me?token=` endpoint | The platform's official bridge designed for the HarmonyOS WebView; signature verification checks signature + validity only, no device fingerprint binding, so the user's browser can use it |
| Payment only does create-order / query / opening the cashier | The payment action and payment credentials always stay between the user and the official Alipay cashier; the agent never handles them |

## Command Reference

| Command | Key arguments | Purpose / when |
|---|---|---|
| `status` | —— | Check flow progress (reads the state file); run this first after an interrupted conversation |
| `gen-password` | —— | Generate a 24-character strong password (upper + lower case + digits), shown on stdout **once only** |
| `prepare-suggest` | `--username --nickname --email` | Record the confirmed info into the state file (register won't need them again afterwards) |
| `send-code` | `--email` | Trigger the platform to send the 6-digit code (valid 10 minutes, 60s cooldown) |
| `register` | `--code` (required); `--username --nickname --avatar --phone` (optional; skip if already in the state file) | Create the pending account; the password goes through the `POWPOW_REGISTER_PASSWORD` environment variable; on success the JWT is stored into the state file automatically |
| `login-link` | `--target pending` or `--target home` | Generate the one-click login link (dual-link design, see below) |
| `create-order` | `--package monthly\|quarterly\|yearly` (Alipay default)<br>`--provider alipay\|paypal` | Creates the payment order; Alipay returns the payment page file path + outTradeNo; PayPal returns the authorization page file path + subscriptionId (recorded into the state file automatically) |
| `query` | —— | Checks the order/subscription status. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; poll every 10–15s |
| `refresh-login` | password via environment variable | Log in again to get a **new JWT** (subscription claim changes from NONE to ACTIVE); must run after payment arrives |
| `whoami` | —— | Use the token in the state file to check the account and subscription status (verify the activation took effect) |
| `cleanup` | —— | Delete the state file (must run at wrap-up) |

**Passing the environment variable** (the password never goes on the command line):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<password>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<password>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<password> && node scripts/powpow-register.mjs register --code 123456
```

## Dual-Link Mechanism (core design)

The platform login state is an HttpOnly cookie; the agent can't plant a cookie into the browser directly. The bridge is the official
`/api/auth/me?token=<JWT>&redirect=<in-site path>` endpoint: verify signature → auto-create a session for pending users →
`Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 days) → validate the
redirect (must start with a single slash, `//` and backslashes forbidden, parsed host must be same-origin) → 307 temporary redirect to the target page.

- **Link 1 (given immediately after successful registration)**: `--target pending` → lands on `/subscription`.
  The user's browser enters a "half-logged-in" state: the subscription page and the Alipay return page are visible and usable; content pages are still walled
  back to the subscription page (three protection layers: JWT claims gateway check → DB re-check → core API check; this is normal behavior).
- **Link 2 (given after `paid` is confirmed)**: first `refresh-login` to get a new JWT (payment only updates the DB, it doesn't change the
  claims of an already-issued JWT — skipping the refresh looks like "paid but no membership"), then `--target home` → lands on the home page
  with full membership status.

## Full Sequence (happy path)

```
1.  status                          # environment self-check
2.  (Step 2: confirm info in conversation, password choice of two; generated mode: gen-password → have the user save it immediately)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → user checks inbox for the code (the only leave-the-conversation moment ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → Link 1 sent to the user
7.  (user picks a payment method)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <payment page file>       # Windows; macOS uses open, Linux uses xdg-open
    # → user completes payment/authorization at the Alipay/PayPal cashier (leave-the-conversation moment ②)
9.  query (every 10–15s) until paid / ACTIVE
10. refresh-login                   # get the new JWT with the ACTIVE claim
11. login-link --target home        # → Link 2 sent to the user
12. whoami                          # confirm subscriptionStatus: ACTIVE (optional)
13. cleanup                         # remove the state file
```

## Command → Platform API Mapping

| Script command | Platform endpoint |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, direct avatar upload) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (the link itself; takes effect when the browser opens it) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Where the rules come from: registration fields and rate limits in `registration-flow.md`; plans and the activation chain in
`payment-and-activation.md` (both cite the platform source files).

## Script-Level Error Handling

| Symptom | Handling |
|---|---|
| `Node version too low` | Fall back to pure guidance mode; don't keep trying |
| Network error / timeout | Retry once; if it still fails, have the user check the network and continue (the state file is still there; run `status` from the top to resume) |
| register returns a business error (username already exists, etc.) | Handle per the table in Step 5 of SKILL.md; **no need to resend the verification code** (still valid within 10 minutes) |
| register returns "email verification code incorrect or expired" | Timed out → `send-code` again |
| User closed the payment page after `create-order` | Just `create-order` again (the old order auto-closes after 2h; PayPal PENDING subscriptions expire after 1h) |
| `create-order --provider paypal` returns 409 | There is already an unfinished PayPal subscription; wait 1h for it to expire, or complete the old authorization in the browser |
| `query` stays pending / PENDING | The user may not have paid; ask. If they really paid → follow the troubleshooting table in payment-and-activation.md |
| `refresh-login` 403 `pending_payment` | Payment/authorization hasn't arrived yet; go back to step 9 and keep polling |
| State file lost (accidentally deleted / different machine) | `whoami`/`refresh-login` are unusable; have the user refresh the subscription page directly in the browser that opened Link 1 to check the status, or log in again (web mode) |

## Fallback Mode (pure guidance)

Fall back to the v1-style pure guidance immediately — stop wrestling with the script — when any of these happens:

- No Node ≥ 18, or the script fails the same way twice in a row;
- The user explicitly says "I'll do it myself on the website";
- Company/device policy restricts the script's network access.

After falling back: give the registration page https://global.powpow.online/register and the subscription page
https://global.powpow.online/subscription, walk alongside the user per the rules in `registration-flow.md` and help troubleshoot,
keep the same tone, and still end every turn with a "next step" block.
