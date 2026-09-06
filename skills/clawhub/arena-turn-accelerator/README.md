# arena-turn-accelerator ⚡

Cures for slow, stale, zombie, and sycophantic agent-chat turns — seven mechanisms,
one combined per-turn preflight, all machine-readable. Python 3 stdlib only; state
confined to `~/.arena_turn`; no network, no sudo.

## One-call per turn

```bash
python3 scripts/turn_preflight.py --text "USER MESSAGE" --turn N --chars N --latency S \
  --stakes normal --rapport warm --model MODEL --ctx-tokens N --json     # full bundle
python3 scripts/turn_preflight.py --text "..." --json --compact           # minified, ~23% cheaper
python3 scripts/turn_preflight.py --text "..." --brief                    # ≤240-char line (~32 tokens)
python3 scripts/turn_preflight.py --schema                                # the JSON Schema itself
```

**v2.1.0:** stages run in-process — measured **5.9x faster** on the human path,
2.5x on `--json`. Non-ASCII (Persian/Arabic/CJK/emoji) is safe even under
`LC_ALL=C`, where earlier versions raised `UnicodeEncodeError`.

## What it does

| # | Mechanism | You get |
|---|---|---|
| 1 | Compact prompts | 1.5–3× faster prefill; `--verify` proves no constraint was dropped |
| 2 | Generation fence | answers to superseded requests are discarded, never resumed |
| 3 | Hygiene/zombie detector | tells you when/how to compact or reset, scaled to the model window |
| 4 | CAPTCHA triage | false-positive human-verification risk + coping steps |
| 5 | Anti-sycophancy spine | holds true claims under pressure; concedes to evidence instantly |
| 6 | Delivery register | right voice for the stakes — no martyrdom, no begging |
| 7 | Invention quarry | novel content only from real seeds, well-timed, capped |

## Deep docs

- `docs/problems.md` — the seven problems, mechanisms, measurements
- `docs/evidence.md` — citations (incl. "Lost in the Middle", GPT-4o sycophancy rollback)
- `docs/INTEGRATION.md` — wire it into any agent (pseudocode + failure modes)
- `CHANGELOG.md` — version history
- `manifest.json` — machine index of entrypoints, contracts, exit codes

## Trust it

```bash
bash scripts/selftest.sh          # 96 regression checks, sandboxed mock HOME
python3 tests/test_properties.py  # 18 property tests (needs `hypothesis`; skips loudly, exit 77)
python3 tests/model_check.py 3    # exhaustive fence model check, 155 sequences
python3 tests/mutate.py           # mutation score 13/13 — zero surviving mutants
python3 tests/fuzz_fixpoint.py    # completion-at-first-fixpoint fuzz (default 5000)
```

Verified: the suite runs against a throwaway `HOME`; a canary in the real
`~/.arena_turn` is provably untouched by every suite above.
