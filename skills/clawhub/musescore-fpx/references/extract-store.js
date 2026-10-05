#!/usr/bin/env node
// Pull a value out of MuseScore's HTML-entity-encoded JSON store.
//
// MuseScore server-renders NO result cards / DOM tables — the data is a JSON
// blob embedded in the markup as HTML-attribute-escaped text (its analogue of
// a Next.js `__NEXT_DATA__` blob). This mirrors musescore-mcp's
// `src/store.ts` (`recoverJson` + `findArrayByKey` / `findEnclosingObject`)
// as a dependency-free script so the fpx skill doesn't need the MCP installed.
//
// Usage:
//   node extract-store.js <key>            # the ARRAY that is the value of "<key>":
//   node extract-store.js <key> --object    # the enclosing OBJECT that contains "<key>":
//
// Reads HTML on stdin, writes JSON on stdout.
//
// Examples:
//   fpx get '.../sheetmusic?text=zelda&recording_type=free-download' -p musescore \
//     | node extract-store.js scores
//   fpx get '.../user/12345/scores/67890' -p musescore \
//     | node extract-store.js type_download_list
//   fpx get '.../user/12345/scores/67890' -p musescore \
//     | node extract-store.js license --object   # the main score object

const key = process.argv[2];
const wantObject = process.argv.includes('--object');
if (!key) {
  console.error('usage: extract-store.js <key> [--object]');
  process.exit(1);
}

let html = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (chunk) => (html += chunk));
process.stdin.on('end', () => {
  const decoded = recoverJson(html);
  const result = wantObject
    ? findEnclosingObject(decoded, key)
    : findArrayByKey(decoded, key);
  if (result === null) {
    console.error(`No ${wantObject ? 'object' : 'array'} found for key "${key}".`);
    process.exit(1);
  }
  process.stdout.write(JSON.stringify(result));
});

// Reverse HTML-attribute escaping. Order matters: decode `&amp;` LAST so a
// literal `&quot;` in the data (encoded as `&amp;quot;`) round-trips instead
// of collapsing into a bare quote.
function recoverJson(s) {
  return s
    .replace(/&quot;/g, '"')
    .replace(/&#0?39;/g, "'")
    .replace(/&#x27;/gi, "'")
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&amp;/g, '&');
}

// String-aware bracket match so quoted brackets don't confuse the depth
// count. `s[start]` must be `{` or `[`.
function matchBracket(s, start) {
  const open = s[start];
  const close = open === '[' ? ']' : open === '{' ? '}' : '';
  if (!close) return null;
  let depth = 0;
  let inStr = false;
  let esc = false;
  for (let p = start; p < s.length; p++) {
    const c = s[p];
    if (inStr) {
      if (esc) esc = false;
      else if (c === '\\') esc = true;
      else if (c === '"') inStr = false;
    } else if (c === '"') inStr = true;
    else if (c === open) depth++;
    else if (c === close) {
      depth--;
      if (depth === 0) return s.slice(start, p + 1);
    }
  }
  return null;
}

// The array that is the value of the first `"<key>":[` in `decoded` — e.g.
// search results live under `"scores"`, distinct from sibling feeds like
// `"see_other_scores"` / `"scores_to_be_promoted"` (none of those contain the
// literal `"scores":`). Skips occurrences whose value isn't a non-empty array
// of predicate-matching objects, mirroring musescore-mcp's `src/store.ts`.
function findArrayByKey(decoded, key, predicate = () => true) {
  const needle = `"${key}":`;
  let from = 0;
  for (;;) {
    const at = decoded.indexOf(needle, from);
    if (at < 0) return null;
    from = at + needle.length;
    let p = from;
    while (p < decoded.length && /\s/.test(decoded[p])) p++;
    if (decoded[p] === '[') {
      const slice = matchBracket(decoded, p);
      if (slice) {
        try {
          const arr = JSON.parse(slice);
          if (
            Array.isArray(arr) &&
            arr.length > 0 &&
            arr[0] &&
            typeof arr[0] === 'object' &&
            predicate(arr[0])
          ) {
            return arr;
          }
        } catch {
          // not valid JSON here — keep scanning for another match
        }
      }
    }
  }
}

// The innermost JSON object that contains the literal `"<key>":` and also
// satisfies the predicate — backtracks to the enclosing `{`, then
// bracket-matches forward. Use this to pull the main score object off a
// score-detail page (identify it by a field only it carries, e.g.
// "license"). Retries subsequent occurrences of the key when an earlier one
// fails to parse or fails the predicate, mirroring musescore-mcp's
// `src/store.ts`.
function findEnclosingObject(decoded, key, predicate = () => true) {
  const needle = `"${key}":`;
  let from = 0;
  for (;;) {
    const i = decoded.indexOf(needle, from);
    if (i < 0) return null;
    // backtrack to the enclosing object's opening brace
    let depth = 0;
    let start = -1;
    for (let p = i; p >= 0; p--) {
      const c = decoded[p];
      if (c === '}') depth++;
      else if (c === '{') {
        if (depth === 0) {
          start = p;
          break;
        }
        depth--;
      }
    }
    if (start >= 0) {
      const slice = matchBracket(decoded, start);
      if (slice) {
        try {
          const obj = JSON.parse(slice);
          if (obj && typeof obj === 'object' && predicate(obj)) {
            return obj;
          }
        } catch {
          // fall through to next occurrence
        }
      }
    }
    from = i + needle.length;
  }
}
