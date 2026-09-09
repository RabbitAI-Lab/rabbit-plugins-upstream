#!/usr/bin/env bash
# session-closeout.sh — read-only end-of-session checks plus one intentional
# append to today's daily memory file. Runs nothing else: no builders, no hooks.
set -euo pipefail

# ── Workspace root ───────────────────────────────────────
ROOT="${OPENCLAW_WORKSPACE:-$(pwd)}"
TODAY_UTC="$(date -u +%F)"
NOW_UTC="$(date -u '+%Y-%m-%d %H:%M UTC')"
MEM_DIR="$ROOT/memory"
MEM_FILE="$MEM_DIR/$TODAY_UTC.md"
MASTER_TODO_FILE="$ROOT/MASTER_TODO.md"
PROJECTS_DIR="${CLOSEOUT_PROJECTS_DIR:-$ROOT/projects}"
STALE_HOURS="${CLOSEOUT_TODO_STALE_HOURS:-24}"

# ── Optional inputs (pipe-delimited) ─────────────────────
CLOSEOUT_OUTCOMES="${CLOSEOUT_OUTCOMES:-}"
CLOSEOUT_BLOCKERS="${CLOSEOUT_BLOCKERS:-}"
CLOSEOUT_NEXT="${CLOSEOUT_NEXT:-}"
CLOSEOUT_PROJECTS="${CLOSEOUT_PROJECTS:-}"

split_pipe() { # "a|b" -> one trimmed item per line
  local raw="$1"; [[ -z "$raw" ]] && return 0
  local IFS='|'; read -r -a _parts <<< "$raw"
  local p
  for p in "${_parts[@]}"; do
    p="${p#"${p%%[![:space:]]*}"}"; p="${p%"${p##*[![:space:]]}"}"
    [[ -n "$p" ]] && printf '%s\n' "$p"
  done
}

mtime_epoch() { # portable file mtime (GNU or BSD stat), 0 if missing
  stat -c %Y "$1" 2>/dev/null || stat -f %m "$1" 2>/dev/null || echo 0
}

# ── 1) Task hygiene: report MASTER_TODO.md freshness (never rebuilds it) ──
NOW_EPOCH="$(date -u +%s)"
if [[ -f "$MASTER_TODO_FILE" ]]; then
  AGE_H=$(( (NOW_EPOCH - $(mtime_epoch "$MASTER_TODO_FILE")) / 3600 ))
  if (( AGE_H > STALE_HOURS )); then
    MASTER_TODO_STATUS="stale"; MASTER_TODO_DETAIL="last updated ${AGE_H}h ago"
  else
    MASTER_TODO_STATUS="fresh"; MASTER_TODO_DETAIL="updated ${AGE_H}h ago"
  fi
else
  MASTER_TODO_STATUS="missing"; MASTER_TODO_DETAIL="no MASTER_TODO.md"
fi

# ── 2) Repo hygiene: dirty repos (read-only) ─────────────
mapfile -t GIT_DIRS < <(find "$ROOT" -maxdepth 4 -type d -name .git 2>/dev/null | sed 's#/\.git$##' | sort)
DIRTY=()
for repo in "${GIT_DIRS[@]}"; do
  if [[ -n "$(git -C "$repo" status --porcelain 2>/dev/null || true)" ]]; then
    DIRTY+=("$repo")
  fi
done
rel_path() { local r="${1#"$ROOT"/}"; [[ "$r" == "$1" ]] && r="."; printf '%s' "$r"; }

# ── 3) Project-doc hygiene: were core docs touched today? (warn only) ──
STALE_PROJECT_DOCS=()
if [[ -n "$CLOSEOUT_PROJECTS" ]]; then
  while IFS= read -r slug; do
    found_today="no"; any_doc="no"
    for doc in STATUS.md DECISIONS.md PROJECT.md BACKLOG.md; do
      f="$PROJECTS_DIR/$slug/$doc"
      [[ -f "$f" ]] || continue
      any_doc="yes"
      if [[ "$(date -u -r "$(mtime_epoch "$f")" +%F 2>/dev/null || date -u -d "@$(mtime_epoch "$f")" +%F)" == "$TODAY_UTC" ]]; then
        found_today="yes"; break
      fi
    done
    if [[ "$any_doc" == "no" ]]; then
      STALE_PROJECT_DOCS+=("$slug (no core docs found under $(rel_path "$PROJECTS_DIR")/$slug)")
    elif [[ "$found_today" == "no" ]]; then
      STALE_PROJECT_DOCS+=("$slug (no core doc updated today)")
    fi
  done < <(split_pipe "$CLOSEOUT_PROJECTS")
fi

# ── 4) Automation hygiene: not verifiable from here ──────
AUTOMATION_STATUS="not_verified"
AUTOMATION_REASON="manual_review_required"

# ── 5) Compute the final status BEFORE writing anything ──
EXCEPTIONS=()
[[ "$MASTER_TODO_STATUS" == "missing" ]] && EXCEPTIONS+=("high|MASTER_TODO.md missing|Create or restore it")
[[ "$MASTER_TODO_STATUS" == "stale" ]]   && EXCEPTIONS+=("medium|MASTER_TODO.md $MASTER_TODO_DETAIL|Refresh it as a separate, reviewed step")
((${#DIRTY[@]} > 0)) && EXCEPTIONS+=("medium|${#DIRTY[@]} dirty repo(s)|Review git status manually")
for s in "${STALE_PROJECT_DOCS[@]:-}"; do
  [[ -n "$s" ]] && EXCEPTIONS+=("low|project docs: $s|Update STATUS/DECISIONS if the session changed them")
done

CLOSEOUT_STATUS="ok"
if [[ "$MASTER_TODO_STATUS" == "missing" ]]; then
  CLOSEOUT_STATUS="error"
elif ((${#EXCEPTIONS[@]} > 0)); then
  CLOSEOUT_STATUS="warning"
fi

# ── 6) Memory hygiene: the one intentional write ─────────
mkdir -p "$MEM_DIR"
[[ -f "$MEM_FILE" ]] || printf '# %s\n\n' "$TODAY_UTC" > "$MEM_FILE"

DEFAULT_OUTCOMES=("Closeout completed")
((${#DIRTY[@]} == 0)) && DEFAULT_OUTCOMES+=("All repos clean") || DEFAULT_OUTCOMES+=("${#DIRTY[@]} dirty repo(s) found")
DEFAULT_BLOCKERS=()
((${#DIRTY[@]} > 0)) && DEFAULT_BLOCKERS+=("${#DIRTY[@]} dirty repo(s) need manual review")
[[ "$MASTER_TODO_STATUS" != "fresh" ]] && DEFAULT_BLOCKERS+=("MASTER_TODO.md $MASTER_TODO_STATUS ($MASTER_TODO_DETAIL)")
((${#DEFAULT_BLOCKERS[@]} == 0)) && DEFAULT_BLOCKERS+=("None")
DEFAULT_NEXT=()
((${#DIRTY[@]} > 0)) && DEFAULT_NEXT+=("Resolve dirty repo(s) before next work block")
DEFAULT_NEXT+=("Resume from highest-priority item in MASTER_TODO.md")

emit_bullets() { # $1 = override string, rest = defaults
  local override="$1"; shift
  if [[ -n "$override" ]]; then split_pipe "$override" | sed 's/^/  - /'
  else local b; for b in "$@"; do printf '  - %s\n' "$b"; done; fi
}

{
  echo "## Session Closeout — $NOW_UTC"
  echo "- Status: $CLOSEOUT_STATUS"
  echo "- MASTER_TODO: $MASTER_TODO_STATUS ($MASTER_TODO_DETAIL)"
  if ((${#DIRTY[@]} == 0)); then echo "- Dirty repos: none"
  else
    echo "- Dirty repos: ${#DIRTY[@]}"
    for d in "${DIRTY[@]}"; do echo "  - $(rel_path "$d")"; done
  fi
  if ((${#STALE_PROJECT_DOCS[@]} > 0)); then
    echo "- Project docs not updated today:"
    for s in "${STALE_PROJECT_DOCS[@]}"; do echo "  - $s"; done
  fi
  echo "- Key outcomes:";            emit_bullets "$CLOSEOUT_OUTCOMES" "${DEFAULT_OUTCOMES[@]}"
  echo "- Blockers:";                emit_bullets "$CLOSEOUT_BLOCKERS" "${DEFAULT_BLOCKERS[@]}"
  echo "- Next session starts with:"; emit_bullets "$CLOSEOUT_NEXT" "${DEFAULT_NEXT[@]}"
  echo
} >> "$MEM_FILE"

# ── 7) Summary (key=value for the agent) ─────────────────
echo "SESSION_CLOSEOUT_OK"
echo "CLOSEOUT_STATUS=$CLOSEOUT_STATUS"
echo "MASTER_TODO_STATUS=$MASTER_TODO_STATUS"
echo "MASTER_TODO_DETAIL=$MASTER_TODO_DETAIL"
echo "DIRTY_REPO_COUNT=${#DIRTY[@]}"
echo "PROJECT_DOC_WARNINGS=${#STALE_PROJECT_DOCS[@]}"
echo "AUTOMATION_STATUS=$AUTOMATION_STATUS"
echo "AUTOMATION_REASON=$AUTOMATION_REASON"
echo "MEMORY_FILE=$(rel_path "$MEM_FILE")"
echo "EXCEPTION_COUNT=${#EXCEPTIONS[@]}"
i=1
for e in "${EXCEPTIONS[@]:-}"; do
  [[ -n "$e" ]] && { echo "EXCEPTION_$i=$e"; ((i++)); }
done
if ((${#DIRTY[@]} > 0)); then
  echo "DIRTY_REPOS:"
  for d in "${DIRTY[@]}"; do echo "- $(rel_path "$d")"; done
fi
