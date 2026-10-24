# Medical Bill Decoding — Full Reference

## 1. The paperwork cast
| Document | Sent by | What it's for |
|---|---|---|
| Itemized bill | provider | every line: CPT/HCPCS, charge, units, date, rev code |
| CMS-1500 / UB-04 | provider→insurer | the actual claim (professional / facility) |
| EOB / EID (Medicare) | insurer | allowed amount, payment, patient responsibility, denial codes |
| Good Faith Estimate | provider (on request / self-pay) | pre-care price, NSA protections |
| Notice of denial | insurer | why not paid; starts YOUR appeal clock (often 180 days) |

## 2. Code families
- **CPT** (00100–99607, AMA): what was DONE. 992xx = eval & management; 7xxxx =
  radiology; 8xxxx = lab; J-codes = drugs (HCPCS). Modifiers matter:
  - `50` bilateral, `59` distinct service, `25` significant separate E/M same day,
    `76` repeat by same provider, `77` repeat by another.
- **HCPCS Level II** (A/V/J/W…): supplies, drugs, ambulance.
- **Revenue codes (UB-04)**: 0450 ER, 0636 drugs, 0730 EKG, 030x lab, 032x radiology,
  0480/0481 surgical services. Rev code + no CPT on a hospital bill = demand the CPT.
- **NDC numbers**: drug package IDs — ask for them on any J-code line to verify units.
- **ICD-10** codes = diagnoses (medical necessity — denial often means mismatch).

## 3. The money chain
```
charge − writeoff = allowed = paid + patient(share)
```
- In-network: writeoff is contractual; balance beyond allowed CANNOT be billed to you
  (balance billing). Out-of-network (non-emergency, consent given): possible.
- Patient share decomposes into: copay (flat), coinsurance (% of ALLOWED, never of
  charge), deductible (remaining). One service usually applies only one mechanism.
- **Chain rule: patient share ≤ allowed − paid. Violation = billing error.**
- Denial codes on EOB: PR = patient responsibility (you owe, if correct); CO = contract
  obligation (provider writes off — NOT yours). CO-45 = exceeds fee schedule; CO-97 =
  bundled into another service. A CO-coded amount on your bill = remove it.

## 4. High-yield error patterns
1. **Duplicates**: same CPT+modifier, same date (labs are the classic — see 85025).
2. **Unbundling**: 80053 (CMP) billed alongside its components (82040, 84155…);
   93000 EKG + 93010 interpretation separately; panel + components = pick panel.
3. **Bilateral double-bill**: 27447 (TKA) ×2 or bilateral procedure ×2 without
   modifier 50 (insurer pays 150% — not 200%).
4. **E/M level jump**: 99213→99214→99215 across routine visits, or new-patient code
   (99203/04) after the first visit (must be established 99213/14 after 3 years).
5. **Incident-to / same-day**: procedure + E/M without modifier 25.
6. **Canceled/no-show services billed** (pre-op labs for surgery that didn't happen).
7. **OR time**: facility bills first hour (66984 → rev 0360) + extra time overlapping.
8. **Rev-code-only lines** (no CPT): un-auditable → demand CPTs.
9. **Units errors**: J-code billed ×4 when 1 vial used (check NDC + vial size).
10. **Chain violations** (patient share > allowed − paid).

## 5. Common codes table (extract — see scripts/bill_audit.py CODES)
| CPT | Meaning | Typical allowed (2024–26 US, commercial) |
|---|---|---|
| 99202/03/04/05 | New patient visit L1–L5 | $110 / $160 / $260 / $380 |
| 99211/12/13/14/15 | Established visit L0–L4 | $50 / $90 / $110 / $160 / $220 |
| 99281/82/83/84/85 | ER visit levels | $280 / $450 / $700 / $1,100 / $1,600 |
| 99291 | Critical care, first hour | $700–1,000 |
| 71046 | Chest X-ray 2 views | $45–80 |
| 80053 | Comprehensive metabolic panel | $25–45 |
| 85025 | CBC with differential | $15–30 |
| 84443 | TSH | $30–50 |
| 81001/81003 | Urinalysis w/wo scope | $10–25 |
| 93000 | ECG 12-lead w/ interpretation | $40–70 |
| 96372 | Therapeutic injection SC/IM | $30–60 |
| 96365/96375/96376 | IV infusion init/add-on/seq | $120 / $45 / $30 |
| 43239 | Upper GI endoscopy w/ biopsy | $900–1,400 |
| 70551 / 70553 | MRI brain w/wo and w contrast | $400–900 |
| 72148 | MRI lumbar spine w/o | $400–900 |
| 66984 | Cataract surgery w/ IOL | $1,600–2,400 |
| 27447 | Total knee arthroplasty | $18,000–28,000 (facility swings huge) |
| J1885 | Ketorolac 15 mg | $2–4/unit |
| J3420 | Vitamin B12 1000 mcg | $8–15/unit |
| 36415 | Venipuncture | $10–20 |
| 94640 | Nebulizer treatment | $40–70 |
| 20610 | Arthrocentesis major joint | $90–150 |
| 20552 | Trigger point injections ≤2 | $80–140 |
| 97110 / 97140 | PT each 15 min / manual therapy | $35–60 |

## 6. No Surprises Act (2022, US)
- Emergency services: must be treated in-network regardless of facility; patient owes
  only in-network cost share. Balance billing = banned.
- Out-of-network care AT an in-network facility (anesthesia, radiology, assistant
  surgeon, lab) without informed consent: same protection.
- Self-pay/uninsured: entitled to a Good Faith Estimate; final bill **> $400 over GFE**
  opens the NSA patient-provider dispute process.
- Air ambulances: covered.

## 7. Dispute ladder & letters
1. Itemized-bill request (bill_audit.py `--letter itemized`).
2. Line-item dispute (bill_audit.py `--letter dispute`) — cite lines, chain math,
   duplicates; request collections hold + reference number; 30-day response ask.
3. Insurer appeal (denial letter says the deadline — often 180 days; ask for
   "peer-to-peer" review; escalate to external/Independent Review Org — free, binding
   in many states).
4. Hospital patient advocate / ombudsman / financial assistance office (nonprofits:
   501(r) assistance policies, often 200–400% FPL).
5. State DOI/insurance commissioner complaint (free, tracked, providers hate them) or
   state AG health care bureau; CMS 1-800-MEDICARE for Medicare.
6. Collections received: written validation request within 30 days; dispute the debt
   in writing; a disputed medical debt can't be credit-reported without marking it
   disputed (FCRA); Vantage/FICO newer models ignore paid/small collections.

## 8. Negotiation reality
- Cash-pay prompt-pay discounts: 20–40% common.
- Ask "what would Medicare pay?" — Medicare rates are a public anchor (PFS lookup).
- Payment plans: interest-free commonly available; nonprofits often must offer them.
- Never let "we'll send it to collections" rush a dispute — collections-hold is a
  normal, reasonable request.
