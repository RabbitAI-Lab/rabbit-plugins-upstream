# Persona Hardware Bias — Historical Record (Fixed 2026-07-17)

## What Happened

The `architect.md`, `inspector.md`, `cross_review.md`, and `synthesis.md` personas
in `adversarial-common/personas/` were originally hardcoded with embedded/RF context
(ESP32-S3, CC1101 at 433 MHz, BLE, DSP, noise floor, SPI bus, IRAM). When reviewing
a pure-software project (no hardware layer), these references caused the reviewers
to fabricate irrelevant analysis.

## The Fix (2026-07-17)

All 4 persona files were rewritten to be **100% generic** — no hardware-specific
references remain:

- **architect.md** — architecture, security, concurrency, resilience, assumptions
- **inspector.md** — edge cases, error handling, resource management, race conditions, input validation
- **cross_review.md** — system constraints, design trade-offs, resilience, security boundaries
- **synthesis.md** — deduplication, dispute resolution, "Hardware Risk Assessment" → "Operational Risk Assessment"

See the `adversarial-code-review` SKILL.md for full model pairing rules and the
"Never pin a specific Claude model" guideline.

## Original Symptom (for reference)

- Raw architect/inspector JSON findings referenced hardware constraints that didn't exist.
- The synthesis phase detected and discarded this noise (wasting ~10% prompt budget).
- Triggered by the `rdespres87/chatter` review (2026-07-17), a pure Rust chat app.

## If Hardware Bias Reappears

If any persona file still contains embedded-specific language, patch
`../adversarial-common/personas/<file>.md` to remove it. The personas should be
usable for any software project without modification.
