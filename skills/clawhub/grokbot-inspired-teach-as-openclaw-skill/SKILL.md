---
name: teach
description: Record a screen demonstration and turn it into a reusable, parameterized OpenClaw SKILL.md.
version: 1.0.0
metadata:
  openclaw:
    requires:
      bins:
        - ffmpeg
    anyBins:
      - python3
      - python
    emoji: "\U0001F3A5"
---

# Teach — demonstrate a workflow, get a reusable skill

Use this skill when the user wants to capture a screen demonstration and turn it
into a new OpenClaw skill. Everything runs locally on the user's machine; no
cloud computer is involved.

## Steps

1. **Agree the goal.** Ask the user, in one sentence, what result they are about
   to demonstrate. Confirm before recording.

2. **Record.** First ask the user whether they want to **narrate** the demo
   (speak the intent out loud as they go). Narration is optional and
   consent-gated — never record microphone audio without an explicit yes.

   - **No narration:** `python3 "{baseDir}/scripts/record.py" "<output.mp4>"`
   - **With narration:** add `--with-audio`
     (`--audio-device "Name"` only if auto-detect picks the wrong mic).

   Default cap is 600s (10 min), matching Grok Bot's Teach limit. Pass a
   `max_seconds` arg to change the cap (e.g. `300`). The script records the
   primary display cross-platform (Windows `gdigrab`, macOS `avfoundation`,
   Linux `x11grab`) and, with `--with-audio`, the microphone (Windows `dshow`,
   macOS `avfoundation`, Linux `pulse`). It prints the ffmpeg PID, an `AUDIO
   on/off` flag, and the final duration. It stops on Ctrl-C or when the cap is
   reached. Tell the user to perform the workflow once, then stop the recording
   (Ctrl-C) or let it hit the cap.

3. **Sanity-check.** Run:

   ```bash
   python3 "{baseDir}/scripts/frames.py" "<output.mp4>" --check
   ```

   This writes two frames (≈20% and ≈70% of duration) and reports their paths
   and the duration. Look at both frames. If they show an idle desktop or the
   wrong surface, the capture is bad: tell the user, offer a redo, and — if they
   decline — delete the recording. Do not proceed to transcription on a bad
   capture.

4. **Transcribe.** Run:

   ```bash
   python3 "{baseDir}/scripts/frames.py" "<output.mp4>"
   ```

   It extracts evenly spaced frames (and splits the video losslessly if it
   exceeds ~12MB so each part stays under attachment limits) and prints the
   frame/part paths. Use your own vision to analyze them and produce a
   structured play-by-play:

   - Starting state (page/app open)
   - Every meaningful action in order (clicks, typing, navigation, URL changes,
     menus, scrolling)
   - Ending state
   - Approximate timing
   - Exact non-secret text typed — **NEVER** transcribe passwords, one-time
     codes, API keys, financial account numbers, or private personal details;
     use placeholders

   If you have no vision capability, ask the user for a written step list
   instead.

   **Narration (only if `--with-audio` was used).** Run:

   ```bash
   python3 "{baseDir}/scripts/transcribe.py" "<output.mp4>"
   ```

   If Whisper is installed (`pip install openai-whisper`) it prints a
   `TRANSCRIPT_START … TRANSCRIPT_END` block; if not, it prints
   `WHISPER_MISSING` with install guidance. Merge the narration into the
   play-by-play: trust narration for **why/intent** and frames for **what
   happened**, and line up utterances with their timestamps. Redact any secret
   spoken aloud (passwords, OTPs, keys) — use placeholders. If Whisper is
   missing, ask the user for a written narration instead.

5. **Optional browser cross-check.** If the user consents and a Chrome/Chromium
   DevTools endpoint is reachable (`HTTP GET http://127.0.0.1:9222/json/list`),
   copy its `History` sqlite read-only to corroborate visited URLs. Trust
   history for URLs, frames for in-page actions. This reads browser history —
   keep it optional and consent-gated.

6. **Decide the skill.** Identify the goal, the steps, and which demonstrated
   values are INPUTS (`{item}`, recipient, date, account) versus fixed
   constants. If ambiguity would materially change the skill, ask the user
   concise questions and wait for answers.

7. **Write the skill.** Create
   `~/.openclaw/workspace/skills/<derived-slug>/SKILL.md` with:

   - frontmatter: `name` (lowercase-hyphen, ≤64 chars), `description` (one line,
     <160 chars)
   - body: the generic, reusable, parameterized recipe — signed-in browser where
     needed, stable targets (URLs, labeled buttons/fields, not coordinates),
     prefer a connector/MCP tool over UI replay when one exists, consequential
     steps (orders, messages, payments, deletes, production changes) marked
     **confirm with the user first**, no embedded credentials ("assumes signed
     in to X")
   - **if narration was captured** (step 4), add a `## Narration script` section
     to the body: the spoken cues from the demo, parameterized with
     `{placeholders}` for inputs, as a concise numbered checklist. On each rerun
     the skill presents these cues to the user so they can repeat (or adapt) the
     same intent. Keep cues short; redact any spoken secrets (placeholders only).

   See `{baseDir}/references/skill-schema.md` for the exact schema and
   `{baseDir}/references/teach-principles.md` for the rules.

8. **Clean up.** Delete `<output.mp4>` and every extracted frame/part file.

9. **Report.** Short numbered learned steps, which values are inputs, key
   assumptions, and the path to the written skill. Note whether a `## Narration
   script` was embedded. Tell the user the skill is a **DRAFT** (add decision
   rules, failure handling, and approval boundaries that may not be obvious from
   one example; test on a safe example before scheduling). Offer a dry run.
   **NEVER** run the learned skill unprompted.

## Hard rules

- Never transcribe or store secrets. If the demo was mostly entering
  credentials, say so and do not create a skill.
- Never embed credentials in the generated skill.
- Never run destructive commands; never leave recordings on disk.
