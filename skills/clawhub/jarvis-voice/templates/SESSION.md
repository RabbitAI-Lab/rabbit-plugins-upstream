# SESSION.md — session start

> **Optional file.** Copying this into your workspace root changes agent behaviour in every
> future session. Delete it to stop. Your explicit instructions outrank anything here.

<trigger>
These steps run **only on an explicit new-session start** — the first turn of a fresh session.
Not on every message, not on resumed turns, not mid-conversation. If you are unsure whether
this is a session start, it is not: skip straight to answering.
</trigger>

<startup_steps>
Keep this light. The goal is a greeting that references something real, not an audit.

1. Read today's and yesterday's daily log if one exists. Files already injected into context do
   not need re-reading.
2. Only if the log looks incomplete, list recent sessions to see actual activity. Calling a day
   "quiet" from a stale log misleads the user.
3. Greet, referring to real recent work — true and specific, never invented.
4. Mention pending items and suggest a next step.

**Do not** enumerate directories, open unrelated files, or read anything outside the workspace
as part of this routine. If a step needs a file the user has not pointed you at, ask first.
</startup_steps>

<voice>
If `VOICE.md` is installed, the greeting follows its rules like any other reply — including its
mute and channel gates. If it is not installed, greet normally without audio. Voice is never a
prerequisite for answering.
</voice>

<output_rules>
- If the running model differs from the configured default, say so.
- These bootstrap steps are scaffolding — do not narrate them back to the user.
</output_rules>
