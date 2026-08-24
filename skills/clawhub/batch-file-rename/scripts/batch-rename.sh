#!/usr/bin/env bash
# batch-rename.sh — Safely rename multiple files with preview-first semantics
# Usage: bash batch-rename.sh [OPTIONS]

set -euo pipefail

# ── Defaults ──────────────────────────────────────────────────────────────────
DIR=""
DRY_RUN=false
NUMBER=false
KEEP_NAME=false
PREFIX=""
SUFFIX=""
START=1
DIGITS=3
REPLACE_FROM=""
REPLACE_TO=""
LOWERCASE=false
UPPERCASE=false
EXT_LOWER=false
EXT_UPPER=false
GLOB_PAT="*"
UNDO_FILE=""
LOG_FILE=""

# ── Helpers ───────────────────────────────────────────────────────────────────
die() { echo "ERROR: $*" >&2; exit 1; }

usage() {
  cat <<'HELP'
batch-rename.sh — Safely rename multiple files with preview-first semantics

Usage: bash batch-rename.sh [OPTIONS]

Options:
  --dir DIR        Target directory (required)
  --dry-run        Preview changes without renaming
  --number         Add sequential numbers
  --keep-name      Keep original filename when using --number (default: replace)
  --prefix P       Prepend P to each filename
  --suffix S       Append S before extension
  --start N        Starting number for --number (default: 1)
  --digits N       Pad width for --number (default: 3)
  --replace FROM   Replace FROM pattern in filenames
  --with TO        Replace with TO (default: empty)
  --lowercase      Convert filenames to lowercase
  --uppercase      Convert filenames to uppercase
  --ext-lower      Convert extensions to lowercase
  --ext-upper      Convert extensions to uppercase
  --glob PAT       Only match files matching PAT (default: *)
  --undo FILE      Undo using a previous rename log
  --log FILE       Write rename log to FILE (default: <dir>/.rename-log-<timestamp>)
  -h, --help       Show this help
HELP
  exit 0
}

# ── Parse args ────────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dir)        DIR="$2"; shift 2 ;;
    --dry-run)    DRY_RUN=true; shift ;;
    --number)     NUMBER=true; shift ;;
    --keep-name)  KEEP_NAME=true; shift ;;
    --prefix)     PREFIX="$2"; shift 2 ;;
    --suffix)     SUFFIX="$2"; shift 2 ;;
    --start)      START="$2"; shift 2 ;;
    --digits)     DIGITS="$2"; shift 2 ;;
    --replace)    REPLACE_FROM="$2"; shift 2 ;;
    --with)       REPLACE_TO="$2"; shift 2 ;;
    --lowercase)  LOWERCASE=true; shift ;;
    --uppercase)  UPPERCASE=true; shift ;;
    --ext-lower)  EXT_LOWER=true; shift ;;
    --ext-upper)  EXT_UPPER=true; shift ;;
    --glob)       GLOB_PAT="$2"; shift 2 ;;
    --undo)       UNDO_FILE="$2"; shift 2 ;;
    --log)        LOG_FILE="$2"; shift 2 ;;
    -h|--help)    usage ;;
    *)            die "Unknown option: $1" ;;
  esac
done

# ── Undo mode ────────────────────────────────────────────────────────────────
if [[ -n "$UNDO_FILE" ]]; then
  [[ -f "$UNDO_FILE" ]] || die "Undo log not found: $UNDO_FILE"
  count=0
  while IFS='|' read -r tag new old; do
    [[ "$tag" == "RENAME" && -n "$new" && -n "$old" ]] || continue
    if [[ -e "$DIR/$new" && ! -e "$DIR/$old" ]]; then
      mv -- "$DIR/$new" "$DIR/$old"
      echo "  $new → $old"
      count=$((count + 1))
    else
      echo "SKIP: $new → $old (target or source missing)"
    fi
  done < "$UNDO_FILE"
  echo "Undid $count renames"
  exit 0
fi

# ── Validate ─────────────────────────────────────────────────────────────────
[[ -n "$DIR" ]] || die "--dir is required"
[[ -d "$DIR" ]] || die "Not a directory: $DIR"
[[ $DIGITS =~ ^[0-9]+$ ]] || die "--digits must be a number"
[[ $START =~ ^[0-9]+$ ]] || die "--start must be a number"

# Collect files (sorted for deterministic numbering)
mapfile -t FILES < <(find "$DIR" -maxdepth 1 -type f -name "$GLOB_PAT" -not -name ".*" | sort)
[[ ${#FILES[@]} -gt 0 ]] || die "No files matching '$GLOB_PAT' in $DIR"

# ── Build new names ──────────────────────────────────────────────────────────
declare -a OLDS=()
declare -a NEWS=()
counter=$START

for filepath in "${FILES[@]}"; do
  old=$(basename "$filepath")
  name="${old%.*}"
  ext="${old##*.}"
  has_ext=false
  [[ "$old" == *.* ]] && has_ext=true

  new="$name"

  # Pattern replace
  if [[ -n "$REPLACE_FROM" ]]; then
    new="${new//$REPLACE_FROM/$REPLACE_TO}"
  fi

  # Case transforms on filename part
  if $LOWERCASE; then new=$(echo "$new" | tr '[:upper:]' '[:lower:]'); fi
  if $UPPERCASE; then new=$(echo "$new" | tr '[:lower:]' '[:upper:]'); fi

  # Numbering
  if $NUMBER; then
    num=$(printf "%0${DIGITS}d" "$counter")
    if $KEEP_NAME; then
      new="${PREFIX}${new}${num}"
    else
      new="${PREFIX}${num}"
    fi
    counter=$((counter + 1))
  else
    new="${PREFIX}${new}"
  fi

  # Suffix before extension
  new="${new}${SUFFIX}"

  # Extension transforms
  if $EXT_LOWER && $has_ext; then ext=$(echo "$ext" | tr '[:upper:]' '[:lower:]'); fi
  if $EXT_UPPER && $has_ext; then ext=$(echo "$ext" | tr '[:lower:]' '[:upper:]'); fi

  # Reassemble
  if $has_ext; then
    new="${new}.${ext}"
  fi

  # Skip if unchanged
  [[ "$new" != "$old" ]] || continue

  OLDS+=("$old")
  NEWS+=("$new")
done

[[ ${#OLDS[@]} -gt 0 ]] || { echo "Nothing to rename."; exit 0; }

# ── Collision detection ──────────────────────────────────────────────────────
declare -A SEEN
for n in "${NEWS[@]}"; do
  if [[ -n "${SEEN[$n]:-}" ]]; then
    die "Collision: multiple files would be renamed to '$n'"
  fi
  SEEN[$n]=1
done

# Check target doesn't already exist
for i in "${!OLDS[@]}"; do
  if [[ -e "$DIR/${NEWS[$i]}" && "${OLDS[$i]}" != "${NEWS[$i]}" ]]; then
    die "Target already exists: ${NEWS[$i]} (refusing to overwrite)"
  fi
done

# ── Execute ──────────────────────────────────────────────────────────────────
if $DRY_RUN; then
  echo "=== DRY-RUN — no files will be renamed ==="
  for i in "${!OLDS[@]}"; do
    echo "  ${OLDS[$i]} → ${NEWS[$i]}"
  done
  echo "${#OLDS[@]} files will be renamed"
  exit 0
fi

# Setup log
TS=$(date +%Y%m%d-%H%M%S)
LOG_FILE="${LOG_FILE:-$DIR/.rename-log-$TS}"
echo "Rename log: $LOG_FILE"

> "$LOG_FILE"
renamed=0
for i in "${!OLDS[@]}"; do
  old="${OLDS[$i]}"
  new="${NEWS[$i]}"
  mv -- "$DIR/$old" "$DIR/$new"
  echo "RENAME|$new|$old" >> "$LOG_FILE"
  echo "  $old → $new"
  renamed=$((renamed + 1))
done

echo "Renamed $renamed files. Log saved to $LOG_FILE"
echo "To undo: bash $0 --undo $LOG_FILE --dir $DIR"
