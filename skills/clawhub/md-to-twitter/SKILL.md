---
name: md-to-twitter
description: "Convert Markdown for X Articles, Premium long posts, or threads. Article mode exports HTML prose with visible code fences, or optional native-code placeholders. Use when the user asks to prepare an article for X or Twitter, preserve code formatting, attach images, or create posts."
---

# md-to-twitter — Markdown for X Articles and posts

## Choose the editor first

Use the conversation or editor screenshot to identify the target. If the target is unclear, ask before conversion.

| Target | Mode | Result |
| --- | --- | --- |
| X Articles | `--article --clip` | HTML prose with visible code fences and media placeholders |
| X Articles with native code panels | `--article --article-code native --clip` | HTML prose with code and media placeholders |
| Premium long post | `--limit 25000` | Plain text with attachment notes |
| Thread | Default 280-character mode | Split plain-text posts with attachment notes |

Prefer the Article workflow for the full technical-article task verified below. Use thread mode only when requested.

Get approval before generating output. Get separate approval before posting, committing, pushing, or publishing the skill.

## X Articles: accepted workflow

Generate the Article export from the repository root:

```sh
uv run .opencode/skills/md-to-twitter/scripts/md2twitter.py \
  docs/261119-backup-opencode-sqlite-sessions-zh-hans.md --article --clip
```

The first H1 becomes the separate article title. The body retains headings, paragraphs, emphasis, lists, and links.

Code appears between visible Markdown fences inside HTML `<pre><code>`. Shell fences use the `bash` label.

**These are literal fences, not native code panels.** They do not provide syntax highlighting or a code-copy button.

Images and table screenshots remain manual uploads. Their numbered placeholders mark their positions in the body.

### Verified in X Articles on 2026-11-28

The user accepted the full Simplified-Chinese SQLite backup article after a normal HTML paste. It contained 11 fenced code blocks and four media placeholders.

| Test | Observed result |
| --- | --- |
| Plain-text newlines | Large paragraph gaps |
| Shift+Enter in the editor | Tight line spacing |
| HTML `<p>` and `<br>` | Paragraph separation and tight internal line breaks |
| HTML `<pre><code>` without fences | Ordinary text, not a native code panel |
| `<blockquote><pre><code>` | Quote border with an unwanted final blank line |
| `<blockquote><p>` with internal `<br>` | Compact quote without a final blank line |
| Native panel copied back into X | Plain text, not a reconstructed panel |
| Literal fences inside `<pre><code>` | Visible fences, language label, and tightly grouped code |
| Insert → Code → Bash | Native panel with highlighting and a copy button |

Keep the accepted fenced format as the default. Do not replace it with blockquotes.

These results describe the tested editor. They do not prove that every future X editor handles HTML identically.

### Outputs

For a source in `docs/`, output goes to `exports/`. The source Markdown stays unchanged.

| Output | Purpose |
| --- | --- |
| `<source>-twitter-article.html` | Paste body with fenced code and media placeholders |
| `<source>-twitter-article-instructions.md` | Title and ordered assembly instructions |
| `<source>-twitter-article.json` | Title, code mode, and ordered asset manifest |
| `<source>-twitter-article-assets/code-01.txt` | Plain-text reference copy of a code block |
| `<source>-twitter-article-assets/table-01.png` | Table screenshot for upload |

Code files preserve indentation and internal line breaks. The converter omits fence markers and trailing newlines from their content.

In default mode, code files are reference copies. No manual code insertion is needed.

The default HTML contains no code placeholders. It still contains media placeholders until their images are uploaded.

### Copy and paste

1. Enter the reported title in X's article title field.
2. Click inside an empty article body.
3. Paste with **Ctrl+V**.
4. Replace each media placeholder through Insert → Media.
5. Upload the corresponding file from the assembly instructions.
6. Check headings, code spacing, indentation, long lines, and images.
7. Remove all remaining placeholders before publishing.

Use normal paste, not **Ctrl+Shift+V**. Plain-text paste discards the HTML structure used by this workflow.

If the clipboard expires, reload the existing HTML without regenerating assets:

```sh
wl-copy --foreground --type text/html \
  < exports/261119-backup-opencode-sqlite-sessions-zh-hans-twitter-article.html
```

Keep that terminal running until the paste finishes. Then press Ctrl+C in the terminal to stop the clipboard owner.

For the browser fallback, open the HTML file. Copy the rendered page, not its source. Keep the tab open until you paste.

The converter's `--clip` option also starts a clipboard owner. If that process disappears, use the foreground command above.

### Optional native-code panels

Use this mode only when the user accepts manual insertion for every code block:

```sh
uv run .opencode/skills/md-to-twitter/scripts/md2twitter.py \
  docs/261119-backup-opencode-sqlite-sessions-zh-hans.md \
  --article --article-code native --clip
```

For each code placeholder:

1. Delete its text without removing its paragraph.
2. Keep the cursor there.
3. Choose Insert → Code.
4. Select the language from the assembly instructions.
5. Paste the entire corresponding code file as plain text.
6. Click Insert.

Shell fences map to Bash. SQL fences map to SQL. Unlabelled blocks request Plain text.

If the requested language is unavailable, select a suitable editor option manually.

### Article mode boundaries

- Article mode never posts through the API.
- It rejects thread options such as `--limit`, `--post`, and `--tables image`.
- `--out` must name an HTML file.
- Tables become screenshots automatically. Native table insertion remains untested.
- Local images must exist. Remote images need local upload files before export.
- The four-image limit for regular posts does not control the Article export.
- Repeated exports replace generated output at the same paths.

## Premium long posts and threads

These modes produce plain text. They do not use the Article editor's HTML workflow.

For Premium, use a 25,000-character ceiling:

```sh
uv run .opencode/skills/md-to-twitter/scripts/md2twitter.py \
  docs/261119-backup-opencode-sqlite-sessions-zh-hans.md \
  --limit 25000 --tables image \
  --out exports/261119-backup-opencode-sqlite-sessions-zh-hans-twitter.txt
```

Keep `-twitter.txt` in the filename so the destination is obvious. Choose a different output path if retaining both a thread and a long-post export.

The converter reports the actual post count. Text beyond the ceiling or more than four attachments can produce multiple posts.

Remove the trailing `[image: …]` notes before pasting text. Upload the listed images separately.

The converter preserves words rather than summarizing. Formatting markers disappear, while inline-code backticks remain.

Code stays copyable plain text by default. Tables become pipe-separated rows unless `--tables image` is selected.

### Post and thread flags

| Flag | Effect |
| --- | --- |
| Default | 280 weighted characters per post |
| `--limit N` | Custom per-post ceiling |
| `--number` | Add `n/N` prefixes |
| `--out PATH` | Select the text output file |
| `--print` | Print instead of writing the text file |
| `--at N` | Select one post |
| `--post` | Upload attachments and send selected posts |
| `--reply-to ID` | Reply under an existing post |
| `--dry-run` | With `--post`, preview without sending |
| `--code image` | Replace code text with screenshots |
| `--tables image` | Replace tables with screenshots |
| `--image-dir DIR` | Override the default `imgs/twitter-blocks/` directory |

Screenshots preserve appearance but make code uncopyable. Prefer plain-text code unless the user requests images.

### Posting

Only use `--post` after explicit approval. The API posting path remains unverified against the live service.

Credentials come from environment variables or `~/.config/md-to-twitter/keys.json`.

Environment variable names:

```text
X_CONSUMER_KEY
X_CONSUMER_SECRET
X_ACCESS_TOKEN
X_ACCESS_TOKEN_SECRET
```

Configuration field names:

```json
{"consumer_key": "...", "consumer_secret": "...",
 "access_token": "...", "access_token_secret": "..."}
```

Signing uses OAuth 1.0a HMAC-SHA1. JSON and multipart bodies are not OAuth form parameters.

For one-at-a-time posting:

```sh
uv run .opencode/skills/md-to-twitter/scripts/md2twitter.py \
  docs/<article>.md --at 1 --post

uv run .opencode/skills/md-to-twitter/scripts/md2twitter.py \
  docs/<article>.md --at 2 --post --reply-to PREVIOUS_POST_ID
```

The script prints each posted URL and the next reply command. It stores no continuation state between runs.

If a post fails, the script stops without retrying. Inspect the last successful ID before resuming to avoid duplicates.

### Counting and conversion

| Limit | Value |
| --- | --- |
| Default text ceiling | 280 weighted characters |
| Numbered-post reserve | Six characters |
| Images per post | Four |
| Image size | 5 MB |
| Image types | PNG, JPEG, WebP, GIF |

The counter assigns one unit to most characters and two to CJK and emoji. URLs cost 23 units.

Chinese splitting recognizes `。！？；` alongside English punctuation. Adjacent CJK sentence fragments join without an inserted space.

The converter removes frontmatter and translation-header links. It retains the article's body.

Post mode joins source blocks with one newline. Remote and data-URI images are skipped in post mode.

## Verification

Run the Article regression tests:

```sh
uv run --with markdown --with beautifulsoup4 --with requests \
  --with pymdown-extensions python \
  .opencode/skills/md-to-twitter/scripts/test_article.py
```

For an Article export:

1. Compare every exported code file with its source block.
2. Check the manifest's asset paths.
3. Confirm the default HTML contains fenced code rather than code placeholders.
4. Confirm there is no newline after each closing fence inside its code element.
5. Inspect the pasted draft before publishing.

Automated checks cannot verify X's current paste behavior. The full-article user test above verifies the accepted workflow for this editor version.

## Related converters

| Target | Text delivery | Image delivery |
| --- | --- | --- |
| LinkedIn | HTML paste | Embedded image bytes |
| Medium | HTML paste | Public image URLs |
| X Articles | HTML paste | Manual uploads at placeholders |
| X posts and threads | Plain-text paste or API | Manual uploads or API attachments |
