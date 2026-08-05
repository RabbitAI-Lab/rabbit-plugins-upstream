# Monitoring Background Adversarial Reviews

When launching an adversarial review as a background process (long pipelines, Fable 5
extended thinking), use this incremental-check pattern to show intermediate results to
the user between phases — instead of waiting silently for the entire pipeline to finish.

## The Pattern

```python
# After launching with terminal(background=true, notify_on_complete=true):

# 1. Wait for initial output dir (the script creates it immediately)
sleep 30
tail $LOG_FILE
ls -la $OUTPUT_DIR/

# 2. Poll at intervals between known phase durations
sleep 180
tail $LOG_FILE
ls -la $OUTPUT_DIR/
# Check for new artifact files: 01_architect.txt, 02_inspector.txt, etc.

# 3. Show intermediate findings to the user
# Read reviewer artifacts as they appear to surface high-value content early
```

## Artifact File Progression

| Phase | Artifact | Typical Duration | Notes |
|-------|----------|-----------------|-------|
| Setup | `diff.txt` | < 5s | Project snapshot / file tree |
| REVIEW A (Architect) | `01_architect.txt` | 5-15 min | Fable 5: 8-15 min; Codex/DeepSeek: 2-5 min |
| REVIEW B (Inspector) | `02_inspector.txt` | 2-5 min | Codex fast, DeepSeek medium, Fable slow |
| CROSS A→B | `03_cross_1.txt` | 5-15 min | Architect command reviews Inspector findings; usually the same speed as A |
| CROSS B→A | `04_cross_2.txt` | 5-15 min | Inspector command reviews Architect findings and receives A→B output as context; usually the same speed as B |
| SYNTHESIS | `05_synthesis.txt` + `final.json` | 2-5 min | Fast: just consolidating |

## What to Check Per Poll

```bash
# Quick status: most recent log lines and file listing
tail -5 $LOG_FILE && ls -la $OUTPUT_DIR/

# Check if a new phase started (log shows "PHASE: ...")
grep "PHASE:" $LOG_FILE | tail -3

# Read findings as soon as they're available (before synthesis)
# to give the user a preview
cat $OUTPUT_DIR/01_architect.txt | python3 -c "
import sys, json
d = json.load(sys.stdin)
print(f'Findings: {len(d[\"findings\"])} — Verdict: {d[\"verdict\"]}')
for f in d['findings']:
    print(f'  [{f[\"severity\"]}] {f[\"id\"]}: {f[\"title\"]}')
"
```

## Phase Timing Reference (measured)

| A model | B model | Phase A | Phase B | Cross 1 | Cross 2 | Synth | Total |
|---------|---------|---------|---------|---------|---------|-------|-------|
| Fable 5 | Codex | 12 min | 2 min | 8 min | 8 min | 2 min | ~32 min |
| Codex | DeepSeek | 3 min | 5 min | 4 min | 4 min | 2 min | ~18 min |
| Codex | Codex | 3 min | 3 min | 3 min | 3 min | 2 min | ~14 min |

Fable 5 times include extended thinking (8-12 min of '...' before any visible output).
The wrapper captures the output file when the done.sentinel appears, not before.
