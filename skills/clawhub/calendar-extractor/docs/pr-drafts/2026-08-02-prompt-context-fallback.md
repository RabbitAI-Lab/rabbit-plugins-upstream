# calendar-extractor: use embedded UNIT CONTEXT; a fetch miss no longer aborts the write

- **Branch:** `feat/calendar-extractor-prompt-context-fallback`
- **Date:** 2026-08-02
- **Skill:** `calendar-extractor` (currently `0.7.1`)
- **Spec:** `javis-server/docs/superpowers/specs/2026-08-02-dispatch-prompt-embed-unit-context-resilience-design.md` (Approved — root-caused via systematic-debugging). This is the **coordinated skill-side half** of that spec; the server half (embed the unit context in the dispatch prompt) ships separately on javis-server branch `feat/dispatch-prompt-embed-unit-context`.

## Why

A proactive, dispatcher-invoked extraction **silently vanished** when its source unit row was dropped after dispatch.

Observed (wmp425, 2026-08-02): a "meeting at 1 PM today" keyboard input reached the server, `calendar-extractor` was auto-invoked, and its agent **extracted the event** (container log: *"Extracted and pushed… PENDING card"*) — but **no `skill_data` row was ever written** (`skill_data MAX(id)` stuck at 319; no POST in the server logs). No calendar event → no voice-call arming → no "Javis calls you" ring.

Root cause: the dispatcher handed the skill **only the unit id**, so the skill had to **re-fetch** the unit via `GET /api/transcripts/keyboard-input/<id>`. For this event `keyboard_input 1189` **did not exist** (server `MAX(id)=1187`; rolled-back/dropped inserts — the fragile draft double-save path). The re-fetch 404'd → the skill aborted before the `/api/skill/data` POST → the extracted event was lost.

The server fix threads the already-loaded transcript + `source_ref`/`source_kind`/`reference_date`/`tz` into the dispatch prompt as a delimited `UNIT CONTEXT` block. This PR makes the skill **use that embedded context as the source of truth** and treat `fetch` as an optional enrichment whose failure must not suppress the write.

## What changed

**`scripts/calendar-extractor.js` — `doFetch` degrades instead of throwing.**
- Wrapped the single `httpGet` in a try/catch. On failure (e.g. a 404 keyboard-input miss) it no longer propagates the throw that aborts the run. Instead it logs `⚠️ fetch miss (…) — not aborting; fall back to the run-prompt UNIT CONTEXT.` to stderr and continues with `data = null`.
- The existing envelope normalization already handles a null/empty payload → an empty `sessions` array, so the emitted envelope still carries the relative-time anchor (`reference_time`/`reference_date`/`reference_weekday`/`reference_time_utc`/`tz`).
- Surfaces the miss in the emitted envelope too (not just stderr): `out.fetch_error = fetchError`, so the agent can *see* the re-fetch missed and knowingly fall back to the `UNIT CONTEXT`.

**`SKILL.md` — document the embedded-context path and the no-abort rule.**
- Step 1 (Fetch): added the dispatcher-path **Exception** — a failed single-unit `fetch --session`/`fetch --kbd-input` (surfaced as `fetch_error`, empty sessions) does NOT mean "emit nothing"; fall back to the prompt-embedded transcript/`reference_date`/`tz` and STILL extract and push.
- "How this skill is invoked" (dispatcher auto-run): the agent now reads the embedded **`UNIT CONTEXT`** block (transcript + `reference_date`/`tz` + `source_ref`/`source_kind`) as the source of truth for extraction; `fetch --session`/`fetch --kbd-input` is now **optional enrichment** and a **failed fetch must not abort the push**.
- Added a dedicated **`UNIT CONTEXT` block** subsection: resolve relative times against its `reference_date`/`tz`; carry its `source_ref`/`source_kind` onto each event so provenance flows to the `/api/skill/data` mirror; on a re-fetch empty/404, fall back and still POST the PENDING row; report the miss non-silently but never let it suppress the write; for `source_ref` use the prompt's value, or the `<unit>` id itself when absent. **No change** to the `dedup_key` / pending-write / `lead_time` contract — only the source of the extraction input when a re-fetch misses.

## Tests

`test/cli.test.js` — two new tests (both reference the spec in-comment); full suite **14 pass / 0 fail** (`node --test test/cli.test.js`):

- **`doFetch degrades to an empty-sessions envelope on a failing fetch (no throw, anchor + fetch_error present)`** — `httpGet` rejects exactly as the real 404 keyboard-input miss does; asserts no throw, zero sessions, `fetch_error` matches `/404/`, and the anchor (`reference_date` `2026-06-03`, `tz`) is still emitted.
- **`failing fetch --kbd-input + prompt UNIT CONTEXT still produces the /api/skill/data upsert (source_ref from prompt)`** — the re-fetch 404s and degrades; the agent extracts from the prompt `UNIT CONTEXT` ("meeting at 1 PM today") carrying the prompt's `source_ref` (`1189`)/`source_kind` (`keyboard`); `doPush` still writes the `skill_data` upsert. Asserts the write happened (not "emitting nothing"), `source_ref` rides through from the prompt, and `status` is still `pending` (contract unchanged).

## Files

- `calendar-extractor/SKILL.md` (+29 / −2)
- `calendar-extractor/scripts/calendar-extractor.js` (+21 / −1)
- `calendar-extractor/test/cli.test.js` (+72)

(`git diff --stat`: 3 files changed, 119 insertions(+), 4 deletions(-))

## Not in this PR

- The server half (embed `UNIT CONTEXT` in `_dispatch_prompt`, `_load_unit_context`) — javis-server branch `feat/dispatch-prompt-embed-unit-context`. Both halves must ship together for the end-to-end fix; the skill change is backward-compatible (if no `UNIT CONTEXT` is present, the manual/windowed `fetch` path is unchanged).
- Fixing the underlying `keyboard_input` insert drops / id gaps (the true persistence bug — the fragile draft double-save path) — separate track.
- `consecutive_discards → 3 = auto-disable` fragility; earbud-heartbeat staleness — separate tracks.
- Version bump / `clawhub publish` — do after both halves merge.

## Verification gate (from the spec)

On prod: a fresh keyboard/voice "meeting at &lt;time&gt; today" whose source row is subsequently absent still lands a **pending** `calendar-extractor` `skill_data` event (the write no longer depends on re-fetch) → confirmable in the iOS calendar table → arms a voice-call job.
