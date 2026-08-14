# Teach principles (applied to every generated skill)

These rules are enforced by the `teach` skill when it turns a screen
demonstration into a new OpenClaw `SKILL.md`. They are derived from Grok Bot's
"Teach a task" pipeline.

1. **Sanity-check the capture first.** Extract one frame at ~20% and one at
   ~70% of duration. If they show an idle desktop or the wrong surface, the
   capture is bad — tell the user and offer a redo; do not transcribe.

2. **Redact secrets.** Never transcribe passwords, one-time codes, API keys,
   financial account numbers, or private personal details. Use placeholders in
   any summary or skill body. If the demonstration was mostly entering
   credentials, say so and **do not create a skill**.

3. **Parameterize.** Separate INPUTS (search term, recipient, date, account)
   from fixed constants. The generated skill uses `{placeholders}` for inputs.

4. **Prefer stable targets.** Reference URLs, labeled buttons, and form fields
   by name/aria, not screen coordinates.

5. **Prefer connectors/MCP over UI replay.** When a connector or MCP tool covers
   a step, use it. Use the browser only for steps nothing else supports.

6. **Confirm consequential steps.** Mark orders, messages, payments, deletions,
   and production changes as **confirm with the user first**.

7. **No embedded credentials.** Sign-in state lives in the browser profile, so a
   step needing login says "assumes signed in to X". Never store secrets in the
   skill body.

8. **The skill is a draft.** Tell the user to add decision rules, failure
   handling, and approval boundaries that may not be obvious from one example,
   and to test on a safe example before scheduling.

9. **Clean up.** Delete the recording and all extracted frames/parts after the
   skill is written. Never leave recordings on disk.

## Narration (optional)

Narration is captured only with explicit consent (`--with-audio`). It enriches
the play-by-play with intent but is never required. Whisper transcription is
best-effort: if it is not installed, fall back to a written narration from the
user. Spoken secrets are redacted exactly like typed ones — placeholders only.

When authoring the skill, capture the spoken cues as a parameterized
`## Narration script` section so reruns prompt the user with the same intent.
Replace concrete values (names, dates, account IDs) with `{placeholders}`; keep
each cue to one line. The generated skill presents this script to the user on
every run.
