# Cross-Model Diversity in Adversarial Reviews

## Finding: Different Model Pairings Find Completely Different Bugs

Validated 2026-07-01 on **omnisense firmware** (ESP32, C/embedded, ~450 source files, 52 files in scope):

| Review | Architect | Inspector | Total Findings | Unique |
|--------|-----------|-----------|----------------|--------|
| V1 | GLM-5.2 | Claude (tmux best) | 18 | 18 |
| V2 | Claude (tmux best) | GLM-5.2 | 17 | 17 |
| **Union** | | | **35** | **35** |

**ZERO findings overlapped between V1 and V2.** Not a single finding was independently reported by both pairings.

### Implications

1. **Single-model reviews leave blind spots.** A review by one pairing (even adversarial with 2 different models) misses ~50% of the findings another pairing would find.
2. **Inverting roles matters as much as changing models.** V1 had GLM as Architect + Claude as Inspector; V2 swapped them. The different role focuses (Architect looks at structure/security, Inspector at bugs/edge cases) combined with different model strengths produced completely orthogonal results.
3. **For critical code, run ≥2 adversarial reviews with different model pairings.** The marginal cost is low (the pipeline is automated) and the return is high (2× the findings).
4. **Cross-validation is a flawed confidence metric.** Zero findings were cross-validated (independently found by both reviewers) — not because any finding was wrong, but because different reviews find different things. Absence of cross-validation does NOT mean findings are weak.

### When to Use Multiple Pairings

- **Safety-critical firmware** (medical, automotive, aerospace): run 3+ pairings
- **Security-sensitive code** (auth, crypto, network): run 2+ pairings with different Architect models
- **Public-facing web apps**: 1 high-quality pairing (Codex DEV + Claude REVIEW) is usually sufficient
- **Internal tools / quick fixes**: 1 pairing is fine
