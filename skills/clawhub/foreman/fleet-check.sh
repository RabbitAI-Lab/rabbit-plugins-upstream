#!/bin/bash
# foreman fleet-check — pipeline health check before a batch dispatch.
# Any FAIL exits non-zero. Optional channels only WARN.
fail=0
ok(){ printf 'PASS  %s\n' "$1"; }
bad(){ printf 'FAIL  %s\n      fix: %s\n' "$1" "$2"; fail=1; }
warn(){ printf 'WARN  %s\n' "$1"; }

# 1. Builder line: handoff (public CLI, this is the one foreman dispatches through)
command -v handoff >/dev/null 2>&1 && ok "handoff CLI" \
  || bad "handoff not installed" "uv tool install handoff-cli && handoff init"
[ -f "$HOME/.handoff/config.yaml" ] && ok "handoff config" \
  || bad "handoff has no config" "edit ~/.handoff/config.yaml and configure your backends (e.g. deepseek / hosted / local)"

# 2. QA line: a second-opinion CLI from another vendor, for escalation
if command -v codex >/dev/null 2>&1; then
  ok "codex CLI (for non-interactive calls remember --skip-git-repo-check and stdin from /dev/null)"
  # Ask the CLI about its own auth rather than stat-ing its credential file.
  if codex login status >/dev/null 2>&1; then
    ok "codex logged in"
  else
    warn "codex login state unconfirmed — if dispatch fails with 401, run: codex login"
  fi
else
  warn "codex CLI absent — escalation falls back to the main session (npm i -g @openai/codex)"
fi

# 3. Acceptance line: dynamic checker (optional; see verify.md section 1)
if [ -n "${FOREMAN_HARDENING_CMD:-}" ]; then
  ok "dynamic checker configured (FOREMAN_HARDENING_CMD)"
else
  warn "no FOREMAN_HARDENING_CMD — acceptance degrades to task-level verification only (correct for libraries/CLIs/backends)"
fi

# 4. Overflow line: cursor agent (optional)
command -v cursor-agent >/dev/null 2>&1 || command -v agent >/dev/null 2>&1 \
  && ok "cursor agent CLI" \
  || warn "cursor agent absent (optional overflow channel; see cursor.com for its installer)"

# 5. Container line: caged worker (optional)
if docker image inspect foreman-worker:latest >/dev/null 2>&1 && docker info >/dev/null 2>&1; then
  ok "caged worker (foreman-worker image + live daemon)"
else
  warn "caged worker unavailable (start your container runtime, then: see the inlined Dockerfile in dispatch.md §3)"
fi

# 6. Environment contamination (hard rule: a worker's key must never leak into your shell)
case "${ANTHROPIC_BASE_URL:-}" in
  ""|https://api.anthropic.com|https://api.anthropic.com/) ok "no ANTHROPIC_BASE_URL leak" ;;
  *) bad "ANTHROPIC_BASE_URL is set to a non-default value (not printed here — it can carry a token)" \
        "remove it from your shell rc — it silently reroutes every agent session on this machine to another backend" ;;
esac

exit $fail
