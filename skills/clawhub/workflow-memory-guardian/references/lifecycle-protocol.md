# Lifecycle Protocol — M0–M3 Detailed Procedures
**Protokol Daur Ulang — Prosedur Detail M0–M3**

This reference gives the full trigger lists, step sequences, gates, marker templates, and failure modes for each lifecycle stage. Read it whenever a stage's exact procedure is unclear.

## M0 — Cold Boot / Restore

### Triggers
- A new session begins (any first substantive turn).
- A continuation message: "lanjut", "lanjutkan", "continue", "kerjakan yang kemarin", "session sebelumnya".
- A recall question: "masih ingat?", "kemarin kita ngapain?", "apa yang kita kerjakan?", "kamu masih paham konteksnya?"
- An edit/refinement request that assumes prior context ("ubah bagian yang tadi", "revisi deck yang kemarin").

### Procedure
1. Read `/home/z/my-project/memory/SESSION-STATE.md`, then `memory/MEMORY.md`. This is the mandatory minimum — do it BEFORE writing any substantive response.
2. If SESSION-STATE references a handoff file for the active task, read that too.
3. Run the **Recall Check** (see `integrity-standard.md`): answer the manifest questions from what you read. Count restored categories.
4. If below 95%: gap-fill — read relevant handoff archives → the last ~3 worklog entries → the actual artifact files on disk. Re-verify. Never guess to fill a gap.
5. Cross-check any auto-provided session summary: conflicts → memory files win; summary-only facts → promote them into memory files (rare but possible).
6. Emit the marker, present restored context briefly, and confirm the restored plan with the user before executing new work.

### Gate
Restore is complete ONLY when: files read + marker emitted + Recall Check ≥95% + restored plan stated. A response that starts executing a "continued" task without showing restoration has violated the gate.

### Marker template
```
[MEM | RESTORED] sumber: SESSION-STATE + MEMORY (+ handoff) — n/7 kategori manifest · task aktif: __ · langkah berikutnya: __
```

### Failure modes
- **Guessing instead of gap-filling** — fabricating "restored" context that is not in any file. Violation: the marker must reflect what the FILES say, not plausibility.
- **Reading but not confirming** — restoring silently then barreling into execution. The gate requires presenting the restored plan and confirming.
- **Trusting the summary over the files** — summaries compress and drop facts; the files are the record.

## M1 — Checkpoint

### Triggers (any of)
- A phase or task completed (started, finished, or materially advanced).
- A decision locked or a pending decision surfaced.
- An artifact written/delivered (file path now exists that didn't before).
- A plan changed or a blocker discovered.
- BEFORE starting a long implementation stretch (many file writes, long script execution, subagent delegation) — the pre-emptive checkpoint that protects mid-task context exhaustion.

### Procedure
1. Rewrite `SESSION-STATE.md` completely (atomic snapshot — all template sections, current values).
2. Append a worklog entry ONLY if this is a major milestone (task started/completed, deliverable shipped) — with Task ID per platform convention.
3. Emit the inline marker.

### Gate
The checkpoint exists ONLY when the file was actually rewritten. Announcing a checkpoint without the write is a violation.

### Marker template
```
[MEM | CHECKPOINT] task __ — SESSION-STATE diperbarui (fase/status/artefak)
```

## M2 — Emergency Compression

### Signals
- The session is unusually long (many turns, many tool calls).
- Large files have been read repeatedly into context.
- The user mentions lag, repetition, or the agent losing the thread.
- Any platform signal that context is being compacted or is near exhaustion.
- You notice yourself: "I can no longer recall the earlier part of this session clearly."

### Procedure
1. STOP other work. Write `SESSION-STATE.md` NOW — CRITICAL items first (task identity, decisions, artifact paths), then HIGH (pending, trajectory), then NORMAL.
2. If pressure is severe (compaction imminent), ALSO write a draft handoff archive immediately — a mid-session handoff is better than a lost session.
3. Emit the marker and continue the task if safe; otherwise surface to the user that state is persisted and the session can safely continue or restart.

### Gate
Full state on disk before anything else proceeds. The ~5% loss budget is spent here and only here — drop narrative verbosity, never manifest items.

### Marker template
```
[MEM | COMPRESS] tekanan konteks terdeteksi — state penuh tersimpan, CRITICAL lengkap
```

## M3 — Handoff

### Triggers
- Explicit session end: "udah dulu", "sampai jumpa", "gtg", "makasih ya bye", "that's all for today".
- Abrupt exit signals: short thanks + farewell, even mid-task ("aku pergi dulu").
- A major task fully closed (ship the handoff while the details are fresh).
- The user announces they will return later ("besok lanjut lagi ya") — treat as session end for handoff purposes.

### Procedure
1. Write `handoffs/YYYY-MM-DD-<slug>.md` with ALL 7 manifest sections filled (template in `memory-architecture.md`). Write "none" explicitly rather than omitting.
2. Promote durable facts into `MEMORY.md`: new preferences, locked decisions, artifact inventory additions, conventions.
3. Rewrite `SESSION-STATE.md` to final state — including "Next Steps" so the next M0 lands running.
4. Emit the marker + a 1–3 line statement of what was persisted and how the next session restores it.

### Gate
Handoff complete ONLY when: archive written + MEMORY promoted (if applicable) + final SESSION-STATE + marker. A polite goodbye with no write is the single most damaging violation — it is exactly how sessions get forgotten.

### Marker template
```
[MEM | HANDOFF] arsip: memory/handoffs/YYYY-MM-DD-<slug>.md — 7/7 bagian · MEMORY + SESSION-STATE final
```

## Marker Convention

`[MEM | LABEL]` is a **protocol constant**: RESTORED, CHECKPOINT, COMPRESS, HANDOFF — always these four labels, always uppercase, so they are greppable and auditable across sessions and by eval tooling. The content AFTER the marker is in the user's language. Markers sit on their own line or at the start of the relevant block; never merge a `[MEM | …]` marker with a `[FASE n | …]` marker.

**Penjelasan (ID):** Empat marker ini adalah jejak audit protokol. Kalau seorang user ( atau eval grader) ingin memverifikasi bahwa memory benar-benar dikelola, ia cukup mencari empat label itu dalam transkrip — keberadaannya membuktikan protokol jalan, formatnya yang konsisten membuatnya bisa diperiksa secara otomatis.
