# Role-Swapped Adversarial Reviews — Zero Overlap Findings

## Principle

Running two adversarial reviews with the same codebase but **swapped roles** (Architect ↔ Inspector) produces **completely disjoint findings**. Models find different bugs depending on which role persona they receive and which role context they're placed in.

## Validated Example

**Codebase:** Omnisense firmware (ESP32, C/embedded, ~35 source files)  
**V1:** GLM-5.2 (Architect) + Claude (Inspector)  
**V2:** Claude (Architect) + GLM-5.2 (Inspector)

| Metric | V1 | V2 | Union |
|--------|----|----|-------|
| Total findings | 18 | 17 | **35 unique** |
| Overlap | — | — | **0** |

Every V1 finding was unique to V1. Every V2 finding was unique to V2. Neither model repeated what the other found under a different role.

## Practical Application

For maximum coverage, run **two adversarial reviews** with swapped roles:

```bash
# V1: Model A as Architect, Model B as Inspector
python3 .../adversarial_review.py \
  --dir src --out .review-v1 \
  --a-cmd "model_a_cmd" \
  --b-cmd "model_b_cmd"

# V2: Model B as Architect, Model A as Inspector
python3 .../adversarial_review.py \
  --dir src --out .review-v2 \
  --a-cmd "model_b_cmd" \
  --b-cmd "model_a_cmd"
```

## Why It Works

1. The ARCHITECT persona biases the model toward architecture, security, design, and integration concerns
2. The INSPECTOR persona biases the model toward bugs, edge cases, error handling, and implementation quality
3. Different models have different blind spots and strengths
4. The combination of different persona + different model yields dramatically different results

## When to Use

- Critical code where maximum coverage is desired
- First review of a new codebase
- Before major refactors or releases
- When comparing two models' capabilities
