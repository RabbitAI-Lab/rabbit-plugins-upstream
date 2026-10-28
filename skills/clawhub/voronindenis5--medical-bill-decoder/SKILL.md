---
name: medical-bill-decoder
description: "Use when a US medical bill, Explanation of Benefits, or collections notice arrives and the numbers make no sense. Decodes CPT/HCPCS/revenue codes, reconstructs the allowed-amount chain (charge → contractual writeoff → insurance payment → patient share), finds upcoding and duplicate-charge patterns, and generates an itemized-bill request + dispute letter."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [medical-bills, eob, healthcare-costs, dispute, cpt-codes]
---

# Medical Bill Decoder

## Overview
80% of US medical bills contain errors (duplicate charges, canceled services, upcoded
levels), but patients can't see them because bills arrive as an unexplained total.
This skill turns an itemized bill or EOB into an **audit report**: it classifies each
line's CPT/HCPCS code (what the code *is*, its typical work), flags classic error
patterns (same CPT billed twice, bilateral codes billed twice + modifier 50 missing,
eval-and-management level jump), computes the expected chain
`charge ≥ allowed = insurance_paid + patient_share (copay/coinsurance/deductible)`,
and drafts the two letters that unlock corrections: the **itemized bill request**
(required first step — you cannot dispute a total) and the **billing error dispute**.

## When to Use
- Any US hospital/clinic/lab bill where the amount seems wrong or unexplained
- An EOB shows "patient responsibility" you don't understand
- A medical bill hit collections (debt validation route)
- Comparing a Good Faith Estimate against the final bill (No Surprises Act)
- **Don't use for:** Medicare/Medicaid plan-specific benefit math (plan rules vary —
  the chain math still applies, but allowed amounts differ), or non-US systems.

## The Chain Every Bill Follows
```
Billed charge  (provider's sticker price — fiction)
  − contractual writeoff  (network discount; you NEVER owe this)
  = allowed amount        (the real price)
  = insurance paid
  + patient share         (copay OR coinsurance% of allowed OR deductible)
  = your balance
```
**Invariant: copay + coinsurance + deductible applied can never exceed the allowed
amount. If patient responsibility > allowed amount, the bill is wrong — full stop.**

## Steps
1. Get the itemized bill. If you only have a total, send the itemized-bill request
   letter first (script generates it). You have the right to it (hospital: itemized
   bill on request; most states require it).
2. Feed lines to the auditor:
   ```bash
   python3 scripts/bill_audit.py bill.txt            # reads CPT/HCPCS lines
   python3 scripts/bill_audit.py --line "99213 145.00" --line "85025 TW 28.00"
   python3 scripts/bill_audit.py --eob eob.txt       # charge/paid/patient columns
   ```
3. Read the flags: DUPLICATE (same CPT+modifier twice same date), UNBUNDLE
   (component billed alongside its panel), UPcode-suspect (E/M level jump across
   visits), SELF-ADMINISTERED (items typically bundled), chain violations
   (patient > allowed).
4. Check coverage dates, place-of-service consistency, and CPT vs what actually
   happened (a 99204 new-patient visit for a 10-minute follow-up = wrong level).
5. Send the dispute letter (script drafts it with the flagged line items cited).
   Phone script: "I am disputing the balance, request an itemized bill with CPT codes
   and NDC numbers, and ask that the account be held from collections during the
   review." Get a reference number.
6. Escalation ladder if stonewalled: hospital billing supervisor → patient advocate /
   ombudsman → state insurance commissioner / state AG health-care bureau; for
   ACA plans, federal marketplace appeal. Collections: written debt validation within
   30 days (script has a template note).

## Built-in Knowledge (summary — full tables in references/)
- ~70 common CPT/HCPCS codes with plain-language names + typical allowed ranges
- Error patterns: duplicates, unbundling (panel + components), missing modifier 50
  (bilateral), rev-code vs CPT mismatch, OR-time double-billing
- No Surprises Act: balance-billing banned for emergency care and out-of-network at
  in-network facilities; GFE vs final bill delta > $400 is disputable
- Timelines: many states require interest-free payment plans; nonprofit hospitals
   must offer financial assistance (community-benefit) — 280g eligibility often
   200–400% FPL

## Worked Example
Itemized bill total $3,182 for an ER visit + blood draw + X-ray:
```
99283  1,850.00   ER level 3
71046    410.00   CXR 2 views
85025     95.00   CBC w/ diff         ← appears AGAIN at line 12
85025     95.00   CBC w/ diff         ← DUPLICATE
J1885  x4   48.00   ketorolac
96375    680.00   IV infusion
```
Audit flags: duplicate 85025 (+$95), E/M level suspect (99283 with only X-ray + IV —
check against 99282 band), and EOB chain: allowed $1,204, insurance paid $936,
"patient responsibility" printed as **$412** — but $1,204 − $936 = **$268**. $412 > $268
= chain violation → dispute wins $144 immediately, plus $95 duplicate after review.

## Common Pitfalls
1. **Disputing a total.** Always demand the itemized bill first — disputing a total
   gets you a payment-plan offer, not an audit.
2. **Paying to make it go away.** Paying is treated as acceptance; disputed balances
   must be held (get the reference number and collections-hold in writing/note).
3. **Ignoring the EOB.** The bill says what they want; the EOB says what you owe.
   Always reconcile bill vs EOB line by line — differences are the errors.
4. **Missing the 30-day debt-validation window** once a collector is involved.
5. **Assuming codes are right because they're codes.** Upcoding (billing 99215 for a
   99213-level visit) is the most common audit finding; you may compare the level
   against the visit documentation you can recall (time, complexity, new vs established).
6. **Forgetting No Surprises Act protection** for emergency/out-of-network-at-in-network
   facility bills — these get disputed to the facility, not negotiated.

## Verification Checklist
- [ ] Every line classified (CPT → plain language) or marked UNKNOWN → ask provider
- [ ] Duplicate/unbundle/chain checks run and cited by line number
- [ ] Bill reconciled against EOB (charge vs allowed vs paid vs patient share)
- [ ] Itemized-bill request sent if only a total was in hand
- [ ] Dispute letter references specific lines + the chain math
- [ ] Collections hold / reference number requested
