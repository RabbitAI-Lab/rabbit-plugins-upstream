# medical-bill-decoder

US medical bills are the least auditable documents in household finance: an unexplained
total, codes nobody translates, and an "amount due" that is wrong in a large share of
cases (duplicate charges, unbundled panels, upcoded visit levels, balances above the
contracted allowed amount). This skill turns an itemized bill + EOB into an audit with
named errors and ready-to-send dispute letters.

## The real-world problem
- Bills arrive as totals; you can't dispute what you can't see.
- The money chain (charge → writeoff → allowed → paid → patient share) is violated on
  real bills: "patient responsibility" exceeding allowed − paid is an error you can win.
- Labs billed twice, panel components billed separately, ER levels upcoded — the most
  common findings, invisible without code knowledge.
- People pay wrong bills to make them go away, or let them hit collections unpaid.

## What it does
`scripts/bill_audit.py` (stdlib only):

- Parses itemized-bill lines (`CPT [modifier] [units] charge`)
- Translates ~70 common CPT/HCPCS codes to plain language with typical allowed bands
- Flags: DUPLICATE codes, UNBUNDLED panel components, E/M level stacking, prices 3×
  above band, unknown codes (→ demand descriptions), EOB chain violations
  (patient share > allowed − paid)
- Drafts the two letters that unlock corrections: itemized-bill request and
  line-cited dispute letter with collections-hold language

```
$ python3 scripts/bill_audit.py --line "99283 1850.00" --line "85025 95.00" \
    --line "85025 95.00" --line "96375 680.00" --allowed 1204 --paid 936 --patient 412
 #  CODE    MOD  UNITS     CHARGE  DESCRIPTION
 1  99283   -       1   1,850.00  ER visit, level 3
 2  85025   -       1      95.00  CBC with differential
 3  85025   -       1      95.00  CBC with differential
 4  96375   -       1     680.00  IV push, add-on
⚠ 2 finding(s):
  [DUPLICATE ] line 3: 85025 already billed at line 2 …
  [PRICE?    ] line 4: 96375 charged $680 — 3× above typical $35-55 …
EOB chain: CHAIN VIOLATION: patient $412.00 > allowed−paid $268.00. Overcharge $144.00.
```

## Files
- `SKILL.md` — triggers, steps, the money-chain invariant, pitfalls
- `references/decoding-guide.md` — code families, error patterns, allowed-amount
  tables, No Surprises Act, dispute ladder, negotiation anchors
- `scripts/bill_audit.py` — the auditor + letter generator

Informational audit tool, not legal or medical advice. Verify codes/amounts against
your EOB and plan documents.
