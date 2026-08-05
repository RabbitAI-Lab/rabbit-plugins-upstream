# Multi-Model Review Strategy

**Finding:** Different model pairings in adversarial reviews find **completely different bugs**, with **zero overlap** in practice.

## Validated Case: Omnisense Firmware (2026-07-01)

Three adversarial reviews on the same C/ESP32 firmware codebase:

| Review | Pairing | Unique Findings | New Bugs |
|--------|---------|----------------|----------|
| V1 (pre-refactor) | GLM-5.2 Arch + Claude Insp | 18 | Config dead code, platform abstraction, SDK hacks |
| V2 (pre-refactor) | Claude Arch + GLM-5.2 Insp | 17 | Concurrency, lifecycle, RINGBUF ABI hazard |
| V3 (post-refactor) | Claude Arch + GLM-5.2 Insp | 22 | Module-level bugs in logger, sensing_bridge, csi_doppler |

**Result:** 0 findings overlapped across the three reviews. 57 unique findings total.

## Strategy

1. **Run at least two reviews with swapped roles** (A/B swap) before fixing anything
2. Each pairing surfaces a different class of issues — architectural vs. concrete bugs
3. Post-refactor reviews find deeper issues (the refactor itself was validated by the 0 god-module findings in V3)

## When to Use

- Before any major fix cycle
- After a refactor (to validate the new structure)
- When the first review only found superficial issues

## Cost

Each review takes ~15-30 minutes (3-5 phases × 3-6 min per model). Two reviews = ~30-60 minutes total, but the combined findings are far more comprehensive than a single review.
