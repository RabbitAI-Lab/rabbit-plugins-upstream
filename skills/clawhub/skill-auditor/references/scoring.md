# Risk Scoring Model

> Why 0-100, why additive, and how to tune it.

## Design Goals

1. **Simple enough to reason about** — no bayesian magic, no ML. If a reviewer sees a score of 42, they should be able to list the rule weights that produced it.
2. **Conservative by default** — false positives (flagging a benign skill) are cheaper than false negatives (missing a malicious one).
3. **Tunable** — every weight is in `scripts/score.py`. Edit and re-run tests.

## The Model

```
risk_score = min(100, Σ weight(violation) for each unique rule triggered)
```

- Each rule fires **at most once per skill** (not per occurrence). A skill that calls `eval()` 50 times still only gets 25 points, not 1250. This prevents one badly-written skill from maxing out on noise.
- Capped at 100. The cap matters because some genuinely malicious skills trigger 8+ critical rules.

## Severity Tiers

| Tier | Weight | Count to max | Description |
|---|---|---|---|
| CRITICAL | 25 | 4 | Direct credential theft, RCE, identity manipulation |
| HIGH | 15 | 7 | Strong malicious indicators: obfuscation, network exfil, command injection |
| MEDIUM | 10 | 10 | Suspicious patterns needing review |
| LOW | 5 | 20 | Bad practice / hygiene issues |

## Score → Tier Mapping

| Score | Tier | Verdict |
|---|---|---|
| 0-15 | 🟢 LOW | ✅ SAFE TO INSTALL |
| 16-40 | 🟡 MEDIUM | ⚠️ INSTALL WITH CAUTION |
| 41-70 | 🔴 HIGH | ⚠️ HUMAN APPROVAL REQUIRED |
| 71-100 | ⛔ EXTREME | ❌ DO NOT INSTALL |

Tier boundaries were chosen so that:
- Any single CRITICAL violation → HIGH tier (needs human approval). This is intentional: even one credential-theft pattern should never auto-install.
- Two unrelated LOW violations (10 pts) stay in LOW tier.
- A skill that triggers one CRITICAL + one HIGH (40 pts) → HIGH tier.
- A skill that triggers 3+ CRITICAL (75+ pts) → EXTREME.

## Why Per-Rule-Once (Not Per-Occurrence)

Consider a malicious skill that reads `~/.ssh/id_rsa`, `~/.ssh/id_ed25519`, `~/.ssh/id_ecdsa`. Should that be 75 pts (3 × CRED_SSH) or 25 pts (1 × CRED_SSH)?

We chose **25 pts** because:
- The behavior is the same (stealing SSH keys); counting each file separately inflates the score without adding signal.
- It prevents false-positive maxing: a skill with 50 `eval()` calls in a 2000-line test file shouldn't be "more malicious" than one with 1 `eval()` call.

If you want per-occurrence scoring, edit `audit_skill()` in `vet.py` to pass all violations (not unique rule IDs) to `score_violations()`.

## Tuning

Common requests:

- **"Make SSH key reads always EXTREME"**: Bump `CRED_SSH` to 100 weight, or add a special-case in `score_violations()` returning 100 if any CRITICAL-cred rule fires.
- **"NET_UNKNOWN_HOST is too noisy"**: Either remove the rule or drop its weight. Better: expand the allowlist in `vet.py DEFAULT_ALLOWLIST`.
- **"I want LOW violations ignored"**: Change `score_violations()` to skip `SEVERITY_LOW`.

After any tuning, run `python3 tests/test_vet.py` to confirm both test samples still classify correctly.

## Comparison to Other Scoring Systems

- **CVSS** (CVE scoring): More complex, environment-aware. Overkill for skill review.
- **Snyk / npm audit**: Use severity levels, not numeric scores. We use both: numeric for sorting, label for humans.
- **GitHub's security advisories**: Per-vuln, no aggregate. We aggregate because a skill's risk is the sum of its behaviors.

## Limitations

- **No data flow analysis**: We pattern-match, we don't trace where input goes. A skill that `eval()`s a hardcoded string is treated the same as one that `eval()`s user input. `RCE_EVAL` fires either way.
- **No semantic understanding**: A skill that legitimately reads `~/.ssh/config` to list known hosts will trigger `CRED_SSH`. Reviewers must use Step 5 (human judgment) for context.
- **Allowlist is opinionated**: Domains not in the default list trigger HIGH. This is intentional but noisy for niche skills. Edit `DEFAULT_ALLOWLIST` per project.
- **Doesn't run the skill**: This is static review only. For runtime monitoring, see the planned `skill-runtime-guard` companion skill (separate project).

## Future Work

- Per-rule occurrence counting as an opt-in flag (`--strict`)
- Confidence scores (regex match strength) to down-weight fuzzy hits
- SBOM-style declared-permissions matching
- Optional online lookups (ClawHub download count, last-updated) to inform Step 1
