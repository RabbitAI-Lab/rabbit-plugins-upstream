# Manual Recovery After Phase Failure

When `adversarial_review.py` fails because of a timeout, rate limit, invalid
model output, or provider error, inspect the artifacts already written under
`--out` (default `.adversarial-review/`). The pipeline has no phase-level
continuation mode: a retry runs the full review again.

## Recovery procedure

1. Inspect the `calls` and `failures` in `final.json` together with the phase
   `.txt` artifacts to identify the failing role and its captured stderr.
2. Correct the underlying issue. Increase `--timeout`, wait for quota to
   recover, or replace the affected role command with `--a-cmd`, `--b-cmd`,
   `--cross-a-cmd`, `--cross-b-cmd`, or `--synth-cmd`.
3. Re-run the original source command. Use a new `--out` directory if the
   failed run's artifacts must be preserved for comparison; otherwise the retry
   may replace phase artifacts in the existing directory.
4. Confirm that the new run writes a complete `final.json` and `review.md`.

For example, retry a timed-out cross-review with a longer phase timeout while
preserving the failed run:

```bash
python3 scripts/adversarial_review.py \
  --project-dir /path/to/project \
  --timeout 1200 \
  --out .adversarial-review-retry
```

The `claude-tmux` wrapper rejects the `--yolo` option. Leave it out of role
commands used for retries.

## Cross-review artifact mapping

The implemented cross-review is symmetric:

- `03_cross_1.txt`: cross-review A (the Architect command by default) reviews
  the Inspector's findings.
- `04_cross_2.txt`: cross-review B (the Inspector command by default) reviews
  the Architect's findings. It also receives cross-review A's output as context
  so it can add missed challenges without repeating the first pass.

Cross-review B is not a second Architect pass over the Inspector findings.
After both passes, synthesis consumes the Architect, Inspector, A-on-B, and
B-on-A artifacts and writes `05_synthesis.txt`, `review.md`, and `final.json`.
