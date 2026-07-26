#!/bin/bash
# research-assistant: illustrate Bear notes tagged 待整理 with topic-relevant GIFs.
# Platform: macOS (requires Bear app + grizzly + gifgrep). See SKILL.md.
set -euo pipefail

TAG="待整理"
MAX=0
MODE="append"
DRY_RUN=0
TOKEN_FILE="${HOME}/.config/grizzly/token"
MARKER="<!-- research-assistant:gif -->"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tag) TAG="$2"; shift 2 ;;
    --max) MAX="$2"; shift 2 ;;
    --mode) MODE="$2"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    --token-file) TOKEN_FILE="$2"; shift 2 ;;
    -h|--help)
      echo "Usage: $0 [--tag NAME] [--max N] [--mode append|prepend] [--dry-run] [--token-file PATH]"
      exit 0 ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

for bin in grizzly gifgrep jq; do
  command -v "$bin" >/dev/null 2>&1 || { echo "❌ Missing required binary: $bin" >&2; exit 1; }
done

# Build a short GIF search query from a note's title + most frequent body words.
topic_query() {
  local title="$1" body="$2"
  local words
  words=$(printf '%s %s' "$title" "$body" \
    | tr '[:upper:]' '[:lower:]' \
    | tr -cs '[:alnum:]' '\n' \
    | awk 'length($0) > 3' \
    | grep -Ev '^(this|that|with|from|have|will|your|they|them|then|than|into|about|note|todo)$' \
    | sort | uniq -c | sort -rn | head -4 | awk '{print $2}' | tr '\n' ' ')
  local q
  q=$(printf '%s %s' "$title" "$words" | xargs)
  [[ -n "$q" ]] && echo "$q" || echo "$title"
}

echo "🔍 Scanning Bear for notes tagged: $TAG"
NOTE_IDS=$(grizzly open-tag --name "$TAG" --enable-callback --json \
  | jq -r '.notes[]?.identifier // .[]?.identifier // empty')

if [[ -z "$NOTE_IDS" ]]; then
  echo "No notes found with tag '$TAG'. Nothing to do."
  exit 0
fi

count=0
while IFS= read -r ID; do
  [[ -z "$ID" ]] && continue
  if [[ "$MAX" -gt 0 && "$count" -ge "$MAX" ]]; then break; fi

  NOTE_JSON=$(grizzly open-note --id "$ID" --enable-callback --json)
  TITLE=$(echo "$NOTE_JSON" | jq -r '.note.title // .title // ""')
  BODY=$(echo "$NOTE_JSON" | jq -r '.note.note // .note // ""')

  if echo "$BODY" | grep -qF "$MARKER"; then
    echo "⏭️  [$ID] already illustrated, skipping."
    continue
  fi

  QUERY=$(topic_query "$TITLE" "$BODY")
  GIF_URL=$(gifgrep "$QUERY" 2>/dev/null | grep -Eo 'https?://[^ ]+\.(gif|GIF)' | head -1 || true)

  if [[ -z "$GIF_URL" ]]; then
    echo "⚠️  [$ID] no GIF found for query: \"$QUERY\""
    continue
  fi

  INSERT=$'\n'"$MARKER"$'\n'"![${QUERY}](${GIF_URL})"$'\n'

  if [[ "$DRY_RUN" -eq 1 ]]; then
    echo "📝 [DRY] [$ID] \"$TITLE\" → query=\"$QUERY\" → $GIF_URL"
  else
    printf '%s' "$INSERT" | grizzly add-text --id "$ID" --mode "$MODE" --token-file "$TOKEN_FILE"
    echo "✅ [$ID] \"$TITLE\" → inserted GIF for \"$QUERY\""
  fi
  count=$((count + 1))
done <<< "$NOTE_IDS"

echo "Done. Processed $count note(s)."
