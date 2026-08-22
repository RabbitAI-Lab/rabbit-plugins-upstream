# Risk Model & Scoring Methodology

## Principles

1. **No plaintext leaves memory for outputs.** Reports reference entries by index and title; passwords are reduced to unsalted SHA-1 (for HIBP k-anonymity) and truncated fingerprints for reuse detection.
2. **Severity ∝ blast radius.** A bad password on an email or bank account outweighs the same bad password on a throwaway forum.
3. **Actionable over academic.** Every finding maps to one concrete user action ("rotate X", "enable 2FA on Y").

## Password Strength (0-4 scale, zxcvbn-inspired)

Computed from: length, character-class coverage, repeated substrings, sequence/run detection (abc, 123, qwerty), dictionary + common-password list hits, and leetspeak normalization (`@→a`, `3→e`, `1→i`, `$→s`, `0→o`).

Estimated guess count ≈ product of pattern-search space; bits = log2(guesses).

| Score | Bits | Meaning |
|---|---|---|
| 0 | < 10 | Trivially cracked (top-10k list) |
| 1 | 10-25 | Minutes to hours |
| 2 | 25-40 | Days to weeks |
| 3 | 40-60 | Years on commodity hardware |
| 4 | > 60 | Practically uncrackable offline |

Passphrases (`correct-horse-battery-staple` style) score well: 4 random words ≈ 44+ bits.

## Reuse Graph

Entries sharing an identical password form a connected component. Component of size N contributes `N * log2(N+1)` risk points — superlinear because cracking one yields N accounts, and attackers automate credential stuffing across sites.

Only components with N ≥ 2 are findings. The largest component is usually the single most important thing to fix.

## Staleness

Days since `last_modified` (falls back to `created`). Thresholds:

- > 1460 days (4 years): high staleness — predates most modern breach disclosures relevant to that era
- > 730 days (2 years): moderate

Unknown dates are excluded rather than assumed stale.

## Breach Exposure (HaveIBeenPwned, k-anonymity)

1. Compute `SHA1(password).upper()`.
2. Send only the first 5 hex chars to `https://api.pwnedpasswords.com/range/XXXXX`.
3. HIBP returns ~800 suffixes for that prefix; match locally against the remaining 35 chars.
4. The response includes a count = how many times that exact password appears in breach corpora.

The server cannot know which of ~800 candidates is yours. Counts > 0 are findings; counts > 1000 mean the password is in every cracker's wordlist.

## Site Criticality Tiers

Tier assignment by domain keyword matching against a curated list:

| Tier | Multiplier | Examples |
|---|---|---|
| Critical | 3.0x | mail providers, banks, payment, cloud storage, identity/SSO, domain registrars |
| Sensitive | 1.5x | shopping with stored cards, social media, healthcare, government |
| Standard | 1.0x | everything else |

A reused *and* breached *and* critical-tier credential is a P0 emergency.

## Composite Score

```
score = 100 - Σ weighted_penalty
weighted_penalty = base_penalty × dimension_weight × criticality_multiplier (capped)
```

Dimension weights: reuse 0.35, weakness 0.30, breach 0.20, staleness 0.10, 2FA 0.05. The result is clamped to [0, 100]. Penalties are normalized so a modest vault with a few issues doesn't bottom out while a huge vault with the same issues does — per-entry penalties are averaged over vault size before weighting.

## Remediation Priority

Each finding gets `priority = risk_points × criticality_multiplier × breach_multiplier`. Sorted descending, the plan reads as a work queue: rotate these first, enable 2FA there next, then split your largest reuse component.

## 2FA Opportunity

The script flags entries on 2FA-capable domains (matched against a bundled seed list; see `references/export-formats.md` for how to extend it) where the vault stores no TOTP secret. Absence of a TOTP field is treated as "2FA likely not enrolled," which is a heuristic — a user may use hardware keys or SMS instead. Findings are informational (hence the 5% weight).
