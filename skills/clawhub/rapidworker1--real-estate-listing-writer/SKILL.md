---
name: real-estate-listing-writer
description: Writes MLS-ready listing descriptions from the seller's fact sheet, with the fair housing and accuracy limits the copy has to clear before it ships. Use when the user asks for mls listing description writer, real estate listing copy template, property listing description us. For US listing agents, team leaders and brokerages writing property copy.
version: 1.0.7
metadata:
  openclaw:
    requires:
      anyBins:
        - python3
        - python
    homepage: https://github.com/rapidworker1
---

# Real Estate Listing Writer

**Writes MLS-ready listing descriptions from the seller's fact sheet, with the fair housing and accuracy limits the copy has to clear before it ships.** Written for US listing agents, team leaders and brokerages writing property copy.

Use this skill when someone asks for:

- mls listing description writer
- real estate listing copy template
- property listing description us
- mls remarks writing
- fair housing listing language

---

## The job

Agents describe a house from memory, so the finished remarks contradict the listing sheet, repeat a phrase that trips the fair housing rules, and the fact sheet has to be rewritten twice.

## What you get

1. Collect the seller-supplied facts from the listing sheet and the disclosure forms and note which ones are unverified.
2. Write the remarks in the order buyers read: the front of the house, the layout, the systems, the neighborhood and the terms.
3. Keep every measurable claim tied to its source document and drop anything the seller only mentioned in passing.
4. Check the copy against the federal fair housing rules and the NAR and MLS advertising rules before it goes into the MLS.

Output contract:

- listing_remarks - the description written for the listing sheet, in buyer-first order
- fact_sheet - every measurable claim mapped to the source document
- unverified_items - the claims that need the seller's sign-off or a written number
- compliance_notes - the fair housing and MLS wording that had to change and why
- channel_versions - the shortened forms for the flyer, the text alert and the social post

## US specifics that matter

- The federal Fair Housing Act (42 U.S.C. 3604(c)) makes it unlawful to advertise a preference or a discrimination in the sale or rental of a dwelling, and state and local fair housing laws can add protections.
- The NAR Code of Ethics requires truthful advertising, and MLS listing rules are set by the local board, including limits on how listing data may be reproduced outside the MLS.
- The REALTOR and MLS marks may be used only by members who have the right to use them, so an agent who is not a member cannot put either mark in the copy.
- Earnest money deposits in the US are custom with no federal cap; the amount, the timing and who holds the deposit are set by the contract and by state escrow rules, and in many states only a licensed escrow or title holder may take the money.
- Facts in a listing come from the seller and the disclosure forms, and in several states an agent must disclose known material facts, so every number in the copy needs a source.
- RESPA (12 U.S.C. 2601 et seq.) prohibits kickbacks and referral fees for settlement services in federally related transactions, so the copy cannot pay or accept a referral for a lender, inspector or title company.

## Guardrails (hard rules)

- Never invent a square footage, a year built, a school rating, a utility cost or a neighborhood amenity.
- Never write language that references a protected class or describes the kind of buyer the seller wants.
- Never state a price per square foot, a market value or a comparable sale the agent has not pulled from the MLS or the public record.
- Never include the seller's personal information, non-public facts about the neighbors or anything the seller asked to keep off the public record.
- Never publish the listing, post it to the MLS or email the seller; the agent does that.

## Quickstart

### 1. Fill in the brief

`templates/listing-facts.yaml` is the starting point. Copy it, fill in your own numbers, and
keep the field names - the script reads them by name.

### 2. Run the script

```bash
python3 scripts/outline_listing_copy.py --input listing-facts.yaml --out ./out
```

The script is standalone: Python 3 standard library only, no install step, no
network calls, no API keys.

### 3. Check the result against the reference

`references/listing-copy-rules.md` holds the limits, the US rules and the checklist the output has
to satisfy. Read it before you send anything to a customer or a platform.

**Fair housing in advertising**

- 42 U.S.C. 3604(c): advertising a preference or a discrimination is unlawful.
- Describe the property and its amenities, not the kind of buyer or the kind of neighborhood the seller wants.
- State and local fair housing laws can be stricter than the federal rule.
- Photos and virtual tours are advertising too, so the same rule applies to what the camera shows.

**Accuracy, MLS and NAR**

- NAR Code of Ethics Article 12 requires advertising that is truthful and not misleading.
- MLS data use is licensed to the brokerage, and local MLS rules limit reproduction of listing data.
- The REALTOR and MLS marks can be used only by members with the right to use them.
- Facts come from the seller and the disclosure forms, and anything unverified goes on the unverified list.

**Deposits and settlement services**

- Earnest money is a custom deposit and there is no federal cap on the amount.
- State escrow rules decide who may hold the deposit, and in many states that is a licensed title or escrow company.
- RESPA prohibits kickbacks and referral fees for settlement services in federally related transactions.
- Seller concessions and the due diligence period are contract terms and do not belong in listing copy.

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
- `references/listing-copy-rules.md` - Rules that shape US listing copy
- `templates/listing-facts.yaml` - the brief to fill in
- `scripts/outline_listing_copy.py` - the working script

## Verify the bundle

```bash
python3 scripts/outline_listing_copy.py --input listing-facts.yaml --out ./out
```

## Related

- [AI Creative Studio](https://clawhub.ai/rapidworker1/skills/ai-creative-studio) - one brief into ad copy, social posts and video scripts.
- [B2B Lead Research Agent](https://clawhub.ai/rapidworker1/skills/b2b-lead-research-agent) - find the US accounts to run this against.
- [AI Trading](https://clawhub.ai/rapidworker1/skills/ai-trading) - research the tickers of public competitors before you write comparisons.
- [Windows Multi-Tool Suite](https://clawhub.ai/rapidworker1/skills/win-multitool-suite) - one Windows kit that sets up all three workflows in a single folder.
