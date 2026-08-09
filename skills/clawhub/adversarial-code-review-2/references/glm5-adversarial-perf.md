# GLM-5.2 Performance in Adversarial Pipelines

## As REVIEWER (adversarial-code-review or adversarial-code-loop CRITIQUE/VERIFY)

- **Finding quality**: Excellent. Returns structured JSON with id, severity, file, line, description, suggestion. Typical review: 5-10KB JSON, 5-15 findings with concrete runnable probes.
- **Speed**: 3-6 minutes per phase on a 35-file C/C++ embedded project. Comparable to Claude Fable 5, slower than Codex.
- **Thoroughness**: Finds more bugs than Claude or Codex when in Inspector role (observed: 11 findings vs 7 for Claude on same codebase).
- **Tendency to find out-of-scope bugs**: HIGH. GLM-5.2 as reviewer routinely finds pre-existing bugs in files unrelated to the spec scope (pitfall #22 in adversarial-code-loop). Always verify code on disk after REJECT.

## As DEV (adversarial-code-loop BUILD/FIX)

- **Reliability**: Good with provider-specific personas (v1.2.0+). 9/9 steps APPROVED cycle #1 in validated session (omnisense firmware).
- **Without pi-specific personas**: FAILS — overwrites source files with prose reports (`<<<SEE BELOW>>>` placeholder). See `references/glm5-pi-prose-behavior.md`.
- **Speed**: BUILD ~3 min per step, FIX ~6-8 min per cycle.

## Known Limitations

| Issue | Workaround |
|-------|-----------|
| **Sentinel file protocol unsupported** | Use `--dir` or `--stdin` mode, never `--project-dir` |
| **Timeout on large files (>800 lines)** | Use `--dir` to scope smaller, increase `--timeout` to 1800 |
| **Quota limits (Z.AI Lite ~80/5h)** | Track usage between steps, fall back to Codex when exhausted |
| **Prone to out-of-scope findings** | Check code on disk after REJECT before discarding changes |
