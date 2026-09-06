---
name: warranty-vault
description: "Use when an appliance or device breaks and you wonder if it is still covered, when you buy anything with a warranty or extended plan, when filing a warranty claim, when selling used items with coverage remaining, or when doing a household coverage audit — stores purchases with price, date, warranty terms, and receipt location, computes remaining coverage including statutory rights (UK 6-year, EU 2-year, US implied warranty + card protections), finds unregistered products, generates a coverage report and claim letters, and flags expiring coverage before it is too late."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [warranty, receipts, consumer-rights, appliance, claims, home-inventory, money]
---

# Warranty Vault

## Overview

Your dishwasher dies 20 months after purchase. Does anyone cover it? The manufacturer warranty was 12 months — gone. But: the retailer's extended plan you vaguely remember… the credit card's extended warranty perk you forgot existed… and if you're in the UK, the Consumer Rights Act presumption that a fault within 6 years was inherent. Most people recover exactly none of this money, not because they weren't covered but because they couldn't marshal the facts: purchase date, price, where the receipt is, what the terms said.

Warranty Vault is the filing system you needed: a JSON vault of purchases with warranty terms, receipt locations, and registration status; a coverage engine that layers manufacturer warranty + extended plan + card perk + statutory rights and tells you **what covers a broken item today**; expiry alerts so you schedule the repair you've been tolerating before coverage lapses; and a claim letter generator with the documentation checklist per jurisdiction.

## When to Use

- **Something broke** → `covered` — what layer applies, what evidence you need, next steps
- **Just bought something** → `add` it while the receipt is still in the bag (30 seconds)
- **Quarterly** → `report` / `expiring` — audit coverage, catch unregistered products, see lapses
- **Filing a claim** → `claim` — generates the letter with statutory citations
- **Selling used gear** → remaining coverage is a selling point; `covered` quantifies it
- **Moving / insurance review** → `report` doubles as a priced possession inventory
- Don't use for: insurance claims (different animal — see home-inventory skill), service contracts you pay monthly (subscription-slayer territory), or legal advice — this is organized knowledge, not a lawyer.

## Coverage Layers (the order that matters)

```
1. manufacturer warranty      — free, from purchase, typical 1–5 yr
2. statutory rights           — jurisdiction-dependent, FREE, from purchase:
     UK: Consumer Rights Act 2015 — 6 years to claim (England/Wales/NI; 5 Scotland);
         fault within 6 months presumed inherent (reversed burden), so ≤6mo = retailer
         refund/replace almost automatically
     EU: 2-year legal guarantee (Directive 1999/44/EC + national law); 12-month
         presumption of non-conformity
     US: no federal repair right; UCC implied warranty of merchantability
         (duration varies by state, often 4 yr UCC statute of limitations);
         "full warranty" terms under Magnuson-Moss bind the maker
3. extended plan (retailer/3rd party) — terms + deductible + claims phone
4. credit card perk           — extends manufacturer warranty (US: Visa Infinite
     +2yr on 3yr-or-less warranties, many World Elite Mastercards +1yr, Amex up to +1
     year matched up to $10k); ALSO purchase protection (90–120 days, theft/damage)
     and return protection (90 days). Requires the card you paid with.
```

The `covered` command evaluates layers in this order and prints what's live, what's expired, and what evidence each needs. Default lengths, caps, and exclusions are editable defaults — your plan's T&Cs override; the vault stores per-purchase terms exactly for this.

## Commands

```bash
# Record a purchase (do this the day you buy)
python3 scripts/warranty_vault.py add --id dishwasher --name "Bosch SMS machine" \
    --category appliance --price 749 --purchased 2024-11-03 \
    --warranty-mo 12 --receipt "email from Appliances.co 11/03" \
    --card "Amex Gold" --registered 2024-11-10 \
    --notes "Model SHEM63W55N; serial in manual p.2"

# Same but with an extended plan
python3 scripts/warranty_vault.py add --id tv-oled --name "LG C4 55\"" \
    --category electronics --price 1299 --purchased 2025-03-14 --warranty-mo 12 \
    --extended-mo 36 --extended-by "Geek Squad" --extended-deductible 0 \
    --receipt "paper, fireproof box" --card "Visa Infinite"

# What covers my broken dishwasher today? (jurisdiction matters)
python3 scripts/warranty_vault.py covered dishwasher --jurisdiction UK
python3 scripts/warranty_vault.py covered tv-oled --jurisdiction US

# What expires in the next 90 days? (schedule tolerated repairs NOW)
python3 scripts/warranty_vault.py expiring --days 90

# Full audit: coverage table, unregistered items, vault health
python3 scripts/warranty_vault.py report
python3 scripts/warranty_vault.py report --category appliance --json

# Claim letter with statutory citations + document checklist
python3 scripts/warranty_vault.py claim dishwasher --fault "Won't drain; E25 error" \
    --jurisdiction UK > claim-letter.txt

# Edit / remove / list / export
python3 scripts/warranty_vault.py update dishwasher --mark-registered
python3 scripts/warranty_vault.py list
python3 scripts/warranty_vault.py export --json
```

Vault file: `~/.warranty-vault.json` (`--file` to override). Back it up — it IS the system.

## How the Coverage Engine Works

For each layer, coverage = purchase_date + term ≥ today (computed per jurisdiction):

- **Manufacturer:** `warranty_mo` months.
- **Statutory:** UK 6y / EU 2y / US none-default. UK ≤6-months-old faults flip the burden of proof to the retailer — the letter says so.
- **Extended:** `extended_mo` from purchase (most run concurrently, some from manufacturer-expiry — store which in notes if the latter).
- **Card perk:** +12 or +24 months added AFTER manufacturer expiry, only if `card` is set and the base warranty was ≤ the card's eligibility window (Visa +24 mo needs base ≤36 mo, etc.).

`expiring` scans all layers for end-dates within `--days` and names the action ("register", "report fault", "schedule repair"). `report` also flags: items never registered (manufacturer registration sometimes extends coverage — e.g., some brands +3 months), items with no receipt location recorded, and total vault value by category.

## Claim Letter Notes

`claim` prints a ready-to-edit letter to the *right* party: manufacturer for warranty claims; **retailer** for statutory claims (UK/EU — your contract is with the seller, not the maker); plan administrator for extended plans. It cites the statute, states purchase facts from the vault, describes the fault, and requests repair/replacement/refund with a 14-day response window. The printed checklist reminds you what to attach: proof of purchase, photos/video of fault, serial, registration confirmation, card statement line.

## Common Pitfalls

1. **Claiming from the manufacturer in the UK/EU.** Statutory rights are against the *retailer*. The letter generator targets correctly — don't reroute it.
2. **Assuming the receipt is "in email somewhere."** When you need it, you need the date AND price. Record the receipt's *location* at `add` time even if you don't file the PDF.
3. **Forgetting card perks.** Extended-warranty and purchase-protection benefits die with the card's terms — but for old purchases, the card you PAID with governs. Vault stores it per purchase.
4. **Missing registration windows.** Some manufacturers require registration (or dangle +3 months for it). `report` flags unregistered items under 90 days old.
5. **Letting a tolerated fault ride past expiry.** The rattle you've ignored for 6 months is a claim until the day coverage ends. `expiring --days 90` is the nag.
6. **Extended plans on cheap items.** A $90 plan on a $300 printer is usually negative EV; self-insure small stuff, vault the savings. The `report` totals make this visible.
7. **UK 6-year ≠ 6-year warranty.** It's a right against inherent faults (must have been present at purchase), with burden shifting after 6 months. Older items need the "fault was inherent" argument; the letter includes the presumption language for ≤6mo items.

## Verification Checklist

- [ ] Every purchase >$100 with a warranty >90 days is in the vault
- [ ] Each entry has receipt location + price + purchase date (report flags gaps)
- [ ] Jurisdiction set correctly for statutory layer (UK/EU/US)
- [ ] `expiring --days 90` run quarterly alongside other home maintenance checks
- [ ] Claim letters name the correct counterparty (retailer vs manufacturer)
- [ ] Vault file backed up (it's JSON — copy it with your documents)
