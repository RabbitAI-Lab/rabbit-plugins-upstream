# Role-Swapped Reviews: Zero Overlap Findings

Validated 2026-07-01: omnisense firmware (35 source files, C/C++ embedded).

## The Pattern

Run two adversarial reviews on the same codebase with the model roles swapped:

| Run | Architect | Inspector | Total findings |
|-----|-----------|-----------|----------------|
| V1 | GLM-5.2 (pi) | Claude | **18** |
| V2 | Claude | GLM-5.2 (pi) | **17** |
| **Overlap** | | | **0** |

Both runs used `--dir` mode on the same source directory.

## Why This Matters

- Different model pairings surface **completely different** finding families
- GLM-5.2 as Architect focused on integration/configuration issues (dead config, duplicate I/O abstraction, undocumented SDK struct dependency)
- Claude as Architect focused on lifecycle/concurrency issues (RINGBUF ABI hazard, SPI concurrency, driver lifecycle)
- GLM-5.2 as Inspector found more concrete bugs (10 vs Claude's 7) with runnable probes
- Claude as Inspector found quality/correctness issues (errno ordering, SSID validation, Doppler timing)

## Recommendation

For critical codebases, run two reviews with swapped `--a-cmd`/`--b-cmd` flags. The combined union covers significantly more ground than either pairing alone.

Combined from both runs: 35 unique findings vs ~17-18 from a single run — roughly **2x coverage**.
