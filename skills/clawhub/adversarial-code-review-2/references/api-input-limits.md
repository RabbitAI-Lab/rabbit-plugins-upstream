# API Input Size Limits for Adversarial Review

When using `--project-dir` or `--dir` modes, the review script sends ALL source
files concatenated to the reviewer's stdin. API-based reviewers enforce strict
input size limits that cause silent failures if exceeded.

## Limits by provider

| Provider | Max input chars | Limit type | Failure mode |
|----------|----------------|------------|-------------|
| Codex (OpenAI) | 1,048,576 (1 MB) | Hard API limit | `turn/start failed: Input exceeds the maximum length` — exit 1, empty stdout, no visible error in truncated stderr |
| Claude (Anthropic) | ~200K tokens (~800K chars) | Soft per-model | Model refuses with "input too long" |
| Claude-tmux | Depends on model | Varies | Usually works up to ~2M chars with extended thinking |

Codex is the most restrictive: 1 MB of input characters. A project with 85 source
files averages ~600K chars (safe). Adding test files, build artifacts, or library
dependencies pushes it over the limit.

## Debugging checklist when Architect phase exits 1

1. Check `01_architect.txt` in the output artifact directory — if it's 0 bytes,
   Codex received no stdin or the input was rejected
2. Look for `input_exceeds_maximum_length` or `input_too_large` in stderr
   (it may be buried deep in the output — grep for it)
3. Run `python3 -c "
import os; SKIP={'.git','.venv','__pycache__','node_modules','.pytest_cache','.pio','build','target','test','unity'}; PREFIX={'.adversarial','.omnisense-'}; out=[]
for dp,dirs,files in os.walk('.'):
  dirs[:]=[d for d in dirs if d not in SKIP and not any(d.startswith(p) for p in PREFIX)]
  for n in files:
    if n.startswith('.'): continue
    out.append(os.path.relpath(os.path.join(dp,n),'.'))
    if len(out)>=200: break
  if len(out)>=200: break
total=sum(os.path.getsize(f) for f in out)
print(f'{len(out)} files, {total:,} chars')
"` from the project root to measure the input size

## Fixes

1. Add `test`, `unity` (test framework dirs) to `_SKIP_DIRS`
2. Add `.pio`, `build`, `target` (build artifact dirs) to `_SKIP_DIRS`  
3. Ensure `_SKIP_DIR_PREFIX` catches `.adversarial-*` and `.omnisense-*` dot-dirs
4. Verify dot-prefixed individual files (`.omnisense-*.md` specs) are filtered

Aim for ≤ 700K chars to leave headroom for the persona text (~1.5K per role).
