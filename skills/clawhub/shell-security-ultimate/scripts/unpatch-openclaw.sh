#!/bin/bash
#
# unpatch-openclaw.sh — the off switch.
#
# Removes the before_tool_call hook patch from your OpenClaw checkout, returning
# that file to its unpatched behaviour. Runs with no confirmation prompt on
# purpose: an off switch you have to argue with is not an off switch.
#
# It does NOT rebuild unless you pass --rebuild. A build executes package
# scripts from the target checkout, which is a separate decision from undoing
# a source edit.
#
set -e

OPENCLAW_DIR="${OPENCLAW_DIR:-$HOME/src/clawdbot-moltbot-openclaw}"
TARGET_REL="src/agents/pi-tool-definition-adapter.ts"
TARGET_FILE="$OPENCLAW_DIR/$TARGET_REL"
START_MARKER="// EXEC-DISPLAY-PATCH: before_tool_call hook"
END_MARKER="// END EXEC-DISPLAY-PATCH"
PATCH_MARKER="EXEC-DISPLAY-PATCH"
IMPORT_LINE='import { getGlobalHookRunner } from "../plugins/hook-runner-global.js";'

# Length of the block patch-openclaw.sh inserts, markers included. If that
# snippet ever changes, this must change with it — tests/test_patch_roundtrip.sh
# fails loudly when the two drift apart. Anything else between the markers is a
# block this script did not write, and it refuses to delete it blind.
EXPECTED_BLOCK_LINES=16

DRY_RUN=0
DO_REBUILD=0
FORCE_RANGE=0

usage() {
    cat <<'USAGE'
Usage: unpatch-openclaw.sh [options]

Removes the before_tool_call hook patch from your OpenClaw checkout.

Options:
  --dry-run      Report whether the patch is present and exit. Touches nothing.
  --rebuild      Rebuild the checkout afterwards. OFF by default: a build runs
                 package scripts from that checkout.
  --force-range  Delete whatever lies between the two markers even when it is
                 not the block this skill inserted. Only for a block that was
                 reformatted after patching. Read the printed range first.
  -h, --help     This text.

Environment:
  OPENCLAW_DIR  Path to the OpenClaw checkout.
                Default: $HOME/src/clawdbot-moltbot-openclaw

A timestamped .unpatch-backup.<date> copy is written before anything is removed.
USAGE
}

while [ $# -gt 0 ]; do
    case "$1" in
        --dry-run)     DRY_RUN=1 ;;
        --rebuild)     DO_REBUILD=1 ;;
        --force-range) FORCE_RANGE=1 ;;
        -h|--help)  usage; exit 0 ;;
        *) echo "❌ Unknown option: $1"; echo; usage; exit 1 ;;
    esac
    shift
done

echo "🔧 OpenClaw Hook Patch Remover"
echo "=============================="
echo ""

if [ ! -f "$TARGET_FILE" ]; then
    echo "❌ Target file not found: $TARGET_FILE"
    echo "   Set OPENCLAW_DIR to your OpenClaw source path."
    exit 1
fi

if ! grep -q "$PATCH_MARKER" "$TARGET_FILE"; then
    echo "✅ Not patched. No changes needed."
    exit 0
fi

echo "Patched file : $TARGET_FILE"

if [ "$DRY_RUN" -eq 1 ]; then
    echo "🔍 Dry run — patch is present, nothing was modified."
    exit 0
fi

# --- Locate the patch, precisely ---------------------------------------------
#
# The obvious implementation is `sed '/START/,/END/d'`. It is also the dangerous
# one: if the end marker is missing — hand-edited, half-applied, truncated — a
# marker-to-marker range runs to end of file and deletes the rest of the source,
# and a success check that only looks for "the marker is gone" reports that as
# a clean removal. So the range is resolved to line NUMBERS and validated before
# a single line is dropped.

count_substr() { grep -F -- "$1" "$2" 2>/dev/null | wc -l | tr -d " "; }
count_exact()  { grep -Fx -- "$1" "$2" 2>/dev/null | wc -l | tr -d " "; }

n_start=$(count_substr "$START_MARKER" "$TARGET_FILE")
n_end=$(count_substr   "$END_MARKER"   "$TARGET_FILE")
n_import=$(count_exact "$IMPORT_LINE"  "$TARGET_FILE")

refuse() {
    echo "❌ Refusing to remove the patch: $1"
    echo ""
    echo "   $TARGET_FILE has NOT been modified."
    echo "   Restore the .backup.<date> file patch-openclaw.sh left beside it, or"
    echo "   run: git -C \"$OPENCLAW_DIR\" checkout -- $TARGET_REL"
    exit 1
}

[ "$n_start" -eq 1 ] || refuse "expected exactly 1 start marker, found $n_start."
[ "$n_end"   -eq 1 ] || refuse "expected exactly 1 end marker, found $n_end. Without a
   matching end marker there is no way to tell where the block stops."
[ "$n_import" -le 1 ] || refuse "found $n_import lines identical to the inserted import;
   removing them all could take out an import this skill did not add."

START_LN=$(grep -Fn -- "$START_MARKER" "$TARGET_FILE" | head -1 | cut -d: -f1)
END_LN=$(grep -Fn   -- "$END_MARKER"   "$TARGET_FILE" | head -1 | cut -d: -f1)

[ "$END_LN" -gt "$START_LN" ] || refuse "the end marker (line $END_LN) is above the start
   marker (line $START_LN)."

BLOCK_LINES=$((END_LN - START_LN + 1))
if [ "$BLOCK_LINES" -ne "$EXPECTED_BLOCK_LINES" ] && [ "$FORCE_RANGE" -eq 0 ]; then
    echo "❌ The block between the markers is $BLOCK_LINES lines; this skill inserts"
    echo "   $EXPECTED_BLOCK_LINES. Something else is in there, so it will not be deleted blind."
    echo ""
    echo "   Lines $START_LN-$END_LN of $TARGET_REL:"
    echo ""
    sed -n "${START_LN},${END_LN}p" "$TARGET_FILE" | sed 's/^/     /'
    echo ""
    echo "   If that really is just the patch, reformatted, re-run with --force-range."
    exit 1
fi

echo "Patch block  : lines $START_LN-$END_LN ($BLOCK_LINES lines)"
if [ "$n_import" -eq 1 ]; then
    IMPORT_LN=$(grep -Fxn -- "$IMPORT_LINE" "$TARGET_FILE" | head -1 | cut -d: -f1)
    echo "Patch import : line $IMPORT_LN"
else
    IMPORT_LN=0
    echo "Patch import : not present (already removed by hand?)"
fi

BACKUP_FILE="$TARGET_FILE.unpatch-backup.$(date +%Y%m%d_%H%M%S)"
cp "$TARGET_FILE" "$BACKUP_FILE"
echo "Backup       : $BACKUP_FILE"
echo ""
echo "📝 Removing patch..."

# Delete by line number, so exactly the validated lines go and nothing else can
# be swept up by a pattern that matched more than it should have.
RESTORED_TMP="$(mktemp)"
trap 'rm -f "$RESTORED_TMP"' EXIT

awk -v s="$START_LN" -v e="$END_LN" -v i="$IMPORT_LN" '
    NR >= s && NR <= e { next }
    i > 0 && NR == i   { next }
    { print }
' "$TARGET_FILE" > "$RESTORED_TMP"

# --- Verify the removal took exactly what it announced ------------------------

EXPECTED_REMOVED=$BLOCK_LINES
# if/then, not `[ ] && ...` — a false test as the last command on a line exits
# the whole script under `set -e`.
if [ "$IMPORT_LN" -gt 0 ]; then
    EXPECTED_REMOVED=$((EXPECTED_REMOVED + 1))
fi

before_lines=$(wc -l < "$TARGET_FILE" | tr -d " ")
after_lines=$(wc -l < "$RESTORED_TMP" | tr -d " ")
actually_removed=$((before_lines - after_lines))

if [ "$actually_removed" -ne "$EXPECTED_REMOVED" ]; then
    echo "❌ Removal would have dropped $actually_removed lines, not $EXPECTED_REMOVED."
    echo "   $TARGET_FILE was NOT modified. Backup left at $BACKUP_FILE."
    exit 1
fi

if grep -Fq -- "$PATCH_MARKER" "$RESTORED_TMP"; then
    echo "❌ A patch marker survives in the result — refusing to write it."
    echo "   $TARGET_FILE was NOT modified. Backup left at $BACKUP_FILE."
    exit 1
fi

cat "$RESTORED_TMP" > "$TARGET_FILE"

if cmp -s "$RESTORED_TMP" "$TARGET_FILE"; then
    echo "   Removed $actually_removed lines (the hook block and its import)"
    echo "✅ Patch removed successfully"
else
    echo "❌ The file on disk does not match the verified result — restoring backup."
    cp "$BACKUP_FILE" "$TARGET_FILE"
    exit 1
fi

echo ""
if [ "$DO_REBUILD" -eq 1 ]; then
    echo "🔨 Rebuilding OpenClaw (this executes that checkout's build scripts)..."
    cd "$OPENCLAW_DIR"
    if command -v pnpm >/dev/null 2>&1; then
        pnpm build
    else
        npm run build
    fi
    echo ""
    echo "✅ Done. Restart the gateway to apply:  systemctl --user restart openclaw-gateway"
else
    echo "ℹ️  Source restored; NOT rebuilt. The running gateway keeps the old build"
    echo "   until you rebuild it yourself:"
    echo ""
    echo "     cd $OPENCLAW_DIR && pnpm build   # or: npm run build"
    echo "     systemctl --user restart openclaw-gateway"
fi
