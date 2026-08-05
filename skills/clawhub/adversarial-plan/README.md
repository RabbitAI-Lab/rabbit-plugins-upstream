# adversarial-plan

**Spec → implementation plan.** Two-role adversarial pipeline that reads a spec (from `adversarial-spec`) and optional review findings (from `adversarial-code-review`), then produces a `plan.md` with ordered steps.

For Hermes Agent, Claude Code, Codex, or any LLM CLI.

## How it works

```text
PREFLIGHT ──→ optional DEEP RESEARCH ──→ GIT SETUP
                                           │
                                           ├─ delegated success ──→ FINALIZE
                                           │
                                           └─ direct/fallback ──→ PLAN ──→ CHALLENGE
                                                                          │
                                               APPROVE + no findings ──────┤
                                                                          │
                                               otherwise ──→ REVISE ──→ VERIFY
                                                                  ↑          │
                                                                  └──────────┘ up to --max-loops
                                                                          │
                                                                      FINALIZE
```

The direct pipeline has one CHALLENGE phase and no `CROSS_2` phase. A successful
delegated run bypasses the adversarial loop; delegated fallback uses the direct
pipeline. FINALIZE squash-merges approval unless `--no-merge` is set, or records
a rejection marker if findings remain.

## Plan format

```yaml
### P1: Step title
- **Files:** /path/to/file1, /path/to/file2
- **Description:** What to implement
- **Dependencies:** []
- **Tests:** How to verify
- **Risks:** What could go wrong
```

`adversarial-code-loop` does not provide a functional plan-file mode. To
implement a generated plan, convert each step's Files, Description, Tests, and
Risks into a focused spec, then invoke the code loop with `--spec` for each step
in dependency order. See [Running plan steps without plan mode](references/run-plan-steps-without-plan-mode.md)
for the complete workflow and launch example.

## Comparison

| Feature | adversarial-plan | Manual planning |
|---------|-----------------|-----------------|
| Adversarial challenge | ✅ plan-challenger critiques order, gaps, risks | ❌ |
| Git-native | ✅ branch-per-plan, squash-merge | ❌ |
| Findings-aware | ✅ accepts structured findings JSON | ❌ |
| Code-loop workflow | ✅ per-step specs feed repeated `--spec` runs | Manual step extraction |

## Quick start

```bash
python3 scripts/adversarial_plan.py \
  --spec spec.md \
  --findings findings.json \
  --dev-cmd "pi --provider zai --model glm-5.2" \
  --review-cmd "pi --provider deepseek --model deepseek-v4-pro"
```

## Dependencies

- Python ≥ 3.11
- Git ≥ 2.5
- Two LLM CLIs (plan-writer + plan-challenger)

Uses `adversarial-common` as the shared engine.

## License

0BSD — see [LICENSE](LICENSE).
