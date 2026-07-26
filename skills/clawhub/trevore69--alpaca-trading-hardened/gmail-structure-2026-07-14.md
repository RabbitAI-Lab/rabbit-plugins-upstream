# Gmail Structure — 14 July 2026

## Snapshot
- **Account:** Trevor Ellish
- **Unread in inbox:** ~201
- **Visible sample:** 20 most recent unread + 1 read (Fortinet)
- **Existing labels:** `INBOX/LinkedIn`, `INBOX/Finance`, `INBOX/Jobs`, `INBOX/iGaming`, `INBOX/Newsletters`, `INBOX/Tech`, `Work`, `Receipts`, `Idiot`

---

## 🚨 Action Required / Security
These need a human decision now.

| From | Subject | Time | Suggested Action |
|------|---------|------|------------------|
| Google | Security alert | 08:31 GMT | **Open and verify** — account activity alert |
| Anthropic | Security alert: new trusted device added to your Claude account | 07:23 UTC | Verify it was you; two duplicate alerts |
| Anthropic | Security alert: new trusted device added to your Claude account | 07:23 UTC | Same as above |
| Anthropic | Security alert: new passkey added to your Claude account | 07:23 UTC | Verify passkey addition |
| Discovery Bank | Discovery Bank Email for your attention | 01:18 SAST | Likely statement/notice; open and file under `INBOX/Finance` |

---

## 💼 Jobs / Recruitment
Mostly automated job alerts. Batch-read or filter into `INBOX/Jobs`.

| From | Subject | Time |
|------|---------|------|
| LinkedIn Job Alerts | Security Engineer at Check Point Software | 06:32 UTC |
| Indeed | Network Engineer @ Colibri Recruitment | 06:27 UTC |
| Emma Jacobs from Pnet | Paradigm Recruitment (PTY) LTD and 12 other companies are looking | 01:08 UTC |
| Emma Jacobs from Pnet | Moksh Infotech Private Limited is looking | 01:07 UTC |
| Emma Jacobs from Pnet | Data Monkey (PTY) LTD and 2 other companies are looking | 01:06 UTC |
| Emma Jacobs from Pnet | Data Monkey (PTY) LTD and 11 other companies are looking | 01:04 UTC |

**Pattern:** Pnet is flooding with near-identical alerts. Consider a filter to skip inbox for Pnet unless subject contains a specific company/role.

---

## 💰 Finance / Investments
| From | Subject | Time | Label |
|------|---------|------|-------|
| Discovery Bank | Discovery Bank Email for your attention | 01:18 SAST | `INBOX/Finance` |
| The Motley Fool | Latest News from My Stocks | 23:16 UTC | `INBOX/Finance` |
| The Motley Fool | Here are $2 million reasons to join us… | 00:06 UTC | `INBOX/Finance` (promo) |
| The Motley Fool | Did you miss this earlier today, Trevor? | 19:38 UTC | `INBOX/Finance` (promo) |

---

## 📰 Newsletters / Education
| From | Subject | Time | Label |
|------|---------|------|-------|
| Udemy Instructor: School of AI | This Is What Top 1% AI Builders Are Doing Differently | 04:39 UTC | `INBOX/Newsletters` |
| Apollo | New France & Italy consent rules for email tracking | 21:55 UTC | `INBOX/Tech` or `INBOX/Newsletters` |

---

## 🛒 Promotions / Retail
Delete or batch-archive these. They age fast.

| From | Subject | Time |
|------|---------|------|
| Michael Kors | These Getaway Styles Are Calling Your Name | 08:05 UTC |
| Checkers Xtra Savings | Trevor, it’s Your Last Chance to SAVE 🚨 | 06:44 UTC |
| One Deal A Day | Create Your Dream Office | 10:45 IST |
| Samurai Guitar Theory | 🎸 Your free Guitar Theory Reference Guide is Inside | 19:04 UTC |
| Fortinet | [Register Today] The Invisible Leak: Catching Shadow SaaS and GenAI Data Loss | 04:09 EDT |

---

## 🏷️ Suggested Filters to Auto-Structure Incoming Mail
These use your existing labels.

1. **Pnet job alerts** → label `INBOX/Jobs`, skip inbox
   - From: `info@jobalerts.pnet.co.za`

2. **LinkedIn Job Alerts** → label `INBOX/LinkedIn`, skip inbox
   - From: `jobalerts-noreply@linkedin.com`

3. **Indeed job alerts** → label `INBOX/Jobs`, skip inbox
   - From: `donotreply@match.indeed.com`

4. **Discovery Bank / Motley Fool** → label `INBOX/Finance`, skip inbox
   - From: `no-reply@discoverybank.co.za`, `*@motley.fool.com`, `*@premiuminfo.fool.com`

5. **Udemy / Apollo / tech newsletters** → label `INBOX/Newsletters` or `INBOX/Tech`
   - From: `no-reply@e.udemymail.com`, `support@apollo.io`

6. **Retail/promos** → label `CATEGORY_PROMOTIONS` (already happening), skip inbox
   - From: `MichaelKors@michaelkorsmail.com`, `hello@mail.checkers.co.za`, `noreply@onedealaday.co.za`, `info@samuraiguitartheory.com`, `info@global.fortinet.com`

7. **Anthropic security alerts** → label `INBOX/Tech` + keep in inbox
   - From: `*@mail.anthropic.com`

---

## ✅ Immediate Cleanup Suggestion
1. Read the 4 security alerts (Google + 3 Anthropic).
2. Open the Discovery Bank email.
3. Select all Pnet, LinkedIn, Indeed, Motley Fool, Michael Kors, Checkers, One Deal A Day, Samurai Guitar, Fortinet → **Archive** or **Delete**.
4. This would clear roughly **15–16** of the 20 visible unread messages instantly.

---

## Raw Data
- Raw unread list saved in session context.
- Fetched via `maton google-mail message list --query 'is:unread' --hydrate --json`.
