# Warranty & Consumer-Rights Reference

The coverage model behind `scripts/warranty_vault.py`: layer definitions, jurisdiction rules, card perk tables, claim procedures, and letter templates.

## 1. The four layers, precisely

| Layer | Source | Cost | Starts | Typical length | Claim against |
|---|---|---|---|---|---|
| Manufacturer warranty | product T&Cs | included | purchase date | 1–5 yr (1–2 common; 10 yr appliance motors; lifetime cutting-tool marketing) | manufacturer |
| Statutory rights | law of your jurisdiction | included | purchase/delivery date | UK 6y, EU 2y, US none-federal | **retailer** |
| Extended plan | retailer / 3rd party | paid | usually purchase (sometimes mfr expiry) | 1–5 yr | plan administrator |
| Card perks | the card you PAID with | included w/ card | manufacturer expiry | +1 to +2 yr; purchase protection 90–120 d | card issuer |

Evaluation order for a broken item: cheapest-evidence first — manufacturer warranty (proof of purchase only) → statutory (proof of purchase + fault-is-inherent) → card perk (statement + claim form) → extended plan (plan number, possibly deductible). The script's `covered` command prints all live layers with their end dates.

## 2. Statutory rights by jurisdiction

### United Kingdom — Consumer Rights Act 2015
- Goods must be of satisfactory quality, as described, fit for purpose. Remedies: repair, replacement, price reduction, final right to reject (full/partial refund).
- **Short-term right to reject: 30 days** for most faults → full refund in that window.
- **6 months: reversed burden.** A fault within 6 months is *presumed* present at sale; the retailer must prove otherwise.
- **6 years (England/Wales/NI; 5 in Scotland)** to bring a claim for breach of contract (Limitation Act 1980). After 6 months, YOU must show the fault was inherent — an expert report or documented defect-history of the model helps.
- Delivery claims: goods must arrive within 30 days unless agreed.

### European Union — Directive 1999/44/EC (+ 2019/771 from 2022)
- **2-year legal guarantee** from delivery, minimum, seller-side.
- **12-month presumption** of non-conformity (some states extend; e.g., implementations vary).
- Remedies: repair or replacement first, then price reduction / refund.
- Commercial guarantees (manufacturer warranties) are additional, never a substitute.

### United States
- No general federal right to a working product after sale. UCC §2-314 **implied warranty of merchantability** applies unless conspicuously disclaimed ("as is"); duration bounded by the state's UCC statute of limitations (commonly 4 years, varying).
- **Magnuson-Moss Warranty Act**: "Full" warranties have federal minimums (no charge, choice of replacement); "limited" is everything else. Also: warrantors can't require a specific brand of part/service to keep the warranty (tie-ins), and informal dispute mechanisms may be required.
- **State quirks**: CA Singer–Beverly (repair-or-replace for consumer goods with express warranty + repeated fails), MD/other implied-warranty duration minimums for major appliances. Extended warranties are state-regulated insurance-ish products.

(Elsewhere: AU/NZ consumer law is strong — automatic guarantees, replacements/refunds, "acceptable quality"; many goods effectively covered beyond any cardboard warranty. Canada: provincial sale-of-goods acts + Quebec's legal warranty. The tool defaults to US/UK/EU; add other regimes in the vault notes.)

## 3. Credit-card perk table (defaults in the script — verify YOUR card's guide to benefits)

| Program | Extended warranty | Purchase protection | Notes |
|---|---|---|---|
| Visa Infinite | +24 mo if base warranty ≤36 mo | 90 d theft/damage | issuer-dependent; premium Visas |
| Visa Signature | often +12 mo | 90–120 d | varies by issuer |
| World Elite Mastercard | commonly +12 mo | 90 d | issuer-dependent |
| Amex (most charge/premium) | +12 mo (matches up to $10k) | 90 d theft/damage | generally reliable; itemized claim |
| Entry-level cards | often none | sometimes 90 d | don't assume |

Mechanics: pay in full with the card; keep the statement; file within the window (often 60 d after failure); they may repair/replace/reimburse up to a cap (e.g., $10k/item, $50k/yr). Declining-balance coverage for used items. **Return protection** (90 d, retailer-refused returns) also exists on premium cards.

## 4. Manufacturer-registration quirks worth 30 seconds

- Some brands extend coverage for registering (a few months to a year — e.g., certain appliance brands' +3 mo, tool brands' lifetime-limited upsells).
- Registration also enables recall notices — which are FREE repairs regardless of warranty.
- The script's `report` flags unregistered items <90 days old: that's your window to register.

## 5. Filing workflow (the part people fumble)

1. **Establish the layer** (`covered`) and counterparty: mfr / retailer / administrator / card.
2. **Evidence pack**: proof of purchase (receipt, statement line, order email), serial, photos or video of the fault, error codes, registration confirmation, prior repair records.
3. **Write once, in writing** (email/portal creates a record). State facts + requested remedy + 14-day response. The `claim` command drafts this with citations.
4. **UK/EU trick**: after one failed repair or long delay (typically >2 weeks without goods or repeated faults), you can demand replacement or partial refund — say so in follow-ups.
5. **Card claims**: separate process — issuer's benefit administrator, itemized form, repair estimate sometimes required. Deadlines are shorter; act within days, not weeks.
6. **Escalation**: retailer ombudsman/dispute-resolution (many jurisdictions free), small-claims track (UK money-claim online; US small claims; EU ECC-net for cross-border), card chargeback for undelivered/misdescribed goods (120 d typical).

## 6. Claim letter templates

The script fills these. Structure to keep if editing:

```
[Your name/address/date]
[Counterparty: RETAILER for statutory; MANUFACTURER for warranty]

RE: [Item], purchased [date] for [price], order/receipt [ref]

On [date] the item developed the following fault: [description].
[If UK ≤6mo: Under the Consumer Rights Act 2015, s.19, a fault appearing within
six months of delivery is presumed to have been present at the time of sale.]
[If UK >6mo: The nature of the fault indicates it was inherent at purchase;
the item has been used normally and maintained per the manual.]
[If EU: Under [national implementation of] Directive (EU) 2019/771, the goods
do not conform to the contract; I request repair or replacement within a
reasonable time.]
[If US warranty: This claim is made under the express warranty included with
the product (Magnuson-Moss applies).]

I request [repair / replacement / refund of £X] and a response within 14 days.
Enclosed: proof of purchase, photographs, serial record.

Yours faithfully, [name; reference numbers]
```

## 7. Reasonable defaults for common categories (vault suggestions)

| Category | Typical mfr warranty | Extended plan worth it? |
|---|---|---|
| Major appliances | 1 yr parts+labor (2–5 on some, 10 motors/compressors) | sometimes — check reliability first |
| TVs | 1 yr (panel 1 yr) | rarely; card +1yr covers the gap |
| Laptops/phones | 1 yr limited | rarely; accidental damage ≠ covered anyway (separate insurance) |
| Power tools | 1–3 yr (some lifetime-limited exchange) | no — brand service networks are cheap |
| Mattresses | 10 yr limited (prorated, body-indent thresholds) | no |
| Cars | 3–7 yr / 36–100k mi powertrain | often no at list price; negotiate |
| Furniture | 1–5 yr frame/fabric | case-by-case |

Self-insurance math: if a $90 plan on a $450 item with 8% two-year failure odds — EV ≈ $36 of expected payout. Vault the $90 instead; `report --json` totals show the accumulating reserve.

## 8. Maintenance cadence

- **At purchase:** `add` within the week (receipt location + card + serial).
- **Quarterly:** `expiring --days 90` + `report` — register unregistered items, schedule tolerated-repair claims before lapses.
- **At renewal season:** card perk terms change — skim your current card's benefit guide yearly and update notes.
- **When selling:** `covered` prints remaining coverage; transferable warranties (many appliances/tools) raise resale value.
