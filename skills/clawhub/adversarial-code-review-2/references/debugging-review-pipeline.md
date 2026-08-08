# Debugging the adversarial review pipeline

## Quick diagnostic workflow

When the review fails or hangs, isolate the problem systematically:

```
1. Check exit code and stderr
   → Exit 1 = pipeline/infrastructure failure
   → Exit 2 = nothing to review or git setup failure
   → No output after 60+ seconds = phase is slow or hung

2. Check artifact directory (--out)
   → 01_architect.txt size 0 bytes = Architect phase never finished
   → Missing artifact files = earlier phase failed

3. Test each CLI/tool directly
   echo "Reply TEST_OK" | python3 ~/.../claude-tmux.py --yolo --timeout 30
   → If that works, the tool itself is fine
   → If it hangs, check tmux: tmux list-sessions
```

## Common failure patterns

### `FileNotFoundError` with `~` in the path

```
python3: can't open file '/home/user/project/~/.hermes/skills/script.py'
```

**Cause:** `runner.run_cli` uses `subprocess.Popen(argv, shell=False)`. A literal `~`
in argv is a filesystem character, not a home-directory reference. With `cwd=project`,
it resolves relative to the project directory instead of `$HOME`.

**Fix:** The command must go through `providers.resolve_role_cmd()` which applies
per-token `os.path.expanduser()` via `shlex.split` + `shlex.join`. Verify by
printing the resolved command string from `resolve_role_cmd`.

**Verify:** `python3 -c "import shlex, os; print(' '.join(os.path.expanduser(w) for w in shlex.split(cmd)))"`

### `AttributeError: module 'runner' has no attribute '_fail_phase'`

```
AttributeError: module 'adversarial_common.runner' has no attribute '_fail_phase'
```

**Cause:** The function is named `fail_phase` (no underscore prefix), but the caller
uses `runner._fail_phase()` (with underscore). This is a naming mismatch introduced
by a refactoring that renamed the public function but missed one call site.

**Fix:** Change `runner._fail_phase(...)` to `runner.fail_phase(...)`.

### Phase runs for minutes with no stdout output

```
$ cat /tmp/acr-review.log
bash: ... (harmless shell warnings)
(no further output for 5+ minutes)
```

**Cause:** The phase subprocess (Claude-tmux or Codex) sends output to a tmux pane or
temp file, not to the subprocess stdout. `run_cli` only reads stdout after the process
exits. This is normal — no output ≠ hung.

**Mitigating factors:**
- The code text for `--project-dir` mode can be 300K+ chars (81 files), requiring
  significant LLM processing time per phase (3-5 minutes with Claude).
- The review runs 5 phases sequentially, so total time can be 20-30 minutes.

**Monitor progress:**
- Check `ls -la <out>/01_architect.txt` — non-zero size means Architect completed
- Run `PYTHONUNBUFFERED=1` and redirect to a log file for eventual output
- Use `notify_on_complete=true` with the background process terminal tool

### Claude-tmux hangs inside the pipeline but works when piped directly

```
# Direct test works (fast)
echo "TEST_OK" | python3 claude-tmux.py --yolo --timeout 30

# Pipeline invocation (via run_cli) hangs for minutes
```

**Check:** The pipeline feeds the entire 300K-char codebase as stdin to Claude. This
prompt is large and Claude needs time to process it. A 30-second timeout is too short
for a 300K-char code review prompt — use `--timeout 900` minimum.

**Also check:** Run the claude-tmux command from `resolve_role_cmd` output directly
with a sample of the actual stdin to reproduce the timing.

## Phase-by-phase timing expectations (adversarial-code-loop, 350K chars, 81 files)

| Phase | Tool | Expected time | Notes |
|-------|------|---------------|-------|
| 01_architect | Claude-tmux | 3-5 min | First read of the full codebase |
| 02_inspector | Codex CLI | 2-4 min | Second perspective |
| 03_cross_1 | Claude-tmux | 3-5 min | Architect command reviews Inspector findings |
| 04_cross_2 | Codex CLI | 1-2 min | Inspector command reviews Architect findings; receives Cross 1 as context |
| 05_synthesis | Claude-tmux | 2-4 min | Consolidates all prior phases |

Total: ~11-20 minutes for a codebase of this size.
