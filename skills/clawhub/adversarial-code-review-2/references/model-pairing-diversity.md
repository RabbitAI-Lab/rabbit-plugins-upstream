# Model Pairing Diversity — Verified 0% Finding Overlap

## Observation

When running adversarial-code-review with **different model pairings** on the same codebase,
the findings have **zero overlap**. Each pairing finds a completely different set of issues.

## Validated: Omnisense firmware (2026-06-30, 52 files, 749KB of C/embedded)

| Role | V1 Pairing | V2 Pairing |
|------|-----------|-----------|
| **Architect** (Phase A) | GLM-5.2 (pi) | Claude (claude-tmux) |
| **Inspector** (Phase B) | Claude (claude-tmux) | GLM-5.2 (pi) |
| **Synthesis** (Phase 5) | Codex | Codex |

### Results

| Metric | V1 | V2 |
|--------|-----|-----|
| Architect findings | **10** (GLM) | **6** (Claude) |
| Inspector findings | **7** (Claude) | **10** (GLM) |
| Total unique findings | **18** | **17** |
| **Overlap between V1 and V2** | **0** | **0** |

### What each pairing found

**V1 (GLM Arch + Claude Insp)** focused on:
- Integration-layer bugs (config never applied, dead platform abstraction)
- SDK dependency hazards (undocumented PHY symbols)
- Protocol-level issues (strstr parser, seqlock unbounded spin)

**V2 (Claude Arch + GLM Insp)** focused on:
- Concurrency/lifecycle bugs (SPI non-serialised, teardown races, BLE lifecycle)
- Data-format edge cases (32-octet SSID truncation, delta_t hardcoded, errno ordering)
- Structural concerns (god-module, ODR/ABI hazard)

### Why this matters

1. **One review is not enough.** A single model pairing will miss entire categories of bugs.
2. **Model diversity > model quality.** Even though both pairings used strong models (Claude and GLM-5.2), they saw completely different things. The personas (Architect vs Inspector) guide focus, but the model's own biases and training determine what it actually notices.
3. **Practical recommendation:** For critical code, run 2-3 adversarial reviews with different model pairings (swap A/B roles between runs). The union covers substantially more ground than any single run.

### Cost/timing

- Each review: ~24 min for 52-file project
- GLM-5.2: ~6 min per phase (API latency dominated)
- Claude: ~5 min per phase (tmux wrapper overhead + thinking time)
- Codex synthesis: ~1 min
- Total for both V1+V2: ~48 min, 35 unique findings
