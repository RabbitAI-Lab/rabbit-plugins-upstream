# Gmail Inbox Structure Report

**Account:** trevorellish@gmail.com  
**Date:** 2026-07-14  
**Connection:** Maton (ACTIVE)

## Summary
- **Visible via Maton connection:** ~201 messages in inbox (new mail arriving during cleanup)
- **You mentioned total mailbox:** ~7,000 messages — this Maton OAuth connection only exposes the inbox; archived/sent/trash/spam and the rest of the 7k are not visible here.
- **Processed:** first 100 unread inbox messages
  - 63 labels applied, 0 failures
  - 13 promotional/shopping emails marked as read
  - 4 security alerts tagged with `INBOX/Security`
- **Additional batches completed:**
  - ~49 Michael Kors emails marked read
  - ~37 Pick n Pay emails marked read
  - ~49 Fortinet emails marked read
  - ~49 Samurai Guitar emails marked read
  - 50 additional promotional senders marked read (Vodacom, VALR, FxPro, Humble Bundle, Overloud, DCS World, Audible, DBG, MyClaw Newsletter)
  - 50 LinkedIn, 50 Jobs, 50 Finance, 50 Newsletters, 50 iGaming, 50 Tech/Security messages labeled
- Security/bank alerts reviewed and summarized below

## Existing Labels Used / Created
| Label | Total Messages | Unread |
|---|---|---|
| `INBOX/LinkedIn` | 184 | 169 |
| `INBOX/Finance` | 244 | 223 |
| `INBOX/Jobs` | 419 | 370 |
| `INBOX/iGaming` | 93 | 69 |
| `INBOX/Newsletters` | 470 | 380 |
| `INBOX/Tech` | 184 | 153 |
| `INBOX/Security` | 4 | 4 |
| `Security Alerts` | 6 | 5 |
| `INBOX/Promotions` | 0 | 0 |
| `Promotions` | 0 | 0 |

## Security / Account Alerts — Action Needed
| ID | From | Subject | Body Summary |
|---|---|---|---|
| 19f5f826a082f6f4 | Anthropic | New trusted device added to Claude | Electron on Mac OS X — verify this was you |
| 19f5f824fc6b1108 | Anthropic | New trusted device added to Claude | Electron on Mac OS X — duplicate alert |
| 19f5bd2b51743c79 | Link | New login from macOS (Electron) | Sandton, SA — verified with OTP — review if not you |
| 19f5c7661c23e3eb | FNB | R30,000 transfer | Fusion Private → FNB card via Smartapp |
| 19f5bd2e0006d8a8 | FNB | R664.02 reserved | Moonshot AI purchase |
| 19f5c7d6e5f2d895 | FNB | R235.41 reserved | Hostinger purchase |
| 19f5dc640dbdb6ac | Discovery Bank | Discovery Bank Email for your attention. | Encrypted statement attached |
| 19f5fc0426cb56cc | Google | Security alert | New trusted device / sign-in to Google account |
| 19f59505b1e53754 | 1Password | New 1Password sign-in alert | Verify sign-in |
| 19f59274d5766269 | 1Password | New 1Password sign-in alert | Verify sign-in |

## Notable Items
- **GitLab application confirmation** (IMPORTANT)
- **Monks application confirmation**
- **Greys Recruitment application received**
- **Discovery Bank overdue amount outstanding** (2026-07-12)
- **Google Search Console** disavow file updated for igamingreviews.org
- **Ahrefs Site Audit** — 248 3XX redirects on igamingreviews.org

## Recommended Gmail Filters (set via Gmail web settings)
To keep this structure automatic going forward, create filters in Gmail:
1. From `*@linkedin.com` → apply label `INBOX/LinkedIn`, skip inbox (optional)
2. From `*@indeed.com`, `*@pnet.co.za`, `*@greenhouse-mail.io`, `*@placementpartner.com`, `*@simplify.hr` → label `INBOX/Jobs`
3. From `inContact@fnb.co.za`, `*@discoverybank.co.za`, `*@discovery.bank`, `*@stripe.com`, `*@hostinger.com` → label `INBOX/Finance`
4. From `*@udemy.com`, `*@udemymail.com` → label `INBOX/Newsletters`
5. From `wordpress@igamingreviews.org` → label `INBOX/iGaming`
6. From `*@michaelkorsmail.com`, `*@checkers.co.za`, `*@pnp.co.za`, `*@onedealaday.co.za`, `*@sunglasshut.com` → mark as read, archive

## Next Steps
- [ ] Verify Anthropic/Link/Google/1Password security alerts were you
- [ ] Confirm FNB transactions (R30k transfer, R664 Moonshot, R235 Hostinger)
- [ ] Set up filters in Gmail web UI using the provided `gmail_filters.xml` / rules below
- [ ] Review the 7000-message archive if you want the same structure applied there (currently out of scope via Maton)

## Files Created
- `gmail_structure_report.md` — this report
- `gmail_filters.xml` — importable Gmail filter rules
- `gmail_organize.py`, `gmail_cleanup.py`, `gmail_finish.sh`, `gmail_finish2.sh` — scripts used for bulk operations
